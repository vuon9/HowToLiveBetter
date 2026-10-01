> Bản dịch không chính thức của [docs/核实记录/追加-第15节与病历条回填.md](../../../docs/核实记录/追加-第15节与病历条回填.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Hồ sơ kiểm chứng: Phần 15 bổ sung 2 mục + điền lại TODO của mục bệnh án phần 24

Ngày kiểm chứng: 2026-09-07. Toàn sách 344 → 346 mục; phần 24, mục 6 chuyển từ mức C (nguồn TODO) sang mức A.

**Đợt này đồng thời đính chính một nhận định sai trong hai hồ sơ kiểm chứng trước.** Trước đó trong đợt này, khi tra cứu 《商品房屋租赁管理办法》, 《房地产经纪管理办法》, 《医疗纠纷预防和处理条例》, 《医疗机构病历管理规定》 trong kho văn bản chính sách của 国务院 (Quốc vụ viện Trung Quốc) đều trả về kết quả trống, do đó trong [追加-慢病长护险与个人信息权利.md](追加-慢病长护险与个人信息权利.md) và [24-25-看病与身后事.md](24-25-看病与身后事.md) đã ghi "không có trong kho văn bản chính sách của 国务院 (Quốc vụ viện Trung Quốc)". Kết luận này là sai, nguyên nhân do tham số tìm kiếm đã dùng `searchfield=title|default` - việc kèm theo `default` khiến các văn bản quy hoạch khớp ở phần nội dung bị lẫn vào và đẩy mất kết quả khớp chính xác theo tiêu đề. Sau khi đổi thành `searchfield=title`, cả bốn văn bản đều khớp ngay lần đầu. Kết luận căn cứ theo các dòng liên quan trong hai hồ sơ đó bị hủy bỏ, lấy tài liệu này làm chuẩn.

## I. Nguyên văn đối chiếu được theo từng mục
| Nguồn | Nguyên văn đối chiếu được | Dùng ở đâu |
| --- | --- | --- |
| 《医疗纠纷预防和处理条例》(国务院 (Quốc vụ viện) 令第 701 号) <https://www.gov.cn/zhengce/zhengceku/2018-08/31/content_5318057.htm> | Điều 15 「医疗机构及其医务人员应当按照国务院卫生主管部门的规定，填写并妥善保管病历资料。」「任何单位和个人不得篡改、伪造、隐匿、毁灭或者抢夺病历资料。」Điều 16 「患者有权查阅、复制其门诊病历、住院志、体温单、医嘱单、化验单（检验报告）、医学影像检查资料、特殊检查同意书、手术同意书、手术及麻醉记录、病理资料、护理记录、医疗费用以及国务院卫生主管部门规定的其他属于病历的全部资料。」「患者要求复制病历资料的，医疗机构应当提供复制服务，并在复制的病历资料上加盖证明印记。复制病历资料时，应当有患者或者其近亲属在场。医疗机构应患者的要求为其复制病历资料，可以收取工本费，收费标准应当公开。」「患者死亡的，其近亲属可以依照本条例的规定，查阅、复制病历资料。」 | Phần 24, mục 6 (điền bổ sung) |
| 《医疗机构病历管理规定（2013 年版）》<http://www.gov.cn/gongbao/content/2014/content_2600084.htm> | 「医疗机构应当指定部门或者专（兼）职人员负责受理复制病历资料的申请。」「在申请人在场的情况下复制；复制的病历资料经申请人和医疗机构双方确认无误后，加盖医疗机构证明印记。」「医疗机构复制病历资料，可以按照规定收取工本费。」Liệt kê thêm các loại bệnh án có thể sao chép, gồm tài liệu kiểm tra hình ảnh y khoa, báo cáo bệnh lý, báo cáo xét nghiệm, v.v. | Như trên |
| 《房地产经纪管理办法》(住建部 (Bộ Xây dựng), 发展改革委 (Ủy ban Cải cách và Phát triển), 人社部 (Bộ Nguồn nhân lực và An sinh xã hội) 令第 8 号, sửa đổi theo Lệnh số 29 năm 2016) <http://www.gov.cn/gongbao/content/2011/content_1918920.htm> | Điều 24 「房地产交易当事人约定由房地产经纪机构代收代付交易资金的，应当通过房地产经纪机构在银行开设的客户交易结算资金专用存款账户划转交易资金。」Điều 18 「房地产经纪服务实行明码标价制度……在经营场所醒目位置标明房地产经纪服务项目、服务内容、收费标准以及相关房地产价格和信息。」Điều 19 「两家或者两家以上房地产经纪机构合作开展同一宗房地产经纪业务的，只能按照一宗业务收取佣金，不得向委托人增加收费。」Điều 17 「房地产经纪机构提供代办贷款、代办房地产登记等其他服务的，应当向委托人说明服务内容、收费标准等情况，经委托人同意后，另行签订合同。」 | Phần 15 "Nhà cũ để môi giới thu hộ tiền mua nhà" |
| 《商品房屋租赁管理办法》(住建部 (Bộ Xây dựng) 令第 6 号) <http://www.gov.cn/gongbao/content/2011/content_1845070.htm> | Điều 8 「出租住房的，应当以原设计的房间为最小出租单位，人均租住建筑面积不得低于当地人民政府规定的最低标准。厨房、卫生间、阳台和地下储藏室不得出租供人员居住。」Điều 9 「出租人应当按照合同约定履行房屋的维修义务并确保房屋和室内设施安全……房屋租赁合同期内，出租人不得单方面随意提高租金水平。」 | Phần 15 "Đừng thuê phòng ngăn vách" |

## II. Vẫn chưa thu thập được
| Nội dung cần tìm | Kết quả |
| --- | --- |
| Toàn văn 《社会保险法》 (căn cứ pháp lý về thừa kế tài khoản cá nhân trong bảo hiểm hưu trí, chế độ tuất cho thân nhân) | Kho dữ liệu này chỉ thu thập văn bản thuộc hệ thống Quốc vụ viện (国务院), luật do Đại hội Đại biểu Nhân dân Toàn quốc (全国人大) ban hành không nằm trong số này; chuyên mục pháp luật của Viện Kiểm sát Nhân dân Tối cao Trung Quốc (最高检) chưa thu thập; liên kết phỏng đoán của npc.gov.cn trả về trang điều hướng. Giữ lại TODO liên quan ở phần 25 |
| Tiêu chuẩn cụ thể về trợ cấp mai táng, tiền tuất cho thân nhân | Văn bản của 人社部 (Bộ Nguồn nhân lực và An sinh xã hội) không có trong kho này, máy này không truy cập được mohrss.gov.cn. Giữ lại TODO liên quan ở phần 25 |
| Hạn mức trách nhiệm của bảo hiểm trách nhiệm dân sự bắt buộc của chủ xe cơ giới (交强险), thông báo về xét nghiệm vi chất cho trẻ em, đơn giản hóa thủ tục rút tiền gửi nhỏ của người đã qua đời | Thử lại bằng `searchfield=title` vẫn không có kết quả |

## III. Tiêu chí tính và mức độ lợi ích
- Tài khoản chuyên dùng cho tiền giao dịch nhà cũ xếp loại "Tiền bạc, lớn": số tiền cho một giao dịch từ vài trăm nghìn đến vài triệu nhân dân tệ, là việc có giá trị một lần lớn nhất trong toàn bộ cuốn sách.
- Phòng ngăn vách xếp loại "Tiền bạc, vừa": hậu quả trực tiếp khi bị kiểm tra xử lý là phải chuyển nhà, mất tiền đặt cọc và tiền thuê đã trả, thuộc mức từ vài trăm đến vài nghìn nhân dân tệ; rủi ro hỏa hoạn được ghi trong phần ghi chú, không quy đổi vào mức độ lợi ích (sách này không quy đổi chéo tiêu chí).
- Tiêu chí tính và mức độ của mục bệnh án ở phần 24 không đổi (Tiền bạc, vừa), chỉ nâng mức bằng chứng từ C lên A.
