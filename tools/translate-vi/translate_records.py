#!/usr/bin/env python3
"""Translate docs/核实记录/*.md (source verification records) into docs/核实记录/vi/.

These files are per-source notes: a URL, the English sentence quoted from the
paper, and Chinese commentary. Rules on top of the shared system prompt:
URLs, DOIs, English titles and English quotations stay byte-identical, the
label 原文 becomes "Nguyên văn", and the Chinese commentary is translated.

    VI_TRANSPORT=hermes VI_WORKERS=16 python3 tools/translate-vi/translate_records.py
    python3 tools/translate-vi/translate_records.py --only 01,02
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import os
import re
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_book as tb  # noqa: E402

SRC_DIR = tb.ROOT / "docs" / "核实记录"
tb.REUSE_NAME = os.environ.get("VI_REUSE_NAME", "") == "1"
OUT_DIR = SRC_DIR / "vi"
HEAD_RE = re.compile(r"^##\s+(.*)$")
URL_RE = tb.URL_RE
DIGIT_RUN_RE = tb.DIGIT_RUN_RE
PREFIX_MAP = {
    "追加": "bo-sung",
    "新增": "moi-them",
    "排查": "rac-soat",
    "重写": "viet-lai",
    "issue": "issue",
}
RECORD_RULES = (
    tb.SYSTEM_RULES
    + """
