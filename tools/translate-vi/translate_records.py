#!/usr/bin/env python3
"""Translate docs/核实记录/*.md (source verification records) into docs/核实记录/vi/.

These files are per-source notes: a URL, the English sentence quoted from the
paper, and Chinese commentary. Rules on top of the shared system prompt:
URLs, DOIs, English titles and English quotations stay byte-identical, the
label 原文 becomes "Nguyên văn", and the Chinese commentary is translated.

    VI_TRANSPORT=hermes VI_WORKERS=16 python3 tools/translate-vi/translate_records.py
    python3 tools/translate-vi/translate_records.py --only 01,02
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import re
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_book as tb  # noqa: E402

SRC_DIR = tb.ROOT / "docs" / "核实记录"
OUT_DIR = SRC_DIR / "vi"
HEAD_RE = re.compile(r"^##\s+(.*)$")
URL_RE = tb.URL_RE
DIGIT_RUN_RE = tb.DIGIT_RUN_RE
PREFIX_MAP = {
    "追加": "bo-sung",
    "新增": "moi-them",
    "排查": "rac-soat",
    "重写": "viet-lai",
    "issue": "issue",
}
RECORD_RULES = (
    tb.SYSTEM_RULES
    + """
Bổ sung cho tệp hồ sơ kiểm chứng nguồn:
- Giữ nguyên từng ký tự: URL, DOI, số hiệu văn bản, tên tài liệu và tên tạp chí tiếng Anh, mọi câu trích nguyên văn trong dấu ngoặc kép.
- Nhãn 「原文：」 dịch thành "Nguyên văn:". Nhãn 「核实日期」 giữ nghĩa, viết "Ngày kiểm chứng".
- Dịch toàn bộ chú thích tiếng Trung, kể cả ghi chú trong ngoặc và ghi chú ở cuối dòng.
- Giữ nguyên cấu trúc danh sách: số dấu gạch đầu dòng, mức thụt lề, thứ tự dòng.
- Không thêm nhận xét của người dịch.
"""
)
_print_lock = threading.Lock()


def log(msg: str) -> None:
    with _print_lock:
        print(msg, flush=True)


def pack_sections(title: str, intro: str, sections: list[tuple[str, str]], cap: int = 4200) -> list[str]:
    """Pack heading+body sections into chunks under `cap` characters."""
    chunks, cur, size = [], [], len(title) + len(intro)
    for heading, body in sections:
        piece = f"{heading}\n{body}".strip()
        if cur and size + len(piece) > cap:
            chunks.append("\n\n".join(cur))
            cur, size = [], 0
        cur.append(piece)
        size += len(piece) + 2
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def validate(src: str, out: str) -> list[str]:
    problems = []
    for label, pattern in (("URL", URL_RE), ("DOI", tb.DOI_RE)):
        miss = set(pattern.findall(src)) - set(pattern.findall(out))
        if miss:
            problems.append(f"thiếu {label} {sorted(miss)[:2]}")

    def nums(text: str) -> set[str]:
        return set(DIGIT_RUN_RE.findall(re.sub(r"(?<=\d)[.,](?=\d{3})+", "", text)))

    miss_nums = {n for n in nums(src) if not re.search(rf"{n}\s*[万亿]", src)} - nums(out)
    if miss_nums:
        problems.append(f"thiếu số {sorted(miss_nums)[:5]}")
    if src.count("原文：") != out.count("Nguyên văn:"):
        problems.append(f"nhãn 'Nguyên văn:' {out.count('Nguyên văn:')}/{src.count('原文：')}")
    if len(re.findall(r"^##", src, flags=re.M)) != len(re.findall(r"^##", out, flags=re.M)):
        problems.append("lệch số tiêu đề '##'")
    return problems


def translate_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    h1 = next((ln for ln in lines if ln.startswith("# ")), f"# {path.stem}")
    rest = lines[lines.index(h1) + 1 :] if h1 in lines else lines
    intro, sections, cur_head, cur = [], [], None, []
    for ln in rest:
        m = HEAD_RE.match(ln)
        if m:
            if cur_head is not None:
                sections.append((cur_head, "\n".join(cur).strip("\n")))
            cur_head, cur = ln, []
        elif cur_head is None:
            intro.append(ln)
        else:
            cur.append(ln)
    if cur_head is not None:
        sections.append((cur_head, "\n".join(cur).strip("\n")))
    intro_text = "\n".join(intro).strip("\n")

    schema = {
        "type": "object",
        "properties": {"title": {"type": "string"}, "intro": {"type": "string"}},
        "required": ["title", "intro"],
    }
    head = tb.parse_json_loose(
        tb.call_gemini(
            f"Hồ sơ kiểm chứng nguồn của sách, tệp gốc docs/核实记录/{path.name}.\n"
            f"Dịch tiêu đề và đoạn mở đầu sang tiếng Việt, trả về JSON hai khóa title và intro:\n\n{h1}\n\n{intro_text}",
            RECORD_RULES,
            schema=schema,
            temperature=0.3,
        )
    )
    head["title"] = re.sub(r"^#+\s*", "", head["title"]).strip()
    head["intro"] = head["intro"].strip()
    job = pack_sections(h1, intro_text, sections)
    outs = []
    for chunk in job:
        system, out, problems = RECORD_RULES, "", []
        for _ in range(3):
            out = tb.unfence(
                tb.call_gemini(
                    f"Dịch khối hồ sơ kiểm chứng sau sang tiếng Việt, giữ nguyên URL, số hiệu và mọi câu "
                    f"trích tiếng Anh, chỉ trả về markdown:\n\n{chunk}",
                    system,
                    temperature=0.2,
                )
            )
            problems = validate(chunk, out)
            if not problems:
                break
            system = RECORD_RULES + "\n\nLẦN TRƯỚC SAI, phải sửa: " + "; ".join(problems[:5])
        if problems:
            log(f"  !! {path.name}: {'; '.join(problems[:3])}")
        outs.append(out)
    body = "\n\n".join(outs)
    name = path.name
    m = re.match(r"^(\d\d)-(.*)$", name)
    if m:
        siblings = sorted((tb.ROOT / "book" / "vi").glob(f"{m.group(1)}-*.md"))
        if siblings:
            out_name = siblings[0].name  # keep the record next to its chapter
        else:
            out_name = f"{m.group(1)}-{tb.slugify(head['title'], 40)}.md"
    else:
        prefix, _, tail = name.partition("-")
        out_name = f"{PREFIX_MAP.get(prefix, tb.slugify(prefix, 12))}-{tb.slugify(head['title'], 40)}.md"
    out_path = OUT_DIR / out_name
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        tb.status_line(f"docs/核实记录/{name}", f"../../../docs/核实记录/{name}")
        + "\n[← Về mục lục](../../../README.vi.md)\n\n"
        + f"# {head['title']}\n\n{head['intro']}\n\n{body}\n",
        encoding="utf-8",
    )
    han = len(tb.HAN_RE.findall(out_path.read_text(encoding="utf-8")))
    log(f"  wrote docs/核实记录/vi/{out_name} ({len(sections)} mục, {han} chữ Hán)")
    return {"file": out_name, "source": name, "sections": len(sections), "hanzi": han}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="comma separated source file prefixes")
    args = ap.parse_args()
    files = sorted(p for p in SRC_DIR.glob("*.md"))
    if args.only:
        wanted = {x.strip() for x in args.only.split(",") if x.strip()}
        files = [p for p in files if p.name.split("-")[0] in wanted]
    log(f"{len(files)} file(s), {tb.WORKERS} workers, transport={tb.TRANSPORT}")
    results = []
    with futures.ThreadPoolExecutor(max_workers=max(1, min(tb.WORKERS, len(files)))) as ex:
        for res in ex.map(translate_file, files):
            results.append(res)
    man = OUT_DIR / "manifest.json"
    man.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"done: {len(results)} file(s), tổng chữ Hán còn lại {sum(r['hanzi'] for r in results)}")


if __name__ == "__main__":
    main()
