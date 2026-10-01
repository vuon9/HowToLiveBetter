#!/usr/bin/env python3
"""Translate the guide (Simplified Chinese) into Vietnamese with Gemini.

Conventions preserved from upstream (CLAUDE.md) and from the existing
translations maintained by dlgrv (their TRANSLATION.md):
  * `<!-- 成本标签: ... -->` comments are opaque: pulled out before the model
    sees the text, re-inserted byte-identical right after the heading, because
    index.html parses them.
  * Field lines stay one-per-line, in source order, with labels from
    glossary.vi.json.
  * Citation lines (来源) keep author names, journal titles, DOIs, URLs and
    Chinese regulation names verbatim; only the label is translated.
  * Output lives under book/vi/, docs/vi/ and README.vi.md, each file carrying
    a provenance status line and a back-link to the Vietnamese table of
    contents.

Usage:
  translate_book.py titles                 # pass 1: chapter/item titles (resumable)
  translate_book.py book [--chapters 03,13]
  translate_book.py readme
  translate_book.py docs
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import os
import random
import re
import sys
import threading
import time
import unicodedata
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE_DIR = HERE / "state"
GLOSSARY = json.loads((HERE / "glossary.vi.json").read_text(encoding="utf-8"))
LABELS_VI = GLOSSARY["field_labels"]
TAG_RE = re.compile(r"^<!--\s*成本标签:.*-->\s*$")
ITEM_RE = re.compile(r"^###\s+(\d+)\.\s*(.*)$")
HEAD_RE = re.compile(r"^(#{1,3})\s+(.+)$")
REF_CHAPTER_ITEM_RE = re.compile(r"第\s*(\d+)\s*节第\s*(\d+)\s*条")
REF_CHAPTER_RE = re.compile(r"第\s*(\d+)\s*节")
REF_ITEM_RE = re.compile(r"第\s*(\d+)\s*条")
URL_RE = re.compile(r"https?://[^\s<>\]）)，、；;]+")
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s<>\]）)，、；;]+")
DIGIT_RUN_RE = re.compile(r"\d{2,}")
HAN_RE = re.compile(r"[\u4e00-\u9fff]")
# A "第 N 条" preceded by one of these is a law article, not a cross-reference
# to a book item: same judgment rule as tools/check-refs.mjs.
LAW_MARKERS = ("法", "条例", "解释", "规定", "办法", "意见", "通知", "〔", "》", "号", "细则", "标准")

MODEL = os.environ.get("VI_MODEL", "gemini-3.8-flash")
WORKERS = int(os.environ.get("VI_WORKERS", "10"))
ATTEMPTS = int(os.environ.get("VI_ATTEMPTS", "8"))
API_BASE = os.environ.get("VI_API_BASE", "https://generativelanguage.googleapis.com/v1beta/models")
KEY_PATH = Path(os.environ.get("VI_KEY_PATH", "~/.hermes/config.yaml")).expanduser()

_print_lock = threading.Lock()
API_KEY = None


def log(msg: str) -> None:
    with _print_lock:
        print(msg, flush=True)


def load_key() -> str:
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("VI_API_KEY")
    if key:
        return key.strip()
    import yaml  # noqa: PLC0415

    cfg = yaml.safe_load(KEY_PATH.read_text(encoding="utf-8"))
    key = (cfg.get("providers", {}).get("gemini", {}) or {}).get("api_key")
    if not key:
        sys.exit(f"no gemini api_key in {KEY_PATH}")
    return key.strip()


def call_gemini(
    prompt: str,
    system: str,
    *,
    schema: dict | None = None,
    temperature: float = 0.25,
    attempts: int | None = None,
) -> str:
    attempts = attempts or ATTEMPTS
    global API_KEY
    if API_KEY is None:
        API_KEY = load_key()
    url = f"{API_BASE}/{MODEL}:generateContent?key={API_KEY}"
    gen: dict = {"temperature": temperature}
    if schema:
        gen["responseMimeType"] = "application/json"
        gen["responseSchema"] = schema
    body = {
        "systemInstruction": {"parts": [{"text": system}]},
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": gen,
    }
    last = None
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(
                url, data=json.dumps(body).encode("utf-8"), headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.load(resp)
            cands = data.get("candidates") or []
            if not cands:
                raise RuntimeError(f"no candidates: {json.dumps(data)[:200]}")
            parts = cands[0].get("content", {}).get("parts") or []
            text = "".join(p.get("text", "") for p in parts).strip()
            if not text:
                raise RuntimeError(f"empty text (finishReason={cands[0].get('finishReason')})")
            return text
        except Exception as exc:  # noqa: BLE001
            last = exc
            if attempt < attempts - 1:
                throttled = "429" in str(exc) or "Too Many Requests" in str(exc)
                wait = min(90, 2 ** attempt) if throttled else min(30, 2 ** attempt)
                time.sleep(wait + random.random())
    raise RuntimeError(f"gemini failed after {attempts} attempts: {last}")


SYSTEM_RULES = (
    """Bạn là dịch giả chuyên nghiệp, dịch sách hướng dẫn đời sống Trung Quốc (giản thể) sang tiếng Việt.