Bổ sung cho tệp hồ sơ kiểm chứng nguồn:
- Giữ nguyên từng ký tự: URL, DOI, số hiệu văn bản, tên tài liệu và tên tạp chí tiếng Anh, mọi câu trích nguyên văn trong dấu ngoặc kép.
- Nhãn 「原文：」 luôn viết đúng là "Nguyên văn:" (không dùng "Câu trích", "Trích dẫn" hay cách gọi khác). Nhãn 「核实日期」 viết "Ngày kiểm chứng".
- Dịch toàn bộ chú thích tiếng Trung, kể cả ghi chú trong ngoặc và ghi chú ở cuối dòng.
- Giữ nguyên cấu trúc danh sách: số dấu gạch đầu dòng, mức thụt lề, thứ tự dòng.
- Không thêm nhận xét của người dịch.
"""
)
_print_lock = threading.Lock()


def log(msg: str) -> None:
    with _print_lock:
        print(msg, flush=True)


def pack_sections(title: str, intro: str, sections: list[tuple[str, str]], cap: int = 4200) -> list[str]:
    """Pack heading+body sections into chunks under `cap` characters."""
    chunks, cur, size = [], [], len(title) + len(intro)
    for heading, body in sections:
        piece = f"{heading}\n{body}".strip()
        if cur and size + len(piece) > cap:
            chunks.append("\n\n".join(cur))
            cur, size = [], 0
        cur.append(piece)
        size += len(piece) + 2
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def validate(src: str, out: str) -> list[str]:
    problems = []
    for label, pattern in (("URL", URL_RE), ("DOI", tb.DOI_RE)):
        miss = set(pattern.findall(src)) - set(pattern.findall(out))
        if miss:
            problems.append(f"thiếu {label} {sorted(miss)[:2]}")

    def nums(text: str) -> set[str]:
        return set(DIGIT_RUN_RE.findall(re.sub(r"(?<=\d)[.,](?=\d{3})+", "", text)))

    miss_nums = {n for n in nums(src) if not re.search(rf"{n}\s*[万亿]", src)} - nums(out)
    if miss_nums:
        problems.append(f"thiếu số {sorted(miss_nums)[:5]}")
    # labels are advisory only: 原文 also appears in table headers, so a count
    # mismatch is not evidence of dropped content
    if len(re.findall(r"^##", src, flags=re.M)) != len(re.findall(r"^##", out, flags=re.M)):
        problems.append("lệch số tiêu đề '##'")
    return problems


def translate_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    h1 = next((ln for ln in lines if ln.startswith("# ")), f"# {path.stem}")
    rest = lines[lines.index(h1) + 1 :] if h1 in lines else lines
    intro, sections, cur_head, cur = [], [], None, []
    for ln in rest:
        m = HEAD_RE.match(ln)
        if m:
            if cur_head is not None:
                sections.append((cur_head, "\n".join(cur).strip("\n")))
            cur_head, cur = ln, []
        elif cur_head is None:
            intro.append(ln)
        else:
            cur.append(ln)
    if cur_head is not None:
        sections.append((cur_head, "\n".join(cur).strip("\n")))
    intro_text = "\n".join(intro).strip("\n")

    schema = {
        "type": "object",
        "properties": {"title": {"type": "string"}, "intro": {"type": "string"}},
        "required": ["title", "intro"],
    }
    head: dict = {}
    for attempt in range(3):
        try:
            head = tb.parse_json_loose(
                tb.call_gemini(
                    f"Hồ sơ kiểm chứng nguồn của sách, tệp gốc docs/核实记录/{path.name}.\n"
                    f"Dịch tiêu đề và đoạn mở đầu sang tiếng Việt, trả về JSON hai khóa title và intro, "
                    f"không thêm gì khác:\n\n{h1}\n\n{intro_text}",
                    RECORD_RULES,
                    schema=schema,
                    temperature=0.3,
                )
            )
            if head.get("title") and head.get("intro") is not None:
                break
        except Exception as exc:  # noqa: BLE001
            log(f"  .. {path.name}: JSON tiêu đề lần {attempt + 1} lỗi ({exc}); thử lại")
        head = {}
    if not head:
        # fallback: ask for the two pieces as plain text, one per call
        title = tb.unfence(
            tb.call_gemini(f"Dịch tiêu đề sau sang tiếng Việt, chỉ trả về tiêu đề:\n\n{h1}", RECORD_RULES)
        ).lstrip("# ").strip()
        intro = tb.unfence(
            tb.call_gemini(
                f"Dịch đoạn mở đầu sau sang tiếng Việt, chỉ trả về đoạn dịch:\n\n{intro_text}",
                RECORD_RULES,
            )
        )
        head = {"title": title, "intro": intro}
    head["title"] = re.sub(r"^#+\s*", "", head["title"]).strip()
    head["intro"] = head["intro"].strip()
    job = pack_sections(h1, intro_text, sections)
    outs = []
    for chunk in job:
        system, out, problems = RECORD_RULES, "", []
        for _ in range(3):
            out = tb.unfence(
                tb.call_gemini(
                    f"Dịch khối hồ sơ kiểm chứng sau sang tiếng Việt, giữ nguyên URL, số hiệu và mọi câu "
                    f"trích tiếng Anh, chỉ trả về markdown:\n\n{chunk}",
                    system,
                    temperature=0.2,
                )
            )
            problems = validate(chunk, out)
            if not problems:
                break
            system = RECORD_RULES + "\n\nLẦN TRƯỚC SAI, phải sửa: " + "; ".join(problems[:5])
        if problems:
            log(f"  !! {path.name}: {'; '.join(problems[:3])}")
        outs.append(out)
    body = "\n\n".join(outs)
    name = path.name
    m = re.match(r"^(\d\d)-(.*)$", name)
    if m:
        prefix = m.group(1)
    else:
        head_prefix, _, _tail = name.partition("-")
        prefix = PREFIX_MAP.get(head_prefix, tb.slugify(head_prefix, 12))
    out_name = f"{prefix}-{tb.slugify(head['title'], 40)}.md"
    if tb.REUSE_NAME:  # keep the existing filename so a redo does not duplicate it
        for existing in OUT_DIR.glob("*.md"):
            m3 = re.search(r"核实记录/([^\]]+\.md)\]", existing.read_text(encoding="utf-8"))
            if m3 and m3.group(1) == name:
                out_name = existing.name
                break
    # two source records can share a chapter prefix (07-a.md, 07-b.md): never
    # let one overwrite the other
    if (OUT_DIR / out_name).exists():
        m2 = re.search(r"核实记录/([^\]]+\.md)\]", (OUT_DIR / out_name).read_text(encoding="utf-8"))
        if m2 and m2.group(1) != name:
            out_name = out_name[:-3] + f"-{tb.slugify(name.split('-', 1)[1], 16)}.md"
    out_path = OUT_DIR / out_name
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        tb.status_line(f"docs/核实记录/{name}", f"../../../docs/核实记录/{name}")
        + "\n[← Về mục lục](../../../README.vi.md)\n\n"
        + f"# {head['title']}\n\n{head['intro']}\n\n{body}\n",
        encoding="utf-8",
    )
    han = len(tb.HAN_RE.findall(out_path.read_text(encoding="utf-8")))
    log(f"  wrote docs/核实记录/vi/{out_name} ({len(sections)} mục, {han} chữ Hán)")
    return {
        "file": out_name,
        "source": name,
        "sections": len(sections),
        "hanzi": han,
        "model": f"{tb.TRANSPORT}:{tb.HERMES_MODEL}" if tb.TRANSPORT == "hermes" else f"gemini:{tb.MODEL}",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="comma separated source file prefixes")
    ap.add_argument("--missing", action="store_true", help="chỉ dịch tệp chưa có bản dịch")
    ap.add_argument("--sources", default="", help="tên tệp gốc cụ thể, cách nhau bằng dấu phẩy")
    args = ap.parse_args()
    files = sorted(p for p in SRC_DIR.glob("*.md"))
    if args.only:
        wanted = {x.strip() for x in args.only.split(",") if x.strip()}
        files = [p for p in files if p.name.split("-")[0] in wanted]
    if args.sources:
        wanted = {x.strip() for x in args.sources.split(",") if x.strip()}
        files = [p for p in files if p.name in wanted]
    if args.missing:
        done: set[str] = set()
        if (OUT_DIR / "manifest.json").exists():
            done = {e["source"] for e in json.loads((OUT_DIR / "manifest.json").read_text(encoding="utf-8"))}
        for vi_file in OUT_DIR.glob("*.md") if OUT_DIR.exists() else []:
            m = re.search(r"核实记录/([^\]]+\.md)\]", vi_file.read_text(encoding="utf-8"))
            if m:
                done.add(m.group(1))
        files = [p for p in files if p.name not in done]
    log(f"{len(files)} file(s), {tb.WORKERS} workers, transport={tb.TRANSPORT}"
        + (f" model={tb.HERMES_MODEL} via {tb.HERMES_PROVIDER}" if tb.TRANSPORT == "hermes" else ""))
    results: list[dict] = []
    if not files:
        log("không còn tệp nào cần dịch")
        return
    failed = []
    with futures.ThreadPoolExecutor(max_workers=max(1, min(tb.WORKERS, len(files)))) as ex:
        for fut in futures.as_completed({ex.submit(translate_file, p): p for p in files}):
            try:
                results.append(fut.result())
            except Exception as exc:  # noqa: BLE001
                failed.append(f"{files[0].name}: {exc}")
                log(f"  !! lỗi ở một tệp: {exc}")
    if failed:
        log(f"{len(failed)} tệp lỗi")
    man = OUT_DIR / "manifest.json"
    merged: dict[str, dict] = {}
    if man.exists():
        for entry in json.loads(man.read_text(encoding="utf-8")):
            merged[entry["source"]] = entry
    for entry in results:
        merged[entry["source"]] = entry
    man.write_text(
        json.dumps([merged[k] for k in sorted(merged)], ensure_ascii=False, indent=1), encoding="utf-8"
    )
    log(f"done: {len(results)} file(s) mới, manifest có {len(merged)}; chữ Hán còn lại {sum(r['hanzi'] for r in results)}")


if __name__ == "__main__":
    main()
