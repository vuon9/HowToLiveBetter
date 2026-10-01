#!/usr/bin/env python3
"""Undo redaction placeholders the model transport introduced into the translation.

Long digit runs (10+ digits) come back from the `hermes -z` transport as
`[PHONE]`, because that session applies PII masking to its own answer. URLs and
numbers must stay byte-identical to the Chinese original, so this pass finds
every placeholder and restores the original text: whole URLs are copied from
the source, and placeholders inside numbers are replaced with the matching
digit run of the source line.

    python3 tools/translate-vi/fix_redactions.py --dry-run
    python3 tools/translate-vi/fix_redactions.py
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from translate_book import ROOT, parse_chapter

PLACEHOLDER_RE = re.compile(r"\[(?:PHONE|REDACTED|EMAIL|SSN|CREDIT_CARD|MASKED|ID)[^\]]*\]")
URL_RE = re.compile(r"https?://[^\s<>\]），；;]+")
DIGIT_RUN_RE = re.compile(r"\d{10,}")
ITEM_SPLIT = re.compile(r"(?m)^(?=### \d+\.)")


def item_blocks(text: str) -> dict[int, list[str]]:
    out = {}
    for part in ITEM_SPLIT.split(text):
        m = re.match(r"### (\d+)\.", part)
        if m:
            out[int(m.group(1))] = part.split("\n")
    return out


def fix_chapter(src_path: Path, vi_path: Path) -> int:
    ch = parse_chapter(src_path)
    text = vi_path.read_text(encoding="utf-8")
    src_blocks = {it["n"]: it["lines"] for it in ch["items"]}
    changed = 0
    blocks = ITEM_SPLIT.split(text)
    for bi, part in enumerate(blocks):
        m = re.match(r"### (\d+)\.", part)
        if not m:
            continue
        n = int(m.group(1))
        src_lines = src_blocks.get(n)
        if src_lines is None or not PLACEHOLDER_RE.search(part):
            continue
        lines = part.split("\n")
        src_urls = set(URL_RE.findall("\n".join(src_lines)))
        for li, line in enumerate(lines):
            if not PLACEHOLDER_RE.search(line):
                continue
            for vi_url in URL_RE.findall(line):
                if not PLACEHOLDER_RE.search(vi_url):
                    continue
                prefix = vi_url[:40]
                cand = next((u for u in src_urls if u.startswith(prefix)), None)
                if cand:
                    lines[li] = line.replace(vi_url, cand)
                    line = lines[li]
                    changed += 1
            # placeholders left outside URLs: align with the source digit runs
            src_line = next(
                (s for s in src_lines if len(DIGIT_RUN_RE.findall(s)) >= len(PLACEHOLDER_RE.findall(line))),
                None,
            )
            if src_line and PLACEHOLDER_RE.search(line):
                runs = iter(DIGIT_RUN_RE.findall(src_line))
                lines[li] = PLACEHOLDER_RE.sub(lambda _: next(runs, ""), line)
                changed += 1
        blocks[bi] = "\n".join(lines)
    if changed:
        vi_path.write_text("".join(blocks), encoding="utf-8")
    return changed


def fix_prose(src_path: Path, vi_path: Path) -> int:
    """Repair placeholders in prose files (docs/vi, README.vi.md).

    URL_RE stops at "]", so a URL ending in a placeholder is not a full URL
    match; the placeholder is located first and the URL prefix before it is
    matched against the source URLs instead.
    """
    src_text = src_path.read_text(encoding="utf-8")
    text = vi_path.read_text(encoding="utf-8")
    src_urls = set(URL_RE.findall(src_text))
    changed = 0
    for m in list(PLACEHOLDER_RE.finditer(text)):
        head = re.split(r"[\s<]", text[: m.start()])[-1]
        if not head.startswith("http"):
            continue
        cand = next((u for u in src_urls if u.startswith(head)), None)
        if cand:
            text = text.replace(head + m.group(0), cand)
            changed += 1
    if changed:
        vi_path.write_text(text, encoding="utf-8")
    return changed


def fix_digit_placeholders(src_path: Path, vi_path: Path) -> int:
    """Fallback: put the original digit runs back where [PHONE] stands.

    Used when a placeholder sits inside a URL whose prefix does not literally
    match the source (for example the Europe PMC query form). The original
    digit runs that are missing from the translation are restored in order.
    """
    src_text = src_path.read_text(encoding="utf-8")
    text = vi_path.read_text(encoding="utf-8")
    hits = list(PLACEHOLDER_RE.finditer(text))
    if not hits:
        return 0
    runs = [r for r in DIGIT_RUN_RE.findall(src_text) if r not in text]
    if len(runs) < len(hits):
        return 0
    out, last = [], 0
    for i, m in enumerate(hits):
        out.append(text[last : m.start()])
        out.append(runs[i])
        last = m.end()
    out.append(text[last:])
    vi_path.write_text("".join(out), encoding="utf-8")
    return len(hits)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    total = 0
    for src in sorted(p for p in (ROOT / "book").glob("*.md") if re.match(r"^\d\d-", p.name)):
        vi = sorted((ROOT / "book" / "vi").glob(f"{src.name[:2]}-*.md"))
        if not vi:
            continue
        if args.dry_run:
            n = len(PLACEHOLDER_RE.findall(vi[0].read_text(encoding="utf-8")))
        else:
            n = fix_chapter(src, vi[0])
        if n:
            print(f"{vi[0].name}: {n} chỗ")
        total += n
    for src in sorted((ROOT / "docs").glob("*.md")):
        if src.name == "引用对照.md" or not (ROOT / "docs" / "vi").exists():
            continue
        for vi in (ROOT / "docs" / "vi").glob("*.md"):
            txt = vi.read_text(encoding="utf-8")
            if not PLACEHOLDER_RE.search(txt):
                continue
            n = len(PLACEHOLDER_RE.findall(txt)) if args.dry_run else fix_prose(src, vi)
            if n:
                print(f"{vi.name} (so với docs/{src.name}): {n} chỗ")
            total += n
    man_path = ROOT / "docs" / "核实记录" / "vi" / "manifest.json"
    if man_path.exists():
        import json as _json

        for entry in _json.loads(man_path.read_text(encoding="utf-8")):
            src = ROOT / "docs" / "核实记录" / entry["source"]
            vi = ROOT / "docs" / "核实记录" / "vi" / entry["file"]
            if not vi.exists():
                continue
            txt = vi.read_text(encoding="utf-8")
            if not PLACEHOLDER_RE.search(txt):
                continue
            if args.dry_run:
                n = len(PLACEHOLDER_RE.findall(txt))
            else:
                n = fix_prose(src, vi)
                n += fix_digit_placeholders(src, vi)
            if n:
                print(f"docs/核实记录/vi/{vi.name}: {n} chỗ")
            total += n
    if (ROOT / "README.vi.md").exists():
        txt = (ROOT / "README.vi.md").read_text(encoding="utf-8")
        if PLACEHOLDER_RE.search(txt):
            n = len(PLACEHOLDER_RE.findall(txt)) if args.dry_run else fix_prose(ROOT / "README.md", ROOT / "README.vi.md")
            print(f"README.vi.md: {n} chỗ")
            total += n
    print(f"tổng {total} chỗ{' (dry-run)' if args.dry_run else ' đã sửa'}")


if __name__ == "__main__":
    main()
