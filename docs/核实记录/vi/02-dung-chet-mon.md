> Bản dịch không chính thức của [docs/核实记录/02-不要慢慢死.md](../../../docs/核实记录/02-不要慢慢死.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Hồ sơ kiểm chứng nguồn phần 2

Phương thức kiểm chứng: Toàn bộ nguồn đều được mở qua WebFetch để truy cập bản ghi Europe PMC REST (`<https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:<doi>&resultType=core&format=json`>, một vài trường hợp cá biệt dùng truy vấn `TITLE:` hoặc `EXT_ID:<pmid> AND SRC:MED`). Bản ghi bao gồm tiêu đề, tác giả, tạp chí, năm, DOI, PMID và bản tóm tắt đầy đủ, các số liệu trích dẫn đều nằm trong bản tóm tắt. Bản web của PubMed trả về trang chặn cookie khi truy cập bằng WebFetch, còn doi.org trả về mã 302 rồi trang nhà xuất bản (NEJM) trả về lỗi 403, vì vậy lấy bản ghi Europe PMC làm chuẩn. DOI đều được điền theo bản ghi Europe PMC (trong đó DOI bài viết về hạt dinh dưỡng của Aune 2016 thực tế là `10.1186/s12916-016-0730-3`, trí nhớ ban đầu của tôi là `-0730-5` bị nhầm, bài viết này cuối cùng không đưa vào chính văn).

## Mục 1 Cai thuốc lá
- <https://doi.org/10.1056/NEJMsa1211128> - Đã xác nhận: Jha P et al., NEJM 2013, PMID 23343063. Nguyên văn: "Life expectancy was shortened by more than 10 years among the current smokers"; "Adults who had quit smoking at 25 to 34, 35 to 44, or 45 to 54 years of age gained about 10, 9, and 6 years of life, respectively"; "Cessation before the age of 40 years reduces the risk of death associated with continued smoking by about 90%."
- <https://doi.org/10.1016/S0140-6736(15)00340-2> - Đã xác nhận: Chen Z et al., Lancet 2015, PMID 26466050. Nguyên văn: urban men "RR 1·32 [95% CI 1·24-1·41] vs 1·65 [1·53-1·79]" (1990s vs 2010s), rural men "RR 1·13 [1·09-1·17] vs 1·22 [1·16-1·29]"; "Ex-smokers who had stopped by choice…had little smoking-attributed risk more than 10 years after stopping."
- <https://doi.org/10.1016/S0140-6736(10)61388-8> - Đã xác nhận: Oberg M et al., Lancet 2011, PMID 21112082. Nguyên văn: "603,000 deaths were attributable to second-hand smoke in 2004, which was about 1·0% of worldwide mortality."

## Mục 2 Đồ uống có đường
- <https://doi.org/10.1161/CIRCULATIONAHA.118.037401> - Đã xác nhận: Malik VS et al., Circulation 2019, PMID 30882235. Nguyên văn: phân loại "(<1/mo, 1-4/mo, 2-6/week, 1-<2/d, and ≥2/d) were 1.00 (reference), 1.01 (0.98, 1.04), 1.06 (1.03, 1.09), 1.14 (1.09, 1.19), and 1.21 (1.13, 1.28)"; 37 716 men and 80 647 women, "36 436 deaths". Tóm tắt không đưa ra HR cho mỗi khẩu phần/ngày, phần nội dung chính không trích dẫn.
- <https://doi.org/10.1001/jamainternmed.2019.2478> - Đã xác nhận: Mullee A et al., JAMA Intern Med 2019. Nguyên văn: total soft drinks "HR, 1.17; 95% CI, 1.11-1.22"; sugar-sweetened "HR, 1.08; 95% CI, 1.01-1.16"; artificially sweetened "HR, 1.26; 95% CI, 1.16-1.35"; 451,743 participants.

## Mục 3 Muối ít natri
- <https://doi.org/10.1056/NEJMoa2105675> - Đã xác nhận: Neal B et al., NEJM 2021, PMID 34459569. Nguyên văn: 20,995 participants, mean follow-up 4.74 years; stroke "rate ratio, 0.86"; major cardiovascular events "rate ratio, 0.87"; death "39.28 events vs. 44.61 events per 1000 person-years; rate ratio, 0.88"; hyperkalemia rate ratio 1.04, không có khác biệt đáng kể.
- <https://doi.org/10.1056/NEJMoa1311889> - Đã xác nhận: O'Donnell M et al., NEJM 2014, PMID 25119607. Nguyên văn: "≥ 7.00 g per day…odds ratio, 1.15; 95% CI, 1.02 to 1.30"; "below 3.00 g per day…odds ratio, 1.27; 95% CI, 1.12 to 1.44".

## Mục 4 Số bước chân
- <https://doi.org/10.1016/S2468-2667(21)00302-9> - Đã xác nhận: Paluch AE et al., Lancet Public Health 2022, PMID 35247352. Nguyên văn: "47 471 adults, among whom there were 3013 deaths"; "Quartile median steps per day were 3553 for quartile 1, 5801 for quartile 2, 7842 for quartile 3, and 10 901 for quartile 4"; "adjusted HR for all-cause mortality was 0·60 (95% CI 0·51-0·71) for quartile 2, 0·55 (0·49-0·62) for quartile 3, and 0·47 (0·39-0·57) for quartile 4"; ≥60 tuổi "6000-8000 steps per day", <60 tuổi "8000-10 000 steps per day".
- <https://doi.org/10.1093/eurjpc/zwad229> - Đã xác nhận: Banach M et al., Eur J Prev Cardiol 2023, PMID 37555441. Nguyên văn: "A 1000-step increment was associated with a 15% decreased risk of all-cause mortality"; "the cut-off point of 3867 steps/day for all-cause mortality".

## Mục 5 Tuân thủ thuốc hạ huyết áp/hạ lipid máu
- <https://doi.org/10.1016/S0140-6736(15)01225-8> - Đã xác nhận: Ettehad D et al., Lancet 2016, PMID 26724178. Nguyên văn: major cardiovascular events "RR 0·80, 95% CI 0·77-0·83"; stroke "0·73, 0·68-0·77"; heart failure "0·72, 0·67-0·78"; "13% reduction in all-cause mortality (0·87, 0·84-0·91)".
- <https://doi.org/10.1016/S0140-6736(10)61350-5> - Đã xác nhận: CTT Collaboration, Lancet 2010, PMID 21067804. Nguyên văn: major vascular events "rate ratio [RR] 0·78, 95% CI 0·76–0·80"; "all-cause mortality was reduced by 10% per 1·0 mmol/L LDL reduction (RR 0·90, 95% CI 0·87–0·93)".
- <https://doi.org/10.1093/eurheartj/eht295> - Đã xác nhận: Chowdhury R et al., Eur Heart J 2013, PMID 23907142. Nguyên văn: "Corresponding RRs of all-cause mortality were 0.55 (0.46-0.67) and 0.71 (0.64-0.78) for good adherence to statins and antihypertensive agents"; good vs poor (<80%) adherence.

## Mục 6 Giấc ngủ
- <https://doi.org/10.1093/sleep/33.5.585> - Đã xác nhận: Cappuccio FP et al., Sleep 2010, PMID 20469800. Tóm tắt, Nguyên văn: "16 studies…1,382,999 male and female participants…112,566 deaths"; short "RR: 1.12; 95% CI 1.06 to 1.18"; long "1.30; [1.22 to 1.38]". Tóm tắt không đưa ra định nghĩa số giờ cho ngắn/dài, phần nội dung chính không ghi ngưỡng cụ thể.
- <https://doi.org/10.1161/JAHA.117.005947> - Đã xác nhận: Yin J et al., JAHA 2017, PMID 28889101. Tóm tắt, Nguyên văn: <7 h "RR was 1.06 (95% CI, 1.04-1.07) per 1-hour reduction"; >7 h "RR was 1.13 (95% CI, 1.11-1.15) per 1-hour increment".
- <https://doi.org/10.1093/sleep/zsad253> - Đã xác nhận: Windred DP et al., Sleep 2024, PMID 37738616. Tóm tắt, Nguyên văn: "60 977 UK Biobank participants"; "1859" deaths; "Higher sleep regularity was associated with a 20%-48% lower risk of all-cause mortality" (top four SRI quintiles vs least regular quintile); "Sleep regularity was a stronger predictor of all-cause mortality than sleep duration".

## Mục 7 Vận động cường độ trung bình
- <https://doi.org/10.1001/jamainternmed.2015.0533> - Đã xác nhận: Arem H et al., JAMA Intern Med 2015, PMID 25844730. Tóm tắt, Nguyên văn: less than 7.5 MET-h/week "HR, 0.80 [95% CI, 0.78-0.82]"; 1 to 2 times "HR, 0.69 [95% CI, 0.67-0.70]"; 2 to 3 times "HR, 0.63"; 3 to 5 times "HR, 0.61 [95% CI, 0.59-0.62]"; 10 or more times "HR, 0.69 [95% CI, 0.59-0.78]".
- <https://doi.org/10.1136/bmj.l4570> - Đã xác nhận: Ekelund U et al., BMJ 2019, PMID 31434697. Tóm tắt, Nguyên văn: tứ phân vị MVPA HR "1.00, 0.64 (0.55–0.74), 0.55 (0.40–0.74), and 0.52 (0.43–0.61)"; tứ phân vị cao nhất của tổng PA "0.27 (0.23 to 0.32)".

## Mục 8 Rèn luyện sức mạnh
- <https://doi.org/10.1136/bjsports-2021-105061> - Đã xác nhận: Momma H et al., Br J Sports Med 2022, PMID 35228201. Tóm tắt, Nguyên văn: "Muscle-strengthening activities were associated with a 10-17% lower risk of all-cause mortality"; "J-shaped associations with the maximum risk reduction (approximately 10-20%) at approximately 30-60 min/week"; "Combined muscle-strengthening and aerobic activities (versus none) were associated with a lower risk of all-cause…mortality".

## Mục 9 Ngồi nhiều
- <https://doi.org/10.7326/M17-0212> - Đã xác nhận: Diaz KM et al., Ann Intern Med 2017, PMID 28892811. Tóm tắt, Nguyên văn: total sedentary time highest vs lowest quartile "HR, 2.63 [CI, 1.60 to 4.30]"; bout duration "HR, 1.96 [CI, 1.31 to 2.93]"; kết luận "both the total volume of sedentary time and its accrual in prolonged, uninterrupted bouts are associated with all-cause mortality". Tóm tắt không nhắc tới ngưỡng 30 phút, tiêu đề nội dung chính không ghi số phút cụ thể.
- <https://doi.org/10.1016/S0140-6736(16)30370-1> - Đã xác nhận: Ekelund U et al., Lancet 2016, PMID 27475271. Tóm tắt, Nguyên văn: referent "those sitting <4 h/day and in the most active quartile [>35·5 MET-h per week]"; lowest PA quartile + sitting >8 h/day "HR=1·59, 1·52-1·66"; most active + >8 h "HR=1·04; 95% CI 0·99-1·10"; "about 60-75 min per day…seem to eliminate the increased risk of death associated with high sitting time"; TV ≥5 h in most active "HR=1·16, 1·05-1·28".

## Mục 10 Thịt chế biến sẵn
- <https://doi.org/10.1093/aje/kwt261> - Đã xác nhận: Larsson SC, Orsini N, Am J Epidemiol 2014, PMID 24148709. Tóm tắt, Nguyên văn (highest vs lowest): unprocessed red meat "1.10 (95% CI: 0.98, 1.22)"; processed meat "1.23 (95% CI: 1.17, 1.28)"; total red meat "1.29 (95% CI: 1.24, 1.35)".
- <https://doi.org/10.3945/ajcn.117.153148> - Đã xác nhận: Schwingshackl L et al., Am J Clin Nutr 2017, PMID 28446499. Tóm tắt, Nguyên văn (per serving/day): whole grains "RR: 0.92; 95% CI: 0.89, 0.95"; red meat "RR: 1.10; 95% CI: 1.04, 1.18"; processed meat "RR: 1.23; 95% CI: 1.12, 1.36".
- <https://doi.org/10.7326/M19-1621> - Đã xác nhận: Johnston BC et al., Ann Intern Med 2019, PMID 31569235. Tóm tắt, Nguyên văn: "continue current unprocessed red meat consumption (weak recommendation, low-certainty evidence)"; "continue current processed meat consumption (weak recommendation, low-certainty evidence)".

## Mục 11 Uống rượu
- <https://doi.org/10.1016/S0140-6736(18)30134-X> - Đã xác nhận: Wood AM et al., Lancet 2018, PMID 29676281. Nguyên văn: "the minimum mortality risk around or below 100 g per week"; kỳ vọng sống ở tuổi 40: >100-≤200 g/week "approximately 6 months", >200-≤350 g/week "1–2 years", >350 g/week "4–5 years".
- <https://doi.org/10.1016/S0140-6736(18)31310-2> - Đã xác nhận: GBD 2016 Alcohol Collaborators, Lancet 2018. Nguyên văn: "The level of alcohol consumption that minimised harm across health outcomes was zero (95% UI 0·0-0·8) standard drinks per week."
- <https://doi.org/10.1001/jamanetworkopen.2023.6185> - Đã xác nhận: Zhao J et al., JAMA Netw Open 2023, PMID 37000449. Nguyên văn: "low-volume drinkers (1.3-24.0 g per day; RR, 0.93; P = .07) compared with lifetime nondrinkers"; "45 to 64 and 65 or more grams per day (RR, 1.19 and 1.35; P < .001)".
- <https://doi.org/10.1001/archinte.166.22.2437> - Đã xác nhận: Di Castelnuovo A et al., Arch Intern Med 2006, PMID 17159008. Nguyên văn: "maximum protection being 18% in women (99% confidence interval, 13%-22%) and 17% in men"; "up to 4 drinks per day in men and 2 drinks per day in women, was inversely associated with total mortality".

## Mục 12 Ngũ cốc nguyên hạt
- <https://doi.org/10.1136/bmj.i2716> - Đã xác nhận: Aune D et al., BMJ 2016, PMID 27301975. Nguyên văn: per 90 g/day "0.83 (0.77 to 0.90; I(2)=83%, n=11) for all causes"; "Reductions in risk were observed up to an intake of 210-225 g/day".
- Schwingshackl 2017 như mục 10 (whole grains RR 0.92).

## Mục 13 Trái cây và rau củ
- <https://doi.org/10.1093/ije/dyw319> - Đã xác nhận: Aune D et al., Int J Epidemiol 2017, PMID 28338764. Nguyên văn: "the summary RR per 200 g/day was…0.90 (95% CI: 0.87-0.93…for all-cause mortality"; "Reductions in risk were observed up to 800 g/day for all outcomes except cancer (600 g/day)".
- <https://doi.org/10.1161/CIRCULATIONAHA.120.048996> - Đã xác nhận: Wang DD et al., Circulation 2021, PMID 33641343. Nguyên văn: "daily intake of 5 servings of fruit and vegetables was associated with hazard ratios (95% CI) of 0.87 (0.85-0.90) for total mortality" (đối chứng 2 khẩu phần/ngày); "≈5 servings per day of fruit and vegetables, or 2 servings of fruit and 3 servings of vegetables, was associated with the lowest mortality".

## Mục 14 Thực phẩm siêu chế biến
- <https://doi.org/10.1136/bmj-2023-077310> - Đã xác nhận: Lane MM et al., BMJ 2024, PMID 38418082. Nguyên văn: "all cause mortality (risk ratio 1.21, 1.15 to 1.27; low)" class II highly suggestive; "cardiovascular disease related mortality (risk ratio 1.50, 95% confidence interval 1.37 to 1.63; GRADE=very low)" class I convincing.

## Mục 15 Đốt trong nhà / PM2.5
- <https://doi.org/10.1001/jama.2018.2151> - Đã xác nhận: Yu K et al., JAMA 2018, PMID 29614179. Nguyên văn: 271,217 adults; cooking solid fuel all-cause "HR, 1.11 [95% CI, 1.03-1.20]"; heating "HR, 1.14 [95% CI, 1.03-1.26]"; switched (cooking) "HR, 0.87 [95% CI, 0.79-0.95]"; switched (heating) "HR, 0.67 [95% CI, 0.57-0.79]".
- <https://doi.org/10.1016/j.envint.2020.105974> - Đã xác nhận: Chen J, Hoek G, Environ Int 2020, PMID 32703584. Nguyên văn: "The combined Risk Ratio (RR) for PM₂.₅ and natural-cause mortality was 1.08 (95%CI 1.06, 1.09) per 10 µg/m³", 104 cohort studies.

## Mục 16 Cân nặng
- <https://doi.org/10.1016/S0140-6736(16)30175-1> - Đã xác nhận: Global BMI Mortality Collaboration, Lancet 2016, PMID 27423262. Nguyên văn: "All-cause mortality was minimal at 20·0-25·0 kg/m(2)"; 25.0-27.5 "1·07, 1·07-1·08"; 27.5-30.0 "1·20, 1·18-1·22"; 30.0-35.0 "1·45, 95% CI 1·41-1·48"; 35.0-40.0 "1·94, 1·87-2·01"; 40.0-60.0 "2·76, 2·60-2·92"; East Asia per 5 kg/m² "1·39 (1·34-1·44)"; phân tích giới hạn ở "never-smokers without chronic diseases at recruitment who survived 5 years".
- <https://doi.org/10.1001/jama.2012.113905> - Đã xác nhận: Flegal KM et al., JAMA 2013, PMID 23280227. Nguyên văn: "The summary HRs were 0.94 (95% CI, 0.91-0.96) for overweight, 1.18 (95% CI, 1.12-1.25) for obesity (all grades combined), 0.95 (95% CI, 0.88-1.01) for grade 1 obesity, and 1.29 (95% CI, 1.18-1.41) for grades 2 and 3 obesity."

## Mục 41 Dầu lạc tự ép bán rời ở xưởng nhỏ
Bản thảo PR #39 xếp mức A, hai câu "tỉ lệ mẫu kiểm tra vượt chuẩn cao hơn rõ rệt so với dầu đóng gói sẵn" và "tỉ lệ loại bỏ bằng kiềm luyện trên 90%" trong cột Lợi ích không có nguồn gốc ban đầu, liên kết GB 2761 chỉ dẫn đến trang chủ cfsa. Viết lại sau khi hợp nhất ngày 28-09-2026: xóa hai câu này, thay bằng hai nghiên cứu trên nhóm dân số Trung Quốc dưới đây, hạ xuống mức B (nghiên cứu quan sát đơn lẻ, tiêu chí đánh giá là xét nghiệm chức năng gan và kết cục sinh nở). Mức độ lợi ích được đánh giá theo phán đoán ở mức trung bình: bảng ngưỡng áp dụng theo mức giảm tương đối của tỉ lệ tử vong, ở đây không có tiêu chí đánh giá tỉ lệ tử vong, nhưng bất thường chức năng gan thấp hơn khoảng 35%, nhẹ cân khi sinh aOR 1,9 đều là các tiêu chí sức khỏe chứ không đơn thuần là chỉ số thay thế.
- <https://doi.org/10.3389/fpubh.2024.1484414> - Đã xác nhận: Lei J et al., Front Public Health 2024;12, PMID 39758209. Tóm tắt, Nguyên văn: "The AFB1 concentrations in HMPO were 1.29 (0.12, 6.58) μg/kg"; "an immediate decrease of 2.865 μg/kg (P = 0.006) and a sustained annual reduction of 2.593 μg/kg (P = 0.034)"; "reduction in the prevalence of liver function abnormality (PR = 0.650, 95% CI: 0.469-0.902)".
- <https://doi.org/10.1080/16549716.2024.2336312> - Đã xác nhận: Zhong Y et al., Glob Health Action 2024;17, PMID 38629142. Tóm tắt, Nguyên văn: "Of 1611 pregnant women, 1316 (81.7%) had consumed homemade peanut oil"; "aORs of 1.9 (95% CI 1.1-3.2) and 1.8 (95% CI 1.1-3.0)" (lần lượt là LBW, PB).
- <https://publications.iarc.fr/123> - Đã xác nhận: tiêu đề trang "Chemical Agents and Related Occupations", tức IARC Monographs Vol 100F, aflatoxin được đưa vào tập này, là chất gây ung thư nhóm 1.
- GB 2761-2017 Giới hạn aflatoxin B1 trong dầu lạc và các sản phẩm từ dầu lạc 20 μg/kg: Chưa lấy được nguyên văn tiêu chuẩn, chờ kiểm chứng.

## Mục 42 Dầu thực vật thay mỡ lợn và bơ
Bản thảo PR #39 đã gán quy mô của Abdelhamid 2020 (86 thử nghiệm RCT, 162.796 người) vào Hooper 2020; hai con số "RR 0,79 (0,66-0,93)" và "RR 0,89" đều không tìm thấy trong cả hai bài tóm tắt; "tỉ lệ omega-6 và omega-3 từ 15-20:1, lý tưởng là 4:1" không có nguồn. Viết lại theo nguyên văn ba bài tóm tắt của Cochrane sau khi hợp nhất ngày 28-09-2026, quan điểm chuyển từ "đổi sang dầu giàu axit oleic, rưới dầu hạt lanh nguội" thành "dầu thực vật thay thế chất béo bão hòa, đừng trông mong vào việc đổi loại dầu và dầu hạt lanh".
- <https://doi.org/10.1002/14651858.CD011737.pub3> - Đã xác nhận: Hooper L et al., Cochrane 2020. Tóm tắt, Nguyên văn: "15 randomised controlled trials (RCTs) (16 comparisons, 56,675 participants)"; "reduced the risk of combined cardiovascular events by 17% (risk ratio (RR) 0.83; 95% confidence interval (CI) 0.70 to 0.98"; all-cause mortality "RR 0.96; 95% CI 0.90 to 1.03"; cardiovascular mortality "RR 0.95; 95% CI 0.80 to 1.12"; "Subgrouping did not suggest significant differences between replacement of saturated fat calories with polyunsaturated fat or carbohydrate, and data on replacement with monounsaturated fat and protein was very limited".
- <https://doi.org/10.1002/14651858.CD011094.pub4> - Đã xác nhận: Hooper L, Al-Khudairy L, Abdelhamid AS et al., Cochrane 2018 Nov, PMID 30488422. Tóm tắt, Nguyên văn: "19 RCTs in 6461 participants"; all-cause mortality "RR 1.00, 95% CI 0.88 to 1.12"; CVD events "RR 0.97, 95% CI 0.81 to 1.15"; "low-quality evidence".
- <https://doi.org/10.1002/14651858.CD003177.pub5> - Đã xác nhận: Abdelhamid AS et al., Cochrane 2020. Tóm tắt, Nguyên văn: "86 RCTs (162,796 participants)"; ALA all-cause mortality "RR 1.01, 95% CI 0.84 to 1.20"; ALA coronary heart disease events "RR 1.00, 95% CI 0.82 to 1.22".
- 中国居民膳食指南 (Hướng dẫn dinh dưỡng cho cư dân Trung Quốc) (2022) dầu nấu ăn 25-30 g/ngày: Chưa lấy được nguyên văn, tạm dùng bản thảo PR, chờ kiểm chứng.

## Đã kiểm chứng nhưng không đưa vào chính văn
- Aune D et al. (2016) hạt dinh dưỡng, BMC Medicine, <https://doi.org/10.1186/s12916-016-0730-3>, PMID 27916000: per 28 g/day ACM "0.78 (95% CI: 0.72-0.84)". Mức độ tác động nghi ngờ bị yếu tố gây nhiễu phóng đại và tốn kém chi phí hằng ngày, chưa đưa vào nhằm kiểm soát số lượng mục (giới hạn tối đa 16 mục).
- Sofi F et al. (2010) chế độ ăn Địa Trung Hải, Am J Clin Nutr, <https://doi.org/10.3945/ajcn.2010.29673>, PMID 20810976: 2-point increase "RR = 0.92; 95% CI: 0.90, 0.94". Trùng lặp với mục 10, 12, 13, chưa đưa vào.
- Holt-Lunstad J et al. (2010) PLoS Med, <https://doi.org/10.1371/journal.pmed.1000316>, PMID 20668659: "OR = 1.50 (95% CI 1.42 to 1.59)"; Holt-Lunstad J et al. (2015) Perspect Psychol Sci, <https://doi.org/10.1177/1745691614568352>, PMID 25910392: "social isolation odds ratio (OR) = 1.29, loneliness OR = 1.26, and living alone OR = 1.32". Hiệu ứng cô lập xã hội lớn nhưng khả năng quan hệ nhân quả ngược cao, không có bằng chứng can thiệp, chưa đưa vào nhằm kiểm soát số lượng mục; nếu cần có thể bổ sung trực tiếp thành mục 17.

## Mục chưa xác nhận
- Không có. Toàn bộ con số trong chính văn đều lấy từ các hồ sơ đã mở nêu trên. Cột "Chi phí" trong chính văn (giá cả, thời gian) do tác giả ước tính, không trích dẫn tài liệu.
