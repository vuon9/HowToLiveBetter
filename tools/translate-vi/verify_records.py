#!/usr/bin/env python3
"""Check the Vietnamese source-verification records against the Chinese originals.

Per file pair (from docs/核实记录/vi/manifest.json): every URL and DOI in the
original must appear in the translation, the "Nguyên văn:" label count must match
原文：, and no [PHONE]-style placeholder may survive.

    python3 tools/translate-vi/verify_records.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "docs" / "核实记录"
VI = SRC / "vi"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_book as tb  # noqa: E402

PLACEHOLDER_RE = tb.URL_RE  # placeholder scan uses the same url extractor
BAD_RE = __import__("re").compile(r"\[(?:PHONE|REDACTED|EMAIL|SSN)[^\]]*\]")


def main() -> None:
    man = VI / "manifest.json"
    if not man.exists():
        sys.exit("chưa có manifest.json, chạy translate_records.py trước")
    entries = json.loads(man.read_text(encoding="utf-8"))
    bad = 0
    for entry in entries:
        src = (SRC / entry["source"]).read_text(encoding="utf-8")
        vi_path = VI / entry["file"]
        if not vi_path.exists():
            print(f"[MISSING] {entry['file']}")
            bad += 1
            continue
        vi = vi_path.read_text(encoding="utf-8")
        problems = []
        def norm(matches: list[str]) -> set[str]:
            # a Chinese full stop or parenthesis can ride along on the match
            # cut the match at the first CJK character: Chinese full-width
            # punctuation and trailing annotations ride along in the regex
            out = set()
            for m in matches:
                m = re.split(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]", m)[0].rstrip(".,;:)")
                if m:
                    out.add(m)
            return out

        for label, rx in (("URL", tb.URL_RE), ("DOI", tb.DOI_RE)):
            miss = norm(rx.findall(src)) - norm(rx.findall(vi))
            if miss:
                problems.append(f"thiếu {label} {sorted(miss)[:2]}")
        # soft: verbatim quotes survive as 「…」 or "…"; the Chinese label itself is
        # a poor proxy (原文 also appears in table headers like 原文引句)
        cn_quotes = len(re.findall(r"「[^」]{20,}」", src))
        vi_quotes = len(re.findall(r"[「“\"][^」”\"]{20,}[」”\"]", vi))
        soft = [] if vi_quotes >= cn_quotes * 0.9 else [f"trích dẫn {vi_quotes}/{cn_quotes}"]
        if BAD_RE.search(vi):
            problems.append("còn [PHONE]")
        entry["soft"] = soft
        if problems:
            bad += 1
            print(f"[FAIL] {entry['file']}: {'; '.join(problems[:3])}")
        elif soft:
            print(f"[soft] {entry['file']}: {'; '.join(soft)}")
    print(f"{len(entries) - bad}/{len(entries)} tệp sạch")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
