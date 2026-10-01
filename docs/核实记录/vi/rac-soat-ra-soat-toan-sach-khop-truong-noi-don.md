> Bản dịch không chính thức của [docs/核实记录/排查-说人话栏与收益栏对齐.md](../../../docs/核实记录/排查-说人话栏与收益栏对齐.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Rà soát toàn sách: Khớp trường Nói đơn giản và trường Lợi ích (2026-09-19)

Nguồn gốc nhiệm vụ: Người dùng đọc mục hiến máu ở phần 6, không hiểu câu "'sắc mặt kém, sợ lạnh' không phải chuyện bịa". Người này không biết ai từng nói sắc mặt kém, mà trong sách thực sự cũng không có nguồn nào nhắc đến "sắc mặt kém". Người dùng sau đó chỉ ra tính phổ biến của vấn đề: "Nhiều độc giả quen đọc thẳng phần Nói đơn giản, không xem nguồn cũng không xem hồ sơ kiểm chứng", yêu cầu rà soát toàn sách đối với vấn đề tương tự.

## Phương pháp rà soát
Đầu tiên đã thực hiện hai lượt quét tự động (19 từ mang tính phản bác xuất hiện ở dòng Nói đơn giản, toàn bộ các khẳng định trong ngoặc kép ở phần 6 đối chiếu từng mục với cột Lợi ích). Lượt này chỉ phát hiện thêm một vấn đề mới ở mục tắm nước lạnh, cho thấy quét tự động không bao quát hết. Sau đó đã điều 6 agent hiệu đính đối chiếu song song từng mục, rà soát toàn bộ 32 tệp, 544 mục trong thư mục book/. Mỗi agent nhận cùng một bộ tiêu chí:

Bốn loại vấn đề cần tìm: **[Thêm số liệu]** Số liệu ở dòng Nói đơn giản không tìm thấy ở cột Lợi ích của mục này; **[Thêm dữ kiện]** Triệu chứng, hậu quả, khẳng định dữ kiện nêu ở dòng Nói đơn giản không có căn cứ ở cả cột Lợi ích lẫn cột Nguồn của mục này; **[Tự tạo cơ chế]** Dòng Nói đơn giản diễn giải quan hệ nhân quả hoặc cơ chế cho dữ liệu của cột Lợi ích mà nghiên cứu gốc không đưa ra; **[Không tự trọn vẹn]** Dòng Nói đơn giản dẫn lại nhận định người đọc chưa từng thấy rồi mới đánh giá nhận định đó.

Đồng thời cũng đưa ra sáu nhóm phản ví dụ **không tính là lỗi** để tránh báo sai: diễn đạt khác nhưng nội dung nhất quán, bình dân hóa thuật ngữ, quy đổi HR/RR thành cách nói thông thường, chuyển ý logic tự trọn vẹn, nhận định đã phổ biến rộng rãi hoặc đã nêu rõ nguồn gốc ngay trong dòng, khuyến nghị hành động ở cuối dòng.

Tổng cộng ghi nhận 104 vị trí. Kiểm tra ngẫu nhiên ba vị trí (nhóm đối chứng uống nước nóng ở phần 2, phân loại cấp cứu tính theo Bắc Kinh ở phần 24, thời gian phục vụ của sinh viên y định hướng ở phần 31) đều đúng sự thật. Vì vậy đã đối chiếu xử lý từng mục theo báo cáo.

## Đã chỉnh sửa những gì
**Viết ngược hoặc viết hẹp phạm vi tính toán (loại quan trọng nhất)**

| Mục | Bản gốc | Nội dung thực tế ở cột Lợi ích |
|---|---|---|
| Sinh viên y định hướng phần 31 | Đào tạo chuẩn hóa "3 năm này tính vào thời gian phục vụ" | "Thời gian đào tạo của người vi phạm hợp đồng **không** tính vào thời gian phục vụ", ý nghĩa trái ngược |
| Phân loại cấp cứu phần 24 | 10 phút/30 phút/4 giờ là giới hạn thời gian phổ thông | "Tiêu chuẩn bốn cấp tính theo toàn quốc, **thời gian phản ứng là tiêu chuẩn của thành phố Bắc Kinh**" |
| Khám chữa bệnh trái tuyến phần 24 | Thanh toán "thấp hơn một đoạn" | "Duy trì **chênh lệch hợp lý**", bản gốc không nói rõ chiều hướng |
| Tin đồn phần 9 | "Bản thân không xác thực mà chuyển tiếp" có thể bị phạt | Cấu thành của cả hai điều khoản xử phạt đều là **biết rõ** là giả |
| Đào tiền ảo phần 11 | "Cũng **sẽ** bị phạt từ 50.000 đến 500.000" | "**Có thể** phạt", phạt tiền là điều khoản có biên độ quyết định |
| Nhập hàng phần 12 | "**Trực tiếp** xác định là biết rõ" | "**Có thể** xác định (trừ trường hợp có chứng cứ chứng minh thực sự không biết)" |
| Rối loạn ăn uống phần 28 | "Tách riêng ra xem đều không dự đoán được" | "Sau khi **hiệu chỉnh** tiền sử ăn kiêng và triệu chứng tâm thần" |
| Thất nghiệp phần 29 | "Gần một phần tư khoảng cách do hút thuốc uống rượu giải thích" | "Nhóm nghiên cứu có kiểm soát hành vi sức khỏe có HR thấp hơn 24%", không phải cùng một đại lượng |
| Lao động trẻ em phần 23 | "Xảy ra chuyện thì thương lượng bồi thường riêng" | Điều 10 của 《禁止使用童工规定》 quy định chính xác nghĩa vụ bồi thường theo pháp luật của đơn vị sử dụng lao động |
| Nội soi đại tràng phần 1 | "Nội soi đại tràng một lần" giảm xuống 0,98% | "**Mời** nội soi đại tràng", NordICC là phân tích sàng lọc theo chủ đích điều trị, tỷ lệ thực tế khám khoảng 40% |
| Uống nước nóng phần 2 | "Để hai phút là giảm được phần lớn" | Nhóm đối chứng là "chờ từ **4 phút** trở lên", không có mức hai phút |
| Số bước chân phần 2 | "Trên 7.800 bước cơ bản đi ngang" | Điểm đi ngang chia theo độ tuổi: ≥60 tuổi từ 6.000–8.000 bước, <60 tuổi từ 8.000–10.000 bước |

**Xóa các khẳng định về dữ kiện, cơ chế và tần suất không tra được ở cột Lợi ích**: "Đâm vào chấn thương nặng" của dây an toàn, "không cài quai coi như không đội" của mũ bảo hiểm, "hiếm khi gây tử vong" và đau dây thần kinh của bệnh zona, "thường tự khỏi" của tiểu ra máu, lịch sử tìm kiếm và vệt phanh trong vụ án giết vợ trục lợi bảo hiểm ở phần 8, "iPad 2" và số tiền tự bịa "bốn năm trăm nghìn" trong vụ án bán thận ở phần 9, "phần lớn cả hai cùng mất mạng", "người can ngăn thường là người cuối cùng bị tính vào", "xe là thứ dễ bị tìm ra nhất" ở phần 13, cơ chế ép cầm máu của dị vật ở phần 13, "loét da chuyển đen" của loét do tỳ đè ở phần 17, so sánh đường uống của vitamin K và nguyên nhân hăm tã của tã lót ở phần 20, từ chối bồi thường của giấy phép lái xe nước ngoài ở phần 21, nhận mạo danh tiền lương hưu ở phần 25, danh mục tái khám sau sinh và chi phí nằm viện ở phần 27, cơ chế tắc mạch của chất làm đầy ở phần 28, "sẽ chuyển máy", "chủ động đến tận nhà", "kẻ lừa đảo tập trung nhiều nhất" ở phần 29, "thường kèm buồn nôn nôn mửa" của xoắn tinh hoàn và "không phân biệt tập môn nào" của hoạt động ngoài trời ở phần 30, đánh đồng toàn bộ vay qua mạng ở phần 31, quy đổi sang nhân dân tệ ở phần 32.

**Bổ sung nguồn thay vì xóa** (nội dung có thật, chỉ là mục này chưa ghi xuất xứ):

- Vitamin C phần 6: Rút ngắn thời gian bệnh 8%, nhóm vận động cường độ cao RR 0,48 vốn đã ghi ở phần ghi chú, cùng thuộc một bài Cochrane, chuyển vào cột Lợi ích.
- Tiền trợ cấp thất nghiệp phần 7: Bổ sung Điều 48 của 《社会保险法》 (trong thời gian hưởng trợ cấp tham gia bảo hiểm y tế cho người lao động, tiền bảo hiểm y tế chi trả từ quỹ bảo hiểm thất nghiệp, cá nhân không phải đóng).
- Khám sức khỏe tiền hôn nhân phần 10: Bổ sung Điều 1053 của 《民法典》 (quyền yêu cầu hủy bỏ hôn nhân thực hiện trong vòng một năm kể từ ngày biết hoặc phải biết).
- Xét nghiệm HIV phần 1: Ban đầu viết "có thể ẩn danh", xác minh chỉ tìm thấy căn cứ về **bảo mật** (《全国艾滋病检测工作管理办法》 quy định nhân viên không được làm lộ họ tên, địa chỉ, kết quả xét nghiệm), không tìm thấy quy định chính thức về việc miễn cung cấp tên thật. Bảo mật không đồng nghĩa với ẩn danh, do đó tiêu đề mục và nội dung đều đổi thành "kết quả được bảo mật", đồng thời bổ sung văn bản này vào cột Nguồn.

**Tiện thể sửa lỗi lệch tham chiếu trong phần 7** (agent phát hiện thêm, không liên quan đến phần Nói đơn giản): mục 5 trỏ cứu trợ y tế sang mục 8 (đúng phải là mục 11), mục 8 trỏ trợ giúp pháp lý và hỗ trợ đóng bảo hiểm sang mục 2 và 8 (tự trỏ vào chính mình, đúng phải là mục 3, 10, 11), mục 11 trỏ mức bốn lần LPR sang mục 13 (đúng phải là mục 16), mục 19 và 21 trỏ bảo hiểm y tế cư dân sang mục 8 (đúng phải là mục 10), mục 22 trỏ trạm cứu trợ sang mục 3 (đúng phải là mục 4). Sau đó đã quét toàn bộ cuốn sách để tìm tham chiếu vượt giới hạn (số thứ tự mục được tham chiếu vượt quá số lượng mục của phần đó), không phát hiện thêm vị trí nào khác; kiểu lỗi "nằm trong phạm vi nhưng trỏ sai" này chỉ có thể phát hiện thủ công.

## Hai lỗi cùng dạng do chính tôi phạm phải trong quá trình sửa
Đáng để ghi lại riêng, vì điều này cho thấy lỗi này rất dễ mắc phải:

1. Ở mục mù mắt do thẩm mỹ y khoa tại phần 28, tôi viết lại cơ chế tắc mạch ban đầu thành "trong 48 ca thì 60% xảy ra ở sống mũi, ấn đường và trán" con số "60%" này là do tôi viết theo ấn tượng. Con số thực tế ở cột Lợi ích là vùng mũi 56,3%, ấn đường 27,1%, trán 18,8%, rãnh mũi má 14,6%, hơn nữa một ca có thể liên quan đến nhiều vị trí, cộng lại vượt quá 100%, hoàn toàn không thể gộp thành "60%". Đã sửa lại thành chép nguyên văn từng mục.
2. Ở mục sinh mổ tại phần 27, câu "sau khi vượt quá 10% **không có bằng chứng cho thấy** tỷ lệ tử vong giảm" của WHO đã bị tôi viết thành "tỷ lệ tử vong mẹ và trẻ sơ sinh **không còn giảm nữa**". Thiếu bằng chứng và chứng minh không hiệu quả là hai việc khác nhau. Đã sửa lại theo đúng cách tính ban đầu.

**Bài học**: Khi viết lại phần Nói đơn giản bắt buộc phải mở ngay cột Lợi ích để chép đối chiếu tại chỗ, không được thuật lại theo ấn tượng vừa đọc xong.

## Trường hợp xác định không cần sửa
Phần Nói đơn giản có dẫn nội dung phần khác nhưng **có kèm ghi chú liên phần rõ ràng** (ví dụ phần 3 mục 20 khi nói về phong bì có ghi kèm "(phần 24...)"), không xử lý theo dạng thêm dữ kiện người đọc sẽ không hiểu nhầm là kết luận của nghiên cứu thuộc mục này, bản chất khác với những khẳng định tự nhiên xuất hiện như "sắc mặt kém". Tiêu chí này đã được đưa vào thông lệ đánh giá bên ngoài tệp CLAUDE.md, ghi chú một dòng tại đây để tiện tra cứu.

## Quy tắc đã được đồng bộ
Quy tắc cho phần Nói đơn giản trong CLAUDE.md trước đây chỉ cấm "**con số** không có trong cột Lợi ích", lần này phần lớn lỗi phát sinh đều không phải là con số. Đã bổ sung thành: nội dung không được thêm mới bao gồm cả triệu chứng, khẳng định dữ kiện và diễn giải cơ chế; phần Nói đơn giản phải tự trọn vẹn, cấm các cách viết phụ thuộc vào nhận định đặt trước mới hiểu được như "'XX' không phải chuyện bịa", "'XX' là có thật".
