#!/usr/bin/env python3
"""Check that index.vi.html can parse the Vietnamese corpus.

Mirrors the page's own parser (same regexes, same order) against README.vi.md
and the book/vi files its table of contents links to, then reports how many
sections and entries come out and how many entries carry each field. Also
asserts that the functional strings the page relies on are still in place.

    python3 tools/translate-vi/verify_index.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "index.vi.html"
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


def main() -> None:
    page = INDEX.read_text(encoding="utf-8")
    missing = [needle for needle in REQUIRED_IN_PAGE if needle not in page]
    for needle in missing:
        print(f"[FAIL] index.vi.html thiếu mốc: {needle}")
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
    ok = not missing and sections == 34 and entries == 649 and all(n >= 649 for n in counts.values()) and tags == 649
    print("\nKẾT QUẢ:", "OK, trang đọc được bản tiếng Việt" if ok else "CÓ VẤN ĐỀ")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
