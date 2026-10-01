> Bản dịch không chính thức của [docs/核实记录/03-不要浪费精力.md](../../../docs/核实记录/03-不要浪费精力.md). Nếu có khác biệt, bản gốc tiếng Trung là bản có hiệu lực.
[← Về mục lục](../../../README.vi.md)

# Hồ sơ kiểm chứng nguồn phần 3

Lưu ý: phần lớn trang web của các nhà xuất bản (APA psycnet, Elsevier, SAGE, PNAS, Springer, PubMed) trả về lỗi 403 / mã xác nhận / chỉ có thông báo cookie đối với WebFetch của máy này, do đó quy trình kiểm chứng là: trước hết dùng <https://doi.org/>... phân giải để xác nhận DOI tồn tại và xem đích chuyển hướng (xác nhận nhà xuất bản và tạp chí), sau đó dùng Europe PMC REST API / Crossref API / OpenAlex API / trang toàn văn PMC / bản PDF chính thức của tác giả hoặc trường đại học để lấy tiêu đề, tác giả, năm và nguyên văn phần tóm tắt. Mỗi mục đều liệt kê URL thực tế đã mở cùng vị trí trong nguyên văn của các con số được trích dẫn.

## Mục 1
- <https://doi.org/10.1037/xhp0000100> → 302 đến doi.apa.org, DOI tồn tại; trang psycnet 403
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/xhp0000100&format=json&resultType=core> → Đã xác nhận: Stothart C, Mitchum A, Yehnert C (2015) The attentional cost of receiving a cell phone notification. J Exp Psychol Hum Percept Perform
  - Nguyên văn: "cellular phone notifications alone significantly disrupted performance on an attention-demanding task, even when participants did not directly interact with a mobile device during the task. The magnitude of observed distraction effects was comparable in magnitude to those seen when users actively used a mobile phone, either for voice calls or text messaging."
- <https://doi.org/10.1086/691462> → 302 đến journals.uchicago.edu, DOI tồn tại; trang nhà xuất bản 403
- <https://api.crossref.org/works/10.1086/691462> → Đã xác nhận: Ward AF, Duke K, Gneezy A, Bos MW (2017) Brain Drain: The Mere Presence of One's Own Smartphone Reduces Available Cognitive Capacity. J Assoc Consum Res 2(2):140-154
- <https://api.openalex.org/works/doi:10.1086/691462> → Nguyên văn: "Results from two experiments indicate that even when people are successful at maintaining sustained attention—as when avoiding the temptation to check their phones—the mere presence of these devices reduces available cognitive capacity. Moreover, these costs are highest for those in smartphone dependence."
  - Ba điều kiện "trên bàn/trong túi/phòng khác" và hai chỉ số "trí nhớ làm việc, trí tuệ linh hoạt" đến từ trí nhớ của tôi về bài báo này, phần tóm tắt chỉ viết two experiments và available cognitive capacity, hai chi tiết này **chưa được xác nhận từng chữ trong nguyên văn** (không mở được toàn văn), đã xóa khỏi mục, mục chỉ giữ lại cách diễn đạt được nguyên văn tóm tắt hỗ trợ

## Mục 2
- <https://doi.org/10.1038/s41598-017-03171-4> → 302 đến nature.com, DOI tồn tại; trang nature cần cấp quyền để chuyển hướng
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41598-017-03171-4&format=json&resultType=core> → Đã xác nhận: Phillips AJK, Clerx WM, O'Brien CS, Sano A, Barger LK, Picard RW, Lockley SW, Klerman EB, Czeisler CA (2017) Irregular sleep/wake patterns are associated with poorer academic performance and delayed circadian and sleep/wake timing. Sci Rep
  - Nguyên văn: "We studied 61 undergraduates for 30 days ... DLMO occurred later (00:08 ± 1:54 vs. 21:32 ± 1:48; p < 0.003); the daily sleep propensity rhythm peaked later (06:33 ± 0:19 vs. 04:45 ± 0:11; p < 0.005) ... A positive correlation (r = 0.37; p < 0.004) between academic performance and SRI was observed ... Irregular vs. Regular group differences in circadian timing were likely primarily due to their different patterns of light exposure."
  - "Khoảng 2,5 giờ", "khoảng 1,8 giờ" là giá trị xấp xỉ do tôi tính ra từ chênh lệch thời điểm nêu trên

