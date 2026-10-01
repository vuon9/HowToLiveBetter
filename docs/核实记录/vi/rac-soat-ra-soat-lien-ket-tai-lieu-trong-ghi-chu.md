> Bản dịch không chính thức của [docs/核实记录/排查-备注里的文献链接.md](../../../docs/核实记录/排查-备注里的文献链接.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Rà soát: Liên kết tài liệu trong ghi chú · Bản ghi (2026-09-21)

Nguồn gốc nhiệm vụ: Người dùng đọc ghi chú của phần 2, mục 1 (cai thuốc lá) trên trang tìm kiếm, thấy bên trong chèn cả một chuỗi danh mục tài liệu tiếng Anh, nói: "Sao ở đây vẫn còn thế này, độc giả đều là người Trung Quốc, bạn để nguyên một chuỗi dài thế này làm gì".

Trước đó trong cùng ngày đã xử lý hai mục (phần 2, mục 41 ca đêm; phần 6, mục 26 bữa sáng), lúc đó chỉ sửa hai mục có nhiều liên kết nhất, chưa rà soát toàn bộ sách. Lần này sẽ bổ sung đầy đủ.

## Tiêu chuẩn và cách tính
- **Liên kết tài liệu nhất loạt chuyển vào trường "Nguồn", không để ở trường ghi chú.** Trong ghi chú nhiều nhất chỉ giữ một liên kết, và chỉ được là liên kết tương đối trỏ tới bài viết dài trong docs/.
- Căn cứ: Quy tắc phổ thông hóa của CLAUDE.md viết rõ "**Ngoại trừ trường nguồn**, thư mục tài liệu và số điều khoản phải giữ nguyên dạng mới đối chiếu được". Ngụ ý là nơi đặt danh mục tài liệu tiếng Anh chính là trường nguồn. Ghi chú là nội dung tiếng Trung dành cho độc giả Trung Quốc đọc, nhồi nhét một chuỗi tiêu đề tiếng Anh và DOI thì vừa không hiểu vừa không nên đọc.
- Lệnh quét: `grep -c http` quét toàn bộ các dòng `- 备注：` trong sách.

## Trước và sau xử lý
| | Trước xử lý | Sau xử lý |
|---|---|---|
| Mục có liên kết trong ghi chú | 19 mục (trong đó 11 mục là nguyên chuỗi thư mục tiếng Anh chèn trong tiếng Trung) | **0 mục** |
| Số liên kết nhiều nhất trong một mục ghi chú | 3 liên kết | 0 liên kết |
| Tổng số liên kết tài liệu toàn sách | 1.234 | **1.234 (không đổi)** |

Tổng số liên kết không đổi là bất biến cốt lõi của đợt này: **Thư mục tài liệu được chuyển từ ghi chú sang trường nguồn, không phải bị xóa**. Khi chuyển vào nguồn đã thêm cho mỗi mục một phần đuôi ngắn tiếng Trung giải thích mục đó chứng minh cho luận điểm nào (kiểu như "(bên tranh cãi)", "(thử nghiệm dầu cá kê đơn độ tinh khiết cao trong ghi chú)"), tránh để trường nguồn biến thành một chuỗi danh mục không nhìn ra công dụng.

## Danh sách từng mục
Phần 1: mục 20 (vắc xin cúm Cochrane), mục 28 (PrEP, Fonner 2016), mục 29 (thời kỳ cửa sổ, trang của trung tâm kiểm soát bệnh tật (疾控中心) Quảng Đông).
Phần 2: mục 1 (hút thuốc thụ động Oberg 2011), mục 9 (bên tranh cãi muối natri thấp PURE), mục 19 (bên tranh cãi thịt chế biến hướng dẫn NutriRECS), mục 20 (bên tranh cãi uống rượu Di Castelnuovo 2006), mục 34 (bên tranh cãi BMI Flegal 2013), mục 41 (hai bài ca đêm gây ung thư + ánh sáng Czeisler, đợt trước đã xử lý).
Phần 3: mục 9 (hai bài bên tranh cãi Grubbs 2018, Prause & Pfaus 2015).
Phần 5: mục 17 (bên tranh cãi quỹ chỉ số Harvey & Liu 2022).
Phần 6: mục 1 (vitamin tổng hợp Gaziano 2012), mục 2 (dầu cá Bhatt 2019 REDUCE-IT), mục 26 (ba bài bữa sáng, đợt trước đã xử lý).
Phần 10: mục 3 (Perilloux & Kurzban 2015), mục 6 (Dargie 2015).
Phần 20: mục 12 (thử nghiệm trẻ sơ sinh nói chung EAT, Perkin 2016).
Phần 29: mục 4 (Kristensen 2012), mục 9 (Stroebe 2007).

## Tiêu đề được bổ sung đầy đủ
Có 5 mục ban đầu ở trường ghi chú ở dạng viết tắt (chỉ có tác giả, năm, tạp chí), khi chuyển vào trường nguồn cần bổ sung tiêu đề. **Không viết theo trí nhớ**, từng mục dùng Crossref truy xuất theo DOI:

| DOI | Tiêu đề truy xuất được |
|---|---|
| 10.1097/QAD.0000000000001145 | Effectiveness and safety of oral HIV preexposure prophylaxis for all populations（AIDS, 2016） |
| 10.1001/jama.2012.14641 | Multivitamins in the Prevention of Cancer in Men（JAMA, 2012） |
| 10.1056/NEJMoa1812792 | Cardiovascular Risk Reduction with Icosapent Ethyl for Hypertriglyceridemia（NEJM, 2019） |
| 10.1007/s10508-018-1248-x | Pornography Problems Due to Moral Incongruence: An Integrative Model with a Systematic Review and Meta-Analysis（Arch Sex Behav, **năm Crossref ghi là 2018 không phải 2019 như nguyên văn viết**, đã ghi theo năm 2018） |
| 10.1002/sm2.58 | Viewing Sexual Stimuli Associated with Greater Sexual Responsiveness, Not Erectile Dysfunction（Sexual Medicine, 2015） |

## Kiểm tra đối chiếu
- Số dòng `- 备注：` chứa http trên toàn sách: **0**.
- Sau khi xóa trích dẫn đã quét lại dấu câu một lượt, không để lại dấu chấm kép, ngoặc đơn rỗng hay dấu chấm câu bị cô lập.
- `node tools/check-refs.mjs --check`: 454 vị trí trích dẫn đều trỏ chính xác và có điểm neo, số lượng không đổi.
- `sync-stats.ps1`: 600 mục, 404 mục mức A, 1.234 liên kết, 8 vị trí thống kê không đổi vị trí nào.
