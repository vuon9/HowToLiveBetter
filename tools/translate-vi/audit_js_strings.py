#!/usr/bin/env python3
"""List the Chinese string literals left in index.vi.html's script.

The page builds part of its interface from JS string tables (card badges, filter
labels, messages). A quote-scanning regex is not enough there: an apostrophe in a
comment swallows the next literal and the real ones stay Chinese unnoticed. This
walks the script the way a tokeniser does (code, line comment, block comment,
string, template, regex) and prints every literal that still contains Han, so a
reviewer can see at a glance whether the leftover is a machine key (must stay
Chinese, compared against the 成本标签 values) or display text (a miss).

    python3 tools/translate-vi/audit_js_strings.py            # list
    python3 tools/translate-vi/audit_js_strings.py --check     # exit 1 on a display string
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HAN = re.compile(r"[\u4e00-\u9fff]")

# Values the page compares against the Chinese cost tags, or keys of its own
# tables. Chinese here is on purpose and matches the corpus.
MACHINE = {
    "钱", "时间", "毅力", "收益", "口径", "成本", "成本标签", "说人话", "证据等级", "来源", "备注",
    "0", "少", "多", "中", "否", "些", "是", "大", "小", "高", "一般", "极高", "死亡率", "金钱",
    "自由", "sec", "ratio", "lens", "grade", "money", "time", "will",
}
REGEX_START = set("(,=:[!&|?{};+-*%~^<>")


def literals(js: str) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    i, n = 0, len(js)
    prev = ""
    while i < n:
        c = js[i]
        nxt = js[i + 1] if i + 1 < n else ""
        if c == "/" and nxt == "/":
            i = js.find("\n", i)
            if i < 0:
                break
        elif c == "/" and nxt == "*":
            i = js.find("*/", i + 2)
            if i < 0:
                break
            i += 2
        elif c == "/" and prev in REGEX_START:
            i += 1
            while i < n and js[i] != "\n":
                if js[i] == "\\":
                    i += 1
                elif js[i] == "/":
                    break
                i += 1
            i += 1
        elif c in "'\"`":
            quote, start = c, i + 1
            i += 1
            buf = []
            while i < n and js[i] != quote:
                if js[i] == "\\":
                    buf.append(js[i : i + 2])
                    i += 2
                    continue
                buf.append(js[i])
                i += 1
            out.append((start, "".join(buf)))
            i += 1
        else:
            if not c.isspace():
                prev = c
            i += 1
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="thoát 1 nếu còn chuỗi hiển thị tiếng Trung")
    args = ap.parse_args()

    page = (ROOT / "index.vi.html").read_text(encoding="utf-8")
    scripts = re.findall(r"<script(?![^>]*ld\+json)[^>]*>(.*?)</script>", page, re.S)
    missed = []
    for js in scripts:
        for _, lit in literals(js):
            if HAN.search(lit) and lit.strip() not in MACHINE and not lit.startswith("/"):
                missed.append(lit)

    if not missed:
        print("OK: không còn chuỗi hiển thị tiếng Trung trong script")
        return
    print(f"{len(missed)} chuỗi tiếng Trung trong script (nghi là chuỗi hiển thị):")
    seen = set()
    for lit in missed:
        key = lit.strip()
        if key in seen:
            continue
        seen.add(key)
        print(f"   {key[:110]!r}")
    if args.check:
        sys.exit(1)


if __name__ == "__main__":
    main()