## Mục 3
- <https://doi.org/10.1093/sleep/26.2.117> → 302 đến academic.oup.com, sau đó <https://academic.oup.com/sleep/article-lookup/doi/10.1093/sleep/26.2.117> mở thành công
  - Đã xác nhận: Van Dongen HPA, Maislin G, Mullington JM, Dinges DF (2003) The Cumulative Cost of Additional Wakefulness: Dose-Response Effects on Neurobehavioral Functions and Sleep Physiology From Chronic Sleep Restriction and Total Sleep Deprivation. Sleep 26(2):117-126
  - Nguyên văn tóm tắt (trang OUP + Europe PMC hai nơi khớp nhau): "A total of n = 48 healthy adults (ages 21-38)"; "Chronic restriction of sleep periods to 4 h or 6 h per night over 14 consecutive days resulted in significant cumulative, dose-dependent deficits in cognitive performance on all tasks"; "chronic restriction of sleep to 6 h or less per night produced cognitive performance deficits equivalent to up to 2 nights of total sleep deprivation"; "Subjective sleepiness ratings showed an acute response to sleep restriction but only small further increases on subsequent days, and did not significantly differentiate the 6 h and 4 h conditions."
- <https://doi.org/10.1037/a0018883> → 302 đến doi.apa.org, DOI tồn tại
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/a0018883&format=json&resultType=core> → Đã xác nhận: Lim J, Dinges DF (2010) A meta-analysis of the impact of short-term sleep deprivation on cognitive variables. Psychol Bull
  - Nguyên văn tóm tắt: "short-term (<48 hr) total sleep deprivation"; "70 articles containing 147 cognitive tests"; "lapses in simple attention: g = -0.776, 95% CI [-0.96, -0.60], p < .001"; "reasoning accuracy: g = -0.125, 95% CI [-0.27, 0.02]"

## Mục 4
- <https://doi.org/10.5664/jcsm.3170> → 302, DOI tồn tại; jcsm.aasm.org lỗi chứng chỉ, springer cần ủy quyền
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.5664/jcsm.3170&format=json&resultType=core> → Đã xác nhận: Drake C, Roehrs T, Shambroom J, Roth T (2013) Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed. J Clin Sleep Med; PMID 24235903, PMCID PMC3805807
- <https://pmc.ncbi.nlm.nih.gov/articles/PMC3805807/> → Toàn văn mở thành công
  - Nguyên văn nội dung: "For TST, reductions in duration relative to placebo were significant at each of the caffeine administration time points, reducing TST between 1.1 to 1.2 hours."; "Caffeine administered 6 h prior to bedtime reduced total sleep time by 41 min, which approached significance (p = 0.08)." (nhật ký); "only the objective measure detected differences when caffeine was taken 6 hours prior to bedtime"
- <https://doi.org/10.1016/j.smrv.2023.101764> → 302 đến linkinghub.elsevier.com, DOI tồn tại
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.smrv.2023.101764&format=json&resultType=core> → Đã xác nhận: Gardiner C, Weakley J, Burke LM, Roach GD, Sargent C, Maniar N, Townshend A, Halson SL (2023) The effect of caffeine on subsequent sleep: A systematic review and meta-analysis. Sleep Med Rev
  - Nguyên văn tóm tắt: "Caffeine consumption reduced total sleep time by 45 min and sleep efficiency by 7%"; "coffee (107 mg per 250 mL) should be consumed at least 8.8 h prior to bedtime"

## Mục 5
- <https://doi.org/10.1016/j.chb.2014.11.005> → 302 đến linkinghub.elsevier.com, DOI tồn tại; sciencedirect 403
- <https://api.crossref.org/works/10.1016/j.chb.2014.11.005> → Đã xác nhận: Kushlev K, Dunn EW (2015) Checking email less frequently reduces stress. Comput Hum Behav 43:220-228
- <https://dunn.psych.ubc.ca/wp-content/uploads/2010/11/kushlev-dunn-email-and-stress-in-press1.pdf> (bản thảo được chấp nhận dạng PDF trên trang chính thức thuộc phòng thí nghiệm của tác giả, trích xuất pdftotext nội bộ)
  - Nguyên văn tóm tắt: "During one week, 124 adults were randomly assigned to limit checking their email to three times a day; during the other week, participants could check their email an unlimited number of times per day."
  - Nguyên văn nội dung: "participants felt less daily stress in the limited as compared to the unlimited email condition, F(1, 121) = 4.18, p = .04, Cohen's d = .37"; "the average number of times people reported checking their email on a normal day at work was 15.48 at baseline (SD = 8.69)"; "there were no significant differences between conditions in how many emails people received (Mlimited = 16.64 vs. Munlimited = 16.04 ...) or responded to"

