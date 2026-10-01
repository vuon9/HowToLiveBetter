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
(mặc định `gemini-3.8-flash`) và `VI_WORKERS` (mặc định 10).

Chạy lại là an toàn: bảng tiêu đề được lưu ở `state/vi-titles.json`, và mỗi
tệp dịch được ghi đè trọn vẹn nên chỉ cần chạy lại đúng phần đó.

## Kiểm tra tự động

`verify_vi.py` so từng phần với bản gốc và báo:

- lỗi cứng: thiếu mục, lệch số dòng nhãn, dòng `成本标签` khác bản gốc, thiếu
  URL hoặc DOI;
- lỗi mềm: số có thể thiếu, chữ Hán còn lại (những chỗ cố ý giữ như tên văn
  bản quy phạm), lệch số lượng tham chiếu chéo.

Mã thoát khác 0 khi có lỗi cứng, nên có thể gắn vào CI sau này.
