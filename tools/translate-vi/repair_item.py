#!/usr/bin/env python3
"""Re-translate a single item and splice it back into its translated chapter.

Used when verify_vi.py flags one item (a dropped URL, a truncated source line)
and re-running the whole chapter would be wasteful.

    python3 tools/translate-vi/repair_item.py 31 4
    python3 tools/translate-vi/repair_item.py 31 4 --transport hermes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import translate_book as tb

ITEM_SPLIT = re.compile(r"(?m)^(?=### \d+\.)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("item", type=int)
    ap.add_argument("--transport", default="hermes", choices=["gemini", "hermes"])
    args = ap.parse_args()
    tb.TRANSPORT = args.transport

    src_path = next(p for p in (tb.ROOT / "book").glob(f"{int(args.chapter):02d}-*.md"))
    ch = tb.parse_chapter(src_path)
    vi_path = next(p for p in (tb.ROOT / "book" / "vi").glob(f"{int(args.chapter):02d}-*.md"))
    item = next(it for it in ch["items"] if it["n"] == args.item)
    titles = tb.run_titles([ch])
    meta = titles[src_path.name]

    payload, _ = tb.strip_tags(f"### {item['n']}. {item['title_cn']}\n" + "\n".join(item["lines"]))
    ctx_block = (
        f'Bối cảnh: đây là phần {int(ch["number"])} của sách, tiêu đề tiếng Việt: "{meta["title"]}".\n'
        f"Tiêu đề tiếng Việt của mục này: \"{meta['items'][str(item['n'])]}\"\n"
    )
    system = tb.SYSTEM_RULES
    out, problems = "", []
    for _ in range(4):
        out = tb.unfence(tb.call_gemini(f"{ctx_block}\nDịch sang tiếng Việt, chỉ trả về markdown:\n\n{payload}", system))
        problems = tb.validate_chunk([item], out)
        if not problems:
            break
        system = tb.SYSTEM_RULES + "\n\nLẦN TRƯỚC SAI, phải sửa: " + "; ".join(problems[:6])
    if problems:
        print("vẫn còn lỗi:", problems)
        print(out[:400])
        sys.exit(1)

    translated = out.rstrip()
    text = vi_path.read_text(encoding="utf-8")
    blocks = ITEM_SPLIT.split(text)
    replaced = False
    for i, b in enumerate(blocks):
        if re.match(rf"### {args.item}\.", b):
            body_lines = translated.split("\n")
            tags = [ln for ln in b.split("\n") if tb.TAG_RE.match(ln)]
            new_block = "\n".join(body_lines[:1] + tags + body_lines[1:]).rstrip() + "\n\n"
            blocks[i] = new_block
            replaced = True
            break
    if not replaced:
        sys.exit(f"mục {args.item} không có trong {vi_path.name}")
    vi_path.write_text("".join(blocks), encoding="utf-8")
    print(f"đã dịch lại mục {args.item} của {vi_path.relative_to(tb.ROOT)} ({len(translated)} ký tự)")


if __name__ == "__main__":
    main()
