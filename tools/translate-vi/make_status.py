#!/usr/bin/env python3
"""Write the Vietnamese translation manifest (tools/translate-vi/status.json).

Per chapter: output file, number of items, leftover Han characters outside the
opaque cost tags, and whether the structural verification passes. Refresh after
any translation run:

    python3 tools/translate-vi/make_status.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_vi import check  # noqa: E402

TAG_RE = re.compile(r"^<!--\s*成本标签:.*-->\s*$")
ITEM_RE = re.compile(r"^###\s+(\d+)\.", re.M)
HAN_RE = re.compile(r"[\u4e00-\u9fff]")


def hanzi_outside_tags(path: Path) -> int:
    total = 0
    for ln in path.read_text(encoding="utf-8").split("\n"):
        if TAG_RE.match(ln):
            continue
        total += len(HAN_RE.findall(ln))
    return total


def main() -> None:
    chapters = {}
    for cn in sorted(p for p in (ROOT / "book").glob("*.md") if re.match(r"^\d\d-", p.name)):
        vi = sorted((ROOT / "book" / "vi").glob(f"{cn.name[:2]}-*.md"))
        entry: dict = {"section": cn.name, "items": len(ITEM_RE.findall(cn.read_text(encoding="utf-8")))}
        if not vi:
            entry["status"] = "missing"
        else:
            hard, soft = check(cn, vi[0])
            entry.update(
                {
                    "status": "reviewed" if not hard else "needs-fix",
                    "file": f"book/vi/{vi[0].name}",
                    "hanzi_outside_tags": hanzi_outside_tags(vi[0]),
                    "hard_issues": hard[:5],
                    "soft_issues": soft[:5],
                }
            )
        chapters[cn.name[:2]] = entry
    docs = {}
    for vi in sorted((ROOT / "docs" / "vi").glob("*.md")) if (ROOT / "docs" / "vi").exists() else []:
        docs[vi.name] = {"hanzi_outside_tags": hanzi_outside_tags(vi)}
    readme = {}
    if (ROOT / "README.vi.md").exists():
        readme = {"hanzi_outside_tags": hanzi_outside_tags(ROOT / "README.vi.md")}
    out = {
        "description": "Trạng thái bản dịch tiếng Việt. Sinh ra bởi tools/translate-vi/make_status.py.",
        "generated_by": "tools/translate-vi/make_status.py",
        "model": "gemini-3.8-flash",
        "chapters": chapters,
        "docs": docs,
        "readme": readme,
    }
    dst = HERE / "status.json"
    dst.write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    done = sum(1 for c in chapters.values() if c.get("status") == "reviewed")
    print(f"wrote {dst.relative_to(ROOT)}: {done}/{len(chapters)} phần dịch xong, {len(docs)} bài dài")


if __name__ == "__main__":
    main()