## Mục 6
- <https://doi.org/10.1037/a0030986> → 302 chuyển hướng tới doi.apa.org, DOI tồn tại
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/a0030986&format=json&resultType=core> → Đã xác nhận: Altmann EM, Trafton JG, Hambrick DZ (2014) Momentary interruptions can derail the train of thought. J Exp Psychol Gen
  - Tóm tắt, nguyên văn: "Interruptions averaging 4.4 s long tripled the rate of sequence errors on post-interruption trials relative to baseline trials. Interruptions averaging 2.8 s long--about the time to perform a step in the interrupted task--doubled the rate of sequence errors."
- <https://www.ics.uci.edu/~gmark/CHI2005.pdf> (trang chủ chính thức của tác giả tại UCI dạng PDF, trích xuất cục bộ bằng pdftotext)
  - Tóm tắt, nguyên văn: "detailed observation of 24 information workers"; "57% of their working spheres are interrupted"; nội dung chính: "11 min. 4 sec." (thời lượng trung bình ở chủ đề công việc trọng tâm/ngoại vi trước khi chuyển đổi); "When people did resume work on the same day, it took an average length of time of 25 min. 26 sec (sd=54 min. 48 sec.) ... before resuming work, our informants worked in an average of 2.26 (sd=2.79) working spheres."
  - Kiểm chứng DOI: số 10.1145/1054972.1054989 tôi nhớ ban đầu được kiểm tra qua OpenAlex là một bài báo khác (Marshall & Bly), đã sửa. Cả <https://api.crossref.org/works/10.1145/1054972.1055017> và <https://api.openalex.org/works/doi:10.1145/1054972.1055017> đều xác nhận là Mark, Gonzalez, Harris (2005) No task left behind? Examining the nature of fragmented work. CHI 2005 pp.321-330
- <https://www.ics.uci.edu/~gmark/chi08-mark.pdf> (bản PDF chính thức của tác giả, trích xuất cục bộ)
  - Tóm tắt, nguyên văn: "people completed interrupted tasks in less time with no difference in quality ... but this comes at a price: experiencing more stress, higher frustration, time pressure and effort."; nội dung chính: "Forty-eight subjects participated."
  - <https://api.crossref.org/works/10.1145/1357054.1357072> → Đã xác nhận: Mark G, Gudith D, Klocke U (2008) The cost of interrupted work: more speed and stress. CHI 2008 pp.107-110
  - Ý "khoảng một nửa sự gián đoạn là do bản thân tự khởi phát" trong phần ghi chú xuất phát từ trí nhớ của tôi về bài báo này, chưa được đối chiếu từng chữ trong văn bản trích xuất, đã xóa khỏi ghi chú của mục

## Mục 7
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Task%20switching%22%20AND%20AUTH:Monsell%20AND%20PUB_YEAR:2003&format=json&resultType=core> → Đã xác nhận: Monsell S (2003) Task switching. Trends Cogn Sci; DOI 10.1016/s1364-6613(03)00028-7; PMID 12639695
  - Tóm tắt, nguyên văn: "Subjects' responses are substantially slower and, usually, more error-prone immediately after a task switch."
  - Chú thích: tra trực tiếp bằng DOI trên Europe PMC trả về 0 kết quả (do vấn đề mã hóa dấu ngoặc đơn), đổi sang tra bằng tiêu đề + tác giả thì tìm thấy
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.0903620106&format=json&resultType=core> → Đã xác nhận: Ophir E, Nass C, Wagner AD (2009) Cognitive control in media multitaskers. PNAS
  - Tóm tắt, nguyên văn: "heavy media multitaskers are more susceptible to interference from irrelevant environmental stimuli and from irrelevant representations in memory ... heavy media multitaskers performed worse on a test of task-switching ability"
  - Chú thích: DOI này chưa được mở trực tiếp qua doi.org, được xác nhận nhờ bản ghi trên Europe PMC
- Tra cứu thêm <https://api.crossref.org/works/10.1037/0096-1523.27.4.763> xác nhận Rubinstein, Meyer & Evans (2001) có tồn tại, nhưng không lấy được bản tóm tắt, cuối cùng không trích dẫn trong mục

