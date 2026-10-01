#!/usr/bin/env python3
"""Add Vietnamese renderings for the Chinese text the translation keeps on purpose.

Three kinds of repairs, all additive except for whole-line leftovers:

* quote  - a line carries verbatim Chinese quotes 「…」 (regulation text kept as
           evidence). Each quote gets "(dịch: …)" right after it; the Chinese
           stays untouched.
* prose  - a line is still Chinese prose or a Chinese table row. The whole line
           is translated, keeping numbers, URLs and document numbers.
* gloss  - a heading that is only a Chinese law name gets "(nghĩa: …)" appended.

The build scripts read the files afterwards, so nothing structural moves: only
line content changes.

    VI_TRANSPORT=hermes VI_HERMES_MODEL=deepseek-flash VI_HERMES_PROVIDER=deepseek \\
      python3 tools/translate-vi/gloss_vi.py --area records
    python3 tools/translate-vi/gloss_vi.py --area book --dry-run
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import os
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_book as tb  # noqa: E402

ROOT = tb.ROOT
HAN = tb.HAN_RE
import re  # noqa: E402
TAG_RE = tb.TAG_RE
# only quotes that actually contain Chinese need a Vietnamese rendering;
# 「English …」 quotes are readable as they stand
QUOTE_RE = __import__("re").compile(r"「[^」]*[\u4e00-\u9fff][^」]*」")
LAW_RE = __import__("re").compile(r"《[^》]{2,}》")
VI_DIA = __import__("re").compile(r"[ăâđêôơưàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]")
URL_RE = tb.URL_RE
DIGIT_RE = tb.DIGIT_RUN_RE

AREAS = {
    "book": lambda: sorted((ROOT / "book" / "vi").glob("*.md")),
    "docs": lambda: sorted((ROOT / "docs" / "vi").glob("*.md")),
    "records": lambda: sorted((ROOT / "docs" / "核实记录" / "vi").glob("*.md")),
    "readme": lambda: [ROOT / "README.vi.md"],
}

SYSTEM = (
    "Bạn là biên tập viên song ngữ Trung Việt cho một cuốn sách dịch. "
    "Bản gốc tiếng Trung được giữ lại ở một số chỗ có chủ đích: trích nguyên văn văn bản quy phạm, "
    "tên văn bản, số hiệu văn bản. Nhiệm vụ là thêm phần tiếng Việt bên cạnh, không sửa phần tiếng Trung. "
    "Tuyệt đối giữ nguyên mọi URL, DOI, số hiệu, con số và cấu trúc markdown của dòng. "
    "Trả về đúng JSON theo yêu cầu, không thêm chú thích ngoài JSON."
)


def collect(path: Path) -> list[dict]:
    items = []
    for i, ln in enumerate(path.read_text(encoding="utf-8").split("\n")):
        if TAG_RE.match(ln) or not HAN.search(ln):
            continue
        # idempotent: never gloss the same quote twice
        # one Vietnamese rendering per line is enough: earlier passes append a
        # combined translation after the last quote, so only lines without any
        # "(dịch:" are still pending (keeps re-runs idempotent)
        pending_quotes = QUOTE_RE.findall(ln) if "(dịch:" not in ln else []
        if pending_quotes:
            kind = "quote"
        elif ln.startswith("#"):
            # a heading needs a gloss only when its Chinese law name has none:
            # "(疾控中心)" style parentheticals already carry the Vietnamese term
            # pending only when Han remains outside parentheticals: a heading like
            # "trung tâm kiểm soát bệnh tật (疾控中心)" already carries the Vietnamese term
            outside_parens = re.sub(r"[（(][^（()）]*[\u4e00-\u9fff][^（()）]*[)）]", "", ln)
            glossed_marker = "(nghĩa:" in ln or "→" in ln
            kind = "gloss" if HAN.findall(outside_parens) and not glossed_marker else None
        else:
            outside = HAN.findall(LAW_RE.sub("", QUOTE_RE.sub("", ln)))
            kind = "prose" if len(outside) >= 2 and not VI_DIA.search(ln) else None
        if kind:
            items.append({"line": i, "kind": kind, "text": ln})
    return items


def batches(items: list[dict], size: int) -> list[list[dict]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def validate(item: dict, out: str) -> list[str]:
    bad = []
    out = out.strip("\n")
    for label, rx in (("URL", URL_RE), ("DOI", tb.DOI_RE)):
        miss = set(rx.findall(item["text"])) - set(rx.findall(out))
        if miss:
            bad.append(f"mất {label}")
    if item["kind"] == "quote":
        for q in QUOTE_RE.findall(item["text"]):
            if q not in out:
                bad.append("trích dẫn Hán bị đổi")
                break
        if not VI_DIA.search(out):
            bad.append("chưa thêm tiếng Việt")
    else:
        if not VI_DIA.search(out):
            bad.append("chưa dịch")
    return bad


def work(batch: list[dict]) -> list[tuple[int, str]]:
    payload = json.dumps(
        [
            {
                "id": it["line"],
                "kind": it["kind"],
                "text": it["text"],
                "yêu cầu": {
                    "quote": "Chèn ngay sau mỗi đoạn 「…」 một cụm ` (dịch: <bản dịch tiếng Việt>)`. Giữ nguyên đoạn Hán và mọi thứ khác trong dòng.",
                    "prose": "Dịch cả dòng sang tiếng Việt. Giữ nguyên số liệu, URL, số hiệu văn bản; tên văn bản Trung Quốc giữ chữ Hán kèm nghĩa trong ngoặc.",
                    "gloss": "Giữ nguyên phần còn lại của dòng. Tên văn bản Trung Quốc: thêm ` (nghĩa: <nghĩa tiếng Việt>)` ngay sau tên đó. Chữ số Hán (一、二、八…) nếu có thì đổi thành số Ả Rập, không thêm gì khác.",
                }[it["kind"]],
            }
            for it in batch
        ],
        ensure_ascii=False,
        indent=1,
    )
    last: Exception | None = None
    for _ in range(3):
        raw = tb.call_gemini(
            "Xử lý từng mục trong mảng JSON dưới đây. Trả về JSON dạng "
            '{"results":[{"id":<id>,"out":"<dòng đã sửa>"}]} đúng số mục:\n\n' + payload,
            SYSTEM,
            temperature=0.2,
        )
        try:
            data = tb.parse_json_loose(raw)
            results = data.get("results") if isinstance(data, dict) else None
            if not isinstance(results, list) or len(results) != len(batch):
                raise ValueError("số mục trả về không khớp")
            by_id = {int(r["id"]): str(r["out"]) for r in results}
            problems = []
            for it in batch:
                out = by_id.get(it["line"])
                if out is None:
                    problems.append(f"thiếu id {it['line']}")
                    continue
                problems += [f"{it['line']}: {p}" for p in validate(it, out)]
            if problems:
                raise ValueError("; ".join(problems[:4]))
            return [(it["line"], by_id[it["line"]].strip("\n")) for it in batch]
        except Exception as exc:  # noqa: BLE001
            last = exc
    print(f"  !! lô lỗi: {last}")
    return []


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--area", default="all", choices=["all", *AREAS])
    ap.add_argument("--size", type=int, default=10)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", default=str(tb.HERE / "state" / "gloss-report.json"))
    args = ap.parse_args()

    areas = AREAS.keys() if args.area == "all" else [args.area]
    files: list[Path] = []
    for a in areas:
        files += AREAS[a]()
    print(f"{len(files)} tệp, transport={tb.TRANSPORT}, workers={tb.WORKERS}×{os.environ.get('VI_INNER_WORKERS', '3')}")

    plan: dict[Path, list[dict]] = {f: collect(f) for f in files}
    total = sum(len(v) for v in plan.values())
    by_kind = {}
    for v in plan.values():
        for it in v:
            by_kind[it["kind"]] = by_kind.get(it["kind"], 0) + 1
    print(f"{total} dòng cần xử lý: {by_kind}")
    if args.dry_run:
        for f, items in list(plan.items())[:3]:
            for it in items[:3]:
                print(f"  {f.relative_to(ROOT)}:{it['line'] + 1} [{it['kind']}] {it['text'][:110]}")
        return

    lock = threading.Lock()
    report = []

    def one_file(path: Path) -> None:
        items = plan[path]
        if not items:
            return
        edits: dict[int, str] = {}
        inner = int(os.environ.get("VI_INNER_WORKERS", "3"))
        with futures.ThreadPoolExecutor(max_workers=min(inner, len(batches(items, args.size)))) as ex:
            for res in ex.map(work, batches(items, args.size)):
                for line, out in res:
                    edits[line] = out
        if not edits:
            print(f"  -- {path.name}: không sửa được dòng nào")
            return
        lines = path.read_text(encoding="utf-8").split("\n")
        for line, out in edits.items():
            lines[line] = out
        path.write_text("\n".join(lines), encoding="utf-8")
        with lock:
            report.append({"file": str(path.relative_to(ROOT)), "lines": len(edits), "of": len(items)})
            print(f"  ok {path.relative_to(ROOT)}: {len(edits)}/{len(items)} dòng")

    with futures.ThreadPoolExecutor(max_workers=max(1, min(tb.WORKERS, len(files)))) as ex:
        list(ex.map(one_file, files))
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    done = sum(r["lines"] for r in report)
    print(f"xong: {done}/{total} dòng, báo cáo ở {Path(args.report).relative_to(ROOT)}")


if __name__ == "__main__":
    main()
