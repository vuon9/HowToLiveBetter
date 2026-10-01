#!/usr/bin/env python3
"""Rename translated chapters to the canonical slug (word-boundary cut).

Run after a translation pass if slugify() changed, so filenames stay aligned
with the slugs used for README.vi.md links:

    python3 tools/translate-vi/rename_chapters.py --dry-run
    python3 tools/translate-vi/rename_chapters.py
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from translate_book import ROOT, STATE_DIR, chapters_list, slugify


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    state = json.loads((STATE_DIR / "vi-titles.json").read_text(encoding="utf-8"))
    renames = []
    for ch in chapters_list():
        meta = state.get(ch["path"].name)
        if not meta:
            continue
        want = f"{ch['path'].name[:2]}-{slugify(meta['title'])}.md"
        have = sorted((ROOT / "book" / "vi").glob(f"{ch['path'].name[:2]}-*.md"))
        if have and have[0].name != want:
            renames.append((have[0], ROOT / "book" / "vi" / want))
    for src, dst in renames:
        print(f"{src.name} -> {dst.name}")
        if not args.dry_run:
            src.rename(dst)
    print(f"{len(renames)} tệp{' (dry-run)' if args.dry_run else ' đã đổi tên'}")


if __name__ == "__main__":
    main()
