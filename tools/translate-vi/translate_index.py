#!/usr/bin/env python3
"""Build index.vi.html: the Vietnamese search page.

Two kinds of strings live in index.html:

* functional strings (cost-tag keys and values, field labels used by the parser,
  filter values in `data-v`, the ratio words). These are patched from a fixed
  table, because the corpus keeps 成本标签 comments and tag values in Chinese.
* display strings (page chrome, headings, tooltips, messages). These go through
  the translator, text nodes and title/aria-label/alt/placeholder attributes
  only, so filter values are never touched.

    VI_TRANSPORT=hermes python3 tools/translate-vi/translate_index.py
    python3 tools/translate-vi/translate_index.py --no-translate   # patches only
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_book as tb  # noqa: E402

INDEX = tb.ROOT / "index.html"
OUT = tb.ROOT / "index.vi.html"
HAN = re.compile(r"[\u4e00-\u9fff]")
SCRIPT_RE = re.compile(r"<script[^>]*>.*?</script>", re.S)
STYLE_RE = re.compile(r"<style[^>]*>.*?</style>", re.S)
TEXT_NODE_RE = re.compile(r">([^<>]+)<")
ATTR_RE = re.compile(r'\b(title|aria-label|alt|placeholder|content)="([^"]*)"')
JS_STR_RE = re.compile(r"""(['"`])((?:\\.|(?!\1)[^\\])*?)\1""")

# Functional values that must keep working against the Chinese cost tags.
FUNCTIONAL = {
    "成本标签", "钱", "时间", "毅力", "收益", "口径", "成本", "说人话", "证据等级",
    "来源", "备注", "争议", "待核实", "大", "中", "小", "少", "多", "否", "些", "是",
    "极高", "高", "一般", "死亡率", "金钱", "自由", "术", "读者", "目录",
}

PATCHES: list[tuple[str, str]] = [
    # page metadata
    ('<html lang="zh-CN">', '<html lang="vi">'),
    ('"inLanguage":"zh-CN"', '"inLanguage":"vi"'),
    ('<meta property="og:locale" content="zh_CN">', '<meta property="og:locale" content="vi_VN">'),
    # corpus: read the Vietnamese table of contents, whose links point at book/vi
    ("await readText('README.md')", "await readText('README.vi.md')"),
    ('EMBED.readme', 'EMBED.readme'),
    # glossary section heading in README.vi.md
    (r"/^## 读懂数字[^\n]*\n([\s\S]*?)(?=^## )/m", r"/^## Hiểu đúng các con số[^\n]*\n([\s\S]*?)(?=^## )/m"),
    # field labels produced by the Vietnamese chapters
    (r"/^- 成本：(.*)$/", r"/^- Chi phí:(.*)$/"),
    (r"/^- 说人话：(.*)$/", r"/^- Nói đơn giản:(.*)$/"),
    (r"/^- 收益：(.*)$/", r"/^- Lợi ích:(.*)$/"),
    (r"/^- 证据等级：\s*([ABC])/", r"/^- Mức bằng chứng:\s*([ABC])/"),
    (r"/^- 来源：(.*)$/", r"/^- Nguồn:(.*)$/"),
    (r"/^- 备注：(.*)$/", r"/^- Ghi chú:(.*)$/"),
    (r"/^争议/", r"/^Tranh cãi/"),
    # ratio words: computed, used as filter keys and displayed
    ("e.ratio = e.level === '大' ? (e.cs === 0 ? '极高' : (e.cs <= 2 ? '高' : '一般'))\n            : e.level === '中' ? (e.cs === 0 ? '高' : '一般') : '一般';",
     "e.ratio = e.level === '大' ? (e.cs === 0 ? 'Rất cao' : (e.cs <= 2 ? 'Cao' : 'Trung bình'))\n            : e.level === '中' ? (e.cs === 0 ? 'Cao' : 'Trung bình') : 'Trung bình';"),
    ("{'极高':'3','高':'2','一般':'1'}[e.ratio]", "{'Rất cao':'3','Cao':'2','Trung bình':'1'}[e.ratio]"),
    ('data-v="极高" aria-pressed="false">极高<', 'data-v="Rất cao" aria-pressed="false">Rất cao<'),
    ('data-v="高" aria-pressed="false">高<', 'data-v="Cao" aria-pressed="false">Cao<'),
    ('data-v="一般" aria-pressed="false">一般<', 'data-v="Trung bình" aria-pressed="false">Trung bình<'),
    ("/待核实|TODO/", "/Đang chờ kiểm chứng|TODO/"),
    # lens labels: keys are tag values, the values are shown
    ("const LENS_LABEL = {'死亡率':'换寿命','金钱':'换钱','时间':'换时间精力','自由':'换人身自由'};",
     "const LENS_LABEL = {'死亡率':'đổi tuổi thọ','金钱':'đổi tiền','时间':'đổi thời gian và sức lực','自由':'đổi tự do cá nhân'};"),
]

RULES = (
    tb.SYSTEM_RULES
    + """
Bổ sung cho trang HTML:
- Chỉ dịch phần chữ hiển thị. Tuyệt đối không đổi mã, tên biến, tên lớp CSS, id, thuộc tính, URL, số liệu, hay bất cứ chuỗi nào là khóa dữ liệu.
- Giữ nguyên mọi thẻ HTML, mọi ký tự $ { } ` \\ và dấu nháy như bản gốc.
- Chuỗi phải dịch trọn nghĩa nhưng giữ đúng vai trò: nhãn nút thì ngắn, mô tả thì đầy đủ.
- Trả về đúng số phần tử như đầu vào, cùng thứ tự, không thêm chú thích.
"""
)


def collect(text: str) -> list[str]:
    """Collect translatable display strings (deduped, order kept)."""
    found: list[str] = []

    def add(s: str) -> None:
        s = s.strip()
        if s and HAN.search(s) and s not in FUNCTIONAL and len(s) <= 600 and s not in found:
            found.append(s)

    body = text
    for m in TEXT_NODE_RE.finditer(body):
        add(m.group(1))
    for m in ATTR_RE.finditer(body):
        add(m.group(2))
    return found


def collect_js(text: str) -> list[str]:
    found: list[str] = []

    def add(s: str) -> None:
        if HAN.search(s) and s.strip() not in FUNCTIONAL and len(s) <= 600 and s not in found:
            found.append(s)

    for block in SCRIPT_RE.finditer(text):
        seg = block.group(0)
        if seg.startswith("<script type=\"application/ld+json\""):
            for m in re.finditer(r'"(?:name|description|abstract)":"([^"]+)"', seg):
                add(m.group(1))
            for m in re.finditer(r'"about":\[([^\]]+)\]', seg):
                for v in re.findall(r'"([^"]+)"', m.group(1)):
                    add(v)
            continue
        for m in JS_STR_RE.finditer(seg):
            add(m.group(2))
    return found


def translate_batch(strings: list[str], size: int = 24) -> dict[str, str]:
    out: dict[str, str] = {}
    for i in range(0, len(strings), size):
        batch = strings[i : i + size]
        payload = json.dumps(batch, ensure_ascii=False, indent=1)
        system = RULES
        for _ in range(3):
            raw = tb.call_gemini(
                "Dịch từng chuỗi trong mảng JSON sau sang tiếng Việt. Trả về một mảng JSON "
                "đúng số phần tử, cùng thứ tự:\n\n" + payload,
                system,
                temperature=0.2,
            )
            try:
                arr = tb.parse_json_loose(raw)
                if isinstance(arr, dict):
                    arr = next((v for v in arr.values() if isinstance(v, list)), None)
                if not isinstance(arr, list) or len(arr) != len(batch):
                    raise ValueError(f"cần {len(batch)} chuỗi, nhận {len(arr) if isinstance(arr, list) else 'không phải mảng'}")
                for src, dst in zip(batch, arr):
                    if not isinstance(dst, str):
                        raise ValueError("phần tử không phải chuỗi")
                    bad = set(tb.URL_RE.findall(src)) - set(tb.URL_RE.findall(str(dst)))
                    if bad:
                        raise ValueError(f"mất URL {sorted(bad)[:1]}")
                    out[src] = dst
                break
            except Exception as exc:  # noqa: BLE001
                system = RULES + f"\n\nLẦN TRƯỚC SAI: {exc}"
        print(f"  batch {i // size + 1}: {len(batch)} chuỗi")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-translate", action="store_true")
    ap.add_argument("--batch", type=int, default=24)
    args = ap.parse_args()

    text = INDEX.read_text(encoding="utf-8")
    for old, new in PATCHES:
        if old in text:
            text = text.replace(old, new)
    markup = collect(text)
    js = collect_js(text)
    strings = markup + [s for s in js if s not in markup]
    print(f"{len(strings)} chuỗi cần dịch ({len(markup)} trong HTML, {len(js)} trong JS)")

    mapping = {} if args.no_translate else translate_batch(strings, args.batch)
    out = text
    for src, dst in mapping.items():
        out = out.replace(src, dst)
    # idioms the model tends to leave half-translated: pin them by regex
    out = re.sub(
        r"LENS_LABEL\s*=\s*\{[^}]*\};",
        "LENS_LABEL = {'死亡率':'đổi tuổi thọ','金钱':'đổi tiền','时间':'đổi thời gian và sức lực','自由':'đổi tự do cá nhân'};",
        out,
    )
    out = re.sub(r"(data-v=\")(极高|高|一般)(\" aria-pressed=\"false\">)([^<]*)<",
                 lambda m: m.group(1) + {"极高": "Rất cao", "高": "Cao", "一般": "Trung bình"}[m.group(2)] + m.group(3)
                 + {"极高": "Rất cao", "高": "Cao", "一般": "Trung bình"}[m.group(2)] + "<",
                 out)
    OUT.write_text(out, encoding="utf-8")
    left = len(HAN.findall(SCRIPT_RE.sub("", out)))
    print(f"wrote {OUT.relative_to(tb.ROOT)} ({len(out)} ký tự, {left} chữ Hán ngoài <script>)")


if __name__ == "__main__":
    main()
