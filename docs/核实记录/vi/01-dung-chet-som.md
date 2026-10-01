> Bản dịch không chính thức của [docs/核实记录/01-不要早死.md](../../../docs/核实记录/01-不要早死.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Hồ sơ kiểm chứng nguồn phần 1

Ngày kiểm chứng 2026-09-07. Phần lớn trang web của nhà xuất bản (NEJM, Elsevier, Wiley, BMJ, AHA) trả về lỗi 403 đối với WebFetch. Các tài liệu này được đọc tiêu đề, tác giả, tạp chí, năm và toàn văn phần tóm tắt của bản ghi tương ứng cùng mã DOI qua giao diện REST của Europe PMC (`<https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:">…"&resultType=core&format=json`); bản thân doi.org vẫn phân giải được (chuyển hướng 302 đến nhà xuất bản). Các đoạn "Nguyên văn" dưới đây đều là câu gốc được trích từ phần tóm tắt hoặc nội dung chính.

## 1. Dây an toàn
- <https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813573> (đã mở, dùng pdftotext chuyển PDF thành văn bản). Tiêu đề khớp: "Occupant Protection in Passenger Vehicles: 2022 Data, DOT HS 813 573, May 2024".
  - Nguyên văn: "Fifty percent of passenger vehicle occupants killed in traffic crashes in 2022 were unrestrained (based on known restraint use)."
  - Nguyên văn: "lap/shoulder seat belts, when used, reduce the risk of: fatal injury to front-seat passenger car occupants by 45 percent; … fatal injury to front-seat light-truck occupants by 60 percent"
  - Nguyên văn: "60 percent of those in the second row were unrestrained."
- <https://www.who.int/news-room/fact-sheets/detail/road-traffic-injuries> (đã mở). Nguyên văn: "Wearing a seat-belt can reduce the risk of death among vehicle occupants by up to 50%."
- <https://ghoapi.azureedge.net/api/RS_196?$filter=SpatialDim%20eq%20%27CHN%27> (đã mở, WHO GHO API). China 2021: 248.099 (95% CI 233.685–262.513). Mở RS_198 theo cách tương tự: năm 2021 là 17,4/100.000.
  - Chú ý: Giao diện GHO trả về RS_196 là số tuyệt đối, RS_198 là tỷ lệ, ngược với mã chỉ số dự kiến. Con số thực tế lấy từ JSON trả về.

## 2. Mũ bảo hiểm
- <https://doi.org/10.1002/14651858.CD004333.pub3> (doi.org chuyển tiếp tới Wiley bị lỗi 403, bản ghi trên Europe PMC đã xác nhận): Liu BC, 2008, "Helmets for preventing injury in motorcycle riders".
  - Nguyên văn: "helmets were estimated to reduce the risk of death by 42% (OR 0.58, 95% CI 0.50 to 0.68)"; "reduce the risk of head injury by 69% (OR 0.31, 95% CI 0.25 to 0.38)"

## 3. Thiết bị báo khói / Khí CO
- <https://doi.org/10.1001/jama.279.20.1633> (bản ghi trên Europe PMC đã xác nhận): Marshall SW, Runyan CW et al., JAMA 1998, "Fatal residential fires: who dies and who survives?".
  - Nguyên văn: "Overall, a functioning smoke detector lowered the risk of death (OR, 0.39; 95% CI, 0.18-0.83)."
- <https://www.usfa.fema.gov/downloads/pdf/statistics/v22i2.pdf> (đã mở, chuyển PDF thành văn bản). Tiêu đề khớp: "Fatal Fires in Residential Buildings (2018-2020), Topical Fire Report Series June 2022 Vol 22 Issue 2".
  - Nguyên văn: "Smoke alarms were not present in 24% of fatal fires in occupied residential buildings."; "The leading human factor contributing to the ignition of fatal fires in residential buildings was being 'asleep' (41%)."
- <https://doi.org/10.46234/ccdcw2020.008> (doi.org chuyển tiếp tới weekly.chinacdc.cn chỉ hiện siêu dữ liệu, đã đọc toàn văn qua Europe PMC PMC8392909 fullTextXML). Tác giả You J, Liu J, Zhou M, China CDC Weekly 2020.
  - Nguyên văn: "In 2018, there were 11,523 deaths caused by carbon monoxide poisoning reported in China"; "highest proportions occurring in December (72.59%), January (67.42%), and February (66.48%)"
- Không sử dụng: Trang "Smoke Alarms in US Home Fires" của NFPA chỉ trả về tiêu đề, tệp PDF của báo cáo báo lỗi 500 nên không thể xác minh, do đó không trích dẫn con số "tỷ lệ tử vong thấp hơn 55%" của NFPA.

## 4. Huyết áp
- <https://doi.org/10.1016/S0140-6736(15)01225-8> (trang Elsevier chỉ hiện Redirecting, bản ghi trên Europe PMC đã xác nhận): Ettehad D, Lancet 2016.
  - Nguyên văn: "relative risk [RR] 0·80, 95% CI 0·77-0·83" (biến cố tim mạch chính); "stroke (0·73, 0·68-0·77)"; "heart failure (0·72, 0·67-0·78)"; "a significant 13% reduction in all-cause mortality (0·87, 0·84-0·91)"
  - Nguyên văn: "We identified 123 studies with 613,815 participants for the tabular meta-analysis."
- <https://doi.org/10.1016/S0140-6736(17)32478-9> (bản ghi trên Europe PMC đã xác nhận): Lu J, Lancet 2017, China PEACE Million Persons Project.
  - Nguyên văn: "44·7% (95% CI 44·6-44·8) of the sample had hypertension, of whom 44·7% (44·6-44·8) were aware of their diagnosis, 30·1% (30·0-30·2) were taking prescribed antihypertensive medications, and 7·2% (7·1-7·2) had achieved control"

## 5. Không chạy quá tốc độ, không lái xe khi say rượu
- <https://www.who.int/news-room/fact-sheets/detail/road-traffic-injuries> (đã mở).
  - Nguyên văn: "Every 1% increase in mean speed produces a 4% increase in the fatal crash risk."; "The risk of a road traffic crash starts at low levels of blood alcohol concentration (BAC)."

## 6. Ghế an toàn cho trẻ em
- NHTSA 813573 (như mục 1). Nguyên văn: "NHTSA has estimated that car seats reduce the risk of fatal injury by 71 percent for infants (younger than 1 year old) and by 54 percent for toddlers (1 to 4 years old) in passenger cars."
- Bảng thông tin về an toàn giao thông đường bộ của WHO (như trên). Nguyên văn: "The use of child restraints can lead to a 71% reduction in deaths among infants."

## 7. Đuối nước
- <https://doi.org/10.1136/ip.2010.028688> - doi.org phân giải đến injuryprevention.bmj.com (403); hồ sơ Europe PMC xác nhận: Cummings P, Mueller BA, Quan L. Injury Prevention 2011;17(3):156-159, PMID 20889519.
  - Nguyên văn: "The adjusted RR was 0.51 (95% CI 0.35 to 0.74)."
  - Lưu ý: DOI tôi ghi ban đầu (…028381) bị sai, doi.org trả về 404, đã sửa thành …028688 do Europe PMC cung cấp.
- <https://doi.org/10.46234/ccdcw2023.198> - phân giải đến weekly.chinacdc.cn; toàn văn đọc qua Europe PMC PMC10689961. Li Z, China CDC Weekly 2023.
  - Nguyên văn: "the national drowning mortality rate from 6.60 per 100,000 in 2013 down to 3.28 per 100,000 in 2021"; "rural areas exhibited roughly double the mortality rate found in urban areas"; "in China, it is deemed the primary cause of death for children between the ages of 1 and 14"; "peaking at 3.95 per 100,000 in the 15–19 year age group"
- <https://doi.org/10.46234/ccdcw2024.057> - phân giải đến weekly.chinacdc.cn; tóm tắt đọc qua Europe PMC. Zhou J, China CDC Weekly 2024.
  - Nguyên văn: "In 2021, drowning and road traffic crashes were the top two causes of child injury deaths, explaining 31.1% and 27.9% of total injury deaths, respectively."
- Không sử dụng: trang web của 中国疾控中心 (Trung tâm kiểm soát bệnh tật Trung Quốc) chinacdc.cn/…/t20210809_233793.html trả về 404.

## 8. Phòng ngừa té ngã ở người cao tuổi
- <https://doi.org/10.1002/14651858.CD012424.pub2> - Wiley 403; hồ sơ Europe PMC xác nhận: Sherrington C, 2019.
  - Nguyên văn: "Exercise reduces the rate of falls by 23% (rate ratio (RaR) 0.77, 95% confidence interval (CI) 0.71 to 0.83"; "reduces the number of people experiencing one or more falls by 15% (risk ratio (RR) 0.85, 95% CI 0.81 to 0.89"
  - Nguyên văn: "We included 108 RCTs with 23,407 participants living in the community in 25 countries."
- <https://doi.org/10.1002/14651858.CD007146.pub3> - hồ sơ Europe PMC xác nhận: Gillespie LD, 2012.
  - Nguyên văn: "Home safety assessment and modification interventions were effective in reducing rate of falls (RR 0.81, 95% CI 0.68 to 0.97; six trials; 4208 participants)"; "Tai Chi did significantly reduce risk of falling (RR 0.71, 95% CI 0.57 to 0.87…)"
- <https://doi.org/10.46234/ccdcw2021.013> - phân giải đến weekly.chinacdc.cn; toàn văn đọc qua Europe PMC PMC8393086. Lu Z, China CDC Weekly 2021.
  - Nguyên văn: "Falls are the top cause for death from injuries in people aged 65 years and above"; "Home (55.97%), road/street (18.69%), and public residential institution (12.80%) were the sites where falls most often occurred"

## 9. Viêm gan B
- <https://doi.org/10.1371/journal.pmed.1001774> - PLOS sau khi chuyển hướng không lấy được toàn văn; hồ sơ Europe PMC xác nhận: Qu C, PLoS Medicine 2014.
  - Nguyên văn: "efficacies of 84% (95% CI 23%-97%)" (tỉ lệ mắc PLC); "catch-up vaccination on HBsAg seroprevalence in early adulthood was 21% (95% CI 10%-30%), substantially weaker than that of the neonatal vaccination (72%, 95% CI 68%-75%)"
- <https://doi.org/10.3201/eid2305.161477> - hồ sơ Europe PMC xác nhận: Cui F, Emerging Infectious Diseases 2017.
  - Nguyên văn: "HBV surface antigen prevalence declined 46% by 2006 and by 52% by 2014"; dưới 5 tuổi "the decline was 97%"

## 10. Vắc-xin HPV
- <https://doi.org/10.1056/NEJMoa1917338> - NEJM 403; hồ sơ Europe PMC xác nhận: Lei J, NEJM 2020.
  - Nguyên văn: "the incidence rate ratio was 0.12 (95% CI, 0.00 to 0.34) among women who had been vaccinated before the age of 17 years and 0.47 (95% CI, 0.27 to 0.75) among women who had been vaccinated at the age of 17 to 30 years"
  - Nguyên văn: "follow an open population of 1,672,983 girls and women who were 10 to 30 years of age from 2006 through 2017"

## 11. Sàng lọc ung thư cổ tử cung
- <https://doi.org/10.1056/NEJMoa0808516> - NEJM 403; hồ sơ Europe PMC xác nhận: Sankaranarayanan R, NEJM 2009.
  - Nguyên văn: "hazard ratio for the detection of advanced cancer in the HPV-testing group, 0.47; 95% confidence interval [CI], 0.32 to 0.69"; "34 deaths from cancer in the HPV-testing group, as compared with 64 in the control group (hazard ratio, 0.52; 95% CI, 0.33 to 0.83)"

## 12. Sàng lọc ung thư đại trực tràng
- <https://doi.org/10.1002/14651858.CD001216.pub2> - Bản ghi Europe PMC xác nhận: Hewitson P, 2007.
  - Nguyên văn: "a 16% reduction in the relative risk of colorectal cancer mortality (RR 0.84, CI: 0.78-0.90)"; "25% relative risk reduction (RR 0.75, CI: 0.66 - 0.84) for those attending at least one round of screening"
- <https://doi.org/10.1056/NEJMoa2208375> - Bản ghi Europe PMC xác nhận: Bretthauer M, NEJM 2022.
  - Nguyên văn: "the risk of colorectal cancer at 10 years was 0.98% in the invited group and 1.20% in the usual-care group, a risk reduction of 18% (risk ratio, 0.82; 95% confidence interval [CI], 0.70 to 0.93)"; "The risk of death from colorectal cancer was 0.28% in the invited group and 0.31% in the usual-care group (risk ratio, 0.90; 95% CI, 0.64 to 1.16)"

## 13. Vắc-xin cúm
- <https://doi.org/10.1161/CIRCULATIONAHA.121.057042> - AHA 403; bản ghi Europe PMC xác nhận: Fröbert O, Circulation 2021 (IAMI).
  - Nguyên văn: "Rates of all-cause death were 2.9% and 4.9% (hazard ratio, 0.59 [95% CI, 0.39-0.89]; P=0.010)"; "rates of cardiovascular death were 2.7% and 4.5%, (hazard ratio, 0.59 [95% CI, 0.39-0.90]"
  - Nguyên văn: "2571 participants were randomized at 30 centers across 8 countries"; "Over the 12-month follow-up, the primary outcome occurred in…"
- <https://doi.org/10.1001/jamanetworkopen.2022.8873> - Mở trực tiếp trang JAMA thành công. Behrouzi B, JAMA Network Open 2022.
  - Nguyên văn: "influenza vaccine was associated with a lower risk of composite cardiovascular events (3.6% vs 5.4%; RR, 0.66; 95% CI, 0.53-0.83"; "1.7% of vaccine recipients died of cardiovascular causes compared with 2.5% of placebo or control recipients (RR, 0.74; 95% CI, 0.42-1.30"
- <https://doi.org/10.1002/14651858.CD004876.pub4> - Bản ghi Europe PMC xác nhận: Demicheli V, 2018.
  - Nguyên văn: "may experience less influenza over a single season compared with placebo, from 6% to 2.4%" (low-certainty); "very low-certainty evidence for the effect on mortality"

## 14. Vi khuẩn Helicobacter pylori
- <https://doi.org/10.1136/bmj.l5016> - BMJ 403; bản ghi Europe PMC xác nhận: Li WQ, BMJ 2019.
  - Nguyên văn: "A protective effect of H pylori treatment on gastric cancer incidence persisted 22 years post-intervention (odds ratio 0.48, 95% confidence interval 0.32 to 0.71)"; "fully adjusted hazard ratio for H pylori treatment was 0.62 (95% confidence interval 0.39 to 0.99)"

## 15. Chụp cắt lớp vi tính (CT) liều thấp
- <https://doi.org/10.1056/NEJMoa1102873> - NEJM 403; bản ghi Europe PMC xác nhận (PMID 21714641), và đã mở tóm tắt toàn văn tại <https://pmc.ncbi.nlm.nih.gov/articles/PMC4356534/>.
  - Nguyên văn: "53,454 persons at high risk for lung cancer at 33 U.S. medical centers"; "24.2% with low-dose CT and 6.9% with radiography over all three rounds"; "96.4% of the positive screening results in the low-dose CT group … were false positive results"; "20.0% (95% CI, 6.8 to 26.7; P = 0.004)"; "6.7% (95% CI, 1.2 to 13.6; P = 0.02)"
  - Tiêu chuẩn tuyển chọn (55-74 tuổi, ≥30 bao-năm, bỏ thuốc lá ≤15 năm) đã được xác nhận trong tóm tắt trên Europe PMC.

## 16. Khủng hoảng tâm lý
- <https://doi.org/10.1016/S2215-0366(16)30030-X> - Trang Elsevier chỉ hiển thị Redirecting; bản ghi Europe PMC xác nhận: Zalsman G, Lancet Psychiatry 2016.
  - Nguyên văn: "Evidence for restricting access to lethal means in prevention of suicide has strengthened since 2005"; "overall decrease of 43% since 2005" (kiểm soát thuốc giảm đau); "hot-spots for suicide by jumping (reduction of 86% since 2005, 79% to 91%)"; "School-based awareness programmes have been shown to reduce suicide attempts (odds ratio [OR] 0·45, 95% CI 0·24-0·85"
- <https://www.gov.cn/zhengce/zhengceku/202412/content_6994470.htm> - Đã mở. Tiêu đề "国家卫生健康委关于应用"12356"全国统一心理援助热线电话号码的通知" (Thông báo của 国家卫生健康委 (Ủy ban Y tế Sức khỏe Quốc gia Trung Quốc) về việc áp dụng số điện thoại đường dây nóng hỗ trợ tâm lý thống nhất toàn quốc "12356"), 国卫医政函〔2024〕259 号, 2024-12-06.
  - Nguyên văn: "设置'12356'作为全国统一心理援助热线电话号码"; "每日提供不少于18小时心理援助服务"; "确保于2025年5月1日0时前，实现拨打'12356'电话号码接通心理援助热线的功能"
  - Liên kết gốc nhc.gov.cn trả về 412, đổi sang dẫn cùng văn bản từ kho văn bản chính sách của 国务院 (Quốc vụ viện Trung Quốc).

## Chưa xác nhận / Chưa áp dụng
- Trang web NHTSA nhtsa.gov/risky-driving/seat-belts, car-seats-and-booster-seats: 403, chưa xác nhận, đổi sang dùng PDF chính thức từ crashstats.
- Báo cáo thiết bị báo khói của NFPA: chưa xác nhận, chưa trích dẫn.
- PDF country profile Trung Quốc trong WHO Global status report on road safety 2023: 404, chưa xác nhận; số liệu tử vong do giao thông đường bộ tại Trung Quốc đổi sang dùng GHO API.
- Fact sheet về đuối nước của WHO (đã mở, bản 2026-05-01): không có số liệu Trung Quốc, chưa trích dẫn; "around 300 000 annual drowning deaths worldwide" chưa dùng đến.
- Con số quy mô thử nghiệm ở mục lợi ích (Ettehad 123 nghiên cứu/613.815 người, Sherrington 108 nghiên cứu/23.407 người, Lei 1.672.983 người, IAMI 2571 người) đã được đối soát từng chữ trong lượt cào dữ liệu thứ hai từ Europe PMC, xem nguyên văn từng mục.
- Mức giá trong mục chi phí (mũ bảo hiểm, thiết bị báo khói, vắc-xin, chi phí kiểm tra...) là ước tính sơ bộ của tác giả theo giá thị trường, không thuộc diện số liệu trích dẫn, chưa kiểm chứng.
