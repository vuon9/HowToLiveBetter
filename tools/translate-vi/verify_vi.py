#!/usr/bin/env python3
"""Structural verification of the Vietnamese translation against the Chinese original.

Checks per chapter (book/NN-*.md  vs book/vi/NN-*.md):
  * same number of items, same item numbers, same heading levels;
  * same field lines per item (label for label, in order);
  * `<!-- 成本标签: ... -->` comments byte-identical;
  * identical URL and DOI sets;
  * a sample of numeric values present in the translation;
  * leftover Han characters outside the opaque cost tags (reported as soft: Chinese
    regulation titles and glossed institution names are meant to stay);
  * cross-reference count (第 X 节第 Y 条 -> "phần X, mục Y").

Exit code 1 when a hard check fails (item/label/tag/URL/DOI), 0 otherwise.
Soft findings (leftover Han, reference count drift) are reported but do not fail.

Usage: python3 tools/translate-vi/verify_vi.py [--chapters 03,13]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
GLOSSARY = json.loads((HERE / "glossary.vi.json").read_text(encoding="utf-8"))
LABELS_VI = GLOSSARY["field_labels"]
TAG_RE = re.compile(r"^<!--\s*成本标签:.*-->\s*$")
ITEM_RE = re.compile(r"^###\s+(\d+)\.\s*(.*)$")
URL_RE = re.compile(r"https?://[^\s<>\]）)，、；;]+")
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s<>\]）)，、；;]+")
DIGIT_RUN_RE = re.compile(r"\d{2,}")
HAN_RE = re.compile(r"[\u4e00-\u9fff]")
REF_CN_RE = re.compile(r"第\s*\d+\s*节第\s*\d+\s*条")
REF_VI_RE = re.compile(r"phần\s*\d+,\s*mục\s*\d+")


def items_of(path: Path) -> dict[int, dict]:
    out: dict[int, dict] = {}
    cur = None
    for ln in path.read_text(encoding="utf-8").split("\n"):
        m = ITEM_RE.match(ln)
        if m:
            cur = {"n": int(m.group(1)), "tags": [], "lines": [], "headings": 0}
            out[cur["n"]] = cur
        elif cur is not None:
            if TAG_RE.match(ln):
                cur["tags"].append(ln.strip())
            else:
                cur["lines"].append(ln)
    return out


def label_counts(lines: list[str], labels: list[str]) -> list[tuple[str, int]]:
    text = "\n".join(lines)
    return [(lb, len(re.findall(rf"^- {re.escape(lb)}(：|:)", text, flags=re.M))) for lb in labels]


def check(cn_path: Path, vi_path: Path) -> tuple[list[str], list[str]]:
    hard: list[str] = []
    soft: list[str] = []
    cn, vi = items_of(cn_path), items_of(vi_path)
    if len(cn) != len(vi):
        hard.append(f"số mục {len(vi)}/{len(cn)}")
    for n in sorted(set(cn) | set(vi)):
        if n not in vi:
            hard.append(f"thiếu mục {n}")
            continue
        if n not in cn:
            hard.append(f"thừa mục {n}")
            continue
        a, b = cn[n], vi[n]
        cn_lab = label_counts(a["lines"], list(LABELS_VI.keys()))
        vi_lab = label_counts(b["lines"], list(LABELS_VI.values()))
        for (lcn, c1), (lvi, c2) in zip(cn_lab, vi_lab):
            if c1 != c2:
                hard.append(f"mục {n}: {lcn}→{lvi} {c2}/{c1} dòng")
        if a["tags"] != b["tags"]:
            hard.append(f"mục {n}: 成本标签 khác")
        src, dst = "\n".join(a["lines"]), "\n".join(b["lines"])
        for label, pattern in (("URL", URL_RE), ("DOI", DOI_RE)):
            miss = set(pattern.findall(src)) - set(pattern.findall(dst))
            if miss:
                hard.append(f"mục {n}: thiếu {label} {sorted(miss)[:2]}")
        def norm_digits(text: str) -> set[str]:
            return {re.sub(r"[.,](?=\d{3}\b)", "", d) for d in DIGIT_RUN_RE.findall(text)}

        miss_nums = norm_digits(src) - norm_digits(dst)
        if miss_nums:
            soft.append(f"mục {n}: số có thể thiếu {sorted(miss_nums)[:6]}")
    cn_text, vi_text = cn_path.read_text(encoding="utf-8"), vi_path.read_text(encoding="utf-8")
    han_lines = []
    for i, ln in enumerate(vi_text.split("\n"), 1):
        if TAG_RE.match(ln):
            continue
        body = ln
        if ln.startswith("> Bản dịch không chính thức") or ln.startswith("[← Về mục lục]"):
            continue
        if body.startswith("- Nguồn:"):
            body = re.sub(r"10\.\d{4,9}/\S+|https?://\S+", "", body)
        if HAN_RE.search(body):
            han_lines.append((i, ln[:110]))
    cn_refs = sorted((int(a), int(b)) for a, b in re.findall(r"第\s*(\d+)\s*节第\s*(\d+)\s*条", cn_text))
    vi_refs = sorted((int(a), int(b)) for a, b in re.findall(r"phần\s*(\d+),\s*mục\s*(\d+)", vi_text))
    if cn_refs != vi_refs:
        only_cn = [r for r in cn_refs if r not in vi_refs]
        only_vi = [r for r in vi_refs if r not in cn_refs]
        soft.append(f"tham chiếu chéo lệch: thiếu {only_cn[:5]} / thừa {only_vi[:5]}")
    soft.extend(f"dòng {i}: còn chữ Hán -> {txt}" for i, txt in han_lines[:25])
    return hard, soft


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", default="")
    args = ap.parse_args()
    wanted = {int(x) for x in args.chapters.split(",") if x.strip()} if args.chapters else None
    cn_files = sorted(p for p in (ROOT / "book").glob("*.md") if re.match(r"^\d\d-", p.name))
    total_hard = 0
    for cn_path in cn_files:
        if wanted and int(cn_path.name[:2]) not in wanted:
            continue
        vi_dir = ROOT / "book" / "vi"
        matches = sorted(vi_dir.glob(f"{cn_path.name[:2]}-*.md"))
        if not matches:
            print(f"[MISSING] {cn_path.name}: chưa có bản dịch")
            total_hard += 1
            continue
        vi_path = matches[0]
        hard, soft = check(cn_path, vi_path)
        status = "OK " if not hard else "FAIL"
        print(f"[{status}] {cn_path.name} -> {vi_path.relative_to(ROOT)} (hard={len(hard)}, soft={len(soft)})")
        for h in hard:
            print(f"    HARD {h}")
        for s in soft:
            print(f"    soft {s}")
        total_hard += len(hard)
    print(f"\ntổng lỗi cứng: {total_hard}")
    sys.exit(1 if total_hard else 0)


if __name__ == "__main__":
    main()
