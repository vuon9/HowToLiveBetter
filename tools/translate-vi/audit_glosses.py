#!/usr/bin/env python3
"""Audit Chinese text that is still visible to a Vietnamese reader.

The translation keeps certain Chinese strings on purpose: regulation names and
document numbers in source lines, verbatim regulation quotes, institution names
(the rule is to keep the Chinese and add a Vietnamese gloss next to it) and the
opaque cost-tag comments. This script lists every line that carries Han
characters and says whether a Vietnamese gloss already sits next to them, so the
gaps can be filled.

    python3 tools/translate-vi/audit_glosses.py            # summary
    python3 tools/translate-vi/audit_glosses.py --list      # every line
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HAN_RE = re.compile(r"[\u4e00-\u9fff]")
TAG_RE = re.compile(r"^<!--\s*成本标签:.*-->\s*$")
# a Vietnamese gloss right after a Chinese run, e.g. 公安部 (Bộ Công an) or
# 《失业保险条例》 (Quy định về bảo hiểm thất nghiệp)
GLOSS_AFTER_RE = re.compile(r"[\u4e00-\u9fff》」]+\s*[（(]([^()（）]{2,80})[)）]")
VI_DIACRITICS = re.compile(r"[ăâđêôơưàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]")

CATEGORIES = {
    "cost-tag": lambda ln, f: TAG_RE.match(ln),
    "source": lambda ln, f: ln.startswith("- Nguồn:") or ln.startswith("- 来源："),
    "note": lambda ln, f: ln.startswith("- Ghi chú:") or ln.startswith("- 备注："),
    "field": lambda ln, f: ln.startswith("- ") and not ln.startswith(("- Nguồn:", "- Ghi chú:")),
    "record-quote": lambda ln, f: "核实记录/vi" in str(f),
    "other": lambda ln, f: True,
}


def category(ln: str, path: Path) -> str:
    for name, test in CATEGORIES.items():
        if test(ln, path):
            return name
    return "other"


def targets() -> list[Path]:
    files = sorted((ROOT / "book" / "vi").glob("*.md"))
    files += sorted((ROOT / "docs" / "vi").glob("*.md"))
    files += sorted((ROOT / "docs" / "核实记录" / "vi").glob("*.md"))
    if (ROOT / "README.vi.md").exists():
        files.append(ROOT / "README.vi.md")
    if (ROOT / "index.vi.html").exists():
        files.append(ROOT / "index.vi.html")
    return files


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    per_cat: Counter = Counter()
    unglossed: Counter = Counter()
    examples: dict[str, list[str]] = {}
    for path in targets():
        for i, ln in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            if not HAN_RE.search(ln):
                continue
            cat = category(ln, path)
            per_cat[cat] += 1
            runs = [m.group(0) for m in re.finditer(r"[\u4e00-\u9fff]+", ln)]
            has_vi = bool(VI_DIACRITICS.search(ln)) or bool(GLOSS_AFTER_RE.search(ln))
            if not has_vi:
                unglossed[cat] += 1
                examples.setdefault(cat, []).append(f"{path.relative_to(ROOT)}:{i}: {ln[:150]}")
            elif args.list:
                examples.setdefault(cat + " (đã có chú thích)", []).append(
                    f"{path.relative_to(ROOT)}:{i}: {ln[:150]}"
                )
    print(f"{'nhóm':<14}{'dòng có chữ Hán':>18}{'chưa có chú thích':>20}")
    for cat, n in per_cat.most_common():
        print(f"{cat:<14}{n:>18}{unglossed[cat]:>20}")
    for cat, rows in examples.items():
        print(f"\n=== {cat} ({len(rows)}) ===")
        for row in rows[: (8 if not args.list else len(rows))]:
            print("  ", row)


if __name__ == "__main__":
    main()
