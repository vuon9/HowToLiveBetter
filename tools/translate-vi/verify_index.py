#!/usr/bin/env python3
"""Check that index.vi.html can parse the Vietnamese corpus and still runs.

Mirrors the page's own parser (same regexes, same order) against README.vi.md
and the book/vi files its table of contents links to, then reports how many
sections and entries come out and how many entries carry each field.

Beyond the parser it checks the things that a translation round can break
silently:

* the functional strings the page relies on are still in place;
* the script of both pages is valid JavaScript (a model asked to rewrite a
  template literal can drop a bracket, and the page then dies in the browser);
* the cross-reference matcher recognises how the Vietnamese corpus writes a
  reference, which is a different wording from the Chinese one;
* no Chinese is left in an interface string, and no Chinese is left in the
  markup outside the quotes it keeps on purpose.

    python3 tools/translate-vi/verify_index.py
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "index.vi.html"
ZH_INDEX = ROOT / "index.html"
SEC_RE = re.compile(r"^#{1,2} (\d+)\. (.+)$", re.M)
ENTRY_RE = re.compile(r"^### (\d+)\. (.+)$", re.M)
TOC_RE = re.compile(r"\]\((book/vi/[^)]+\.md)\)")
TAG_RE = re.compile(r"^<!--\s*成本标签:\s*(.*?)\s*-->", re.M)
FIELDS = {
    "cost": re.compile(r"^- Chi phí:(.*)$", re.M),
    "human": re.compile(r"^- Nói đơn giản:(.*)$", re.M),
    "gain": re.compile(r"^- Lợi ích:(.*)$", re.M),
    "grade": re.compile(r"^- Mức bằng chứng:\s*([ABC])", re.M),
    "src": re.compile(r"^- Nguồn:(.*)$", re.M),
    "note": re.compile(r"^- Ghi chú:(.*)$", re.M),
}
REQUIRED_IN_PAGE = [
    "成本标签",          # cost tags in the corpus stay Chinese
    "k==='钱'",          # tag value keys
    "'死亡率':'đổi tuổi thọ'",
    "- Chi phí:",
    "- Mức bằng chứng:",
    "README.vi.md",
    "Hiểu đúng các con số",
]
HAN = re.compile(r"[\u4e00-\u9fff]")
# Chinese kept inside brackets is a gloss of a China-specific term (hộ khẩu (户口))
GLOSS_RE = re.compile(r"[（(][^（()）]*[)）]")
XREF_SCRIPT = """
const fs = require('fs');
const out = [];
for (const [page, files, label] of [[%s, %s, 'vi'], [%s, %s, 'zh']]){
  const t = fs.readFileSync(page, 'utf8');
  const numLine = (t.match(/const NUMS = '[^\\n]*';/) || [])[0];
  const xrefLine = (t.match(/const XREF_RE = new RegExp\\([^\\n]*/) || [])[0];
  if (!numLine || !xrefLine){
    out.push(label + ': không thấy NUMS/XREF_RE');
    continue;
  }
  const built = (0, eval)('(function(){' + numLine + ';' + xrefLine + '; return {NUMS: NUMS, re: XREF_RE};})()');
  let hits = 0;
  for (const f of files){
    const text = fs.readFileSync(f, 'utf8');
    hits += (text.match(new RegExp(built.re.source, 'g')) || []).length;
  }
  out.push(label + ' ' + hits);
}
console.log(out.join('\\n'));
"""


def check_js(html: str) -> list[str]:
    """Every <script> block must parse. Returns the failures."""
    node = shutil.which("node")
    if not node:
        print("  (bỏ qua kiểm cú pháp JS: không có node)")
        return []
    bad = []
    for i, body in enumerate(re.findall(r"<script(?![^>]*ld\+json)[^>]*>(.*?)</script>", html, re.S)):
        if not body.strip():
            continue
        f = Path(tempfile.mkdtemp()) / f"block{i}.js"
        f.write_text(body, encoding="utf-8")
        r = subprocess.run([node, "--check", str(f)], capture_output=True, text=True)
        if r.returncode:
            lines = [l for l in r.stderr.splitlines() if l.strip()]
            bad.append(f"khối script {i}: {lines[2] if len(lines) > 2 else r.stderr[:80]}")
    return bad


def check_xref() -> list[str]:
    """The cross-reference matcher must match the Vietnamese corpus, not the Chinese one."""
    node = shutil.which("node")
    if not node:
        print("  (bỏ qua kiểm mắt nối tham chiếu: không có node)")
        return []
    vi_files = sorted(str(p) for p in (ROOT / "book/vi").glob("*.md")) + sorted(
        str(p) for p in (ROOT / "docs/vi").glob("*.md")
    )
    zh_files = sorted(str(p) for p in (ROOT / "book").glob("*.md"))
    script = XREF_SCRIPT % (
        repr(str(INDEX)),
        repr([str(p) for p in (ROOT / "book/vi").glob("*.md")]),
        repr(str(ZH_INDEX)),
        repr([str(p) for p in (ROOT / "book").glob("*.md")]),
    )
    f = Path(tempfile.mkdtemp()) / "xref.cjs"
    f.write_text(script, encoding="utf-8")
    r = subprocess.run([node, str(f)], capture_output=True, text=True)
    if r.returncode:
        return [f"không chạy được phép thử tham chiếu: {r.stderr.strip().splitlines()[-1][:120]}"]
    hits = {}
    for line in r.stdout.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1].isdigit():
            hits[parts[0]] = int(parts[1])
    print(f"  mắt nối tham chiếu: bản Việt {hits.get('vi', 0)} chỗ, bản Trung {hits.get('zh', 0)} chỗ")
    problems = [l for l in r.stdout.splitlines() if "không thấy" in l]
    if hits.get("vi", 0) < hits.get("zh", 0) * 0.5:
        problems.append(f"mắt tham chiếu tiếng Việt khớp quá ít ({hits.get('vi')} so với {hits.get('zh')})")
    return problems


def check_no_chinese(page: str) -> list[str]:
    """No interface string, and no markup text, may still be Chinese."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import audit_js_strings as ajs

    problems = []
    scripts = re.findall(r"<script(?![^>]*ld\+json)[^>]*>(.*?)</script>", page, re.S)
    for js in scripts:
        for _, lit in ajs.literals(js):
            text = lit.strip()
            if HAN.search(text) and text not in ajs.MACHINE and not text.startswith("/"):
                problems.append(f"chuỗi trong script còn tiếng Trung: {text[:70]!r}")
    blanked = list(page)
    for m in re.finditer(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", page):
        for i in range(m.start(), m.end()):
            blanked[i] = "\n" if blanked[i] == "\n" else " "
    markup = "".join(blanked)
    for m in re.finditer(r">([^<>]+)<", markup):
        text = m.group(1)
        if HAN.search(GLOSS_RE.sub("", text)):
            problems.append(f"văn bản trong trang còn tiếng Trung: {text.strip()[:70]!r}")
    for m in re.finditer(r'\b(title|aria-label|alt|placeholder|content)="([^"]*)"', markup):
        if HAN.search(GLOSS_RE.sub("", m.group(2))):
            problems.append(f"thuộc tính {m.group(1)} còn tiếng Trung: {m.group(2)[:60]!r}")
    return problems


def main() -> None:
    page = INDEX.read_text(encoding="utf-8")
    problems = []
    missing = [needle for needle in REQUIRED_IN_PAGE if needle not in page]
    problems += [f"index.vi.html thiếu mốc: {n}" for n in missing]
    readme = (ROOT / "README.vi.md").read_text(encoding="utf-8")
    files = sorted(set(TOC_RE.findall(readme)))
    sections, entries, counts = 0, 0, dict.fromkeys(FIELDS, 0)
    tags = 0
    for rel in files:
        text = (ROOT / rel).read_text(encoding="utf-8")
        sections += len(SEC_RE.findall(text))
        entries += len(ENTRY_RE.findall(text))
        tags += len(TAG_RE.findall(text))
        for key, rx in FIELDS.items():
            counts[key] += len(rx.findall(text))
    print(f"mục lục trỏ tới {len(files)} tệp")
    print(f"phần: {sections} | mục: {entries} | dòng cost tag: {tags}")
    for key, n in counts.items():
        print(f"  trường {key}: {n}")
    if sections != 34 or entries != 649 or tags != 649 or not all(n >= 649 for n in counts.values()):
        problems.append(f"bộ đếm lệch: {sections} phần, {entries} mục, {tags} cost tag")

    problems += check_js(page)
    problems += check_xref()
    problems += check_no_chinese(page)

    for p in problems:
        print(f"[FAIL] {p}")
    print("\nKẾT QUẢ:", "OK, trang đọc được bản tiếng Việt" if not problems else f"CÓ VẤN ĐỀ ({len(problems)})")
    sys.exit(0 if not problems else 1)


if __name__ == "__main__":
    main()