Bản dịch dành cho người đọc Việt Nam phổ thông, không có kiến thức chuyên ngành. Văn phong tự nhiên, bình tĩnh, câu ngắn, đọc một lần là hiểu. Không lên giọng dạy bảo. Không dùng dấu gạch dài (—). Không dùng dấu chấm than. Tránh sáo ngữ kiểu "đáng chú ý là", "về cơ bản", "nhìn chung".

Quy tắc bắt buộc:
1. Giữ nguyên cấu trúc markdown: cấp tiêu đề, số thứ tự "### N.", thứ tự dòng, thứ tự mục, bảng và danh sách.
2. Mỗi trường nằm trên đúng một dòng, giữ dạng "- Nhãn: nội dung". Nhãn dịch theo bảng thuật ngữ.
3. Không thêm, không bớt, không bình luận, không thêm dữ kiện không có trong bản gốc. Không thêm thông tin về Việt Nam.
4. Dòng nguồn (来源): chỉ dịch nhãn. Giữ nguyên không đổi: tên tác giả, tên tạp chí, năm, DOI, URL, số hiệu văn bản và tên văn bản quy phạm. Tên cơ quan, tổ chức tiếng Trung giữ nguyên chữ Hán nhưng thêm nghĩa tiếng Việt trong ngoặc ngay sau, ví dụ 公安部 (Bộ Công an), 中国睡眠研究会 (Hiệp hội Nghiên cứu Giấc ngủ Trung Quốc). Chữ 等 trong danh sách tác giả đổi thành "et al.". Chú thích tiếng Trung trong ngoặc ở dòng nguồn (ví dụ （备注里的争议方之一）) phải dịch. Đổi dấu câu toàn phần (；（）) trong dòng nguồn sang dấu ASCII, trừ khi nằm trong tên văn bản hoặc số hiệu văn bản.
5. Mọi con số, đơn vị, tỉ lệ, khoảng tin cậy (CI), HR/RR/OR, giá tiền giữ nguyên giá trị.
6. Tham chiếu tới mục khác trong sách: "见第 X 节第 Y 条" → "xem phần X, mục Y"; "第 X 节" → "phần X"; "第 Y 条" trong cùng phần → "mục Y". Cụm trong ngoặc ngay sau tham chiếu là từ neo, phải dịch đúng bằng tiêu đề tiếng Việt của mục đích (dùng danh sách tiêu đề được cung cấp).
6b. Điều khoản pháp luật thì khác: tên văn bản + "第 N 条" dịch thành "Điều N", "第 N 款" thành "khoản N", giữ nguyên tên và số hiệu văn bản. Không biến điều luật thành "mục".
7. Trường 备注 mở đầu bằng "争议" thì bản dịch mở đầu bằng "Tranh cãi".
8. Trường 说人话 (Nói đơn giản) dịch trọn ý, tự nhiên như người Việt nói; không đưa vào số liệu không có ở trường 收益.
9. Thuật ngữ riêng của Trung Quốc (医保, 户口, 低保, ICP 备案, 疾控中心...) lần đầu xuất hiện trong mỗi tệp thì dịch nghĩa kèm nguyên ngữ trong ngoặc, ví dụ "bảo hiểm y tế (医保)". Các lần sau chỉ dùng tiếng Việt.
10. Dấu câu dùng kiểu Việt Nam: dấu phẩy cho phần thập phân (2,5), dấu chấm cho hàng nghìn (1.000). Đổi dấu câu toàn phần của bản gốc (；、，（）) thành dấu câu ASCII tương ứng, trừ khi chúng nằm trong tên văn bản quy phạm hoặc số hiệu văn bản.
11. Chỉ trả về markdown đã dịch, không thêm lời dẫn, không bọc trong dấu ```.

Bảng thuật ngữ (Trung → Việt):
"""
    + "\n".join(f"- {k} → {v}" for k, v in GLOSSARY["terms"].items())
    + "\n- Nhãn trường: "
    + "; ".join(f"{k} → {v}" for k, v in LABELS_VI.items())
    + "\n"
)


# ------------------------------------------------------------------ helpers


def slugify(text: str, maxlen: int = 48) -> str:
    text = text.lower().replace("đ", "d")
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    text = re.sub(r"-{2,}", "-", text)
    if len(text) > maxlen:  # cut on a word boundary, not mid-word
        text = text[:maxlen].rsplit("-", 1)[0]
    return text.strip("-")


def strip_tags(block: str) -> tuple[str, list[str]]:
    tags = [ln for ln in block.split("\n") if TAG_RE.match(ln)]
    clean = "\n".join(ln for ln in block.split("\n") if not TAG_RE.match(ln)).strip("\n")
    return clean, tags


def unfence(text: str) -> str:
    return re.sub(r"^```[a-zA-Z]*\n|\n```$", "", text.strip()).strip()


# ------------------------------------------------------------- book parsing


def parse_chapter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").split("\n")
    head_idx = next(i for i, ln in enumerate(lines) if ln.startswith("# "))
    m = re.match(r"^#\s+(\d+)\.\s*(.*)$", lines[head_idx])
    number, title_cn = (m.group(1), m.group(2)) if m else ("", lines[head_idx].lstrip("# ").strip())
    items, intro_lines, cur = [], [], None
    for ln in lines[head_idx + 1 :]:
        m = ITEM_RE.match(ln)
        if m:
            cur = {"n": int(m.group(1)), "title_cn": m.group(2).strip(), "lines": [], "tags": []}
            items.append(cur)
        elif cur is None:
            intro_lines.append(ln)
        elif TAG_RE.match(ln):
            cur["tags"].append(ln)
        else:
            cur["lines"].append(ln)
    for it in items:
        while it["lines"] and not it["lines"][-1].strip():
            it["lines"].pop()
    while intro_lines and not intro_lines[-1].strip():
        intro_lines.pop()
    while intro_lines and not intro_lines[0].strip():
        intro_lines.pop(0)
    return {
        "path": path,
        "number": number,
        "title_cn": title_cn,
        "intro_cn": "\n".join(intro_lines),
        "items": items,
        "prefix": lines[:head_idx],
    }


def chapters_list() -> list[dict]:
    files = sorted(p for p in (ROOT / "book").glob("*.md") if re.match(r"^\d\d-", p.name))
    return [parse_chapter(p) for p in files]


def item_title(titles_state: dict, ch_by_no: dict, ch_no: str, item_no: str | int) -> str | None:
    ch = ch_by_no.get(str(int(ch_no)))
    if not ch:
        return None
    return (titles_state.get(ch["path"].name, {}).get("items", {}) or {}).get(str(int(item_no)))


def is_law_ref(text: str, start: int) -> bool:
    window = text[max(0, start - 12) : start]
    return any(mark in window for mark in LAW_MARKERS)


def ref_hints(text: str, chapter_no: str, titles_state: dict, ch_by_no: dict) -> list[str]:
    hints: list[str] = []

    def add(h: str | None) -> None:
        if h and h not in hints:
            hints.append(h)

    for m in REF_CHAPTER_ITEM_RE.finditer(text):
        if is_law_ref(text, m.start()):
            continue
        t = item_title(titles_state, ch_by_no, m.group(1), m.group(2))
        add(f'phần {int(m.group(1))}, mục {int(m.group(2))} → "{t}"' if t else None)
    for m in REF_CHAPTER_RE.finditer(text):
        if is_law_ref(text, m.start()):
            continue
        ch = ch_by_no.get(str(int(m.group(1))))
        t = titles_state.get(ch["path"].name, {}).get("title") if ch else None
        add(f'phần {int(m.group(1))} → "{t}"' if t else None)
    rest = REF_CHAPTER_ITEM_RE.sub(" ", text)
    for m in REF_ITEM_RE.finditer(rest):
        if is_law_ref(rest, m.start()):
            continue
        t = item_title(titles_state, ch_by_no, chapter_no, m.group(1))
        add(f'mục {int(m.group(1))} (trong cùng phần) → "{t}"' if t else None)
    return hints[:20]


# --------------------------------------------------------------- pass 1: titles


TITLE_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "intro": {"type": "string"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"n": {"type": "integer"}, "title": {"type": "string"}},
                "required": ["n", "title"],
            },
        },
    },
    "required": ["title", "intro", "items"],
}


def translate_titles(ch: dict) -> dict:
    listing = "\n".join(f"{it['n']}. {it['title_cn']}" for it in ch["items"])
    prompt = (
        "Dịch tiêu đề chương, phần mở đầu chương và tiêu đề từng mục sang tiếng Việt.\n"
        "Giữ nguyên số thứ tự. Tiêu đề mục là một lời khuyên bắt đầu bằng động từ, dịch gọn, rõ, "
        "dùng cùng một cách gọi cho cùng một khái niệm trong cả chương.\n\n"
        f"Tiêu đề chương: {ch['title_cn']}\n\nMở đầu chương:\n{ch['intro_cn']}\n\n"
        f"Danh sách tiêu đề mục:\n{listing}"
    )
    data = json.loads(call_gemini(prompt, SYSTEM_RULES, schema=TITLE_SCHEMA, temperature=0.3))
    titles = {int(x["n"]): x["title"].strip() for x in data["items"]}
    missing = [it["n"] for it in ch["items"] if it["n"] not in titles]
    if missing:
        raise RuntimeError(f"{ch['path'].name}: title pass missing {missing}")
    return {"title": data["title"].strip(), "intro": data["intro"].strip(), "items": titles}


def run_titles(chapters: list[dict], refresh: bool = False) -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_path = STATE_DIR / "vi-titles.json"
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() and not refresh else {}
    todo = [c for c in chapters if c["path"].name not in state]
    log(f"titles: {len(todo)} to do, {len(state)} cached")
    lock = threading.Lock()

    def work(ch: dict) -> None:
        res = translate_titles(ch)
        with lock:
            state[ch["path"].name] = res
            state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
            log(f"  titles: {ch['path'].name} -> {res['title']}")

    if todo:
        with futures.ThreadPoolExecutor(max_workers=6) as ex:
            list(ex.map(work, todo))
    return state


# --------------------------------------------------------------- pass 2: items


def chunk_items(items: list[dict], max_chars: int = 2600) -> list[list[dict]]:
    chunks, cur, size = [], [], 0
    for it in items:
        ln = len(it["title_cn"]) + sum(len(x) for x in it["lines"])
        if cur and size + ln > max_chars:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(it)
        size += ln
    if cur:
        chunks.append(cur)
    return chunks


def validate_chunk(src_items: list[dict], out: str) -> list[str]:
    problems: list[str] = []
    got: dict[int, str] = {}
    for b in re.split(r"(?m)^(?=###\s+\d+\.)", out):
        m = ITEM_RE.match(b.split("\n", 1)[0])
        if m:
            got[int(m.group(1))] = b
    for it in src_items:
        if it["n"] not in got:
            problems.append(f"thiếu mục {it['n']}")
            continue
        body = got[it["n"]]
        src_text = "\n".join(it["lines"])
        for cn, vi in LABELS_VI.items():
            src_count = len(re.findall(rf"^- {cn}：", src_text, flags=re.M))
            out_count = len(re.findall(rf"^- {re.escape(vi)}:", body, flags=re.M))
            if src_count != out_count:
                problems.append(f"mục {it['n']}: '{vi}' {out_count}/{src_count} dòng")
        for label, pattern in (("URL", URL_RE), ("DOI", DOI_RE)):
            miss = set(pattern.findall(src_text)) - set(pattern.findall(body))
            if miss:
                problems.append(f"mục {it['n']}: thiếu {label} {list(miss)[:2]}")
        def norm_digits(text: str) -> set[str]:
            # 2.165 / 2,165 / 2165 are the same absolute value
            return set(DIGIT_RUN_RE.findall(re.sub(r"(?<=\d)[.,](?=\d{3})+", "", text)))

        # 万 (10k) is localized to "triệu", which changes the digit string:
        # skip such runs instead of reporting them as missing.
        # 万 (10k) / 亿 (100M) are localized to "nghìn" / "tỷ", which rewrites the
        # digit string: skip such runs instead of reporting them as missing.
        src_nums = {n for n in norm_digits(src_text) if not re.search(rf"{n}\s*[万亿]", src_text)}
        miss_nums = src_nums - norm_digits(body)
        if src_nums and len(miss_nums) / len(src_nums) > 0.05:
            problems.append(f"mục {it['n']}: thiếu số {sorted(miss_nums)[:6]}")
    return problems


def translate_chunk(chunk: list[dict], ctx: dict, hints: list[str]) -> tuple[dict[int, str], list[str]]:
    payload = [strip_tags(f"### {it['n']}. {it['title_cn']}\n" + "\n".join(it["lines"]))[0] for it in chunk]
    title_sheet = "\n".join(f"{n}. {t}" for n, t in sorted(ctx["titles"].items()))
    ctx_block = (
        f'Bối cảnh: đây là phần {int(ctx["chapter_no"])} của sách, tiêu đề tiếng Việt: "{ctx["chapter_title"]}".\n'
        f"Tiêu đề tiếng Việt của các mục trong phần này:\n{title_sheet}\n"
    )
    if hints:
        ctx_block += "Từ neo cho tham chiếu chéo (dùng đúng nguyên văn):\n" + "\n".join(hints) + "\n"
    prompt = (
        f"{ctx_block}\nDịch sang tiếng Việt. Chỉ trả về markdown, giữ đúng số thứ tự mục:\n\n"
        + "\n\n".join(payload)
    )
    system, problems, out = SYSTEM_RULES, [], ""
    for _ in range(3):
        out = unfence(call_gemini(prompt, system, temperature=0.25))
        problems = validate_chunk(chunk, out)
        if not problems:
            break
        system = SYSTEM_RULES + (
            "\n\nLẦN TRƯỚC SAI, phải sửa: " + "; ".join(problems[:6]) + ". Đủ dòng nhãn như bản gốc."
        )
        time.sleep(1)
    blocks: dict[int, str] = {}
    for b in re.split(r"(?m)^(?=###\s+\d+\.)", out):
        m = ITEM_RE.match(b.split("\n", 1)[0])
        if m:
            blocks[int(m.group(1))] = b.rstrip()
    return blocks, problems


def translate_chapter(ch: dict, titles_state: dict, ch_by_no: dict) -> dict:
    meta = titles_state[ch["path"].name]
    ctx = {"chapter_no": ch["number"], "chapter_title": meta["title"], "titles": {str(n): t for n, t in meta["items"].items()}}
    results: dict[int, str] = {}
    unresolved: list[str] = []
    with futures.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        jobmap = {}
        for chunk in chunk_items(ch["items"]):
            text = "\n".join(it["title_cn"] + "\n" + "\n".join(it["lines"]) for it in chunk)
            jobmap[ex.submit(translate_chunk, chunk, ctx, ref_hints(text, ch["number"], titles_state, ch_by_no))] = chunk
        for fut in futures.as_completed(jobmap):
            chunk = jobmap[fut]
            try:
                blocks, problems = fut.result()
            except Exception as exc:  # noqa: BLE001
                nums = ", ".join(str(it["n"]) for it in chunk)
                unresolved.append(f"lỗi API ở mục {nums}: {exc}")
                log(f"  !! {ch['path'].name}: lỗi API ở mục {nums}: {exc}")
                continue
            results.update(blocks)
            if problems:
                unresolved.extend(problems)
                log(f"  !! {ch['path'].name}: {'; '.join(problems[:4])}")
    slug = slugify(meta["title"])
    prefix = ch["path"].name[:2] if re.match(r"^\d\d-", ch["path"].name) else f"{int(ch['number']):02d}"
    out_path = ROOT / "book" / "vi" / f"{prefix}-{slug}.md"
    lines = [
        GLOSSARY["status_line"].format(src=ch["path"].name),
        "[← Về mục lục](../../README.vi.md)",
        "",
        f"# {int(ch['number'])}. {meta['title']}",
        "",
        meta["intro"],
        "",
    ]
    for it in ch["items"]:
        lines.append(f"### {it['n']}. {meta['items'][str(it['n'])]}")
        lines.extend(it["tags"])
        body = results.get(it["n"])
        if body is None:
            unresolved.append(f"mục {it['n']} chưa dịch")
            lines.extend(it["lines"])
        else:
            body_lines = body.split("\n")[1:]
            while body_lines and not body_lines[0].strip():
                body_lines.pop(0)
            lines.extend(body_lines)
        lines.append("")
    while lines and not lines[-1].strip():
        lines.pop()
    lines.append("")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    han = len(HAN_RE.findall("\n".join(lines)))
    log(f"  wrote {out_path.relative_to(ROOT)} ({len(ch['items'])} mục, {han} chữ Hán còn lại)")
    return {"path": out_path, "unresolved": unresolved, "han": han, "meta": meta}


# ------------------------------------------------ prose files (README, docs)


def parse_sections(text: str, level: int = 2) -> tuple[str, str, list[tuple[str, str]]]:
    """Return (h1_line, intro, [(heading_line, body), ...]) split at `level` headings."""
    lines = text.split("\n")
    h1 = next((ln for ln in lines if ln.startswith("# ")), "")
    rest = lines[lines.index(h1) + 1 :] if h1 in lines else lines
    marker = "#" * level + " "
    intro, sections, cur_head, cur = [], [], None, []
    for ln in rest:
        if ln.startswith(marker) and not ln.startswith(marker + "#"):
            if cur_head is not None:
                sections.append((cur_head, "\n".join(cur).strip("\n")))
            cur_head, cur = ln, []
        elif cur_head is None:
            intro.append(ln)
        else:
            cur.append(ln)
    if cur_head is not None:
        sections.append((cur_head, "\n".join(cur).strip("\n")))
    return h1, "\n".join(intro).strip("\n"), sections


def translate_prose(
    text: str, *, context: str, hints: list[str] | None = None, level: int = 2
) -> tuple[str, str, str, list[tuple[str, str]]]:
    h1, intro, sections = parse_sections(text, level=level)
    schema = {
        "type": "object",
        "properties": {"title": {"type": "string"}, "intro": {"type": "string"}},
        "required": ["title", "intro"],
    }
    head = json.loads(
        call_gemini(
            f"{context}\nDịch tiêu đề và phần mở đầu này sang tiếng Việt:\n\n{h1}\n\n{intro}",
            SYSTEM_RULES,
            schema=schema,
            temperature=0.3,
        )
    )
    out_sections: list[tuple[str, str]] = []
    for heading, body in sections:
        chunk = f"{heading}\n\n{body}".strip()
        extra = ""
        if hints:
            extra = "Từ neo tham chiếu (dùng đúng nguyên văn):\n" + "\n".join(hints) + "\n\n"
        out = unfence(
            call_gemini(
                f"{context}\n{extra}Dịch sang tiếng Việt, giữ nguyên cấu trúc markdown, số liệu, URL, "
                f"chỉ trả về markdown:\n\n{chunk}",
                SYSTEM_RULES,
                temperature=0.25,
            )
        )
        out_sections.append((heading, out))
    return h1, head["title"], head["intro"], out_sections  # type: ignore[return-value]


def rewrite_links(text: str, book_map: dict[str, str], docs_map: dict[str, str]) -> str:
    for src, dst in book_map.items():
        text = text.replace(f"](book/{src})", f"](book/vi/{dst})")
        text = text.replace(f"](book/{src}#", f"](book/vi/{dst}#")
    for src, dst in docs_map.items():
        text = text.replace(f"](docs/{src})", f"](docs/vi/{dst})")
    return text


def build_maps(titles_state: dict) -> tuple[dict[str, str], dict[str, str]]:
    book_map = {}
    for ch in chapters_list():
        meta = titles_state.get(ch["path"].name)
        if meta:
            book_map[ch["path"].name] = f"{ch['path'].name[:2]}-{slugify(meta['title'])}.md"
    docs_map = {}
    doc_titles = STATE_DIR / "vi-docs-titles.json"
    if doc_titles.exists():
        meta = json.loads(doc_titles.read_text(encoding="utf-8"))
        for name, data in meta.items():
            docs_map[name] = f"{slugify(data['title'])}.md"
    return book_map, docs_map


def run_readme(titles_state: dict) -> None:
    book_map, docs_map = build_maps(titles_state)
    src = (ROOT / "README.md").read_text(encoding="utf-8")
    log("README: translating")
    _, title, intro, sections = translate_prose(
        src,
        context='Đây là README của sách "Cẩm nang sống tốt với chi phí thấp" (中文: 高性价比人生指南).',
    )
    body = "\n\n".join(text for _, text in sections)
    body = rewrite_links(body, book_map, docs_map)
    intro = rewrite_links(intro, book_map, docs_map)
    out = (
        GLOSSARY["status_line"].format(src="../README.md").replace("../", "")
        + "\n\n"
        + f"# {title}\n\n{intro}\n\n{body}\n"
    )
    (ROOT / "README.vi.md").write_text(out, encoding="utf-8")
    han = len(HAN_RE.findall(out))
    log(f"  wrote README.vi.md ({len(sections)} sections, {han} chữ Hán còn lại)")


def run_docs(titles_state: dict) -> None:
    docs = sorted(p for p in (ROOT / "docs").glob("*.md") if p.name not in {"引用对照.md"})
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_path = STATE_DIR / "vi-docs-titles.json"
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    book_map, docs_map = build_maps(titles_state)
    # docs cross-reference chapters; give every doc the full anchor sheet once
    anchor_sheet = [
        f'phần {int(ch["number"])} "{titles_state[ch["path"].name]["title"]}"'
        for ch in chapters_list()
        if ch["path"].name in titles_state
    ]
    for p in docs:
        text = p.read_text(encoding="utf-8")
        log(f"docs: {p.name}")
        h1, title, intro, sections = translate_prose(
            text,
            context=f'Đây là một bài viết dài trong sách "Cẩm nang sống tốt với chi phí thấp", tệp gốc docs/{p.name}.',
            hints=anchor_sheet,
            level=2,
        )
        body = rewrite_links("\n\n".join(t for _, t in sections), book_map, docs_map)
        intro = rewrite_links(intro, book_map, docs_map)
        slug = slugify(title)
        out_path = ROOT / "docs" / "vi" / f"{slug}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            GLOSSARY["status_line"].format(src=f"docs/{p.name}")
            + "\n[← Về mục lục](../../README.vi.md)\n\n"
            + f"# {title}\n\n{intro}\n\n{body}\n",
            encoding="utf-8",
        )
        state[p.name] = {"title": title, "slug": slug}
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"  wrote docs/vi/{slug}.md")


# -------------------------------------------------------------------- main


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("phase", choices=["titles", "book", "readme", "docs", "all"])
    ap.add_argument("--chapters", default="")
    ap.add_argument("--refresh-titles", action="store_true")
    args = ap.parse_args()

    all_chapters = chapters_list()
    ch_by_no = {str(int(c["number"])): c for c in all_chapters}
    selected = all_chapters
    if args.chapters:
        wanted = {int(x) for x in args.chapters.split(",") if x.strip()}
        selected = [c for c in all_chapters if int(c["number"]) in wanted]
    log(f"{len(selected)} chapter(s) selected, {sum(len(c['items']) for c in selected)} mục")

    if args.phase == "docs":
        run_docs(run_titles(all_chapters))
        return
    titles_state = run_titles(all_chapters, refresh=args.refresh_titles)
    if args.phase == "titles":
        return
    if args.phase == "readme":
        run_readme(titles_state)
        return
    if args.phase == "all":
        run_readme(titles_state)
        run_docs(titles_state)
        return

    unresolved: list[str] = []
    han_total = 0
    for ch in selected:
        log(f"chapter {ch['number']}: {ch['title_cn']}")
        res = translate_chapter(ch, titles_state, ch_by_no)
        unresolved.extend(f"{ch['path'].name}: {p}" for p in res["unresolved"])
        han_total += res["han"]
    log(f"done. hanzi left in book: {han_total}; unresolved: {len(unresolved)}")
    for u in unresolved:
        log(f"  - {u}")


if __name__ == "__main__":
    main()
