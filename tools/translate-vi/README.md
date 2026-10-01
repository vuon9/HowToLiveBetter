# tools/translate-vi · Bản dịch tiếng Việt

Dịch cuốn sách này sang tiếng Việt bằng Gemini (`gemini-3.8-flash`), theo cách
làm mà bản dịch EN / RU / ES / PT của [dlgrv](https://github.com/dlgrv/HowToLiveBetter)
đã dùng: bản gốc tiếng Trung luôn là bản có hiệu lực, bản dịch nằm ở thư mục
riêng và ghi rõ xuất xứ.

## Vị trí tệp

| Nội dung | Bản gốc | Bản dịch |
| --- | --- | --- |
| 34 phần chính | `book/NN-*.md` | `book/vi/NN-<slug>.md` |
| Bài dài | `docs/*.md` | `docs/vi/<slug>.md` |
| Trang giới thiệu | `README.md` | `README.vi.md` |

Mỗi tệp dịch có dòng đầu là dòng xuất xứ trỏ về tệp gốc, dòng thứ hai là liên
kết về mục lục tiếng Việt. Không có liên kết nào từ `README.md` (bản Trung)
hay `index.html` trỏ sang bản dịch, nên các script thống kê, kiểm tra tham
chiếu và bộ dựng EPUB/PDF/offline vẫn chỉ đọc bản gốc.

## Quy tắc dịch (giữ nguyên như bản gốc)

- Dòng `<!-- 成本标签: ... -->` là dữ liệu cho `index.html`: không gửi cho mô
  hình, chèn lại nguyên ký tự ngay sau dòng tiêu đề mục.
- Dòng `- 来源：` chỉ dịch nhãn. Tên tác giả, tên tạp chí, năm, DOI, URL, số
  hiệu văn bản giữ nguyên. Tên cơ quan và tên văn bản quy phạm Trung Quốc giữ
  nguyên chữ Hán kèm nghĩa tiếng Việt trong ngoặc, ví dụ `公安部 (Bộ Công an)`.
  Chữ `等` trong danh sách tác giả thành `et al.`.
- Mọi con số, đơn vị, CI, HR/RR/OR giữ nguyên giá trị; phần thập phân viết
  theo kiểu Việt Nam (`2,5`), hàng nghìn dùng dấu chấm (`1.068`).
- Tham chiếu chéo `见第 X 节第 Y 条` thành `xem phần X, mục Y`, và từ neo
  trong ngoặc phải trùng tiêu đề tiếng Việt của mục đích. `第 N 条` của một
  văn bản quy phạm thì thành `Điều N`, không thành `mục N`.
- Thuật ngữ riêng của Trung Quốc (医保, 户口, 低保, ICP 备案...) dịch nghĩa
  kèm nguyên ngữ trong ngoặc ở lần xuất hiện đầu tiên trong mỗi tệp.
- Không thêm dữ kiện không có trong bản gốc, không thêm thông tin về Việt Nam.

## Chạy

```bash
# 1. Dịch tiêu đề chương và tiêu đề từng mục (bảng neo cho tham chiếu chéo)
python3 tools/translate-vi/translate_book.py titles

# 2. Dịch thân bài; --chapters để chạy thử một vài phần
python3 tools/translate-vi/translate_book.py book
python3 tools/translate-vi/translate_book.py book --chapters 3,13

# 3. Trang giới thiệu và các bài dài
python3 tools/translate-vi/translate_book.py readme
python3 tools/translate-vi/translate_book.py docs

# 4. Kiểm tra cấu trúc bản dịch so với bản gốc
python3 tools/translate-vi/verify_vi.py
```

Khóa API lấy từ `providers.gemini.api_key` trong `~/.hermes/config.yaml`, hoặc
biến môi trường `GEMINI_API_KEY` / `VI_API_KEY`. Có thể đổi `VI_MODEL`
(mặc định `gemini-3.8-flash`), `VI_WORKERS` (mặc định 10) và `VI_CHUNK_CHARS`
(mặc định 2600).

Ba đường gọi model, chọn bằng `VI_TRANSPORT`:

- `gemini` (mặc định): gọi thẳng Google bằng khóa trong `~/.hermes/config.yaml`.
- `hermes`: gọi qua provider đã cấu hình trong Hermes, ví dụ
  `VI_HERMES_MODEL=deepseek-flash VI_HERMES_PROVIDER=deepseek`. Đây là đường
  nhanh nhất khi Google hết hạn mức tháng (khoảng 5 giây mỗi lần gọi, so với
  khoảng 2 phút khi đi vòng qua một provider bị giới hạn khác).
- `opencode` không dùng được cho việc này khi tài khoản OpenCode Zen và
  OpenRouter đều hết tiền: cả hai đều trả về lỗi hết số dư.

Khi project Google chạm hạn mức chi tiêu tháng, đặt `VI_TRANSPORT=hermes` để
gọi cùng model đó qua provider đã cấu hình trong Hermes (`VI_HERMES_MODEL` mặc
định `google/gemini-3.8-flash`, `VI_HERMES_PROVIDER` mặc định `openrouter`).
Đường này chậm hơn nhiều (khoảng 2 phút mỗi chunk vì mỗi lần gọi phải dựng một
phiên Hermes), bù lại không phụ thuộc hạn mức của Google. Phiên đó che các
chuỗi số dài thành `[PHONE]`, nên sau khi chạy phải chạy `fix_redactions.py`.

```bash
VI_TRANSPORT=hermes VI_WORKERS=16 python3 tools/translate-vi/translate_book.py docs
```

Chạy lại là an toàn: bảng tiêu đề được lưu ở `state/vi-titles.json`, và mỗi
tệp dịch được ghi đè trọn vẹn nên chỉ cần chạy lại đúng phần đó.

## Sửa một mục lẻ

`repair_item.py` dịch lại một mục rồi ghép vào tệp, dùng khi `verify_vi.py` chỉ
ra một mục hỏng (ví dụ dòng Nguồn bị cắt):

```bash
python3 tools/translate-vi/repair_item.py 31 4
```

## Dọn dẹp sau khi dịch

- `fix_redactions.py`: khôi phục URL và chuỗi số bị thay bằng `[PHONE]` (chỉ
  xảy ra với `VI_TRANSPORT=hermes`).
- `normalize_terms.py --dry-run` rồi bỏ `--dry-run`: chốt một cách dịch duy
  nhất cho mỗi tên cơ quan Trung Quốc (mỗi chunk dịch độc lập nên cùng một cơ
  quan có thể ra nhiều cách gọi khác nhau).
- `rename_chapters.py`: đổi tên tệp theo slug chuẩn.
- tên tệp hồ sơ kiểm chứng sinh từ tiêu đề đã dịch, kèm số thứ tự phần; hai hồ
  sơ cùng một số phần (ví dụ `07-a.md` và `07-b.md`) không ghi đè nhau.
  `VI_REUSE_NAME=1` giữ nguyên tên tệp cũ khi dịch lại một tệp.
- `make_status.py`: ghi `status.json`; `make_registry.py`: ghi `translations.json`.

## Bản dịch còn lại

```bash
# 1.2 MB hồ sơ kiểm chứng nguồn (docs/核实记录/*.md, 111 tệp) -> docs/核实记录/vi/
VI_TRANSPORT=hermes VI_WORKERS=16 python3 tools/translate-vi/translate_records.py
python3 tools/translate-vi/translate_records.py --only 01,02     # chạy thử vài tệp

# trang tra cứu: index.html -> index.vi.html
VI_TRANSPORT=hermes python3 tools/translate-vi/translate_index.py
python3 tools/translate-vi/verify_index.py
```

`translate_index.py` tách hai loại chuỗi. Chuỗi chức năng (khóa và giá trị
`成本标签`, nhãn trường mà trang tự phân tích, giá trị `data-v` của bộ lọc) được
vá từ bảng cố định trong script, và vá trước khi dịch để mô hình không sửa vào.
Chuỗi hiển thị thì đưa qua mô hình, chỉ ở nút văn bản và các thuộc tính
`title` / `aria-label` / `alt` / `placeholder`, nên bộ lọc không bị lệch giá
trị. Trang đọc `README.vi.md`, và phần chú thích trong mã vẫn là tiếng Trung
như bản gốc.

### Dịch trọn từng chuỗi, không dịch từng mảnh

Mỗi chuỗi hiển thị được dịch như một đơn vị trọn vẹn (một nút văn bản, một giá
trị thuộc tính, một literal trong script) rồi ghi lại theo vị trí. Không bao
giờ thay thế bằng `str.replace` trên cả trang: thay một mảnh như `条` thành
`mục` sẽ để lại câu nửa Trung nửa Việt kiểu `每一mục都回答两个问题：花掉什么，Đổi
lại được gì。`.

Bốn bảng ghim, vá trước khi dịch nên mô hình không bao giờ thấy chúng:

| Bảng | Nội dung |
| --- | --- |
| `PANEL` | nhãn bảng lọc và nhãn chip (`Đáng tiền`, `Mức bằng chứng`, `Tốn tiền`, `Không cần`...) |
| `JS_PINNED` | chuỗi hiển thị trong script: huy hiệu thẻ, tooltip, thông báo trạng thái, mẫu HTML của thẻ |
| `MESSAGES` | thông báo có nội suy hoặc HTML, ghim theo tiền tố rồi thay cả literal (giữ nguyên kiểu nháy) |
| `PINS` / `PATCHES` | chuỗi chức năng: nhãn trường, khóa cost tag, `LENS_LABEL`, giá trị `data-v` |

`pin_js()` tái tạo **mắt nối tham chiếu chéo** cho tiếng Việt: bản gốc khớp
`第 X 节第 Y 条` / `本节第 N 条` / `第 N 条` / `第 X 节`, bản dịch phải khớp
`phần X, mục Y` / `mục N của phần này` / `mục N` / `phần X`, và nhận cả danh
sách (`mục 7, 19`) lẫn khoảng (`mục 8 đến 10`). Số lượng dấu thoát trong dòng
nguồn được đọc từ chính dòng đó nên không phải đếm tay. Cùng chỗ đó, dấu `;` của
bản tiếng Việt được nhận làm dấu phân cách danh sách nguồn.

`vn_punct()` đổi dấu câu toàn phần (。，、；：！？（）) sang ASCII, trừ phần nằm
trong 「」 (trích nguyên văn). `finalize()` trỏ liên kết của bản dịch về
`README.vi.md` và `book/vi/`.

`gloss_vi.py`/`audit_glosses.py` lo phần chú thích; xem mục cuối.

### Kiểm tra chuỗi trong script

`audit_js_strings.py` đi qua script theo kiểu bộ tách từ (mã, ghi chú dòng, ghi
chú khối, chuỗi, template, regex) rồi liệt kê mọi literal còn chữ Hán, phân biệt
**khóa máy** (giữ tiếng Trung để khớp cost tag) với **chuỗi hiển thị** (phải dịch):

```bash
python3 tools/translate-vi/audit_js_strings.py           # liệt kê
python3 tools/translate-vi/audit_js_strings.py --check   # thoát 1 nếu còn sót
```

Quét bằng regex là không đủ: một dấu nháy đơn trong ghi chú sẽ nuốt mất literal
phía sau, và chuỗi thật thì lọt. Vì vậy `translate_index.py` cũng **không** đưa
cho mô hình những literal có nội suy mã (`${...}` chứa `.split(`, `(`...): mô
hình từng trả về `key.split('-'[1]` thiếu một dấu ngoặc, làm cả trang chết. Những
chuỗi đó được ghim trong `MESSAGES` thay vì dịch máy.

Sau mỗi lần chạy `translate_index.py`: `node tools/translate-vi/build-site.mjs`,
rồi `verify_index.py` và `audit_js_strings.py --check`.


## Hình thức giống các bản dịch khác

| Thành phần | Tệp | Lệnh |
| --- | --- | --- |
| Trang tra cứu | `index.vi.html`, `vi/index.html` | `python3 tools/translate-vi/translate_index.py` rồi `node tools/translate-vi/build-site.mjs` |
| EPUB / PDF / HTML một tệp | `dist/HowToLiveBetter-vi.*` | `node tools/{epub,pdf,offline}/build.mjs --lang vi` |
| Banner mạng xã hội | `tools/og-vi.html` → `og-vi.png` | `node tools/translate-vi/build-og.mjs` |
| Sổ đăng ký bản dịch | `translations.json` | `python3 tools/translate-vi/make_registry.py` |

Ba script dựng đọc ngôn ngữ từ `tools/lib/langs.mjs`: tệp README, thư mục
`book/` và `docs/`, tiêu đề, nhãn trong sách và tên tệp đầu ra. Thêm ngôn ngữ
mới chỉ cần thêm một mục vào đó. Bản tiếng Trung chạy không tham số nên giữ
nguyên đường dẫn và tên tệp như trước.

`tools/sync-stats.mjs` cũng cập nhật số của `README.vi.md`, `index.vi.html`,
`vi/index.html` và `tools/og-vi.html`, nên `--check` trong CI vẫn đối chiếu
được cả hai ngôn ngữ.

GitHub Actions (`book.yml`) dựng cả hai bản, chạy epubcheck cho cả hai tệp
EPUB, và đăng `HowToLiveBetter-vi.{epub,pdf,html}` lên cùng release
`epub-latest`. Trang `/vi/` cần bật GitHub Pages cho kho này; nếu chưa bật thì
`index.vi.html` ở thư mục gốc vẫn mở được trực tiếp.

## Chú thích tiếng Việt cho phần giữ nguyên tiếng Trung

Bản dịch cố ý giữ chữ Hán ở vài chỗ (trích nguyên văn văn bản quy phạm, tên văn
bản, số hiệu, tên cơ quan). Hai script lo phần chú thích:

```bash
python3 tools/translate-vi/audit_glosses.py          # còn bao nhiêu dòng chưa có chú thích
python3 tools/translate-vi/audit_glosses.py --list   # liệt kê từng dòng

VI_TRANSPORT=hermes VI_HERMES_MODEL=deepseek-flash VI_HERMES_PROVIDER=deepseek \
  python3 tools/translate-vi/gloss_vi.py --area all --size 8
```

`gloss_vi.py` xử lý ba loại dòng, tất cả đều chỉ thêm chứ không xóa phần Hán:

- **quote**: mỗi đoạn 「…」 có chữ Hán được thêm ` (dịch: …)` ngay sau.
- **prose**: dòng còn nguyên tiếng Trung (thường là bảng trong hồ sơ kiểm chứng)
  được dịch cả dòng, giữ số liệu và URL.
- **gloss**: tiêu đề chỉ có tên văn bản Trung Quốc được thêm ` (nghĩa: …)`; chữ
  số Hán trong tiêu đề đổi thành số Ả Rập.

Chạy lại là an toàn: dòng đã có ` (dịch:` hoặc ` (nghĩa:` sẽ bị bỏ qua.

Phần không chú thích được, và lý do:

- Dòng `<!-- 成本标签: ... -->` là dữ liệu cho `index.html`, phải giữ nguyên
  từng ký tự; người đọc không thấy nó (HTML comment, và bộ dựng sách bỏ đi).
  Nhãn hiển thị của bộ lọc trong `index.vi.html` đã là tiếng Việt, chỉ giá trị
  `data-v` giữ tiếng Trung để khớp cost tag.
- Chú thích trong mã của `index.vi.html` và các script vẫn là tiếng Trung, giống
  bản gốc; chúng không hiện ra cho người đọc.

## Kiểm tra tự động

`verify_vi.py` so từng phần với bản gốc và báo:

- lỗi cứng: thiếu mục, lệch số dòng nhãn, dòng `成本标签` khác bản gốc, thiếu
  URL hoặc DOI;
- lỗi mềm: số có thể thiếu, chữ Hán còn lại (những chỗ cố ý giữ như tên văn
  bản quy phạm), lệch số lượng tham chiếu chéo.

Mã thoát khác 0 khi có lỗi cứng.

`verify_records.py` so 111 hồ sơ kiểm chứng: lỗi cứng là URL/DOI thiếu hoặc khác
bản gốc, lỗi mềm là độ phủ trích dẫn.

`verify_index.py` kiểm trang tra cứu: bộ đếm (34 phần, 649 mục, đủ sáu trường,
649 cost tag), các mốc chức năng còn nguyên, **cú pháp JS** của cả hai trang,
**mắt nối tham chiếu** khớp bao nhiêu chỗ trên bản dịch so với bản gốc (hiện
751 so với 743), và **không còn chữ Hán** trong chuỗi hiển thị lẫn văn bản
trong trang (chữ Hán trong ngoặc là chú thích cố ý, được bỏ qua).

CI (`book.yml`) có một job `vi` riêng chạy bốn script này, nên một lần dịch lại
làm hỏng cấu trúc, hỏng tham chiếu chéo hay làm chết JavaScript đều đỏ ở PR
trước khi merge.
