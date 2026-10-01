> Bản dịch không chính thức của [docs/核实记录/12-创业与做生意.md](../../../docs/核实记录/12-创业与做生意.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Hồ sơ kiểm chứng nguồn phần 12 (2026-09-07)

Phương thức kiểm chứng: Hạn mức WebSearch của phiên này đã dùng hết, việc định vị văn bản quy phạm chuyển sang dùng giao diện tìm kiếm của kho văn bản chính sách thuộc 中国政府网 (Cổng thông tin Chính phủ Trung Quốc) (sousuo.www.gov.cn/search-gov/data, chỉ dùng để tìm URL, không dùng làm nguồn). Mỗi URL trước tiên dùng WebFetch mở để xác nhận tiêu đề, số hiệu văn bản và điều khoản; trang toàn văn luật dùng riêng curl tải về scratchpad (s12/page_*.html), sau khi bóc tách thẻ thì định vị nguyên văn từng chữ theo "Điều X", các câu trích dẫn bên dưới đều lấy từ định vị cục bộ. Trang của 人社部 (Bộ Nhân lực và An sinh Xã hội) có mã chống thu thập dữ liệu, WebFetch trả về trang trắng, chuyển sang dùng curl mang theo cookie do mã tính toán để mở và lấy toàn văn (đã đối chiếu tiêu đề trang và dòng phiên bản). Chứng chỉ hệ thống nhượng quyền thương mại của 商务部 (Bộ Thương mại) không khớp với tên miền, WebFetch báo lỗi, chuyển sang dùng curl -k để mở và đối chiếu tiêu đề. DOI chuyển hướng qua doi.org tới pubsonline.informs.org trả về 403, chuyển sang dùng Crossref API và Semantic Scholar API để đối chiếu thông tin thư mục và tóm tắt.

## Các nguồn đã xác nhận
### 1. 民法典
- URL: <https://www.spp.gov.cn/spp/fl/202006/t20200602_463888.shtml> (kho văn bản pháp luật của 最高检 (Viện Kiểm sát Nhân dân Tối cao Trung Quốc))
- Tiêu đề trang 「中华人民共和国民法典」, dòng phiên bản có 「2020年5月28日第十三届全国人民代表大会第三次会议通过」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 56: 「个体工商户的债务，个人经营的，以个人财产承担；家庭经营的，以家庭财产承担；无法区分的，以家庭财产承担。」
- Điều 184: 「因自愿实施紧急救助行为造成受助人损害的，救助人不承担民事责任。」
- Điều 469: 「当事人订立合同，可以采用书面形式、口头形式或者其他形式。书面形式是合同书、信件、电报、电传、传真等可以有形地表现所载内容的形式。」
- Điều 585: 「当事人可以约定一方违约时应当根据违约情况向对方支付一定数额的违约金……约定的违约金低于造成的损失的，人民法院或者仲裁机构可以根据当事人的请求予以增加；约定的违约金过分高于造成的损失的，人民法院或者仲裁机构可以根据当事人的请求予以适当减少。」
- Điều 586: 「当事人可以约定一方向对方给付定金作为债权的担保。定金合同自实际交付定金时成立。定金的数额由当事人约定；但是，不得超过主合同标的额的百分之二十，超过部分不产生定金的效力。」
- Điều 587: 「给付定金的一方不履行债务……无权请求返还定金；收受定金的一方不履行债务……应当双倍返还定金。」
- Điều 588: 「当事人既约定违约金，又约定定金的，一方违约时，对方可以选择适用违约金或者定金条款。」
- Điều 668: 「借款合同应当采用书面形式，但是自然人之间借款另有约定的除外。借款合同的内容一般包括借款种类、币种、用途、数额、利率、期限和还款方式等条款。」
- Điều 681: 「保证合同是为保障债权的实现，保证人和债权人约定，当债务人不履行到期债务或者发生当事人约定的情形时，保证人履行债务或者承担责任的合同。」
- Điều 687: 「当事人在保证合同中约定，债务人不能履行债务时，由保证人承担保证责任的，为一般保证。一般保证的保证人在主合同纠纷未经审判或者仲裁，并就债务人财产依法强制执行仍不能履行债务前，有权拒绝向债权人承担保证责任」
- Điều 688: 「当事人在保证合同中约定保证人和债务人对债务承担连带责任的，为连带责任保证。连带责任保证的债务人不履行到期债务……债权人可以请求债务人履行债务，也可以请求保证人在其保证范围内承担保证责任。」
- Điều 1064: 「夫妻双方共同签名或者夫妻一方事后追认等共同意思表示所负的债务……属于夫妻共同债务。夫妻一方在婚姻关系存续期间以个人名义超出家庭日常生活需要所负的债务，不属于夫妻共同债务；但是，债权人能够证明该债务用于夫妻共同生活、共同生产经营或者基于夫妻双方共同意思表示的除外。」

### 2. 公司法 (sửa đổi năm 2023)
- URL: <https://www.gov.cn/yaowen/liebiao/202312/content_6923395.htm> (中国政府网 (Cổng thông tin Chính phủ Trung Quốc))
- Tiêu đề trang 「中华人民共和国公司法」, dòng phiên bản có 「2023年12月29日第十四届全国人民代表大会常务委员会第七次会议第二次修订」. Cả WebFetch và định vị cục bộ đều đã xác nhận, số thứ tự điều khoản được đối chiếu theo bản sửa đổi năm 2023.
- Điều 4: 「有限责任公司的股东以其认缴的出资额为限对公司承担责任；股份有限公司的股东以其认购的股份为限对公司承担责任。」
- Điều 23: 「公司股东滥用公司法人独立地位和股东有限责任，逃避债务，严重损害公司债权人利益的，应当对公司债务承担连带责任。……只有一个股东的公司，股东不能证明公司财产独立于股东自己的财产的，应当对公司债务承担连带责任。」
- Điều 47: 「有限责任公司的注册资本为在公司登记机关登记的全体股东认缴的出资额。全体股东认缴的出资额由股东按照公司章程的规定自公司成立之日起五年内缴足。」
- Điều 49: 「股东应当按期足额缴纳公司章程规定的各自所认缴的出资额。……股东未按期足额缴纳出资的，除应当向公司足额缴纳外，还应当对给公司造成的损失承担赔偿责任。」
- Điều 50: 「有限责任公司设立时，股东未按照公司章程规定实际缴纳出资……设立时的其他股东与该股东在出资不足的范围内承担连带责任。」
- Điều 53: 「公司成立后，股东不得抽逃出资。违反前款规定的，股东应当返还抽逃的出资」
- Điều 54: 「公司不能清偿到期债务的，公司或者已到期债权的债权人有权要求已认缴出资但未届出资期限的股东提前缴纳出资。」

### 3. 合伙企业法 (sửa đổi năm 2006)
- URL: <http://www.gov.cn/gongbao/content/2006/content_413955.htm> (Công báo 国务院 (Quốc vụ viện Trung Quốc) năm 2006, số 29)
- Tiêu đề trang 「中华人民共和国主席令（第五十五号）　中华人民共和国合伙企业法」, 「2006年8月27日修订通过……自2007年6月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 2: 「普通合伙企业由普通合伙人组成，合伙人对合伙企业债务承担无限连带责任。……有限合伙企业由普通合伙人和有限合伙人组成，普通合伙人对合伙企业债务承担无限连带责任，有限合伙人以其认缴的出资额为限对合伙企业债务承担责任。」

### 4. 商业特许经营管理条例
- URL: <https://www.gov.cn/zhengce/zhengceku/2008-03/28/content_4179.htm>
- Tiêu đề trang 「商业特许经营管理条例」, số hiệu 「国令第485号」, 「2007年1月31日国务院第167次常务会议通过……自2007年5月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 7 khoản 2: 「特许人从事特许经营活动应当拥有至少2个直营店，并且经营时间超过1年。」
- Điều 8: 「特许人应当自首次订立特许经营合同之日起15日内，依照本条例的规定向商务主管部门备案。」
- Điều 12: 「特许人和被特许人应当在特许经营合同中约定，被特许人在特许经营合同订立后一定期限内，可以单方解除合同。」
- Điều 22: Liệt kê 12 hạng mục thông tin phải cung cấp, bao gồm 「（三）特许经营费用的种类、金额和支付方式（包括是否收取保证金以及保证金的返还条件和返还方式）」, 「（八）在中国境内现有的被特许人的数量、分布地域以及经营状况评估」, 「（九）最近2年的经会计师事务所审计的财务会计报告摘要和审计报告摘要」, 「（十）最近5年内与特许经营相关的诉讼和仲裁情况」.
- Điều 23: 「特许人隐瞒有关信息或者提供虚假信息的，被特许人可以解除特许经营合同。」
- Điều 25: 「特许人未依照本条例第八条的规定向商务主管部门备案的，由商务主管部门责令限期备案，处1万元以上5万元以下的罚款；逾期仍不备案的，处5万元以上10万元以下的罚款，并予以公告。」

### 5. 商业特许经营信息披露管理办法
- URL: <http://www.gov.cn/gongbao/content/2012/content_2177025.htm> (Công báo 国务院 (Quốc vụ viện Trung Quốc) năm 2012, số 19)
- Tiêu đề trang 「中华人民共和国商务部令（2012年第2号）　商业特许经营信息披露管理办法」, 「自2012年4月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 5 khoản (8) điểm 2: 「现有被特许人的经营状况，包括被特许人实际的投资额、平均销售量、成本、毛利、纯利等信息，同时应当说明上述信息的来源。」
- Điều 9: 「特许人隐瞒影响特许经营合同履行致使不能实现合同目的的信息或者披露虚假信息的，被特许人可以解除特许经营合同。」

### 6. 商务部 (Bộ Thương mại Trung Quốc) 商业特许经营信息管理系统
- URL: <https://txjy.syggs.mofcom.gov.cn/>
- WebFetch báo lỗi do tên miền chứng chỉ không khớp; mở bằng curl -k trả về 200, tiêu đề trang 「商务部业务系统统一平台-商业特许经营信息管理」, trong trang có liên kết đăng nhập doanh nghiệp, đăng ký và thông tin đăng ký hồ sơ. Đã xác nhận là hệ thống của 商务部 (Bộ Thương mại Trung Quốc).

### 7. 无证无照经营查处办法
- URL: <https://www.gov.cn/zhengce/zhengceku/2017-08/23/content_5219861.htm>
- Tiêu đề trang 「无证无照经营查处办法」, số hiệu 「国令第684号」, 「2017年10月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 5: 「经营者未依法取得许可从事经营活动的，由法律、法规、国务院决定规定的部门予以查处」
- Điều 6: 「经营者未依法取得营业执照从事经营活动的，由履行工商行政管理职责的部门……予以查处。」
- Điều 13: 「法律、行政法规对无照经营的处罚没有明确规定的，由工商行政管理部门责令停止违法行为，没收违法所得，并处1万元以下的罚款。」

### 8. 食品经营许可和备案管理办法
- URL: <https://www.gov.cn/gongbao/2023/issue_10606/202307/content_6894763.html> (Công báo 国务院 (Quốc vụ viện Trung Quốc) năm 2023, số 21)
- Tiêu đề trang 「国家市场监督管理总局令（第78号）　食品经营许可和备案管理办法」, 「自2023年12月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 4: 「在中华人民共和国境内从事食品销售和餐饮服务活动，应当依法取得食品经营许可。下列情形不需要取得食品经营许可：……（二）仅销售预包装食品」

### 9. 刑法 (văn bản sửa đổi năm 1997)
- URL: <https://www.spp.gov.cn/spp/fl/201802/t20180206_364975.shtml> (kho văn bản pháp luật của 最高检 (Viện Kiểm sát Nhân dân Tối cao Trung Quốc))
- Tiêu đề trang 「中华人民共和国刑法（1997年修订）」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 205: 「虚开增值税专用发票或者虚开用于骗取出口退税、抵扣税款的其他发票的，处三年以下有期徒刑或者拘役，并处二万元以上二十万元以下罚金；虚开的税款数额较大或者有其他严重情节的，处三年以上十年以下有期徒刑，并处五万元以上五十万元以下罚金；虚开的税款数额巨大或者有其他特别严重情节的，处十年以上有期徒刑或者无期徒刑……虚开增值税专用发票或者虚开用于骗取出口退税、抵扣税款的其他发票，是指有为他人虚开、为自己虚开、让他人为自己虚开、介绍他人虚开行为之一的。」 Trang này là văn bản năm 1997, có chứa khoản về hình phạt tử hình vốn đã bị Bản sửa đổi (VIII) bãi bỏ, phần chính văn không trích dẫn khoản này.
- Điều 225: 「违反国家规定，有下列非法经营行为之一，扰乱市场秩序，情节严重的，处五年以下有期徒刑或者拘役，并处或者单处违法所得一倍以上五倍以下罚金；情节特别严重的，处五年以上有期徒刑……（一）未经许可经营法律、行政法规规定的专营、专卖物品或者其他限制买卖的物品的；……（三）未经国家有关主管部门批准非法经营证券、期货、保险业务的，或者非法从事资金支付结算业务的」 (trên trang ghi chú điểm này được sửa đổi theo Bản sửa đổi (VII)).

### 10. 财政部 税务总局公告 2023 年第 19 号
- URL: <https://www.gov.cn/zhengce/zhengceku/202308/content_6896287.htm>
- Tiêu đề trang 「关于增值税小规模纳税人减免增值税政策的公告」, số hiệu 「财政部 税务总局公告2023年第19号」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- 「一、对月销售额10万元以下（含本数）的增值税小规模纳税人，免征增值税。」 「二、增值税小规模纳税人适用3%征收率的应税销售收入，减按1%征收率征收增值税」 「三、本公告执行至2027年12月31日。」

### 11. 劳动合同法
- URL: <https://www.gov.cn/gongbao/content/2007/content_711013.htm>
- Dòng phiên bản trên trang có 「2007年6月29日通过……自2008年1月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 10: 「已建立劳动关系，未同时订立书面劳动合同的，应当自用工之日起一个月内订立书面劳动合同。」
- Điều 17: 「劳动合同应当具备以下条款：……（六）劳动报酬；（七）社会保险」
- Điều 30: 「用人单位应当按照劳动合同约定和国家规定，向劳动者及时足额支付劳动报酬。用人单位拖欠或者未足额支付劳动报酬的，劳动者可以依法向当地人民法院申请支付令」
- Điều 82: 「用人单位自用工之日起超过一个月不满一年未与劳动者订立书面劳动合同的，应当向劳动者每月支付二倍的工资。」

### 12. 社会保险法 (sửa đổi năm 2018)
- URL: <https://www.mohrss.gov.cn/xxgk2020/fdzdgknr/zcfg/fl/202011/t20201102_394629.html> (人力资源社会保障部 (Bộ Nguồn nhân lực và An sinh xã hội Trung Quốc))
- WebFetch bị script chống cào dữ liệu chặn nên trả về trang trắng; dùng curl kèm cookie do script tính toán đã lấy được toàn văn 93 KB, tiêu đề trang 「中华人民共和国社会保险法_中华人民共和国人力资源和社会保障部」, dòng phiên bản có 「2010年10月28日……通过 根据2018年12月29日……《关于修改〈中华人民共和国社会保险法〉的决定》修正」. Liên kết lấy từ trang danh mục 「法律」 của bộ này (<https://www.mohrss.gov.cn/xxgk2020/fdzdgknr/zcfg/fl/>).
- Điều 58: 「用人单位应当自用工之日起三十日内为其职工向社会保险经办机构申请办理社会保险登记。」
- Điều 60: 「用人单位应当自行申报、按时足额缴纳社会保险费，非因不可抗力等法定事由不得缓缴、减免。」
- Điều 84: 「用人单位不办理社会保险登记的，由社会保险行政部门责令限期改正；逾期不改正的，对用人单位处应缴社会保险费数额一倍以上三倍以下的罚款，对其直接负责的主管人员和其他直接责任人员处五百元以上三千元以下的罚款。」
- Điều 86: 「用人单位未按时足额缴纳社会保险费的，由社会保险费征收机构责令限期缴纳或者补足，并自欠缴之日起，按日加收万分之五的滞纳金；逾期仍不缴纳的，由有关行政部门处欠缴数额一倍以上三倍以下的罚款。」

### 13. Camuffo et al. 2020 (RCT)
- DOI: <https://doi.org/10.1287/mnsc.2018.3249>
- WebFetch mở doi.org trả về mã chuyển hướng 302 sang <https://pubsonline.informs.org/doi/10.1287/mnsc.2018.3249>, trang này trả về lỗi 403. Đã chuyển sang dùng Crossref API (api.crossref.org/works/10.1287/mnsc.2018.3249) để xác nhận: nhan đề 「A Scientific Approach to Entrepreneurial Decision Making: Evidence from a Randomized Control Trial」, Management Science 66(2):564-586, tháng 2 năm 2020, tác giả Camuffo, Cordova, Gambardella, Spina. Semantic Scholar API lấy được bản tóm tắt: 「The panel sample of our randomized control trial includes 116 Italian startups and 16 data points over a period of about one year. … We find that entrepreneurs who behave like scientists perform better, are more likely to pivot to a different idea, and are not more likely to drop out than the control group in the early stages of the startup. … a scientific approach improves precision—it reduces the odds of pursuing projects with false positive returns」. Phần chính văn chỉ sử dụng nhận định từ tóm tắt, không ghi mức độ hiệu ứng cụ thể.

### 14. 强制性产品认证管理规定
- URL: <http://www.gov.cn/gongbao/content/2010/content_1533513.htm> (Công báo 国务院 (Quốc vụ viện Trung Quốc) năm 2010, số 5)
- Tiêu đề trang 「国家质量监督检验检疫总局令（第117号）　强制性产品认证管理规定」, 「自2009年9月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 2: 「国家规定的相关产品必须经过认证（以下简称强制性产品认证），并标注认证标志后，方可出厂、销售、进口或者在其他经营活动中使用。」
- Điều 49: 「列入目录的产品未经认证，擅自出厂、销售、进口或者在其他经营活动中使用的，由地方质检两局依照认证认可条例第六十七条规定予以处罚。」

### 15. 护士条例
- URL: <http://www.gov.cn/zhengce/zhengceku/2008-03/28/content_6169.htm>
- Tiêu đề trang 「护士条例」, số hiệu 「国令第517号」, 「2008年1月23日国务院第206次常务会议通过……自2008年5月12日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận. Đây là bản gốc năm 2008, chưa tìm thấy trang toàn văn chính thức của bản sửa đổi năm 2020.
- Điều 17: 「护士在执业活动中，发现患者病情危急，应当立即通知医师；在紧急情况下为抢救垂危患者生命，应当先行实施必要的紧急救护。护士发现医嘱违反法律、法规、规章或者诊疗技术规范规定的，应当及时向开具医嘱的医师提出；必要时，应当向该医师所在科室的负责人或者医疗卫生机构负责医疗服务管理的人员报告。」

### 16. 市场主体登记管理条例
- URL: <https://www.gov.cn/zhengce/zhengceku/2021-08/24/content_5632964.htm>
- Tiêu đề trang 「中华人民共和国市场主体登记管理条例」, số hiệu 「国令第746号」, 「自2022年3月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 31: 「市场主体因解散、被宣告破产或者其他法定事由需要终止的，应当依法向登记机关申请注销登记。」
- Điều 32: 「清算组应当自清算结束之日起30日内向登记机关申请注销登记。」
- Điều 33: 「市场主体未发生债权债务或者已将债权债务清偿完结，未发生或者已结清清偿费用、职工工资、社会保险费用、法定补偿金、应缴纳税款（滞纳金、罚款），并由全体投资人书面承诺对上述情况的真实性承担法律责任的，可以按照简易程序办理注销登记。……公示期为20日。……个体工商户按照简易程序办理注销登记的，无需公示……有关部门在10日内没有提出异议的，可以直接办理注销登记。……被列入经营异常名录的，不适用简易注销程序。」

### 17. 企业注销指引 (sửa đổi năm 2025)
- URL: <https://www.gov.cn/zhengce/zhengceku/202512/content_7053238.htm>
- Tiêu đề trang 「市场监管总局等六部门关于发布《企业注销指引（2025年修订）》的公告」, số hiệu 「2025年第52号」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- 「简易注销流程 1.适用对象。企业（上市股份有限公司除外）在存续期间未发生债权债务或已将债权债务清偿完结……可以按照简易程序办理注销登记。企业有下列情形之一的，不适用简易注销程序：……在经营异常名录或者市场监督管理严重违法失信名单中」

### 18. 企业破产法
- URL: <http://www.gov.cn/gongbao/content/2006/content_413952.htm> (Công báo 国务院 (Quốc vụ viện Trung Quốc) năm 2006, số 29)
- Tiêu đề trang 「中华人民共和国主席令（第五十四号）　中华人民共和国企业破产法」, 「自2007年6月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 2: 「企业法人不能清偿到期债务，并且资产不足以清偿全部债务或者明显缺乏清偿能力的，依照本法规定清理债务。」
- Điều 7: 「债务人有本法第二条规定的情形，可以向人民法院提出重整、和解或者破产清算申请。……企业法人已解散但未清算或者未清算完毕，资产不足以清偿债务的，依法负有清算责任的人应当向人民法院申请破产清算。」

### 19. 企业信息公示暂行条例
- URL: <https://www.gov.cn/zhengce/zhengceku/2014-08/23/content_9038.htm>
- Tiêu đề trang 「企业信息公示暂行条例」, số hiệu 「国令第654号」, 「自2014年10月1日起施行」. Cả WebFetch và định vị cục bộ đều đã xác nhận.
- Điều 17: 「（一）企业未按照本条例规定的期限公示年度报告……列入经营异常名录……满3年未依照本条例规定履行公示义务的……列入严重违法企业名单……被列入严重违法企业名单的企业的法定代表人、负责人，3年内不得担任其他企业的法定代表人、负责人。」
- Ngoài ra đã đối chiếu theo Lệnh số 777 của 国务院 (Quốc vụ viện Trung Quốc) 《国务院关于修改和废止部分行政法规的决定》 (<https://www.gov.cn/zhengce/zhengceku/202403/content_6939591.htm>): 「七、将《企业信息公示暂行条例》第二条、第五条第一款、第六条第一款、第七条、第八条第一款、第十条第二款、第十三条第一款、第十四条、第十五条、第二十四条中的“工商行政管理部门”修改为“市场监督管理部门”。」 Điều 17 không có trong danh sách. Có văn bản sửa đổi riêng năm 2024 hay không, đánh dấu TODO.

## Không thể kiểm chứng, chưa trích dẫn
- Thống kê chính thức về tỉ lệ sống sót/tuổi thọ trung bình của doanh nghiệp: Tìm kiếm nội bộ trên trang web của 国家统计局 (Cục Thống kê Quốc gia Trung Quốc) và cổng tra cứu gov.cn đều không có văn bản gốc để đối chiếu; không ghi số liệu.
- 最高法 (Tòa án nhân dân tối cao Trung Quốc) 《关于适用〈公司法〉若干问题的规定（三）》 Điều 24 (đứng tên cổ phần hộ): Trang web chính thức của 最高法 không tìm được trang văn bản gốc (đoán URL trên court.gov.cn báo 404, kho giải thích tư pháp của 最高检 (Viện kiểm sát nhân dân tối cao Trung Quốc) không có văn bản này); mục 4 đánh dấu TODO, xếp mức B.
- 医师法 (2021) Điều 23: Trang web của 国家卫健委 (Ủy ban Y tế Sức khỏe Quốc gia Trung Quốc) trả về lỗi 412 khi dùng script thu thập, kho chính sách gov.cn không lưu trữ luật của Nhân đại; chưa trích dẫn.
- 商标法 (2019 修正) Điều 31 nguyên tắc nộp đơn trước: Trang web của 国家知识产权局 (Cục Sở hữu trí tuệ Quốc gia Trung Quốc) không tìm được trang toàn văn; mục 12 chỉ dùng để nhắc nhở, không trích dẫn điều khoản.
- 深圳经济特区个人破产条例: Không tìm được văn bản gốc chính thức; ghi chú ở mục 14 chỉ nêu "thí điểm ở một số địa phương", không trích dẫn.
- 食品安全法 Điều 122 chế tài kinh doanh không phép: Không tìm được trang toàn văn chính thức; mục 6 đổi sang trích dẫn 无证无照经营查处办法 và 食品经营许可办法.
