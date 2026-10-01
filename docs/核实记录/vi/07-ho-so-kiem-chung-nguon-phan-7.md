> Bản dịch không chính thức của [docs/核实记录/07-没钱的时候怎么活.md](../../../docs/核实记录/07-没钱的时候怎么活.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Hồ sơ kiểm chứng nguồn phần 7

Ngày kiểm chứng 2026-09-07. Tất cả đều mở bằng WebFetch. Các đường dẫn cũ `/zhengce/…`, `/xinwen/…`, `/flfg/…` của gov.cn phần lớn trả về 404, còn `/gongbao/…`, `/zhengce/zhengceku/…`, `/guoqing/…`, `/lianbo/…` mở được; trang mohrss.gov.cn trả về trắng (có lẽ do script phía giao diện dựng), mca.gov.cn trả về 403, moj.gov.cn và npc.gov.cn lần lượt gặp vòng lặp chuyển hướng và lỗi bắt tay TLS, nhsa.gov.cn mở được nhưng trong site không tra ra thông báo bảo hiểm y tế cho cư dân năm 2025. Với những trường hợp trang gốc không mở được, trong mục đã ghi "chờ kiểm chứng" hoặc dùng trang chính thức khác và ghi rõ. Phần "Nguyên văn" dưới đây là câu gốc mà WebFetch lấy được từ trang.

## 1. Trợ cấp thất nghiệp
- <https://xzfg.moj.gov.cn/front/law/detail?LawID=517> — Đã mở (Kho văn bản quy phạm hành chính quốc gia, Bộ Tư pháp). Xác nhận 《失业保险条例》, Quyết định số 258 của Quốc vụ viện, ban hành 1999-01-22.
  - Nguyên văn Điều 14: "具备下列条件的失业人员，可以领取失业保险金：(一)按照规定参加失业保险，所在单位和本人已按照规定履行缴费义务满1年的；(二)非因本人意愿中断就业的；(三)已办理失业登记，并有求职要求的。"
  - Nguyên văn Điều 17: "累计缴费时间满1年不足5年的，领取失业保险金的期限最长为12个月；累计缴费时间满5年不足10年的，领取失业保险金的期限最长为18个月；累计缴费时间10年以上的，领取失业保险金的期限最长为24个月。"
  - Nguyên văn Điều 18: "失业保险金的标准，按照低于当地最低工资标准、高于城市居民最低生活保障标准的水平，由省、自治区、直辖市人民政府确定。"
- <https://www.12333.gov.cn/portal/common/bszn/sydysl?pfaId=202105281700000004> — Đã mở (Bộ Nhân lực và An sinh xã hội, hướng dẫn thủ tục trên Nền tảng dịch vụ chính sự nhân sự toàn quốc). Nguyên văn: "参保缴费满1年，并且非因本人意愿中断就业的失业人员"; nguyên văn kênh: "全国人社政务服务平台或国家社会保险公共服务平台", "掌上12333移动应用", "电子社保卡渠道（所有已开通电子社保卡的APP、小程序、公众号）".
- <https://www.ndrc.gov.cn/fggz/jyysr/jysrsbxf/202206/t20220627_1328819.html> — Đã mở (Vụ Việc làm, Ủy ban Cải cách và Phát triển Quốc gia Trung Quốc, 2022-06-27). Nguyên văn: "逐步将失业保险金标准提高至最低工资标准的90%". Trang không ghi số hiệu văn bản.
- Chưa xác nhận: trang nguyên văn 《关于调整失业保险金标准的指导意见》 của Bộ Nhân lực và An sinh xã hội <http://www.mohrss.gov.cn/xxgk2020/fdzdgknr/zcfg/gfxwj/shbx/201709/t20170925_278080.html> trả về trang trắng; trang giải thích của Cổng thông tin Chính phủ <https://www.gov.cn/zhengce/2017-09/27/content_5227865.htm> và <https://www.gov.cn/xinwen/2017-09/26/content_5227678.htm> trả về 404; cổng big5 bị vòng lặp chuyển hướng. Số hiệu văn bản chưa kiểm chứng, ghi chú của mục đã đánh dấu "文号待核实".
- Không sử dụng: si.12333.gov.cn/184890.jhtml và /184927.jhtml sau khi mở chỉ trả về hai chữ "首页".

## 2. Trọng tài lao động (劳动仲裁), nợ lương, trợ giúp pháp lý
- <https://chinajob.mohrss.gov.cn/h5/c/2022-07-15/356212.shtml> — Đã mở (中国就业网, trực thuộc Bộ Nhân lực và An sinh xã hội, tên miền mohrss.gov.cn). Xác nhận 《劳动争议调解仲裁法》, Lệnh Chủ tịch số 80, thông qua 2007-12-29, có hiệu lực 2008-05-01.
  - Nguyên văn Điều 53: "劳动争议仲裁不收费。劳动争议仲裁委员会的经费由财政予以保障。"
  - Nguyên văn khoản 1 Điều 27: "劳动争议申请仲裁的时效期间为一年。仲裁时效期间从当事人知道或者应当知道其权利被侵害之日起计算。"
  - Nguyên văn khoản 1 Điều 43: "应当自劳动争议仲裁委员会受理仲裁申请之日起四十五日内结束。……延长期限不得超过十五日。"
  - Điều khoản này còn được mở và đối chiếu khớp trên trang của Ủy ban Cải cách và Phát triển Thành phố Thượng Hải <https://fgw.sh.gov.cn/ys-laogong-1.7.1.1/20240125/8842664277d44777ab8785e9cff148b4.html>; hai đường dẫn /flfg/ và /ziliao/flfg/ của gov.cn đều 404; trang công báo của Tòa án nhân dân tối cao Trung Quốc trả về 502.
- <https://www.gov.cn/gongbao/content/2020/content_5469641.htm> — Đã mở. Xác nhận 《保障农民工工资支付条例》, Quyết định số 724 của Quốc vụ viện, thông qua 2019-12-04, có hiệu lực 2020-05-01.
  - Nguyên văn Điều 10: "被拖欠工资的农民工有权依法投诉，或者申请劳动争议调解仲裁和提起诉讼。任何单位和个人对拖欠农民工工资的行为，有权向人力资源社会保障行政部门或者其他有关部门举报。"
  - Nguyên văn Điều 41 (trích đoạn): "涉嫌构成拒不支付劳动报酬罪的，应当按照有关规定及时移送公安机关审查并作出决定。"
- <https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/202504/t20250402_4053713.html> — Đã mở (Cổng thông tin Chính quyền Thành phố Bắc Kinh đăng lại toàn văn luật, trang chính thức của địa phương). Xác nhận 《法律援助法》 thông qua 2021-08-20, có hiệu lực 2022-01-01.
  - Nguyên văn Điều 2: "本法所称法律援助，是国家建立的为经济困难公民和符合法定条件的其他当事人无偿提供法律咨询、代理、刑事辩护等法律服务的制度"
  - Nguyên văn điểm (5) khoản 1 Điều 31: "请求确认劳动关系或者支付劳动报酬"
  - Nguyên văn Điều 42 (trích đoạn): "免予核查经济困难状况：……（三）申请支付劳动报酬或者请求工伤事故人身损害赔偿的进城务工人员"
  - Trang của Bộ Tư pháp moj.gov.cn (hai URL) bị vòng lặp chuyển hướng, trang npc.gov.cn của Đại hội đại biểu nhân dân toàn quốc lỗi TLS, đường dẫn gov.cn/xinwen trả về 404, nên đã dùng trang đăng lại của Cổng thông tin Chính quyền Thành phố Bắc Kinh.
- Đường dây nóng 12348: các trang liên quan của Bộ Tư pháp đều không mở được, chưa xác nhận; ghi chú của mục đã ghi rõ số này không xuất hiện trong nguyên văn đã kiểm chứng.

## 3. Trạm cứu trợ
- <https://www.gov.cn/gongbao/content/2003/content_62246.htm> — Đã mở. Xác nhận 《城市生活无着的流浪乞讨人员救助管理办法》, Quyết định số 381 của Quốc vụ viện, công bố 2003-06-20, có hiệu lực 2003-08-01.
  - Nguyên văn Điều 5: "公安机关和其他有关行政机关的工作人员在执行职务时发现流浪乞讨人员的，应当告知其向救助站求助；对其中的残疾人、未成年人、老年人和行动不便的其他人员，还应当引导、护送到救助站。"
  - Nguyên văn Điều 6: "向救助站求助的流浪乞讨人员，应当如实提供本人的姓名等基本情况并将随身携带物品在救助站登记"
  - Điều 7: thức ăn, chỗ ở, đưa đi cấp cứu khi ốm đau, liên hệ người thân và đơn vị, giấy đi đường (WebFetch tóm tắt, khớp với nội dung đã ghi trong mục).
- <https://www.gov.cn/gongbao/content/2003/content_62510.htm> — Đã mở. Xác nhận 《…实施细则》, Lệnh số 24 của Bộ Dân chính, công bố 2003-07-21, có hiệu lực 2003-08-01.
  - Nguyên văn Điều 12: "救助站应当根据受助人员的情况确定救助期限，一般不超过10天"
  - Nguyên văn Điều 11: "受助人员返回常住户口所在地、住所地或者所在单位时没有交通费的，由救助站发给乘车(船)凭证"

## 4. Cấp cứu trước, chữa trị trước
- <https://www.gov.cn/zhengce/zhengceku/2013-03/01/content_6069.htm> — Đã mở. Xác nhận 国办发〔2013〕15 号, ban hành 2013-02-22.
  - Nguyên văn: "在中国境内发生急重危伤病、需要急救但身份不明确或无力支付相应费用的患者"
  - Nguyên văn: "各级各类医疗机构及其工作人员必须及时、有效地对急重危伤患者施救,不得以任何理由拒绝、推诿或拖延救治"
  - Nguyên văn: "1.无法查明身份患者所发生的急救费用。2.身份明确但无力缴费的患者所拖欠的急救费用"
- <https://www.gov.cn/gongbao/content/2014/content_2580977.htm> — Đã mở. Xác nhận 《院前医疗急救管理办法》, Lệnh số 3 của Ủy ban Y tế và Kế hoạch hóa gia đình Quốc gia, công bố 2013-11-29, có hiệu lực 2014-02-01.
  - Nguyên văn Điều 25: "急救中心（站）和急救网络医院按照国家有关规定收取院前医疗急救服务费用，不得因费用问题拒绝或者延误院前医疗急救服务。"
  - Nguyên văn Điều 37 (trích đoạn): "（三）急救中心（站）因指挥调度或者费用等因素拒绝、推诿或者延误院前医疗急救服务的"

## 5. Dịch vụ việc làm công, chợ lao động thời vụ
- <https://www.gov.cn/guoqing/2021-10/29/content_5647636.htm> — đã mở. Xác nhận Luật Xúc tiến việc làm (《就业促进法》) thông qua ngày 30-08-2007, sửa đổi ngày 24-04-2015.
  - Nguyên văn Điều 35: "为劳动者免费提供下列服务：（一）就业政策法规咨询；（二）职业供求信息、市场工资指导价位信息和职业培训信息发布；（三）职业指导和职业介绍；（四）对就业困难人员实施就业援助；（五）办理就业登记、失业登记等事务；（六）其他公共就业服务。"（第五十二、五十三条见第 10 条）
- <https://www.gov.cn/zhengce/zhengceku/2022-07/09/content_5700177.htm> — đã mở. Xác nhận 人社部发〔2022〕38 号, ngày 22-06-2022.
  - Nguyên văn: "免费向社会提供零工求职招聘信息登记和发布服务。"；"将零工信息纳入公共就业信息服务范围"；"对待工时间长、低收入家庭、残疾等大龄和困难零工人员加强就业帮扶"
  - Lưu ý: phiếu nhiệm vụ ghi là "văn bản chợ lao động thời vụ năm 2023 của Bộ Nhân lực và Xã hội", thực tế văn bản cấp quốc gia là văn bản số 38 năm 2022, mục này ghi theo kết quả kiểm chứng là năm 2022.

## 6, 7. Cứu trợ tạm thời, trợ cấp sinh hoạt tối thiểu (低保)
- <https://www.gov.cn/gongbao/content/2019/content_5468952.htm> — đã mở (Công báo Quốc vụ viện 2019, số tăng). Xác nhận Biện pháp tạm thời về cứu trợ xã hội (《社会救助暂行办法》) Quốc vụ viện lệnh số 649, công bố ngày 21-02-2014, sửa đổi theo Quốc vụ viện lệnh ngày 02-03-2019.
  - Nguyên văn Điều 9: "国家对共同生活的家庭成员人均收入低于当地最低生活保障标准，且符合当地最低生活保障家庭财产状况规定的家庭，给予最低生活保障。"
  - Nguyên văn Điều 10: "最低生活保障标准，由省、自治区、直辖市或者设区的市级人民政府按照当地居民生活必需的费用确定、公布，并根据当地经济社会发展水平和物价变动情况适时调整。"
  - Nguyên văn khoản 1 Điều 11: "由共同生活的家庭成员向户籍所在地的乡镇人民政府、街道办事处提出书面申请；家庭成员申请有困难的，可以委托村民委员会、居民委员会代为提出申请。"
  - Nguyên văn Điều 47: "国家对因火灾、交通事故等意外事件，家庭成员突发重大疾病等原因，导致基本生活暂时出现严重困难的家庭...给予临时救助。"
  - Nguyên văn Điều 48: "申请临时救助的，应当向乡镇人民政府、街道办事处提出，经审核、公示后，由县级人民政府民政部门审批。"
  - Nguyên văn Điều 49: "临时救助的具体事项、标准，由县级以上地方人民政府确定、公布。"
- <https://www.gov.cn/lianbo/bumen/202509/content_7042627.htm> — đã mở (báo cáo của Cục Thống kê Quốc gia Trung Quốc, ngày 28-09-2025).
  - Nguyên văn: "2024年末，我国城市、农村最低生活保障人数分别为625.0万人、3361.5万人；城市和农村最低生活保障平均标准分别为每人每月798.1元和593.9元"
- <https://www.gov.cn/zhengce/zhengceku/202403/content_7007237.htm> — đã mở. Xác nhận 民发〔2024〕16 号, bốn bộ ngành gồm Bộ Dân chính, ngày 21-03-2024.
  - Nguyên văn: "低保标准=当地上年度城镇（农村）居民人均消费支出×量化比例。"
- Không sử dụng: trang báo cáo thống kê quý của Bộ Dân chính mca.gov.cn trả lỗi 403, trang tra cứu chuẩn trợ cấp sinh hoạt tối thiểu chỉ liệt kê đến quý I năm 2022; tệp PDF Công báo phát triển sự nghiệp dân chính năm 2024 (mca.gov.cn …/400985.pdf) tải được nhưng trích xuất văn bản thất bại, không dẫn. Trang tin gov.cn ngày 01-01-2026 content_7053625 có "截至2025年10月底…低保对象3910.4万人" nhưng không có số liệu chuẩn bình quân, không dẫn.

## 8. Bảo hiểm y tế (医保) cư dân
- <https://www.nhsa.gov.cn/art/2024/8/26/art_105_13634.html> — đã mở (giải thích chính sách của Cục Bảo hiểm Y tế Quốc gia, ngày 26-08-2024, số hiệu văn bản 医保发〔2024〕19 号).
  - Nguyên văn: "财政补助和个人缴费标准分别较上年增加30元和20元，每人每年分别不低于670元和400元"
- <https://www.renqiu.gov.cn/renqiu/ybjbmwj/202510/6d90754638a248cba655e94ea518a3bb.shtml> — đã mở (trang thành phố Nhâm Khâu đăng lại văn bản của Cục Bảo hiểm Y tế tỉnh Hà Bắc và các đơn vị, 冀医保发〔2025〕6 号, ngày 25-09-2025, văn bản địa phương).
  - Nguyên văn: "2025年居民医保人均财政补助标准较上年提高30元，达到每人每年不低于700元"；"可维持每人每年不低于400元"；"全额资助特困人员、孤儿，对最低生活保障对象、纳入监测范围且未消除风险的防止返贫监测对象按不低于60%的标准定额资助"
  - Chưa xác nhận: Thông báo về việc làm tốt công tác bảo đảm y tế cơ bản cho cư dân thành thị và nông thôn năm 2025 (《关于做好 2025 年城乡居民基本医疗保障有关工作的通知》) của Cục Bảo hiểm Y tế Quốc gia (kết quả tìm kiếm ghi là 医保发〔2025〕22 号) không tìm thấy trang văn bản gốc trên nhsa.gov.cn và gov.cn, ghi chú của mục đã đánh dấu chờ kiểm chứng. Thông báo cấp quốc gia năm 2026 tính đến ngày kiểm chứng chưa tìm thấy.
- <https://www.gov.cn/gongbao/content/2021/content_5659514.htm> — đã mở. Xác nhận 国办发〔2021〕42 号, ngày 28-10-2021.
  - Nguyên văn: "全额资助特困人员，定额资助低保对象、返贫致贫人口。"；"对低保对象、特困人员符合规定的医疗费用可按不低于70%的比例救助"
- <https://www.gov.cn/zhengce/content/202408/content_6965741.htm> — đã mở. Xác nhận 国办发〔2024〕38 号, ban hành ngày 26-07-2024.
  - Nguyên văn: "对未在居民医保集中参保期内参保或未连续参保的人员，设置参保后固定待遇等待期3个月"；"未连续参保的，每多断保1年，原则上在固定待遇等待期基础上增加变动待遇等待期1个月"
  - Văn bản này cũng được mở và đối chiếu tại <https://app.www.gov.cn/govdata/gov/202408/01/517878/article.html>, kết quả nhất quán, và có thêm "每多缴纳1年可减少1个月变动待遇等待期".
- <https://www.nhsa.gov.cn/art/2026/3/5/art_14_19809.html> — đã mở (Cục Bảo hiểm Y tế Quốc gia, ngày 05-03-2026). Nguyên văn: "居民医保人均财政补助标准提高24元。"

## 9. Căn cước công dân
- <https://www.gov.cn/gongbao/content/2003/content_62254.htm> — đã mở. Xác nhận Luật Căn cước công dân (《居民身份证法》) Chủ tịch lệnh số 4, ngày 28-06-2003.
  - Nguyên văn Điều 12: "公安机关应当自公民提交《居民身份证申领登记表》之日起六十日内发放居民身份证。"
  - Nguyên văn Điều 20: "公民申请领取、换领、补领居民身份证，应当缴纳证件工本费。居民身份证工本费标准，由国务院价格主管部门会同国务院财政部门核定。"
  - Lưu ý: bản được dẫn là bản công bố năm 2003, luật này có sửa đổi năm 2011, ghi chú của mục đã nêu rõ.
- <https://www.gov.cn/zhengce/2021-12/25/content_5712922.htm> — đã mở. Xác nhận Biện pháp quản lý căn cước công dân tạm thời (《临时居民身份证管理办法》) Bộ Công an lệnh số 78, ngày 07-06-2005, thi hành từ ngày 01-10-2005.
  - Nguyên văn Điều 2: "在申请领取换领、补领居民身份证期间，急需使用居民身份证的，可以申请领取临时居民身份证。"
  - Nguyên văn Điều 7: "临时居民身份证的有效期限为三个月"
  - Nguyên văn Điều 9: "可以向常住户口所在地的公安派出所申请领取临时居民身份证。"
  - Nguyên văn Điều 12: "并在收到申请后的三日内将临时居民身份证发给申领人。"
  - Nguyên văn Điều 17: "公民申请领取、换领、补领临时居民身份证，应当缴纳证件工本费。"

## 10. Trợ cấp cho người khó khăn về việc làm
- <https://www.gov.cn/zhengce/zhengceku/202401/content_6926462.htm> — đã mở. Xác nhận Biện pháp quản lý vốn trợ cấp việc làm (《就业补助资金管理办法》) của Bộ Tài chính và Bộ Nhân lực và Xã hội (bản sửa đổi 财社〔2017〕164 号), ngày 20-12-2023.
  - Nguyên văn: "对就业困难人员灵活就业后缴纳的社会保险费，给予一定数额的社会保险补贴，补贴标准原则上不超过其实际缴费的2/3"；"最长不超过3年"
  - Nguyên văn: "对公益性岗位安置的就业困难人员给予岗位补贴，补贴标准参照当地最低工资标准执行"
  - Nguyên văn: "对在毕业学年积极求职创业的低保家庭、零就业家庭、防止返贫监测对象家庭和特困人员中的高校毕业生，残疾及获得国家助学贷款的高校毕业生，给予一次性求职补贴"
- Luật Xúc tiến việc làm (cùng trang với mục 5) nguyên văn Điều 52: "采取税费减免、贷款贴息、社会保险补贴、岗位补贴等办法，通过公益性岗位安置等途径，对就业困难人员实行优先扶持和重点帮助"；nguyên văn Điều 53: "政府投资开发的公益性岗位，应当优先安排符合岗位要求的就业困难人员。"
- Không sử dụng: trợ cấp nâng cao kỹ năng từ bảo hiểm thất nghiệp (人社部发〔2017〕40 号, 1000/1500/2000 元) trang văn bản gốc của Bộ Nhân lực và Xã hội trống, trang tin gov.cn trả lỗi 404, không kiểm chứng được, bỏ toàn bộ mục.

## 11. Can thiệp tìm việc
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1037/a0035923%22&resultType=core&format=json> — đã mở (bản ghi Europe PMC, trang PubMed chỉ trả về thông báo cookie). Xác nhận Liu S, Huang JL, Wang M, Psychological Bulletin 2014;140:1009-1041, DOI 10.1037/a0035923.
  - Nguyên văn: "Summarizing the data from 47 experimentally or quasi-experimentally evaluated job search interventions"; "the odds of obtaining employment were 2.67 times higher for job seekers participating in job search interventions"
  - Nguyên văn (thành phần hiệu quả): "teaching job search skills, improving self-presentation, boosting self-efficacy, encouraging proactivity, promoting goal setting, and enlisting social support"; cần đồng thời có "skill development and motivation enhancement".

## 12. Tránh hố
- <https://www.gov.cn/gongbao/content/2007/content_711013.htm> — đã mở. Xác nhận 《劳动合同法》 lệnh Chủ tịch số 65, thông qua ngày 2007-06-29.
  - Nguyên văn Điều 9: "用人单位招用劳动者，不得扣押劳动者的居民身份证和其他证件，不得要求劳动者提供担保或者以其他名义向劳动者收取财物。"
  - Nguyên văn Điều 84 (trích): "以担保或者其他名义向劳动者收取财物的，由劳动行政部门责令限期退还劳动者本人，并以每人五百元以上二千元以下的标准处以罚款"
  - Còn đối chiếu tại trang Tổng cục Quản lý thị trường nhà nước <https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/bgt/art/2023/art_0abfdd261c03417b949df19d869add8d.html> (bản sửa đổi 2012), chữ của Điều 9 và Điều 84 khớp nhau.
- <https://www.gov.cn/zhengce/2022-11/28/content_5711307.htm> — đã mở. Xác nhận 《就业服务与就业管理规定》 lệnh Bộ Lao động và Bảo đảm xã hội số 28, ban hành 2007-11-05.
  - Nguyên văn Điều 14 (trích): "扣押被录用人员的居民身份证和其他证件"; "以担保或者其他名义向劳动者收取财物"
  - Nguyên văn Điều 55: "提供职业中介服务不成功的，应当退还向劳动者收取的中介服务费"; Điều 58 cấm "扣押劳动者的居民身份证和其他证件，或者向劳动者收取押金"
- <https://chinajob.mohrss.gov.cn/h5/c/2026-05-18/543038.shtml> — đã mở (Bộ Nhân lực và Bảo đảm xã hội, Văn phòng Thông tin hóa của Ban Chỉ đạo Trung ương, Bộ Giáo dục, Bộ Công an, Tổng cục Giám sát Tài chính, ngày 2026-05-18).
  - Nguyên văn: "一些不法分子以招聘为名进行引流，变相推销培训课程，诱导求职者支付高额费用，甚至申请贷款参加培训"; "应果断拒绝"
- <https://www.gov.cn/gongbao/content/2005/content_80604.htm> — đã mở. Xác nhận 《禁止传销条例》 lệnh Quốc vụ viện số 444, thông qua 2005-08-10, thi hành 2005-11-01.
  - Nguyên văn khoản 1 Điều 7 (trích): "要求被发展人员发展其他人员加入，对发展的人员以其直接或者间接滚动发展的人员数量为依据计算和给付报酬"
  - Nguyên văn Điều 24: "有本条例第七条规定的行为，参加传销的，由工商行政管理部门责令停止违法行为，可以处2000元以下的罚款。"
- <https://www.court.gov.cn/fabu/xiangqing/249031.html> — đã mở. Xác nhận quyết định sửa đổi của Tòa án nhân dân tối cao Trung Quốc, 法释〔2020〕6 号, thi hành 2020-08-20.
  - Nguyên văn Điều 26: "双方约定的利率超过合同成立时一年期贷款市场报价利率四倍的除外。"
- <https://www.court.gov.cn/zixun/xiangqing/249051.html> — đã mở (tin của Tòa án nhân dân tối cao Trung Quốc, 2020-08-20).
  - Nguyên văn: "以…一年期贷款市场报价利率（LPR）的4倍为标准确定民间借贷利率的司法保护上限，取代原规定中"以24%和36%为基准的两线三区"的规定"
  - Chưa xác nhận: toàn văn sau lần sửa đổi thứ hai tháng 12 năm 2020 (trang công báo của Tòa án nhân dân tối cao Trung Quốc gongbao.court.gov.cn ba lần lỗi 502, trang Tòa án Thương mại Quốc tế lặp vòng chuyển hướng), nên mục này dẫn Điều 26 của bản tháng 8 năm 2020, và ghi chú rằng số điều đã thay đổi.
- Gợi ý tìm việc ngày 2024-05-22 của Bộ Giáo dục <https://app.www.gov.cn/govdata/gov/202405/22/515248/article.html> — đã mở, có "培训贷、购车贷、美容贷等新型招聘陷阱", dùng làm bằng chứng bên lề, chưa đưa vào nguồn.

## 13. Nhà ở xã hội cho thuê
- <https://www.gov.cn/gongbao/content/2012/content_2226147.htm> — đã mở. Xác nhận 《公共租赁住房管理办法》 lệnh Bộ Nhà ở và Xây dựng thành thị - nông thôn số 11, công bố 2012-05-28, thi hành 2012-07-15.
  - Nguyên văn Điều 7: "申请公共租赁住房，应当符合以下条件：（一）在本地无住房或者住房面积低于规定标准；（二）收入、财产低于规定标准；（三）申请人为外来务工人员的，在本地稳定就业达到规定年限。"
  - Nguyên văn Điều 8: "申请人应当根据市、县级人民政府住房保障主管部门的规定，提交申请材料，并对申请材料的真实性负责。"
  - Nguyên văn Điều 10: "对登记为轮候对象的申请人，应当在轮候期内安排公共租赁住房。轮候期一般不超过5年。"

## 14. Chi tiêu cố định
- <https://www.stats.gov.cn/sj/zxfbhjd/202601/t20260119_1962321.html> — đã mở (Cục Thống kê Quốc gia Trung Quốc, 2026-01-19).
  - Nguyên văn: "2025年，全国居民人均消费支出29476元"; "人均食品烟酒消费支出8631元，增长2.6%，占人均消费支出的比重为29.3%"; "人均居住消费支出6397元，增长2.1%，占人均消费支出的比重为21.7%"
- <https://www.gov.cn/govweb/zhengce/zhengceku/202310/content_6911233.htm> — đã mở. Xác nhận 《积极发展老年助餐服务行动方案》 民发〔2023〕58 号, 2023-10-20.
  - Nguyên văn: "完善老年食堂、老年餐桌、老年助餐点等老年助餐服务设施配置"; "对享受助餐服务的老年人给予差异化补贴"; "面向其他老年人的助餐服务广泛开展"
- <https://rst.sc.gov.cn/rst/ylbxjwjgzxx/2026/7/10/89a8ef06cc264d29b282d7c62f362a6b.shtml> — đã mở (Sở Nhân lực và Bảo đảm xã hội tỉnh Tứ Xuyên, 2026-07-10, tiêu đề 「全国各省、自治区、直辖市最低工资标准情况（截至2026年1月1日）」, trang ghi nguồn là trang web chính thức của Bộ Nhân lực và Bảo đảm xã hội). Mức lương tối thiểu tháng bậc một cao nhất là Thượng Hải 2740 nhân dân tệ, thấp nhất là Thanh Hải 2080 nhân dân tệ.
  - Chưa xác nhận: trang gốc của Bộ Nhân lực và Bảo đảm xã hội <https://www.mohrss.gov.cn/SYrlzyhshbzb/laodongguanxi_/fwyd/> trả về trắng, trang kỳ 2025-01 lỗi 403. Số lương tối thiểu theo giờ chưa dùng.

## 15. Đứt đóng bảo hiểm xã hội
- <https://www.gov.cn/guoqing/2021-10/29/content_5647616.htm> — đã mở. Xác nhận 《社会保险法》 thông qua 2010-10-28, sửa đổi 2018-12-29.
  - Nguyên văn Điều 16: "参加基本养老保险的个人，达到法定退休年龄时累计缴费满十五年的，按月领取基本养老金。"
  - Nguyên văn Điều 19: "个人跨统筹地区就业的，其基本养老保险关系随本人转移，缴费年限累计计算。"
  - Nguyên văn Điều 27: "参加职工基本医疗保险的个人，达到法定退休年龄时累计缴费达到国家规定年限的，退休后不再缴纳基本医疗保险费。"
- 国办发〔2024〕38 号 giống mục 8.

## 16. Địa điểm 24 giờ
- Mục kinh nghiệm cấp C, không có nguồn.

## Ứng viên không đưa vào
- Trợ cấp thất nghiệp (人社部发〔2020〕40 号): thuộc chính sách giai đoạn 2020, trang gốc có trên chinajob.mohrss.gov.cn, nhưng không xác minh được liệu còn hiệu lực đến nay hay không, nên không đưa vào.
- Thông báo riêng về cứu trợ khẩn cấp (国发〔2014〕47 号): chưa xác minh riêng, cứu trợ khẩn cấp lấy căn cứ theo 《社会救助暂行办法》.
- Hậu quả của việc nợ tiền nước, điện, gas: không tìm được văn bản gốc chính thức ở cấp quốc gia, không đưa vào.
