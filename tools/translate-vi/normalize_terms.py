#!/usr/bin/env python3
"""Make Chinese institution glosses consistent across the Vietnamese translation.

Each chunk is translated on its own, so the same Chinese institution can come
back with two different Vietnamese glosses (for example 人力资源社会保障部 as
both "Bộ Nguồn nhân lực và An sinh xã hội Trung Quốc" and "Bộ Nhân lực và An
sinh Xã hội Trung Quốc"). This script collects every `<Chinese name> (<gloss>)`
pair, asks the model once for the canonical gloss of each disputed name, and
rewrites the variants with that single wording. Only names that already carry a
gloss are touched, so citation text stays as it is.

    python3 tools/translate-vi/normalize_terms.py --dry-run
    python3 tools/translate-vi/normalize_terms.py
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from translate_book import MODEL, ROOT, call_gemini  # noqa: F401  (call_gemini used below)

TAG_RE = re.compile(r"^<!--\s*成本标签:.*-->\s*$")
GLOSS_RE = re.compile(r"([\u4e00-\u9fff]{2,12})\s*\(([^()（）]{2,60})\)")


def TARGETS() -> list[Path]:
    files = list((ROOT / "book" / "vi").glob("*.md"))
    docs_vi = ROOT / "docs" / "vi"
    if docs_vi.exists():
        files += list(docs_vi.glob("*.md"))
    if (ROOT / "README.vi.md").exists():
        files.append(ROOT / "README.vi.md")
    return files


INSTITUTION_SUFFIXES = ("部", "委", "局", "会", "院", "署", "网", "政府", "银行", "中心", "协会", "组织", "厅", "总局", "办公室")
GLOSS_STOPWORDS = ("sửa đổi", "hiệu lực", "áp dụng", "khoản", "Điều", "ban hành", "phần", "chương")
GLOSS_STARTS = ("Bộ ", "Ủy ban", "Cục ", "Chính quyền", "Trang ", "Đại hội", "Tòa án", "Viện ", "Ngân hàng", "Hiệp hội", "Trung tâm", "Tổng cục")


def looks_like_institution_gloss(name: str, gloss: str) -> bool:
    """Keep out law-name annotations that merely sit in front of a parenthesis.

    Only institution names carrying an actual Vietnamese gloss are normalized;
    anything with digits or administrative boilerplate (sửa đổi năm 2018, Điều
    12 ...) is a citation annotation, not a gloss, and must be left alone.
    """
    if not name.endswith(INSTITUTION_SUFFIXES):
        return False
    if any(ch.isdigit() for ch in gloss):
        return False
    if any(word in gloss for word in GLOSS_STOPWORDS):
        return False
    return gloss.startswith(GLOSS_STARTS)


def scan() -> tuple[dict[str, Counter], dict[str, set[str]]]:
    per_file: dict[str, Counter] = defaultdict(Counter)
    variants: dict[str, set[str]] = defaultdict(set)
    for path in TARGETS():
        for ln in path.read_text(encoding="utf-8").split("\n"):
            if TAG_RE.match(ln):
                continue
            for name, gloss in GLOSS_RE.findall(ln):
                gloss = gloss.strip()
                if not looks_like_institution_gloss(name, gloss):
                    continue
                per_file[path.name][name] += 1
                variants[name].add(gloss)
    return per_file, variants


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    _, variants = scan()
    disputed = {n: sorted(v) for n, v in variants.items() if len(v) > 1}
    print(f"{len(disputed)} tên cơ quan có nhiều cách dịch khác nhau")
    for name, opts in sorted(disputed.items()):
        print(f"  {name}: {opts}")
    if not disputed or args.dry_run:
        return

    schema = {
        "type": "object",
        "properties": {
            "choices": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}, "gloss": {"type": "string"}},
                    "required": ["name", "gloss"],
                },
            }
        },
        "required": ["choices"],
    }
    prompt = (
        "Với mỗi tên cơ quan Trung Quốc dưới đây, chọn một cách dịch tiếng Việt duy nhất, "
        "ngắn gọn và đúng chức năng, dùng cho toàn bộ bản dịch:\n\n"
        + "\n".join(f"{name}: {opts}" for name, opts in sorted(disputed.items()))
    )
    data = json.loads(call_gemini(prompt, "Bạn là biên tập viên thuật ngữ.", schema=schema, temperature=0.2))
    chosen = {c["name"]: c["gloss"].strip() for c in data["choices"]}
    changed = 0
    for path in TARGETS():
        text = path.read_text(encoding="utf-8")
        new = text
        for name, opts in disputed.items():
            canon = chosen.get(name)
            if not canon:
                continue
            for opt in opts:
                if opt != canon:
                    new = new.replace(f"{name} ({opt})", f"{name} ({canon})")
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"đã sửa {changed} tệp; {len(chosen)} tên cơ quan được chốt cách dịch")


if __name__ == "__main__":
    main()