## Mục 8
- <https://doi.org/10.1073/pnas.1418490112> → 302 chuyển hướng tới pnas.org, DOI tồn tại; pnas.org 403
- Tìm kiếm trên Europe PMC xác nhận: Chang AM, Aeschbach D, Duffy JF, Czeisler CA (2015) Evening use of light-emitting eReaders negatively affects sleep, circadian timing, and next-morning alertness. PNAS; PMCID PMC4313820
- <https://pmc.ncbi.nlm.nih.gov/articles/PMC4313820/> → Mở toàn văn thành công
  - Nội dung chính, nguyên văn: "took longer to fall asleep ... 25.65 ± 18.78 min vs. 15.75 ± 13.09 min"; "suppressed evening levels of melatonin by 55.12 ± 20.12%"; "Dim light melatonin onset was >1.5 h later on the day following the LE-eBook condition (22:31 ± 0:42) than in the print-book condition (21:01 ± 0:49)"; "feeling sleepier the morning after reading an LE-eBook ... it took them hours longer to fully wake up"
  - Chi tiết "độ sáng tối đa, đọc liên tục vài giờ" trong phần ghi chú là do tôi nhớ về thiết lập thực nghiệm, chưa đối chiếu từng chữ, đã xóa khỏi ghi chú của mục

## Mục 9
- <https://doi.org/10.1093/sleep/29.6.831> → 302, sau đó mở thành công <https://academic.oup.com/sleep/article-lookup/doi/10.1093/sleep/29.6.831>
  - Đã xác nhận: Brooks A, Lack L (2006) A Brief Afternoon Nap Following Nocturnal Sleep Restriction: Which Nap Duration is Most Recuperative? Sleep 29(6):831-840
  - Tóm tắt, Nguyên văn: "The 5-minute nap produced few benefits in comparison with the no-nap control."; "The 10-minute nap produced immediate improvements in all outcome measures (including sleep latency, subjective sleepiness, fatigue, vigor, and cognitive performance), with some of these benefits maintained for as long as 155 minutes."; 20 phút: cải thiện xuất hiện sau khi chợp mắt 35 phút, duy trì đến 125 phút; "The 30-minute nap produced a period of impaired alertness and performance immediately after napping, indicative of sleep inertia, followed by improvements lasting up to 155 minutes after the nap."

## Mục 10
- <https://doi.org/10.1016/j.jenvp.2011.07.002> → 302 chuyển hướng tới linkinghub.elsevier.com, DOI tồn tại; sciencedirect 403; PubMed không có bài này (không phải tạp chí thuộc MEDLINE)
- <https://api.crossref.org/works/10.1016/j.jenvp.2011.07.002> → Đã xác nhận: Jahncke H, Hygge S, Halin N, Green AM, Dimberg K (2011) Open-plan office noise: Cognitive performance and restoration. J Environ Psychol 31(4):373-382
- <http://hig.diva-portal.org/smash/record.jsf?pid=diva2%3A434794&dswid=2269> (bản ghi kho lưu trữ chính thức của Đại học Gävle) → mở thành công, tiêu đề/tác giả/tạp chí/DOI trùng khớp
  - Tóm tắt, Nguyên văn: "The background sound level increased by 12 dB, from 39 to 51 dB LAeq."; "Decreased word memory performance, increased fatigue and motivational deficits when the background sound level increased."; "A break with a nature movie with corresponding sound increased energy ratings compared to just listening to river sounds or office noise."
  - N = 47, mỗi lần làm việc 2 giờ: trích từ đoạn trích tóm tắt do WebSearch trả về, không thấy từng chữ trên trang diva, đã xóa khỏi mục nội dung

## Mục 11
- <https://doi.org/10.1111/ecoj.12166> → 302 chuyển hướng tới academic.oup.com/ej/article/125/589/2052-2076/5078088, DOI tồn tại; trang OUP chỉ hiển thị thanh điều hướng
- <https://api.crossref.org/works/10.1111/ecoj.12166> → Đã xác nhận: Pencavel J (2015) The Productivity of Working Hours. The Economic Journal 125(589):2052-2076
- <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1111/ecoj.12166> → Tóm tắt, Nguyên văn: "below an hours threshold, output is proportional to hours; above a threshold, output rises at a decreasing rate as hours increase."
- <https://docs.iza.org/dp8129.pdf> (IZA DP No. 8129, bản thảo nghiên cứu của cùng bài báo, trang chính thức của viện; trích xuất bằng pdftotext cục bộ)
  - Thân bài, Nguyên văn: "below 49 weekly hours, variations in output are proportional to variations in hours; for those observations corresponding to 49 or more hours, output rises with hours at a decreasing rate and a maximum of output occurs at about 63 hours. Output at 70 hours differs little from output at 56 hours"; phần kết luận: "The working week threshold for the munition workers considered in this paper was at 48 hours, but for other workers it may be more or less."
  - Chú thích: phân tích trong thân bài lấy mốc 49 giờ, đoạn kết luận viết 48 giờ; mục nội dung chọn 49. Việc đối chiếu số liệu dùng bản thảo nghiên cứu, bản chính thức trên tạp chí không mở được

