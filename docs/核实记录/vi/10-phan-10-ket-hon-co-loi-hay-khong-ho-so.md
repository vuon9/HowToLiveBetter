> Bản dịch không chính thức của [docs/核实记录/10-结婚划不划算.md](../../../docs/核实记录/10-结婚划不划算.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Phần 10 "Kết hôn có lợi hay không" hồ sơ kiểm chứng nguồn (2026-09-07)

Công cụ: WebFetch; những trang WebFetch không mở được hoặc chỉ hiển thị đến phần điều hướng thì dùng curl (qua proxy của máy) lấy HTML/PDF/JSON gốc rồi phân tích cục bộ. WebSearch hết hạn ngạch giữa chừng ở phần này (200/200), từ đó về sau chỉ dùng WebFetch và curl.

## Thống kê chính thức
### Bộ Dân chính《Công báo thống kê phát triển sự nghiệp dân chính năm 2024》
- Trang: <https://www.mca.gov.cn/n1288/n1294/n1554/c1662004999980006190/content.html> : WebFetch mở, tiêu đề trang "2024年民政事业发展统计公报", đăng 2025-07-30 17:00; trang là bản vỏ thân thiện với người già, nội dung chính nằm trong tệp PDF đính kèm
- PDF: <https://www.mca.gov.cn/gdnps/n2445/n2451/n2458/n2681/c1662004999980006189/attr/400985.pdf> : curl tải 14 trang, pypdf trích văn bản
- Nguyên văn nguyên văn (trang 13): "1. Dịch vụ đăng ký kết hôn. Năm 2024, cả nước có tổng cộng 4190 cơ quan và địa điểm đăng ký kết hôn, trong đó 1134 cơ quan đăng ký kết hôn, cả năm xử lý đăng ký kết hôn hợp pháp 610,6 vạn cặp, giảm 20,5％ so với năm trước. Tỷ lệ kết hôn là 4,3‰, giảm 1,1 điểm phần nghìn so với năm trước. Xử lý thủ tục ly hôn hợp pháp 351,3 vạn cặp, trong đó: cơ quan dân chính đăng ký ly hôn 262,2 vạn cặp, tòa án phán quyết, hòa giải ly hôn 89,1 vạn cặp. Tỷ lệ ly hôn là 2,5‰."
- Nguyên văn nguyên văn (chú thích 5 trang 14): "Số liệu tòa án phán quyết, hòa giải ly hôn trong dịch vụ đăng ký ly hôn lấy từ Tòa án nhân dân tối cao Trung Quốc. Công thức tính tỷ lệ kết hôn (ly hôn) là: số cặp kết hôn (ly hôn) trong năm / tổng dân số bình quân trong năm x1000‰."
- "Tỷ lệ ly hôn trên kết hôn ≈ 57,5%" là kết quả số học của bài này khi chia hai số trên, công báo không có chỉ tiêu này, phần chính văn đã ghi chú

### Cục Thống kê Quốc gia Trung Quốc, Công báo điều tra sử dụng thời gian toàn quốc lần thứ ba
- Bản số một <https://www.stats.gov.cn/sj/zxfb/202410/t20241031_1957217.html> : WebFetch mở; chỉ gồm phương pháp (điều tra ngày 11–31 tháng 5 năm 2024, 3,85 vạn hộ, 10,7 vạn người), không có số liệu phân nhóm
- Bản số hai <https://www.stats.gov.cn/sj/zxfb/202410/t20241031_1957216.html> : WebFetch mở; câu trích: "居民每日平均时间为1小时17分钟，参与者每日平均时间为1小时59分钟，活动参与率为64.9%" (việc nhà); "居民每日平均时间为30分钟，参与者每日平均时间为1小时46分钟，活动参与率为28.4%" (chăm sóc, trông nom người thân); không phân nhóm theo giới tính, tình trạng hôn nhân
- Bản số ba <https://www.stats.gov.cn/sj/zxfb/202410/t20241031_1957215.html> : WebFetch mở và curl kiểm chứng lại; câu trích: "无酬劳动领域的参与者每日平均时间为2小时45分钟。其中，男性1小时52分钟，女性3小时29分钟" "无酬劳动领域的活动参与率为75.6%。其中，男性67.5%，女性83.9%"; không phân nhóm theo tình trạng hôn nhân
- Trả lời phỏng vấn báo chí <https://www.stats.gov.cn/sj/sjjd/202410/t20241031_1957218.html> : WebFetch mở; câu trích: "家务劳动活动的参与者每日平均时间为1小时59分钟，比2018年减少28分钟"

### Cục Thống kê Quốc gia Trung Quốc, Công báo điều tra sử dụng thời gian toàn quốc năm 2018
- <https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900224.html> : WebFetch mở
- Ý chính các câu trích: việc nhà bình quân người dân 1 giờ 26 phút, nam 45 phút, nữ 2 giờ 6 phút; tỷ lệ tham gia 58,5%, nam 40,4%, nữ 75,6%; chăm sóc, trông nom con cái sinh hoạt bình quân 36 phút, nam 17 phút, nữ 53 phút; tỷ lệ tham gia 18,9%, nam 12,3%, nữ 25,1%

### Điều tra dân số lần thứ bảy (tuổi kết hôn lần đầu / tỷ lệ chưa kết hôn)
- <https://www.stats.gov.cn/sj/pcsj/rkpc/7rp/indexch.htm> : mở, là trang khung; chỉ mục cột trái (left.htm) liệt kê bảng 2-5 "全国各民族分性别、初婚年龄的人口", 5-1 "各地区分性别、婚姻状况的15岁及以上人口" và các bảng khác, nhưng toàn bộ bảng là ảnh JPG, không thể trích số liệu, phần này không dẫn tuổi kết hôn lần đầu và tỷ lệ chưa kết hôn

## Điều khoản pháp luật
### 中华人民共和国民法典 (nghĩa: Bộ luật Dân sự nước Cộng hòa Nhân dân Trung Hoa)
- Trang Cơ sở dữ liệu văn bản quy phạm pháp luật quốc gia <https://flk.npc.gov.cn/detail?title=...&id=ff808081729d1efe01729d50b5c500bf> : WebFetch chỉ hiển thị đến phần điều hướng (ứng dụng một trang); curl gọi giao diện backend của trang `<https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=ff808081729d1efe01729d50b5c500bf`> trả về JSON: title "中华人民共和国民法典", flxz "法律", zdjgName "全国人民代表大会", gbrq "2020-05-28", sxrq "2021-01-01", cây điều khoản gồm các nút từ Điều 1062 đến Điều 1066, Điều 1076 đến Điều 1079, Điều 1088; giao diện chỉ cho số điều không cho chính văn, tệp PDF đính kèm là bản ảnh không thể trích văn bản
- Chính văn điều khoản kiểm chứng từ trang đăng lại Công báo Tòa án nhân dân tối cao Trung Quốc <http://gongbao.court.gov.cn/Details/7f184078694d811fb3314f6af9accf.html> ("中华人民共和国民法典（续）", chuyên mục văn bản quy phạm pháp luật): curl lấy về rồi phân tích cục bộ
- Nguyên văn:
  - Điều 1062 "夫妻在婚姻关系存续期间所得的下列财产，为夫妻的共同财产，归夫妻共同所有：（一）工资、奖金、劳务报酬；（二）生产、经营、投资的收益；（三）知识产权的收益；（四）继承或者受赠的财产，但是本法第一千零六十三条第三项规定的除外；（五）其他应当归共同所有的财产。夫妻对共同财产，有平等的处理权。"
  - Điều 1063 "下列财产为夫妻一方的个人财产：（一）一方的婚前财产；（二）一方因受到人身损害获得的赔偿或者补偿；（三）遗嘱或者赠与合同中确定只归一方的财产；（四）一方专用的生活用品；（五）其他应当归一方的财产。"
  - Điều 1065 "男女双方可以约定婚姻关系存续期间所得的财产以及婚前财产归各自所有、共同所有或者部分各自所有、部分共同所有。约定应当采用书面形式。没有约定或者约定不明确的，适用本法第一千零六十二条、第一千零六十三条的规定。夫妻对婚姻关系存续期间所得的财产以及婚前财产的约定，对双方具有法律约束力。"
  - Điều 1076 "夫妻双方自愿离婚的，应当签订书面离婚协议，并亲自到婚姻登记机关申请离婚登记。离婚协议应当载明双方自愿离婚的意思表示和对子女抚养、财产以及债务处理等事项协商一致的意见。"
  - Điều 1077 "自婚姻登记机关收到离婚登记申请之日起三十日内，任何一方不愿意离婚的，可以向婚姻登记机关撤回离婚登记申请。前款规定期限届满后三十日内，双方应当亲自到婚姻登记机关申请发给离婚证；未申请的，视为撤回离婚登记申请。"
  - Điều 1079 "夫妻一方要求离婚的，可以由有关组织进行调解或者直接向人民法院提起离婚诉讼。人民法院审理离婚案件，应当进行调解；如果感情确已破裂，调解无效的，应当准予离婚。有下列情形之一，调解无效的，应当准予离婚：（一）重婚或者与他人同居；（二）实施家庭暴力或者虐待、遗弃家庭成员；（三）有赌博、吸毒等恶习屡教不改；（四）因感情不和分居满二年；（五）其他导致夫妻感情破裂的情形。……经人民法院判决不准离婚后，双方又分居满一年，一方再次提起离婚诉讼的，应当准予离婚。"
  - Điều 1088 "夫妻一方因抚育子女、照料老年人、协助另一方工作等负担较多义务的，离婚时有权向另一方请求补偿，另一方应当给予补偿。具体办法由双方协议；协议不成的，由人民法院判决。"
- Bản sao chính thức chưa mở được (ghi lại để tra cứu): các trang điều khoản trên npc.gov.cn (http/https đều chuyển về trang chủ hoặc bắt tay TLS thất bại); gov.cn 2020-06-01 content_5516649 và các biến thể đều 404

### 民政部 民发〔2020〕116 号 (nghĩa: Bộ Dân chính, văn bản số 民发〔2020〕116)
- <https://www.gov.cn/zhengce/zhengceku/2020-12/04/content_5567010.htm> : WebFetch mở; số hiệu văn bản "民发〔2020〕116号", ngày 24 tháng 11 năm 2020; văn bản dẫn Điều 1076, Điều 1077, Điều 1078 làm căn cứ cho thủ tục đăng ký ly hôn, và trong thủ tục quy định thời gian cân nhắc ly hôn ba mươi ngày; không trích nguyên văn từng chữ điều khoản, phần này chỉ dùng làm bằng chứng phụ cho thủ tục cân nhắc

## 期刊论文（DOI） (nghĩa: Bài báo tạp chí (DOI))
### Manzoli 2007, Soc Sci Med 64:77–94, doi 10.1016/j.socscimed.2006.08.031
- <https://doi.org/10.1016/j.socscimed.2006.08.031> : phân giải DOI thành công, chuyển hướng 302 tới linkinghub.elsevier.com (trang này chỉ trả về "Redirecting", sciencedirect trả 403)
- Siêu dữ liệu và tóm tắt được kiểm chứng từ giao diện Europe PMC (PMID 17011690): tiêu đề, tác giả, tập và trang tạp chí khớp với DOI
- Nguyên văn: "Pooling 53 independent comparisons, consisting of more than 250,000 elderly subjects, the overall relative risk (RR) for married versus non-married individuals (including widowed, divorced/separated and never married) was 0.88 (95% Confidence Interval: 0.85-0.91). This estimate did not vary by gender, study quality, or between Europe and North America. Compared to married individuals, the widowed had a RR of death of 1.11 (1.08-1.14), divorced/separated 1.16 (1.09-1.23), never married 1.11 (1.07-1.15). Although some evidence of publication bias was found … (RR=0.94; 0.92-0.95)."

### Roelfs 2011, Am J Epidemiol 174(4):379–389, doi 10.1093/aje/kwr111
- <https://doi.org/10.1093/aje/kwr111> → <https://academic.oup.com/aje/article-lookup/doi/10.1093/aje/kwr111> : WebFetch mở trang nhà xuất bản
- Nguyên văn: "The authors used meta-analysis to examine 641 risk estimates from 95 publications that provided data on more than 500 million persons. The comparison group consisted of currently married individuals. The mean hazard ratio for mortality was 1.24 (95% confidence interval: 1.19, 1.30) among multivariate-adjusted hazard ratios with a high subjective quality rating. Meta-regressions showed that hazard ratios have been modestly increasing over time for both genders, but have done so somewhat more rapidly for women. The results also showed that the hazard ratio decreased with age and that study quality has an important relation to hazard ratio magnitude."

### Wang 2020, Glob Health Res Policy 5:4, doi 10.1186/s41256-020-00133-8
- <https://doi.org/10.1186/s41256-020-00133-8> : phân giải DOI thành công, chuyển tới ghrp.biomedcentral.com → link.springer.com (trang sau yêu cầu cấp phép cookie, không hiển thị nội dung)
- Siêu dữ liệu và tóm tắt được kiểm chứng từ giao diện Europe PMC (tra theo DOI): tiêu đề "Sex differences in the association between marital status and the risk of cardiovascular, cancer, and all-cause mortality: a systematic review and meta-analysis of 7,881,040 individuals", tác giả Wang Y, Jiao Y, Nie J, O'Neil A, Huang W, Zhang L, Han J, Liu H, Zhu Y, Yu C, Woodward M
- Nguyên văn: "Twenty-one studies with 7,891,623 individuals and 1,888,752 deaths were included in the meta-analysis. Compared with married individuals, being unmarried was significantly associated with all-cause, cancer, CVD and coronary heart disease mortalities for both sexes. However, the association with CVD and all-cause mortality was stronger in men. … The pooled ratio for women versus men showed 31 and 9% greater risk of stroke mortality and all-cause mortality associated with never married in men than in women."
- Lưu ý: tiêu đề ghi 7,881,040 người, tóm tắt ghi 7,891,623 người, bản gốc tự mâu thuẫn; phần chính viết theo tóm tắt là "hơn 7,89 triệu người"
- Cụm "Wang 2020 Heart" trong bản thảo nhiệm vụ không tìm thấy; PubMed 31204239 tương ứng với Dhindsa 2020 (xem bên dưới), không phải tạp chí Heart

### Robles 2014, Psychol Bull 140(1):140–187, doi 10.1037/a0031859
- <https://doi.org/10.1037/a0031859> : phân giải DOI thành công, chuyển tới doi.apa.org → psycnet.apa.org (trang render bằng JS, chỉ hiện Loading)
- Siêu dữ liệu và tóm tắt được kiểm chứng từ giao diện Europe PMC (PMID 23527470): tiêu đề, tác giả, tập và trang tạp chí khớp với DOI
- Nguyên văn: "This meta-analysis reviewed 126 published empirical articles over the past 50 years describing associations between marital relationship quality and physical health in more than 72,000 individuals. … Greater marital quality was related to better health, with mean effect sizes from r = .07 to .21, including lower risk of mortality (r = .11) and lower cardiovascular reactivity during marital conflict (r = -.13), but not daily cortisol slopes or cortisol reactivity during conflict. The small effect sizes were similar in magnitude to previously found associations between health behaviors (e.g., diet) and health outcomes. Effect sizes for a small subset of clinical outcomes were susceptible to publication bias. … we found little evidence for gender differences in studies that explicitly tested gender moderation … designs that limit causal inferences."

### Dhindsa 2020, Trends Cardiovasc Med 30:215–220, doi 10.1016/j.tcm.2019.05.012
- Trang PubMed <https://pubmed.ncbi.nlm.nih.gov/31204239/> WebFetch chỉ trả về thông báo cookie; siêu dữ liệu và tóm tắt được kiểm chứng từ giao diện Europe PMC (PMID 31204239), DOI do giao diện này cung cấp
- Nguyên văn: "Across multiple U.S. and international cohorts, patients who are unmarried, including those who are divorced, separated, widowed, or never married, have an increased rate of adverse cardiovascular events when compared to their married counterparts. Some studies suggest that marriage may have a more protective role for men compared to women. Furthermore, dissatisfaction in a marriage and marriage quality have significant impact on cardiovascular risk."
- Tính chất: tổng quan tường thuật, không có số liệu gộp, phần chính chỉ dùng làm chứng cứ bổ trợ mức B

## Chưa đưa vào
- Chi phí sinh con / nuôi dạy con: trước khi hết hạn mức WebSearch, chưa tra được nguyên văn về chi phí nuôi dạy con của Cục Thống kê Quốc gia Trung Quốc hay cơ quan nghiên cứu chính thức, theo yêu cầu nhiệm vụ nên không thu thập
- Sính lễ, chi phí cưới hỏi: không có thống kê chính thức, không ghi số liệu
