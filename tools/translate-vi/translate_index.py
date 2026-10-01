#!/usr/bin/env python3
"""Build index.vi.html: the Vietnamese search page.

Two kinds of strings live in index.html:

* functional strings (cost-tag keys and values, field labels used by the parser,
  filter values in `data-v`, the ratio words). These are patched from a fixed
  table, because the corpus keeps 成本标签 comments and tag values in Chinese.
* display strings: page chrome, headings, tooltips, messages, and the filter chip
  labels. These go through the translator.

Every display string is translated as a WHOLE unit (a text node, an attribute
value, a JS string literal) and written back by offset, never by substring
replacement: swapping a fragment like 条 on its own leaves the page half
translated ("每一mục都回答…"). Chip labels are translated per filter group, so
"花钱" and "花时间" do not share one wording.

    VI_TRANSPORT=hermes python3 tools/translate-vi/translate_index.py
    python3 tools/translate-vi/translate_index.py --no-translate   # patches only
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_book as tb  # noqa: E402

INDEX = tb.ROOT / "index.html"
OUT = tb.ROOT / "index.vi.html"
HAN = re.compile(r"[\u4e00-\u9fff]")
# A JS literal that interpolates real code must never be handed to a model: it
# comes back with a bracket dropped (key.split('-')[1] -> key.split('-'[1]).
# Anything Chinese left in one of those is pinned in JS_PINNED instead.
CODEY = re.compile(r"\$\{[^}]*[()\[\].]|=>|\breturn\b|\.split\(|\.replace\(")
TAG_RE = re.compile(r"<(/?)([a-zA-Z0-9]+)([^>]*)>")
ATTR_RE = re.compile(r'\b(title|aria-label|alt|placeholder|content)="([^"]*)"')
JS_STR_RE = re.compile(r"""(['"`])((?:\\.|(?!\1)[^\\])*?)\1""")
JSONLD_VALUE_RE = re.compile(r'"(name|description|abstract)":"([^"]+)"')
CHIPS_BLOCK_RE = re.compile(r'<div class="chips" data-dim="([^"]+)">(.*?)</div>', re.S)
CHIP_RE = re.compile(r'<button class="chip" data-v="([^"]*)" aria-pressed="false">([^<]*)</button>')
GROUP_RE = re.compile(r'<div class="gt">([^<]*)(?:<small>(.*?)</small>)?</div>')

# Functional values that must keep working against the Chinese cost tags.
FUNCTIONAL = {
    "成本标签", "钱", "时间", "毅力", "收益", "口径", "成本", "说人话", "证据等级",
    "来源", "备注", "争议", "待核实", "大", "中", "小", "少", "多", "否", "些", "是",
    "极高", "高", "一般", "死亡率", "金钱", "自由", "术", "读者", "目录",
}

PATCHES: list[tuple[str, str]] = [
    ('<html lang="zh-CN">', '<html lang="vi">'),
    ('"inLanguage":"zh-CN"', '"inLanguage":"vi"'),
    ('<meta property="og:locale" content="zh_CN">', '<meta property="og:locale" content="vi_VN">'),
    ("await readText('README.md')", "await readText('README.vi.md')"),
    (r"/^## 读懂数字[^\n]*\n([\s\S]*?)(?=^## )/m", r"/^## Hiểu đúng các con số[^\n]*\n([\s\S]*?)(?=^## )/m"),
    (r"/^- 成本：(.*)$/", r"/^- Chi phí:(.*)$/"),
    (r"/^- 说人话：(.*)$/", r"/^- Nói đơn giản:(.*)$/"),
    (r"/^- 收益：(.*)$/", r"/^- Lợi ích:(.*)$/"),
    (r"/^- 证据等级：\s*([ABC])/", r"/^- Mức bằng chứng:\s*([ABC])/"),
    (r"/^- 来源：(.*)$/", r"/^- Nguồn:(.*)$/"),
    (r"/^- 备注：(.*)$/", r"/^- Ghi chú:(.*)$/"),
    (r"/^争议/", r"/^Tranh cãi/"),
    ("e.ratio = e.level === '大' ? (e.cs === 0 ? '极高' : (e.cs <= 2 ? '高' : '一般'))\n            : e.level === '中' ? (e.cs === 0 ? '高' : '一般') : '一般';",
     "e.ratio = e.level === '大' ? (e.cs === 0 ? 'Rất cao' : (e.cs <= 2 ? 'Cao' : 'Trung bình'))\n            : e.level === '中' ? (e.cs === 0 ? 'Cao' : 'Trung bình') : 'Trung bình';"),
    ("{'极高':'3','高':'2','一般':'1'}[e.ratio]", "{'Rất cao':'3','Cao':'2','Trung bình':'1'}[e.ratio]"),
    ("/待核实|TODO/", "/Đang chờ kiểm chứng|TODO/"),
    ("const LENS_LABEL = {'死亡率':'换寿命','金钱':'换钱','时间':'换时间精力','自由':'换人身自由'};",
     "const LENS_LABEL = {'死亡率':'đổi tuổi thọ','金钱':'đổi tiền','时间':'đổi thời gian và sức lực','自由':'đổi tự do cá nhân'};"),
]

# Filter panel wording is pinned here: these labels are short, repeat across the
# page and must match the filter values they belong to.
PANEL: list[tuple[str, str]] = [
    ('<div class="gt">章节</div>', '<div class="gt">Phần</div>'),
    ('<div class="gt">性价比 <small>作者判断，同口径内可比</small></div>',
     '<div class="gt">Đáng tiền <small>Tác giả đánh giá, chỉ so sánh trong cùng thước đo</small></div>'),
    ('<div class="gt">换回什么 <small>口径，不跨口径比较</small></div>',
     '<div class="gt">Đổi lại được gì <small>Thước đo, không so sánh giữa các thước đo</small></div>'),
    ('<div class="gt">证据等级 <small>荟萃/RCT · 有研究 · 共识</small></div>',
     '<div class="gt">Mức bằng chứng <small>Tổng hợp/RCT · có nghiên cứu · đồng thuận</small></div>'),
    ('<div class="gt">花钱</div>', '<div class="gt">Tốn tiền</div>'),
    ('<div class="gt">花时间</div>', '<div class="gt">Tốn thời gian</div>'),
    ('<div class="gt">要毅力</div>', '<div class="gt">Cần kiên trì</div>'),
    ('<div class="gt">广告</div>', '<div class="gt">Quảng cáo</div>'),
    ('data-v="死亡率" aria-pressed="false">寿命<', 'data-v="死亡率" aria-pressed="false">Tuổi thọ<'),
    ('data-v="金钱" aria-pressed="false">钱<', 'data-v="金钱" aria-pressed="false">Tiền<'),
    ('data-v="时间" aria-pressed="false">时间精力<', 'data-v="时间" aria-pressed="false">Thời gian, sức lực<'),
    ('data-v="自由" aria-pressed="false">人身自由<', 'data-v="自由" aria-pressed="false">Tự do cá nhân<'),
    ('data-v="A" aria-pressed="false">A 级<', 'data-v="A" aria-pressed="false">Cấp A<'),
    ('data-v="B" aria-pressed="false">B 级<', 'data-v="B" aria-pressed="false">Cấp B<'),
    ('data-v="C" aria-pressed="false">C 级<', 'data-v="C" aria-pressed="false">Cấp C<'),
    ('data-v="0" aria-pressed="false">不花钱<', 'data-v="0" aria-pressed="false">Không tốn tiền<'),
    ('data-v="少" aria-pressed="false">少<', 'data-v="少" aria-pressed="false">Tốn ít<'),
    ('data-v="多" aria-pressed="false">多<', 'data-v="多" aria-pressed="false">Tốn nhiều<'),
    ('data-v="少" aria-pressed="false">顺手<', 'data-v="少" aria-pressed="false">Vài phút<'),
    ('data-v="中" aria-pressed="false">几小时<', 'data-v="中" aria-pressed="false">Vài giờ<'),
    ('data-v="多" aria-pressed="false">每天占用<', 'data-v="多" aria-pressed="false">Mỗi ngày<'),
    ('data-v="否" aria-pressed="false">不用<', 'data-v="否" aria-pressed="false">Không cần<'),
    ('data-v="些" aria-pressed="false">一点<', 'data-v="些" aria-pressed="false">Cần chút ít<'),
    ('data-v="是" aria-pressed="false">很多<', 'data-v="是" aria-pressed="false">Cần nhiều<'),
    ('> 只看标了争议的</label>', '> Chỉ xem mục ghi tranh cãi</label>'),
    ('> 只看有待核实的</label>', '> Chỉ xem mục cần kiểm chứng</label>'),
    ('>清空筛选</button>', '>Xóa bộ lọc</button>'),
    ('>觉得有用？请作者喝杯咖啡</button>', '>Thấy hữu ích? Mời tác giả một ly cà phê</button>'),
]

# JS strings are pinned rather than translated. Two reasons: part of them is code
# (the cross-reference matcher must match the Vietnamese corpus, the source
# splitter must accept an ASCII semicolon), and the ones that build HTML come
# back with their attributes mangled when a model rewrites them. Pinning also
# keeps the wording of badges and tooltips stable between runs.
JS_PINNED: list[tuple[str, str]] = [
    # cross-reference matcher: must recognise how the Vietnamese corpus writes
    # "xem phần 9, mục 3", "mục 7 của phần này", "mục 8 đến 10", "xem phần 13"
    (r"for (const part of String(spec).split('、')){", r"for (const part of String(spec).split(',')){"),
    (r"? String(m[5]).split('、')", r"? String(m[5]).split(',')"),
    # sources are joined with ';' in the Vietnamese edition, not with '；'
    # card badges and tooltips
    (r"const LABEL = { money:{'0':'不花钱','少':'花少量钱','多':'花不少钱'}, time:{'少':'顺手','中':'花几小时','多':'每天占时间'}, will:{'否':'不用毅力','些':'要一点毅力','是':'要很多毅力'} };",
     r"const LABEL = { money:{'0':'Không tốn tiền','少':'Tốn ít tiền','多':'Tốn khá nhiều tiền'}, time:{'少':'Vài phút','中':'Vài giờ','多':'Chiếm thời gian mỗi ngày'}, will:{'否':'Không cần ý chí','些':'Cần chút ý chí','是':'Cần nhiều ý chí'} };"),
    (r"add(e.grade, `证据 ${e.grade} 级`);", r"add(e.grade, `Bằng chứng cấp ${e.grade}`);"),
    (r"t.textContent = '性价比 ' + e.ratio;", r"t.textContent = 'Đáng tiền: ' + e.ratio;"),
    (r"t.title = '作者判断：由收益量级（' + e.level + '）和三项成本合成，只在同一口径（' + LENS_LABEL[e.lens] + '）内可比，与证据等级无关';",
     r"t.title = 'Tác giả đánh giá: tổng hợp từ mức lợi ích (' + e.level + ') và ba loại chi phí, chỉ so sánh được trong cùng một thước đo (' + LENS_LABEL[e.lens] + '), không liên quan tới mức bằng chứng';"),
    (r"if (e.dispute) add('danger', '争议');", r"if (e.dispute) add('danger', 'Tranh cãi');"),
    (r"if (e.todo) add('warn', '含待核实');", r"if (e.todo) add('warn', 'Cần kiểm chứng');"),
    (r"f.srcN.textContent = nSrc > 1 ? ` · ${nSrc} 条` : '';",
     r"f.srcN.textContent = nSrc > 1 ? ` · ${nSrc} mục` : '';"),
    # card template and its labels
    (r'aria-label="本条链接"', r'aria-label="Liên kết tới mục này"'),
    (r'<div class="k">成本</div>', r'<div class="k">Chi phí</div>'),
    (r'<div class="k">收益</div>', r'<div class="k">Lợi ích</div>'),
    (r'<div class="k">备注</div>', r'<div class="k">Ghi chú</div>'),
    (r'<summary>来源<span class="cnt">', r'<summary>Nguồn<span class="cnt">'),
    (r'title="展开或收起本节目录"', r'title="Mở hoặc thu gọn mục lục phần này"'),
    # status and performance messages
    (r"命中 ${shown} 条，重渲染 ${rerender} 张", r"Khớp ${shown} mục, vẽ lại ${rerender} thẻ"),
    (r"取不到 ${path}（网络中断或超时）", r"Không lấy được ${path} (mất mạng hoặc quá thời gian chờ)"),
    (r"PERF.log('滚动补渲染', t0, n + ' 张');", r"PERF.log('cuộn bù', t0, n + ' thẻ');"),
    (r"PERF.log('建 DOM', t2, CARDS.length + ' 张卡');", r"PERF.log('dựng DOM', t2, CARDS.length + ' thẻ');"),
]

# The cross-reference matcher has to be rebuilt, not just translated: it must
# recognise how the Vietnamese corpus writes a reference ("xem phần 9, mục 3",
# "mục 7 của phần này", "mục 8 đến 10", "xem phần 13"). The escaping in the
# source line is taken from the line itself, so this keeps working whatever the
# number of backslashes is.
def pin_js(text: str) -> str:
    line = re.search(r"const NUMS = '([^\n]*)';", text)
    if not line:
        print("  !! không thấy dòng NUMS để tái tạo")
        return text
    m = re.match(r"\[(\\+)d", line.group(1))
    if not m:
        print("  !! không đọc được cách thoát dấu trong NUMS")
        return text
    E = m.group(1)                      # escape unit the source uses before s/d
    sp, dp = E + "s", E + "d"
    join = sp + "*," + sp + "*"
    nums = dp + "+(?:" + join + dp + "+)*(?:" + sp + "*đến" + sp + "*" + dp + "+)?"
    items = dp + "+(?:" + join + dp + "+)*"
    xref = (
        "const XREF_RE = new RegExp(`phần" + sp + "*(" + dp + "+)" + sp + "*," + sp + "*mục" + sp + "*(${NUMS})"
        + "|mục" + sp + "*(${NUMS})" + sp + "*(?:của|trong)" + sp + "*phần" + sp + "*này"
        + "|phần" + sp + "*này" + sp + "*," + sp + "*mục" + sp + "*(${NUMS})"
        + "|mục" + sp + "*(${NUMS})"
        + "|phần" + sp + "*(" + items + ")`, 'g');"
    )
    text, n1 = re.subn(r"const NUMS = '[^\n]*';", lambda _: "const NUMS = '" + nums + "';", text)
    text, n2 = re.subn(r"const XREF_RE = new RegExp\([^\n]*", lambda _: xref, text)
    pins = [
        (r"^\s*const semi = c === '[^\n]*$", lambda _: "  const semi = c === '；' || c === ';';"),
        (r"(\s*const r = /[^\n]*?)到([^\n]*?\.exec\(part\);)", r"\1đến\2"),
        (r">正在读取 …</div>", ">Đang đọc …</div>"),
    ]
    for pat, rep in pins:
        text, n = re.subn(pat, rep, text, flags=re.M)
        if not n:
            print(f"  !! mẫu JS (regex) không khớp: {pat[:50]}")
    if not (n1 and n2):
        print("  !! không tái tạo được NUMS/XREF_RE")
    return text


# Interface messages that are built with string interpolation or HTML inside the
# script. They are pinned by a distinctive prefix instead of by exact text,
# because the escaping of ${...} and of the quotes inside them is easy to get
# wrong by hand; the whole literal is replaced, quote style preserved.
MESSAGES: list[tuple[str, str]] = [
    ("⚠ 最长帧", "⚠ Khung hình dài nhất ${worst.toFixed(0)}ms"),
    ("⚠ 长任务", "⚠ Tác vụ dài ${e.duration.toFixed(0)}ms"),
    ("整节，共", "Cả phần, ${sec.entries.length} mục"),
    ("第 ${e.sec} 节第", "Phần ${e.sec}, mục ${e.n}"),
    ("<span>全部章节</span>", "<span>Tất cả các phần</span><i>${sections.reduce((n,s)=>n+s.entries.length,0)}</i>"),
    ("没有符合当前筛选的条目", "Không có mục nào khớp bộ lọc hiện tại"),
    ("在 GitHub 打开", '" target="_blank" rel="noopener">Mở trên GitHub</a></div>'),
    ("正在读取正文", "Đang đọc nội dung ${done}/${total}"),
    ("离线副本里缺", "Bản ngoại tuyến thiếu "),
    ("解析正文", "phân tích nội dung"),
    ("个文件", " tệp"),
    ("DOM 节点", "DOM ${document.getElementsByTagName('*').length} nút, ${GLOSS.length} thuật ngữ"),
    ("这个页面要通过 http 打开", "Trang này phải mở qua http mới đọc được nội dung. Trong thư mục kho chạy <code>python -m http.server</code>, rồi vào <code>http://localhost:8000/</code>; hoặc dùng thẳng địa chỉ GitHub Pages."),
    ("加载失败", "Tải thất bại: ${esc(String(err.message))}"),
    ("继续加载", '<div><button type="button" id="retry">Tiếp tục tải</button></div>'),
    ("读取正文失败", "Đọc nội dung thất bại (${esc(String(err.message))}). Kiểm tra xem README.vi.md và thư mục book/vi/ có nằm cạnh index.html không."),
]


def pin_messages(text: str) -> str:
    """Replace whole literals that carry an interface message, by their prefix.

    The literals are located with the same tokeniser the JS audit uses (offset
    based, quote aware) rather than by a regex over the page: a regex cannot tell
    a literal from an apostrophe in a comment and happily spans half the file.
    """
    import audit_js_strings as ajs

    for prefix, vi in MESSAGES:
        for m in reversed(list(re.finditer(r"<script(?![^>]*ld\+json)[^>]*>(.*?)</script>", text, re.S))):
            body = m.group(1)
            hit = next((off for off, lit in ajs.literals(body) if prefix in lit), None)
            if hit is None:
                continue
            end_off = hit + len(next(lit for off, lit in ajs.literals(body) if off == hit))
            base = m.start(1)
            text = text[: base + hit] + vi + text[base + end_off :]
            break
        else:
            print(f"  !! không thấy chuỗi thông báo: {prefix[:24]}")
    return text


RULES = (
    tb.SYSTEM_RULES
    + """
Bổ sung cho trang HTML:
- Dịch TRỌN VẸN chuỗi được đưa: không dịch từng mảnh, không bỏ sót chữ Hán nào trong câu.
- Tuyệt đối không đổi mã, tên biến, tên lớp CSS, id, thuộc tính, URL, số liệu, hay bất cứ chuỗi nào là khóa dữ liệu.
- Giữ nguyên mọi thẻ HTML, mọi ký tự $ { } ` \\ và dấu nháy như bản gốc.
- Nhãn nút và bộ lọc thì ngắn gọn; đoạn mô tả thì dịch đầy đủ, tự nhiên.
- Trả về đúng số phần tử như đầu vào, cùng thứ tự, không thêm chú thích.
"""
)


FULLWIDTH = {"。": ".", "，": ", ", "、": ", ", "；": "; ", "：": ": ", "！": "!", "？": "?", "（": "(", "）": ")"}


def vn_punct(s: str) -> str:
    """Full-width punctuation becomes ASCII, except inside 「」 quoted evidence."""
    out, depth = [], 0
    for ch in s:
        if ch == "「":
            depth += 1
        elif ch == "」":
            depth = max(0, depth - 1)
        out.append(FULLWIDTH.get(ch, ch) if depth == 0 else ch)
    return "".join(out)


def finalize(html: str) -> str:
    """Links of the Vietnamese edition point at its own front page and corpus."""
    for old, new in [
        ('href="README.md"', 'href="README.vi.md"'),
        (">README.md<", ">README.vi.md<"),
        ('href="book/"', 'href="book/vi/"'),
        (">book/<", ">book/vi/<"),
    ]:
        html = html.replace(old, new)
    return html


def segments(html: str) -> list[dict]:
    """Translatable display units, found without ever touching code.

    Script blocks are scanned on their own for string literals (a JS `err.message
    === 'file'` message is display text and must be translated as one unit), then
    blanked out so the markup scan cannot mistake code for a text node. Style
    blocks are blanked out as well: CSS comments stay Chinese like the original.
    """
    out: list[dict] = []
    blanked = list(html)

    def blank(a: int, b: int) -> None:
        for i in range(a, b):
            if blanked[i] != "\n":
                blanked[i] = " "

    for m in re.finditer(r"<script([^>]*)>(.*?)</script>", html, re.S):
        attrs, body, base = m.group(1), m.group(2), m.start(2)
        if "ld+json" in attrs:
            for vm in JSONLD_VALUE_RE.finditer(body):
                if HAN.search(vm.group(2)):
                    out.append(
                        {"start": base + vm.start(2), "end": base + vm.end(2), "kind": "jsonld", "text": vm.group(2)}
                    )
        else:
            for sm in JS_STR_RE.finditer(body):
                if HAN.search(sm.group(2)) and not CODEY.search(sm.group(2)):
                    out.append(
                        {"start": base + sm.start(2), "end": base + sm.end(2), "kind": "js", "text": sm.group(2)}
                    )
        blank(m.start(), m.end())
    for m in re.finditer(r"<style[^>]*>.*?</style>", html, re.S):
        blank(m.start(), m.end())

    markup = "".join(blanked)
    for m in re.finditer(r">([^<>]+)<", markup):
        if HAN.search(m.group(1)):
            out.append({"start": m.start(1), "end": m.end(1), "kind": "text", "text": m.group(1)})
    for m in re.finditer(r'\b(title|aria-label|alt|placeholder|content)="([^"]*)"', markup):
        if HAN.search(m.group(2)):
            base = m.start(2)
            out.append({"start": base, "end": base + len(m.group(2)), "kind": "attr:" + m.group(1), "text": m.group(2)})
    out.sort(key=lambda s: s["start"])
    return out


def translate_units(units: list[str], size: int, label: str, context: str = "", keep_functional: bool = False) -> dict[str, str]:
    """Translate whole strings; returns {source: translation}.

    `keep_functional` is used for filter chip labels: their data-v value is a
    machine key that must stay Chinese, but the visible label is display text.
    """
    mapping: dict[str, str] = {}
    todo = [u for u in units if (keep_functional or u not in FUNCTIONAL) and u.strip()]
    if not todo:
        return mapping

    def batch(chunk: list[str]) -> None:
        payload = json.dumps(chunk, ensure_ascii=False, indent=1)
        system = RULES + (f"\nBối cảnh: {context}\n" if context else "")
        for _ in range(3):
            raw = tb.call_gemini(
                "Dịch từng chuỗi trong mảng JSON sau sang tiếng Việt. Trả về một mảng JSON đúng số phần tử, "
                "cùng thứ tự:\n\n" + payload,
                system,
                temperature=0.2,
            )
            try:
                arr = tb.parse_json_loose(raw)
                if isinstance(arr, dict):
                    arr = next((v for v in arr.values() if isinstance(v, list)), None)
                if not isinstance(arr, list) or len(arr) != len(chunk):
                    raise ValueError(f"cần {len(chunk)} chuỗi, nhận {len(arr) if isinstance(arr, list) else 'không phải mảng'}")
                for src, dst in zip(chunk, arr):
                    if not isinstance(dst, str):
                        raise ValueError("phần tử không phải chuỗi")
                    # Chinese inside parentheses is a deliberate gloss of a
                    # China-specific term (hộ khẩu (户口)); Han anywhere else means
                    # the string was not translated
                    outside = re.sub(r"[（(][^（()）]*[)）]", "", dst)
                    if HAN.search(outside):
                        raise ValueError(f"còn chữ Hán: {dst[:60]}")
                    miss = set(tb.URL_RE.findall(src)) - set(tb.URL_RE.findall(dst))
                    if miss:
                        raise ValueError(f"mất URL {sorted(miss)[:1]}")
                    mapping[src] = vn_punct(dst)
                break
            except Exception as exc:  # noqa: BLE001
                system = RULES + f"\n\nLẦN TRƯỚC SAI: {exc}"

    chunks = [todo[i : i + size] for i in range(0, len(todo), size)]
    with futures.ThreadPoolExecutor(max_workers=min(6, len(chunks))) as ex:
        list(ex.map(batch, chunks))
    missing = [u for u in todo if u not in mapping]
    if missing:  # a few strings fail inside a batch; retry them alone
        with futures.ThreadPoolExecutor(max_workers=min(6, len(missing))) as ex:
            list(ex.map(batch, [[u] for u in missing]))
    print(f"  {label}: {len(mapping)}/{len(todo)} chuỗi ({len(chunks)} lô, {len(missing)} thử lại lẻ)")
    return mapping


def chip_units(html: str) -> list[dict]:
    """Chip labels with their filter group, so each group gets its own wording."""
    units = []
    for block in CHIPS_BLOCK_RE.finditer(html):
        dim = block.group(1)
        header = ""
        before = html[: block.start()]
        groups = GROUP_RE.findall(before)
        if groups:
            header = (groups[-1][0] or "").strip()
        for chip in CHIP_RE.finditer(block.group(2)):
            if HAN.search(chip.group(2)):
                base = block.start(2) + chip.start(2)
                units.append(
                    {
                        "start": base,
                        "end": base + len(chip.group(2)),
                        "kind": f"chip:{dim}",
                        "text": chip.group(2),
                        "group": header,
                        "value": chip.group(1),
                    }
                )
    return units


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-translate", action="store_true")
    ap.add_argument("--batch", type=int, default=10)
    args = ap.parse_args()

    text = INDEX.read_text(encoding="utf-8")
    for old, new in PANEL:
        if old in text:
            text = text.replace(old, new)
        else:
            print(f"  !! mẫu bảng lọc không khớp: {old[:50]}")
    text = pin_js(text)
    text = pin_messages(text)
    for old, new in JS_PINNED:
        if old in text:
            text = text.replace(old, new)
        else:
            print(f"  !! mẫu JS không khớp: {old[:60]}")
    for old, new in PATCHES:
        if old in text:
            text = text.replace(old, new)
        else:
            print(f"  !! không thấy mẫu cần vá: {old[:60]}")

    chips = chip_units(text)
    chip_span = {(c["start"], c["end"]) for c in chips}
    segs = [s for s in segments(text) if (s["start"], s["end"]) not in chip_span]
    print(f"{len(segs)} đoạn văn bản + {len(chips)} nhãn chip cần dịch")

    mapping: dict[str, str] = {}
    if not args.no_translate:
        mapping.update(translate_units([s["text"] for s in segs], args.batch, "text/attr/js"))
        by_group: dict[tuple[str, str], list[dict]] = {}
        for c in chips:
            by_group.setdefault((c["group"], c["kind"]), []).append(c)
        for (group, kind), items in by_group.items():
            ctx = f'bộ lọc "{group}" (mã nhóm {kind.split(":")[1]}), các giá trị: {", ".join(i["value"] for i in items)}'
            mapping.update(
                translate_units([i["text"] for i in items], len(items), f"chip {kind}", ctx, keep_functional=True)
            )

    out = text
    missed = 0
    for s in sorted(segs + chips, key=lambda s: s["start"], reverse=True):
        dst = mapping.get(s["text"])
        if dst is None:
            if s["text"].strip() not in FUNCTIONAL:
                missed += 1
            continue
        out = out[: s["start"]] + dst + out[s["end"] :]
    if missed:
        print(f"  !! {missed} đoạn chưa dịch được")

    out = re.sub(
        r"LENS_LABEL\s*=\s*\{[^}]*\};",
        "LENS_LABEL = {'死亡率':'đổi tuổi thọ','金钱':'đổi tiền','时间':'đổi thời gian và sức lực','自由':'đổi tự do cá nhân'};",
        out,
    )
    out = finalize(out)
    OUT.write_text(out, encoding="utf-8")

    left = [s for s in segments(out) if s["kind"] != "js" and s["text"].strip() not in FUNCTIONAL]
    print(f"wrote {OUT.relative_to(tb.ROOT)} ({len(out)} ký tự); đoạn còn chữ Hán ngoài JS: {len(left)}")
    for s in left[:8]:
        print(f'    [{s["kind"]}] {s["text"][:90]!r}')


if __name__ == "__main__":
    main()
