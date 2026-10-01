#!/usr/bin/env python3
"""Write translations.json: the Vietnamese translation registry at the repo root.

One entry per translated file, in the shape the other language forks publish
(status + file + sections/items + which model produced it), so the state of the
Vietnamese edition is visible without reading the tools directory.

    python3 tools/translate-vi/make_registry.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

TAG_RE = re.compile(r"^<!--\s*成本标签:.*-->\s*$")
HAN_RE = re.compile(r"[\u4e00-\u9fff]")


def hanzi_outside_tags(path: Path) -> int:
    return sum(
        len(HAN_RE.findall(ln))
        for ln in path.read_text(encoding="utf-8").split("\n")
        if not TAG_RE.match(ln)
    )


def main() -> None:
    status = json.loads((HERE / "status.json").read_text(encoding="utf-8"))
    docs_manifest = HERE / "state" / "vi-docs-titles.json"
    docs = json.loads(docs_manifest.read_text(encoding="utf-8")) if docs_manifest.exists() else {}
    records_dir = ROOT / "docs" / "核实记录" / "vi"
    records = json.loads((records_dir / "manifest.json").read_text(encoding="utf-8")) if (records_dir / "manifest.json").exists() else []

    entries: dict[str, dict] = {}
    for key, ch in sorted(status["chapters"].items()):
        vi = ROOT / ch.get("file", "")
        entries[key] = {
            "status": "translated" if ch.get("status") == "reviewed" else ch.get("status", "missing"),
            "source": f"book/{ch['section']}",
            "file": ch.get("file"),
            "items": ch.get("items"),
            "hanzi_kept": hanzi_outside_tags(vi) if vi.exists() else None,
            "hard_issues": ch.get("hard_issues", []),
        }
    for name, meta in sorted(docs.items()):
        entries[f"doc:{name}"] = {
            "status": "translated",
            "source": f"docs/{name}",
            "file": f"docs/vi/{meta['slug']}.md",
            "hanzi_kept": hanzi_outside_tags(ROOT / "docs" / "vi" / f"{meta['slug']}.md"),
        }
    for rec in records:
        entries[f"record:{rec['source']}"] = {
            "status": "translated",
            "source": f"docs/核实记录/{rec['source']}",
            "file": f"docs/核实记录/vi/{rec['file']}",
            "model": rec.get("model"),
            "hanzi_kept": rec.get("hanzi_kept"),
        }
    entries["readme"] = {
        "status": "translated",
        "source": "README.md",
        "file": "README.vi.md",
        "hanzi_kept": hanzi_outside_tags(ROOT / "README.vi.md"),
    }
    entries["site"] = {"status": "translated", "source": "index.html", "file": "index.vi.html", "page": "vi/index.html"}

    out = {
        "description": "Bản dịch tiếng Việt của 《高性价比人生指南》. Bản gốc tiếng Trung luôn là bản có hiệu lực; xem tools/translate-vi/README.md.",
        "language": "vi",
        "layout": {
            "chapters": "book/vi/<NN>-<slug>.md",
            "docs": "docs/vi/<slug>.md",
            "records": "docs/核实记录/vi/<slug>.md",
            "readme": "README.vi.md",
            "site": "index.vi.html, vi/index.html",
            "builds": "dist/HowToLiveBetter-vi.{epub,pdf,html}",
        },
        "counts": {
            "chapters": sum(1 for k in entries if k.isdigit()),
            "items": sum(e.get("items") or 0 for e in entries.values()),
            "docs": sum(1 for k in entries if k.startswith("doc:")),
            "records": sum(1 for k in entries if k.startswith("record:")),
        },
        "files": entries,
    }
    dst = ROOT / "translations.json"
    dst.write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    c = out["counts"]
    print(f"wrote translations.json: {c['chapters']} phần, {c['items']} mục, {c['docs']} bài dài, {c['records']} hồ sơ")


if __name__ == "__main__":
    main()
