> Bản dịch không chính thức của [docs/核实记录/32-出国留学.md](../../../docs/核实记录/32-出国留学.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Phần 32 Du học nước ngoài: Tư cách lưu trú, làm thêm, bảo hiểm và công nhận văn bằng khi về nước · Hồ sơ kiểm chứng (2026-09-18)

Nguồn nhiệm vụ: Độc giả nêu câu hỏi tại issue #8 của kho lưu trữ: "Có lời khuyên nào dành cho du học sinh tại các quốc gia du học phổ biến như Mỹ, Canada, Anh, Úc không, với tư cách là du học sinh thì có những quyền lợi gì và bảo vệ quyền lợi như thế nào".

Nội dung bao quát ban đầu: Phần 21 viết về ra nước ngoài và an toàn ở nước ngoài (cảnh báo an toàn của 外交部 (Bộ Ngoại giao), 12308, ranh giới bảo hộ lãnh sự, bảo hiểm y tế và vận chuyển cấp cứu ở nước ngoài, bẫy tuyển dụng lương cao ở nước ngoài), không bao gồm tư cách lưu trú và việc học tập của du học sinh. Phần 23 viết về lợi ích từ bằng cấp, không bao gồm công nhận văn bằng ở nước ngoài. Vì vậy mở thêm một phần mới, không trùng lặp với hai phần trước, trong bài viết đã dẫn chiếu lẫn nhau.

Vị trí triển khai: Thêm mới `book/32-出国留学.md`, 10 mục. Các quốc gia được đề cập giới hạn theo câu hỏi của độc giả gồm Mỹ, Canada, Anh, Úc, số liệu được liệt kê theo từng nước. **Toàn bộ số liệu chính sách nước ngoài trong phần này được ghi chú tính đến tháng 9 năm 2026, phần chính văn và đầu phần đều ghi rõ độc giả cần tự kiểm tra lại theo liên kết nguồn, không duy trì cập nhật lâu dài.**

Công cụ lấy nguồn: curl trên máy gặp lỗi phân đoạn, `Invoke-WebRequest` bị hết thời gian chờ hoặc ngắt kết nối với canada.ca và cscse.edu.cn, chuyển sang dùng Chrome không đầu `--dump-dom` để lấy DOM sau khi kết xuất (jsj.moe.gov.cn và immi.homeaffairs.gov.au kết xuất ở phía máy khách, bắt buộc phải dùng cách này). Toàn bộ 17 liên kết ngoài trong phần này đã được kiểm tra khả năng truy cập từng liên kết vào ngày 2026-09-18, trừ canada.ca thì tất cả đều trả về mã 200; canada.ca không lấy được bằng PowerShell trên máy nhưng Chrome không đầu lấy được toàn văn, nội dung đã được đối chiếu từng chữ.

## Mục 1 (Danh sách cơ sở giáo dục được công nhận)
| URL | Kiểm tra lại | Căn cứ |
|---|---|---|
| <http://yxcx.cscse.edu.cn/> (Cổng tra cứu "Tra cứu cơ sở giáo dục được công nhận" của Trung tâm Dịch vụ Du học, lấy từ điểm neo trên trang chủ cscse.edu.cn) | Có | Trang web là cổng tra cứu theo quốc gia và tên cơ sở giáo dục |
| <https://jsj.moe.gov.cn/> (Trang chủ Mạng Thông tin Giám sát Giáo dục Ngoài nước của 教育部 (Bộ Giáo dục)) | Có | Chuyên mục gồm văn bản chính sách, thông tin cảnh báo, liên kết đào tạo |
| <http://rzzccx.crs.jsj.edu.cn/> (Tra cứu thông tin đăng ký công nhận văn bằng chứng chỉ liên kết đào tạo Trung - nước ngoài) | Có | "自 2008 年入学就读的学生，可凭本人姓名、身份证号码查询境外学历学位证书认证注册序号" |

Mức bằng chứng A: Cổng tra cứu và quy định đều có thể đối chiếu từng chữ trên trang web chính thức. Lợi ích mức "lớn", tính theo tiền ở mức chục nghìn nhân dân tệ, học phí cùng thời gian một đến hai năm vượt xa mức chục nghìn. Trong ghi chú, câu "danh sách có thể thay đổi, cần kiểm tra lại hằng năm" là khuyến nghị thực hành, không phải nguyên văn tài liệu.

## Mục 2 (Thời hạn nhập cảnh cố định và thời hạn rời cảnh 30 ngày của Mỹ)
| URL | Kiểm tra lại | Ý chính nguyên văn |
|---|---|---|
| <https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-214/section-214.2> (Văn bản hiện hành eCFR 8 CFR 214.2(f)) | Có | F-1 đã hoàn thành chương trình học và thực tập đã được phê duyệt, kể từ ngày kết thúc chương trình, thời hạn nhập cảnh tối đa 4 năm hoặc ngày kết thúc cấp phép OPT/STEM OPT có "an additional 30-day period" để chuẩn bị rời cảnh hoặc tìm kiếm tư cách pháp nhân hợp pháp khác; người kết thúc sớm việc học hoặc đào tạo phải rời cảnh hoặc tìm kiếm tư cách pháp nhân hợp pháp khác trong vòng 30 ngày kể từ ngày kết thúc |
| <https://www.federalregister.gov/documents/2026/07/17/2026-14439/establishing-a-fixed-time-period-of-admission-and-an-extension-of-stay-procedure-for-nonimmigrant> (Quy tắc cuối cùng trên Federal Register) | Có | publication_date 2026-07-17, effective_on 2026-09-15 (đối chiếu các trường lấy từ API federalregister.gov) |

**Đính chính ngày 25-09-2026 (issue #32)**: Quy tắc này **không** có hiệu lực vào ngày 15-09-2026. Ngày 14-09-2026, Thẩm phán Saylor tại Tòa án Quận Liên bang Massachusetts, trong vụ kiện Presidents' Alliance on Higher Education and Immigration v. DHS (No. 1:26-cv-13799-FDS), căn cứ theo 5 U.S.C. § 705 đã hoãn hiệu lực của toàn bộ quy tắc trên phạm vi toàn quốc; yêu cầu hủy bỏ (vacatur) và phán quyết rút gọn bị bác bỏ nhưng được phép nộp lại. Mục này đã được viết lại thành "quy tắc mới bị tạm dừng, hiện tại vẫn là D/S và thời gian ân hạn 60 ngày".

| URL | Kiểm tra lại | Ý chính nguyên văn |
|---|---|---|
| <https://oiss.yale.edu/news/important-update-court-action-on-the-ds-rule> (Văn phòng Sinh viên và Học giả Quốc tế Yale, 14-09-2026) | Có | "issued an order preliminarily enjoining DHS from implementing this rule" "the current D/S framework remains in place for now" "You do not currently need to apply for an Extension of Stay" "The administration may appeal" |
| <https://www.aila.org/blog/think-immigration-one-day-before-taking-effect-federal-court-postpones-the-f-j-and-i-fixed-admission-period-rule> (Hiệp hội Luật sư Di trú Mỹ) | Có | "The relief is nationwide, and it reaches the whole rule" "The rule is postponed, not vacated" "the 60-day grace period stands, and there is no new I-539 requirement" "denying the vacatur and summary judgment requests without prejudice to renewal" "the government may seek review in the First Circuit" |
| <https://www.courtlistener.com/docket/74661796/presidents-alliance-on-higher-education-and-immigration-v-united-states/> (Hồ sơ tòa án) | Có | Số 50 (14-09-2026) MEMORANDUM AND ORDER: "GRANTED to the extent that it seeks to postpone the effective date of the Final Rule pursuant to … 5 U.S.C. § 705. To the extent that plaintiffs seek vacatur of the Final Rule, summary judgment, or other relief, the motion is DENIED without prejudice to its renewal"; số 51 (14-09-2026) "PRELIMINARY INJUNCTION ORDER POSTPONING EFFECTIVE DATE OF FINAL RULE"; thông báo cùng ngày "Status Conference set for 10/2/2026 12:00 PM". Truy cập trực tiếp bị lỗi 403, dùng proxy cục bộ có thể tải được |

Giải thích phân hạng ban đầu (dưới đây) được giữ lại làm bản ghi lịch sử, trong đó câu "kể từ 15-09-2026 đã bị quy tắc thời hạn cố định thay thế" không còn đúng.

Mức bằng chứng A: Điều khoản và ngày có hiệu lực đều có thể đối chiếu từng chữ. **Mục này là cập nhật quan trọng nhất của phần này**: văn bản hiện hành eCFR ghi là 30 ngày, các thông tin lưu hành trên mạng về "thời gian ân hạn 60 ngày" và "duration of status học đến khi tốt nghiệp" đều là cơ chế cũ, từ ngày 15-09-2026 đã bị quy tắc thời hạn cố định thay thế, tính đến thời điểm viết bài này chỉ mới ba ngày. Lợi ích mức "lớn", tính theo tự do cá nhân, hậu quả là cư trú bất hợp pháp và trục xuất, xếp tương đương mức "tránh trách nhiệm hình sự Lớn". Thủ tục gia hạn nằm ở khoản (f)(7), phần chính chỉ hướng dẫn đường dẫn chứ không đi vào chi tiết.

## Mục 3 (Số giờ làm thêm tại bốn quốc gia)
| URL | Kiểm chứng lại | Ý chính nguyên văn |
|---|---|---|
| <https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-214/section-214.2> (8 CFR 214.2(f)(9)) | Có | Việc làm trong trường "must not exceed 20 hours a week while school is in session"; việc làm thêm ngoài trường đã được phê duyệt "limited to no more than 20 hours a week when school is in session", kỳ nghỉ có thể làm toàn thời gian |
| <https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-student> (Phụ lục Quy tắc nhập cư Student, Bảng ST26.1) | Có | Bậc đại học trở lên và bên bảo lãnh tuân thủ quy định: 20 giờ mỗi tuần trong kỳ học; dưới bậc đại học: 10 giờ; các trường hợp còn lại bao gồm toàn bộ hệ bán thời gian: không được đi làm. ST26.5 cấm thêm tự kinh doanh, vận động viên và huấn luyện viên chuyên nghiệp, biểu diễn nghệ thuật |
| <https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/work-off-campus.html> (IRCC) | Có | "You can work up to 24 hours per week"; giấy phép cũ in 20 giờ, nếu đủ điều kiện vẫn có thể làm đến 24 giờ; căn cứ theo Điều 186(v) của IRPR |
| <https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/student-500> (Bộ Nội vụ Student visa 500) | Có | "work up to 48 hours a fortnight when your course of study or training is in session", thạc sĩ nghiên cứu và tiến sĩ cùng người phụ thuộc không bị giới hạn giờ làm |

Xếp mức A: Bốn quốc gia đều dùng trang thông tin hiện hành hoặc quy tắc thành văn của cơ quan quản lý nhập cư, số liệu đối soát được từng chữ. Lợi ích mức "lớn", tính theo quyền tự do, làm việc quá số giờ quy định là vi phạm điều kiện thị thực, có thể dẫn đến việc bị hủy thị thực và trục xuất.

## Mục 4 (Học toàn thời gian là gốc rễ của tư cách làm thêm)
| URL | Kiểm chứng lại | Ý chính nguyên văn |
|---|---|---|
| <https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/work-off-campus.html> | Có | Trong thời gian nghỉ học có phép, hoặc trong thời gian chuyển trường mà không học tập, không được làm thêm ngoài trường, sau khi khôi phục việc học mới được đi làm lại |
| <https://studyinthestates.dhs.gov/students/work/working-in-the-united-states> (DHS Study in the States) | Có | Việc làm trong trường chỉ giới hạn cho sinh viên diện F-1 có trạng thái Active trong hệ thống SEVIS; việc làm ngoài trường phải được duyệt trước, trong thời gian xét duyệt I-765 không được bắt đầu làm việc |
| <https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-student> (ST26.1) | Có | Giấy phép làm thêm cấp theo loại khóa học, khóa học bán thời gian không được đi làm |

Xếp mức A. Trang của Canada diễn đạt rõ ràng nhất, Mỹ và Anh đối chiếu bằng quy tắc riêng của từng nước. Lợi ích mức "lớn", lý do giống mục 3.

## Mục 5 (Báo cáo đổi địa chỉ tại Mỹ trong vòng 10 ngày)
| URL | Kiểm chứng lại | Ý chính nguyên văn |
|---|---|---|
| <https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-265/section-265.1> | Có | Người có nghĩa vụ đăng ký phải "within 10 days of such change" báo cáo thay đổi địa chỉ và địa chỉ mới theo yêu cầu của USCIS |
| <https://www.uscis.gov/ar-11> | Có | Trang mẫu đơn AR-11, giải thích việc cần thông báo thay đổi địa chỉ càng sớm càng tốt để tránh thất lạc giấy tờ |

Xếp mức A: Thời hạn 10 ngày ghi rõ trong điều khoản. Lợi ích mức "vừa", tính theo quyền tự do xếp vào bậc "tránh phạt hành chính", hậu quả thực tế của việc thất lạc giấy tờ chủ yếu là bất lợi về mặt thủ tục, chưa đến mức trách nhiệm hình sự.

## Mục 6 (Cảnh báo du học của Bộ Giáo dục)
| URL | Kiểm chứng lại | Ý chính nguyên văn |
|---|---|---|
| <https://jsj.moe.gov.cn/n2/2/2/2001.shtml> | Có | Số 1 năm 2025 (2025-04-09), dự luật giáo dục đại học của các bang liên quan tại Mỹ có điều khoản tiêu cực liên quan đến Trung Quốc |
| <https://jsj.moe.gov.cn/n2/2/2/2030.shtml> | Có | Số 2 (2025-07-18), an ninh trật tự tại Philippines bất ổn, tội phạm nhắm vào công dân Trung Quốc xảy ra nhiều |
| <https://jsj.moe.gov.cn/n2/2/2/2035.shtml> | Có | Số 3 (2025-08-30), tiếp tục nhắc nhở về Philippines |
| <https://jsj.moe.gov.cn/n2/2/2/2060.shtml> | Có | Số 4 (2025-11-16), tình hình an ninh và môi trường du học tại Nhật Bản không tốt, khuyến nghị thận trọng khi lên kế hoạch du học Nhật Bản |

Xếp mức A: Số hiệu, ngày tháng, quốc gia hướng tới của bốn bản cảnh báo đều được đối soát từng mục. Dòng nguồn ở phần nội dung chính chỉ liệt kê số 4, số 1 và trang chủ chuyên mục, tránh để dòng nguồn quá dài. Lợi ích mức "vừa", cảnh báo là nhắc nhở rủi ro chứ không phải lệnh cấm, không tương ứng trực tiếp với hậu quả định lượng được. Danh sách cảnh báo thay đổi theo tình hình, phần này làm theo thông lệ tại phần 21 của CLAUDE.md, không duy trì lâu dài.

## Mục 7 (Bảo hiểm OSHC của Australia)
| URL | Kiểm chứng lại | Ý chính nguyên văn |
|---|---|---|
| <https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/student-500> | Có | Phải có và duy trì liên tục OSHC trong toàn bộ quá trình, trừ trường hợp được miễn; không được để khoảng trống bảo hiểm so với thị thực trước; người không chứng minh được đã mua bảo hiểm khi nhập cảnh có thể bị từ chối nhập cảnh; người nhập cảnh trước khi khóa học bắt đầu thì ngày bắt đầu bảo hiểm là ngày đến Australia |

Xếp mức A. Lợi ích mức "vừa", tính theo tiền bạc, phí bảo hiểm từ vài nghìn đến hơn chục nghìn nhân dân tệ, nằm ở ranh giới giữa mức "vài trăm đến vài nghìn" và mức chục nghìn, chọn mức vừa. Chi phí đánh nhãn tiền = nhiều (khoản chi một lần theo thời hạn thị thực).

## Mục 8 (Lệ phí thị thực và phụ phí y tế của Anh)
| URL | Kiểm chứng lại | Ý chính nguyên văn |
|---|---|---|
| <https://www.gov.uk/student-visa> | Có | Nộp đơn ngoài nước và gia hạn hoặc chuyển đổi trong nước đều là £558; đủ 18 tuổi học bậc đại học trở lên thông thường ở lại tối đa 5 năm, dưới bậc đại học là 2 năm |
| <https://www.gov.uk/healthcare-immigration-application> | Có | Sinh viên và người phụ thuộc là £776 mỗi năm (thị thực 2 năm là £1.552), người nộp đơn khác là £1.035 mỗi năm; trên 6 tháng nhưng chưa đủ 1 năm thu tính tròn cả năm |

Xếp mức A: Số tiền trích nguyên văn từ trang gov.uk kỳ hiện tại. Lợi ích mức "vừa", tính theo tiền bạc, tổng hai khoản nằm ở mức vài nghìn nhân dân tệ. Nội dung chính không quy đổi cụ thể sang nhân dân tệ, chỉ viết mức "hơn mười nghìn nhân dân tệ theo tỷ giá hiện tại", tránh việc tỷ giá biến động làm sai lệch số liệu.

## Mục 9 (Thời hạn xác nhận văn bằng của Trung tâm Dịch vụ Du học)
| URL | Kiểm chứng lại | Ý chính nguyên văn |
|---|---|---|
| <http://zwfw.cscse.edu.cn/> (Sảnh dịch vụ trực tuyến của Trung tâm Dịch vụ Du học) | Có | Quy trình xác nhận văn bằng học vị gồm đăng ký xác thực danh tính thực, nộp đơn và hồ sơ, thanh toán trực tuyến, đánh giá và xét duyệt; "认证工作时限 10-20 个工作日"; hồ sơ xin gồm chứng nhận văn bằng, hộ chiếu hoặc giấy thông hành, thẻ cư trú hoặc thị thực kèm dấu thị thực, ảnh thẻ, tuyên bố ủy quyền; hồ sơ xuất nhập cảnh do hệ thống tự lấy |

Xếp mức A: Thời hạn và danh mục hồ sơ được nêu rõ trên trang. Lợi ích mức "vừa", tính theo thời gian, khoản tiết kiệm được là rủi ro lỡ hạn chót, không phải thời gian mỗi ngày, tính theo "một lần" thì vốn nên xếp mức nhỏ, nhưng hậu quả của việc lỡ đợt tuyển dụng mùa thu hoặc đăng ký thi công chức tính theo khung thời gian cơ hội, nên chọn mức vừa; đây là nhận định đánh giá, không rập khuôn máy móc theo ngưỡng, ghi rõ tại đây theo đúng yêu cầu của CLAUDE.md.

## Mục 10 (Danh sách tăng cường xét duyệt xác nhận văn bằng)
| URL | Kiểm chứng lại | Ý chính nguyên văn |
|---|---|---|
| <https://www.cscse.edu.cn/cscse/sy/tzgg/2025102809225023345/index.html> | Có | 《关于对部分国外院校学历学位认证加强认证审查的公告（九）》, ban hành ngày 2025-10-28 |
| <https://www.cscse.edu.cn/> | Có | Mục thông báo đồng thời liệt kê "关于谨防借国（境）外学历学位认证实施诈骗的重要提示", "关于对部分国（境）外学历学位认证书失效处置的公告", "关于暂停泰国彭世洛大学学历学位认证申请的公告" |

Xếp mức A: Tiêu đề thông báo, số kỳ và ngày tháng có thể đối soát từng chữ. Lợi ích mức "vừa", tính theo tiền bạc, hậu quả là việc xác nhận bị cản trở hoặc chậm trễ, chưa chắc mất toàn bộ học phí, nên không lấy mức lớn. Nội dung chính không nêu tên cụ thể trường nào (trừ một trường đã công khai trong tiêu đề thông báo được trích dẫn), tránh việc sai lệch khi danh sách thay đổi.

## Phần này chưa viết
- Nghĩa vụ kê khai thuế của các quốc gia (như diện F-1 tại Mỹ không có thu nhập cũng phải nộp biểu mẫu) đợt này chưa lấy được trang chính thức đối soát được từng chữ, nên chưa đưa vào.
- Thời hạn báo cáo đổi địa chỉ của Canada, Anh, Australia khác nhau, chưa lấy nguyên văn của từng nước, mục 5 chỉ viết về Mỹ và ghi chú nhắc ba nước còn lại thực hiện theo quy định riêng của từng nước.
- Thủ tục khắc phục sau khi bị từ chối thị thực sinh viên hoặc mất tư cách lưu trú (như reinstatement của Mỹ) chưa viết, thuộc về thủ tục chuyên sâu, vượt quá định vị "không biết thì chịu thiệt" của phần này.
- Các quốc gia du học khác như Nhật Bản, New Zealand, Singapore không nằm trong phạm vi câu hỏi của độc giả, nên chưa đưa vào.
