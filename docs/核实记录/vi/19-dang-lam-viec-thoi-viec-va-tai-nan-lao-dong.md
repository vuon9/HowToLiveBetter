> Bản dịch không chính thức của [docs/核实记录/19-工伤.md](../../../docs/核实记录/19-工伤.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Hồ sơ kiểm chứng: Phần 19 bổ sung 4 mục (tai nạn lao động)

Ngày kiểm chứng: 2026-09-07. Phần 19 từ 6 → 10 mục, tiêu đề phần đổi từ "Bị sa thải và chủ động thôi việc" thành "Bị sa thải, thôi việc và tai nạn lao động", toàn sách từ 318 → 322 mục.

Tai nạn lao động (工伤) vốn là khoảng trống đơn lẻ lớn nhất toàn sách: phần 7, mục 3 từng nhắc vụ việc tai nạn lao động thuộc phạm vi trợ giúp pháp lý, nhưng "công nhận thế nào, thời hạn ra sao, nhận được bao nhiêu" thì không có mục nào. Khoản tiền này lớn hơn khoản N khi sa thải một bậc quy mô, thời hạn lại còn ngặt nghèo hơn.

Phương pháp: dùng `Invoke-WebRequest` lấy byte gốc từ trang công báo gov.cn, giải mã theo GB18030 rồi xóa thẻ, đối chiếu từng mục với nguyên văn điều luật.

## 1、 Nguyên văn đối chiếu từng điều khoản
Nguồn đều từ toàn văn công báo trên website Chính phủ Trung Quốc của 《工伤保险条例》(Lệnh Quốc vụ viện số 586, sửa đổi năm 2010) <https://www.gov.cn/gongbao/content/2011/content_1778064.htm>.

| Điều luật | Nguyên văn đối chiếu được | Dùng ở đâu |
| --- | --- | --- |
| Điều 14 | Bảy trường hợp "phải được xác nhận là tai nạn lao động (工伤)", trong đó khoản (6) là cách diễn đạt sau khi sửa đổi năm 2010: "Trên đường đi làm hoặc tan làm, bị tổn thương do tai nạn giao thông hoặc tai nạn đường sắt đô thị, phà khách, tàu hỏa mà không phải chịu trách nhiệm chính" | Mục 7 (Bị tông xe trên đường đi làm hoặc tan làm cũng tính) |
| Điều 15 | "(1) Trong thời gian làm việc và tại vị trí làm việc, phát bệnh đột ngột dẫn đến tử vong hoặc cấp cứu không qua khỏi trong vòng 48 giờ dẫn đến tử vong" cùng ba trường hợp "xem như tai nạn lao động" | Mục 7 trường Ghi chú |
| Điều 16 | "(1) Cố ý phạm tội; (2) Say rượu hoặc dùng ma túy; (3) Tự làm hại bản thân hoặc tự sát" không được xác nhận | Mục 7 trường Ghi chú |
| Điều 17 | "Đơn vị sử dụng lao động phải nộp đơn đề nghị xác nhận tai nạn lao động trong vòng 30 ngày kể từ ngày xảy ra tai nạn thương tích hoặc từ ngày được chẩn đoán, giám định là bệnh nghề nghiệp..."; "Trường hợp người sử dụng lao động không nộp đơn đề nghị xác nhận tai nạn lao động theo quy định tại khoản trên, người lao động bị tai nạn lao động hoặc thân nhân trực hệ, tổ chức công đoàn có thể trực tiếp nộp đơn đề nghị xác nhận tai nạn lao động đến cơ quan hành chính bảo hiểm xã hội (社保) địa phương cấp điều phối nơi người sử dụng lao động đặt trụ sở trong vòng 1 năm kể từ ngày xảy ra tai nạn thương tích hoặc từ ngày được chẩn đoán, giám định là bệnh nghề nghiệp"; "Người sử dụng lao động không nộp đơn đề nghị xác nhận tai nạn lao động trong thời hạn quy định tại khoản 1 Điều này, mọi chi phí liên quan đến chế độ tai nạn lao động theo quy định của Điều lệ này phát sinh trong thời gian đó do người sử dụng lao động gánh chịu" | Hai mốc thời hạn của mục 7 |
| Điều 18 | Hồ sơ đề nghị gồm ba mục: đơn đề nghị xác nhận tai nạn lao động, giấy tờ chứng minh quan hệ lao động, chứng nhận chẩn đoán y tế hoặc chứng nhận chẩn đoán bệnh nghề nghiệp | Mục 7 trường Chi phí |
| Điều 19 | "Người lao động hoặc thân nhân trực hệ cho rằng đó là tai nạn lao động, người sử dụng lao động không thừa nhận là tai nạn lao động thì nghĩa vụ chứng minh thuộc về người sử dụng lao động." | Mục 7 |
| Điều 20 | "Cơ quan hành chính bảo hiểm xã hội phải đưa ra quyết định xác nhận tai nạn lao động trong vòng 60 ngày kể từ ngày tiếp nhận đơn đề nghị xác nhận tai nạn lao động" | Mục 7 trường Nguồn |
| Điều 21, Điều 22 | "Sau khi điều trị, thương tật tương đối ổn định nhưng vẫn có khiếm khuyết, ảnh hưởng đến khả năng lao động thì phải tiến hành giám định khả năng lao động"; "Rối loạn chức năng lao động được chia thành mười mức độ thương tật, nặng nhất là cấp một, nhẹ nhất là cấp mười" | Mục 9 |
| Điều 36 | Cấp năm, cấp sáu: trợ cấp thương tật một lần bằng 18 tháng, 16 tháng tiền lương của bản thân; trường hợp khó bố trí công việc thì chi trả trợ cấp thương tật hằng tháng, bằng 70%, 60% tiền lương của bản thân | Mục 9 |
| Điều 37 | Cấp bảy đến cấp mười: trợ cấp thương tật một lần bằng 13, 11, 9, 7 tháng tiền lương của bản thân; khi hết hạn hợp đồng hoặc bản thân người lao động đề nghị chấm dứt hợp đồng, quỹ chi trả trợ cấp y tế tai nạn lao động một lần, đơn vị chi trả trợ cấp việc làm thương tật một lần, mức chi trả do chính quyền cấp tỉnh quy định | Mục 9 |
| Điều 39 | "(1) Trợ cấp mai táng bằng 6 tháng tiền lương bình quân hằng tháng của người lao động trong năm trước tại địa phương cấp điều phối; (2) Tiền tuất nuôi dưỡng thân nhân... vợ/chồng hưởng 40% mỗi tháng, các thân nhân khác hưởng 30% mỗi người mỗi tháng, người già cô đơn không nơi nương tựa hoặc trẻ mồ côi được cộng thêm 10% mỗi tháng trên mức tiêu chuẩn nêu trên... (3) Mức trợ cấp tử vong do tai nạn lao động một lần bằng 20 lần thu nhập khả dụng bình quân đầu người của cư dân thành thị trên toàn quốc năm trước đó." | Mục 10 |
| Điều 62 | Khoản 2 "Người lao động thuộc đơn vị sử dụng lao động có nghĩa vụ tham gia bảo hiểm tai nạn lao động theo quy định của Điều lệ này nhưng không tham gia mà bị tai nạn lao động thì đơn vị sử dụng lao động đó phải chi trả các chi phí theo danh mục và mức hưởng chế độ bảo hiểm tai nạn lao động quy định tại Điều lệ này." Khoản 1: lệnh yêu cầu tham gia, đóng bù trong thời hạn quy định, "thu thêm tiền chậm nộp mỗi ngày bằng 0,05% số tiền nợ; quá thời hạn mà vẫn không đóng thì phạt tiền từ 1 đến 3 lần số tiền còn nợ" | Mục 8 |

## 2、 Chưa lấy được / Chưa sử dụng
| Muốn tìm | Kết quả | Xử lý |
| --- | --- | --- |
| Số tiền cụ thể của trợ cấp tử vong do tai nạn lao động một lần trong năm | Cần thu nhập khả dụng bình quân đầu người của cư dân thành thị trên toàn quốc năm 2025. Cơ sở dữ liệu văn bản chính sách của Quốc vụ viện không tìm thấy bản thân công báo thống kê; bài viết giải thích công báo của gov.cn chỉ đưa ra "thu nhập khả dụng bình quân đầu người tăng trưởng thực tế 5,0% so với năm trước", không có giá trị tuyệt đối; danh sách phát hành mới nhất của stats.gov.cn cũng không có mục này | Mục 10 chỉ ghi công thức tính theo bội số, số tiền ghi TODO |
| Tài liệu về tranh cãi điều khoản 48 giờ trong thực tế | Chỉ tìm thấy nhiều bài bình luận thứ cấp, chưa lấy được văn bản phán quyết hoặc tính theo chính thức có thể trích dẫn | Phần nội dung chính chỉ nêu nguyên văn điều luật, không mở rộng bình luận |

## 3、 Cách tính và quy mô lợi ích
Cả bốn mục đều tính theo tiền tệ. Quy mô lợi ích được xác định dựa trên ngưỡng tiền tệ từ phần 8 trở đi: trợ cấp thương tật một lần quy đổi theo tiền lương tháng, cấp mười thấp nhất cũng là 7 tháng lương; trợ cấp tử vong do tai nạn lao động là "20 lần thu nhập khả dụng bình quân đầu người của cư dân thành thị trên toàn quốc năm trước đó", đều từ mức hàng vạn nhân dân tệ trở lên, vì vậy toàn bộ xác định là "lớn". Về mặt chi phí, bản thân việc xác nhận và giám định không tốn tiền, nhưng đều phải đi làm thủ tục, chờ kết luận, thời gian ghi "vừa"; mục 8 (đơn vị chưa đóng bảo hiểm) ghi thêm "kiên trì=ít", vì đối phương phần lớn sẽ không nhận, phải theo đến bước trọng tài lao động (劳动仲裁).