## Mục 12
- <https://doi.org/10.1111/j.1745-6924.2008.00088.x> → 302 chuyển hướng tới journals.sagepub.com, DOI tồn tại; trang SAGE báo lỗi 403
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1111/j.1745-6924.2008.00088.x&format=json&resultType=core> → Đã xác nhận: Nolen-Hoeksema S, Wisco BE, Lyubomirsky S (2008) Rethinking Rumination. Perspect Psychol Sci
  - Tóm tắt, Nguyên văn: "rumination exacerbates depression, enhances negative thinking, impairs problem solving, interferes with instrumental behavior, and erodes social support"; ngoài ra có "anxiety, binge eating, binge drinking, and self-harm"

## Mục 13
- <https://api.crossref.org/works/10.1037/0022-3514.46.5.1097> → Đã xác nhận: Rook KS (1984) The negative side of social interaction: Impact on psychological well-being. J Pers Soc Psychol 46(5):1097-1108
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22The%20negative%20side%20of%20social%20interaction%22%20AND%20AUTH:Rook&format=json&resultType=core> → PMID 6737206, DOI 10.1037//0022-3514.46.5.1097
  - Tóm tắt, Nguyên văn: "negative social outcomes were more consistently and more strongly related to well-being than were positive social outcomes"; cỡ mẫu 120 phụ nữ góa bụa từ 60-89 tuổi
- Chú thích: bản thân liên kết <https://doi.org/10.1037/0022-3514.46.5.1097> chưa mở trực tiếp được (các DOI cũ tương tự của APA đều nhảy sang psycnet báo lỗi 403), nhưng hai cơ sở dữ liệu độc lập là Crossref và Europe PMC đều ghi nhận DOI này

## Mục 14
- <https://api.crossref.org/works/10.1037/0022-3514.74.5.1252> → Đã xác nhận: Baumeister RF, Bratslavsky E, Muraven M, Tice DM (1998) Ego depletion: Is the active self a limited resource? J Pers Soc Psychol 74:1252-1265
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Ego%20depletion%3A%20is%20the%20active%20self%20a%20limited%20resource%22&format=json&resultType=core> → PMID 9599441, tóm tắt Nguyên văn: "Choice, active response, self-regulation, and other volition may all draw on a common inner resource."
- <https://doi.org/10.1177/1745691616652873> → 302 chuyển hướng tới SAGE, DOI tồn tại; SAGE 403
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1177/1745691616652873&format=json&resultType=core> → Đã xác nhận: Hagger MS, Chatzisarantis NLD, Alberts H, et al. (2016) A Multilab Preregistered Replication of the Ego-Depletion Effect. Perspect Psychol Sci
  - Tóm tắt Nguyên văn: 23 phòng thí nghiệm, 2.141 người; "the size of the ego-depletion effect was small with 95% confidence intervals (CIs) that encompassed zero (d = 0.04, 95% CI [-0.07, 0.15]"
- <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1177/0956797621989733&format=json&resultType=core> → Đã xác nhận: Vohs KD, Schmeichel BJ, Lohmann S, et al. (2021) A Multisite Preregistered Paradigmatic Test of the Ego-Depletion Effect. Psychol Sci
  - Tóm tắt Nguyên văn: "preregistered multilaboratory project (k = 36; N = 3,531) ... Confirmatory tests found a nonsignificant result (d = 0.06)"
  - Ghi chú: DOI này không mở trực tiếp qua doi.org, được xác nhận dựa trên đăng ký tại Europe PMC

## Tổng hợp các mục chưa xác nhận
- Mục 1 bản thảo từng viết "trên bàn/trong túi/phòng khác" "trí nhớ làm việc và trí thông minh linh hoạt", do chưa thể đối chiếu từng chữ trong văn bản gốc có thể mở được, nên đã xóa khỏi mục này, chỉ giữ lại cách diễn đạt có văn bản gốc phần tóm tắt hỗ trợ
- Ghi chú bản thảo mục 6 "khoảng một nửa số lần ngắt quãng là do bản thân tự khởi phát", ghi chú mục 8 "độ sáng tối đa, liên tục nhiều giờ", mục 10 "N = 47, làm việc 2 giờ" cũng bị xóa do chưa đối chiếu từng chữ
- Toàn bộ số liệu trong cột "Lợi ích" của 14 mục ở phiên bản hiện tại đều có nguồn văn bản gốc liệt kê ở trên; không có mục nào cần đánh dấu TODO / chờ kiểm chứng
