from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')


def replace_once(old: str, new: str):
    global s
    if old in s:
        s = s.replace(old, new, 1)


# Hero: concise first-screen message.
replace_once(
    'Đại học toàn cầu hợp tác Anh – Trung, tọa lạc tại Tô Châu (30 phút đến Thượng Hải)',
    'Đại học quốc tế Anh – Trung tại Tô Châu',
)
replace_once(
    '''<p class="sub">XJTLU Vietnam cung cấp thông tin dành cho học sinh và phụ huynh Việt Nam về <b>học phí XJTLU, học bổng, điều kiện tuyển sinh 2027, ngành học và ký túc xá</b>. Xi'an Jiaotong-Liverpool University (XJTLU) do <b>University of Liverpool</b> (Anh Quốc) và <b>Đại học Giao thông Tây An</b> (Trung Quốc) đồng sáng lập năm 2006. Sinh viên tốt nghiệp đại học nhận <b>bằng của University of Liverpool (Anh Quốc) và bằng của XJTLU</b>, học hoàn toàn bằng tiếng Anh, và có thể bổ sung tiếng Trung như một lợi thế nghề nghiệp.</p>''',
    '''<p class="sub"><b>Xi'an Jiaotong-Liverpool University (XJTLU)</b> là đại học quốc tế Anh – Trung tại Tô Châu. Sinh viên học bằng tiếng Anh và, khi đáp ứng yêu cầu tốt nghiệp, nhận bằng <b>University of Liverpool</b> cùng bằng XJTLU.</p>''',
)

old_mobile = '@media(max-width:560px){.hero{min-height:auto}.hero-actions .btn{width:100%;white-space:normal;text-align:center}.fact b{font-size:28px}}'
new_mobile = '''@media(max-width:560px){
  .hero{min-height:auto}
  .hero .container{padding:40px 0 48px}
  .hero-kicker{margin-bottom:18px;padding:7px 12px 7px 9px;font-size:12px}
  .hero h1 .h1-brand{margin-bottom:11px;font-size:11px;letter-spacing:.11em}
  .hero .sub{margin-top:18px;font-size:15.5px;line-height:1.62}
  .hero-actions{margin-top:24px;gap:8px;flex-direction:column;align-items:stretch}
  .hero-actions .btn{width:100%;white-space:normal;text-align:center}
  .hero-actions .btn-ghost{width:auto;align-self:center;border:0;padding:8px 4px;border-radius:0;font-size:13.5px;color:#dfe4ef;box-shadow:none}
  .hero-actions .btn-ghost::after{content:" →"}
  .hero-facts{margin-top:38px;padding-top:24px;gap:20px 16px}
  .fact b{font-size:28px}
  .route{margin-top:4px}
}'''
replace_once(old_mobile, new_mobile)

# Bar-type phones: keep route cards separated without changing wider layouts.
bar_phone_marker = '/* TNS_BAR_PHONE_ROUTE_LAYOUT */'
if bar_phone_marker not in s:
    anchor = '@media(max-width:640px){.btn{white-space:normal;text-align:center}.nav .btn,.fab{white-space:nowrap}}'
    bar_phone_css = '''/* TNS_BAR_PHONE_ROUTE_LAYOUT */
@media(max-width:430px){
  .route-card{font-size:10.8px;padding:9px 11px}
  .route-card b{font-size:12.2px}
  .route-card.b{left:0;top:-2%;max-width:174px}
  .route-card.c{right:0;top:24%;max-width:188px}
  .route-card.a{right:0;bottom:1%;max-width:205px}
}
'''
    if anchor not in s:
        raise SystemExit('Bar-phone CSS anchor not found')
    s = s.replace(anchor, bar_phone_css + anchor, 1)
replace_once('2 năm Trung Quốc → 2 năm Liverpool (tùy ngành)', '2 năm Trung Quốc → 2 năm Liverpool')

# Main-page editorial rule: overview copy stays brief; details live on dedicated pages.
replacements = [
    ('Không phải "du học nước ngoài" thông thường. Đây là giáo dục quốc tế kiểu châu Á.', 'XJTLU: đại học quốc tế Anh – Trung tại Tô Châu'),
    ('XJTLU là đại học liên doanh Anh – Trung lớn nhất Trung Quốc, được thành lập bởi University of Liverpool và Xi\'an Jiaotong University. Bạn học chuyên ngành bằng tiếng Anh theo cấu trúc bằng cấp Anh Quốc, ngay giữa hệ sinh thái công nghiệp – công nghệ của Tô Châu và Thượng Hải.', 'Học chuyên ngành bằng tiếng Anh, nhận bằng XJTLU và University of Liverpool, tại Tô Châu – gần Thượng Hải.'),
    ('Toàn bộ chương trình đại học dành cho sinh viên quốc tế được giảng dạy bằng tiếng Anh. Tiếng Trung là năng lực cộng thêm, không phải điều kiện bắt buộc để nhập học.', 'Học chuyên ngành bằng tiếng Anh; tiếng Trung là lợi thế bổ sung.'),
    ('Sinh viên tốt nghiệp nhận bằng cử nhân của University of Liverpool (Anh Quốc) cùng bằng của XJTLU. Riêng lễ tốt nghiệp 2026, 3.797 sinh viên đại học đã nhận đồng thời hai văn bằng này.', 'Đủ điều kiện tốt nghiệp, sinh viên nhận bằng University of Liverpool cùng bằng XJTLU.'),
    ('Hơn 28.000 sinh viên, 100+ chương trình đào tạo, sinh viên đến từ hơn 90 quốc gia. Đông Nam Á là một trong những cộng đồng quốc tế phát triển nhanh nhất.', '28.000+ sinh viên, 100+ chương trình và sinh viên từ 90+ quốc gia.'),
    ('Khuôn viên nằm trong Khu công nghiệp Tô Châu (SIP) – một trong những trung tâm sản xuất và đổi mới lớn của Trung Quốc; đi tàu cao tốc đến Thượng Hải chỉ khoảng 30 phút.', 'Cơ sở chính ở Tô Châu (SIP), kết nối nhanh với Thượng Hải.'),
    ('Các khóa tiếng Trung, Business Chinese, ngành International Business with a Language… giúp bạn xây dựng "năng lực Trung Quốc" trên nền tảng tiếng Anh.', 'Có thể bổ sung tiếng Trung và Business Chinese trong quá trình học.'),
    ('Nhiều ngành cho phép học 2 năm tại Tô Châu rồi chuyển sang University of Liverpool học 2 năm cuối (được giảm 10% học phí tại Liverpool). Không phải mọi ngành đều áp dụng – hãy kiểm tra theo ngành.', 'Một số ngành có lộ trình 2+2 sang University of Liverpool.'),
    ('Thành lập năm 2006 tại Tô Châu, tỉnh Giang Tô. Khuôn viên từng đoạt giải tại World Architecture Festival.', 'Thành lập năm 2006 tại Tô Châu, tỉnh Giang Tô.'),
    ('Từ Liverpool đến Tô Châu — và giờ đây đến gần Việt Nam hơn', 'Liverpool × Việt Nam: kết nối ngày càng gần'),
    ('Thông qua XJTLU, University of Liverpool đã xây dựng một trong những mô hình hợp tác giáo dục Anh – châu Á thành công nhất thế giới. Gần đây, Liverpool cũng đang mở rộng nhanh chóng quan hệ hợp tác với Việt Nam, đặc biệt là TP. Hồ Chí Minh, trong các lĩnh vực giáo dục, y tế, AI, khoa học dữ liệu và đổi mới sáng tạo.', 'Liverpool đang mở rộng hợp tác với Việt Nam trong giáo dục, y tế, AI và đổi mới sáng tạo.'),
    ('Tháng 10/2025, Việt Nam và Anh nâng cấp quan hệ song phương lên Đối tác Chiến lược Toàn diện (Comprehensive Strategic Partnership), nhất trí mở rộng hợp tác trong giáo dục, khoa học công nghệ, AI, công nghệ sinh học, dược phẩm và đổi mới sáng tạo.', 'Từ 10/2025, Việt Nam và Anh nâng cấp quan hệ lên Đối tác Chiến lược Toàn diện.'),
    ('Cùng thời điểm, TP. Hồ Chí Minh và Vùng đô thị Liverpool ký kết quan hệ Đối tác City2City chính thức, với các lĩnh vực hợp tác gồm giáo dục &amp; đào tạo, y tế, trí tuệ nhân tạo, khoa học dữ liệu, khoa học công nghệ và đổi mới sáng tạo.', 'TP.HCM và Liverpool thiết lập quan hệ City2City, gồm giáo dục, y tế và công nghệ.'),
    ('Tháng 1/2026, Civic Health Innovation Labs (CHIL) của University of Liverpool ký kết biên bản ghi nhớ hợp tác dài hạn với Đại học Y Dược TP. Hồ Chí Minh (UMP HCMC), tập trung vào AI trong y tế, khoa học dữ liệu, y tế số, tin sinh y học, y tế công cộng, nghiên cứu chung và trao đổi giảng viên - nghiên cứu sinh.', '01/2026, University of Liverpool và UMP TP.HCM ký hợp tác về AI, dữ liệu và y tế số.'),
    ('Vì sao "tiếng Anh + tiếng Trung + trải nghiệm Trung Quốc" đang trở thành lợi thế của người trẻ Việt Nam', 'Tiếng Anh + tiếng Trung: lợi thế đáng chú ý tại Việt Nam'),
    ('Điều XJTLU mang lại là một phương án lai: nhu cầu về bằng cấp Anh Quốc và giáo dục bằng tiếng Anh, gặp cơ hội học tập ngay tại Trung Quốc với chi phí hợp lý.', 'XJTLU kết hợp học bằng tiếng Anh, trải nghiệm Trung Quốc và bằng cấp gắn với Anh Quốc.'),
    ('Số sinh viên Việt Nam đang học tại Trung Quốc (báo cáo 2026). Tăng hơn gấp đôi so với năm 2018.', 'Sinh viên Việt Nam đang học tại Trung Quốc (2026).'),
    ('Lượt thi HSK tại Việt Nam năm 2025 – được báo chí ghi nhận là cao nhất thế giới, chiếm khoảng 18% toàn cầu.', 'Lượt thi HSK tại Việt Nam năm 2025.'),
    ('Tin tuyển dụng yêu cầu tiếng Trung năm 2025 tăng 49% so với 2024 (12.997 tin, theo dữ liệu nền tảng tuyển dụng tư nhân JobOKO).', 'Tin tuyển dụng yêu cầu tiếng Trung tăng 49% trong 2025.'),
    ('Vốn cam kết đầu tư của doanh nghiệp Trung Quốc &amp; Hồng Kông vào Việt Nam trong 11 tháng đầu 2025 (Reuters) – sản xuất, điện tử, EV, chuỗi cung ứng.', 'Vốn cam kết từ doanh nghiệp Trung Quốc &amp; Hồng Kông vào Việt Nam.'),
    ('<b>Cách đọc các con số này:</b> khi đầu tư và chuỗi cung ứng Trung Quốc ngày càng gắn với Việt Nam, sự kết hợp <b>tiếng Anh + tiếng Trung + trải nghiệm sống và học tại Trung Quốc</b> có thể mở rộng lựa chọn nghề nghiệp của bạn – dù bạn làm việc ở Việt Nam, Trung Quốc hay Singapore. Đây là tín hiệu thị trường, không phải cam kết về việc làm hay mức lương.', '<b>Ý nghĩa:</b> tiếng Anh + tiếng Trung + trải nghiệm Trung Quốc có thể mở rộng lựa chọn học tập và nghề nghiệp; đây không phải cam kết việc làm.'),
    ('XJTLU có hơn 50 ngành đại học. Dưới đây là 5 nhóm ngành phù hợp nhất với bối cảnh Việt Nam – nhấn để xem các ngành tiêu biểu và liên kết tới trang chính thức.', '5 nhóm ngành tiêu biểu dành cho sinh viên Việt Nam.'),
    ('Cấu trúc bằng cấp Anh Quốc + tiếng Anh + hiểu biết thị trường Trung Quốc. Phù hợp với sinh viên hướng tới các tập đoàn đa quốc gia, tài chính, thương mại xuyên biên giới Việt – Trung.', 'Phù hợp với kinh doanh quốc tế, tài chính và thương mại Việt – Trung.'),
    ('Học AI, dữ liệu và vi điện tử ngay tại khu vực mà hợp tác AI – bán dẫn – công nghiệp số giữa Trung Quốc và Việt Nam đang được đẩy mạnh.', 'AI, dữ liệu, vi điện tử và kỹ thuật trong hệ sinh thái công nghệ Tô Châu – Thái Thương.'),
    ('Việt Nam đang triển khai Chiến lược phát triển logistics 2025–2035 và kết nối sản xuất – logistics Việt – Trung ngày càng sâu. XJTLU có ngành Intelligent Supply Chain, hệ sinh thái công nghiệp Tô Châu và một giảng viên người Việt trong lĩnh vực này.', 'Supply Chain, logistics và sản xuất thông minh trong hệ sinh thái công nghiệp Tô Châu.'),
    ('Nền tảng khoa học bằng tiếng Anh với cấu trúc bằng Anh Quốc, mở đường lên bậc thạc sĩ – tiến sĩ tại Anh, Singapore, Úc hoặc tiếp tục tại Trung Quốc. Phạm vi nghề nghiệp và chứng chỉ hành nghề cần được xác nhận theo từng ngành.', 'Khoa học sự sống và dược bằng tiếng Anh, phù hợp cho lộ trình học lên quốc tế.'),
    ('Kiến trúc, quy hoạch đô thị, điện ảnh và truyền thông số tại một trong những thành phố có cảnh quan đô thị – di sản đặc sắc nhất Trung Quốc. Một số ngành yêu cầu portfolio và phỏng vấn khi xét tuyển thẳng năm 2 / chuyển tiếp năm 3.', 'Kiến trúc, thiết kế, phim và truyền thông số; một số ngành yêu cầu portfolio.'),
    ('Học phí sinh viên quốc tế được XJTLU công bố cho kỳ nhập học 2027. Các mức giảm và học bổng có thể cộng dồn tùy điều kiện; hãy kiểm tra lại trang chính thức trước khi nộp hồ sơ.', 'Học phí và các học bổng chính cho kỳ nhập học 2027.'),
    ('Thấp hơn đáng kể so với du học Anh, Úc, Mỹ, trong khi vẫn nhận bằng của University of Liverpool.', 'Chi phí cạnh tranh hơn so với học toàn thời gian tại Anh, Úc hoặc Mỹ.'),
    ('Tối đa 50% học phí mỗi năm cho sinh viên quốc tế có thành tích học tập xuất sắc. Gia hạn hằng năm nếu duy trì kết quả tốt. Đánh dấu mục "XJTLU Entry Scholarship" khi nộp hồ sơ online – nộp sớm để còn suất.', 'Tối đa 50% học phí mỗi năm; có thể gia hạn nếu duy trì kết quả tốt.'),
    ('Giảm 10% học phí mỗi năm nếu bạn nộp hồ sơ online và nhận được thư mời (có điều kiện hoặc vô điều kiện) trước 31/3/2027, đồng thời đóng cọc đúng hạn ghi trên thư mời.', 'Giảm 10% học phí nếu đáp ứng điều kiện Early Bird trước 31/3/2027.'),
    ('10.000 RMB cho sinh viên đạt loại xuất sắc, 5.000 RMB cho loại giỏi theo kết quả năm học trước – xét tự động, không cần nộp đơn. Ngoài ra có giảm học phí cho anh chị em cùng học (5–15%).', '5.000–10.000 RMB theo kết quả học tập; xét tự động theo quy định.'),
    ('XJTLU có nhiều lựa chọn ký túc xá ở cả cơ sở Tô Châu (SIP) và Thái Thương. Mức phí phổ biến khoảng 1.700 RMB/tháng (≈ 6,1 triệu VND) cho phòng đơn có nhà vệ sinh riêng.', 'Ký túc xá tại Tô Châu và Thái Thương, với nhiều mức giá và loại phòng.'),
    ('Ba lối vào chương trình đại học: nhập học năm 1 bằng bằng tốt nghiệp THPT Việt Nam, chuyển tiếp năm 2 hoặc năm 3 từ đại học Việt Nam, hoặc xét tuyển thẳng năm 2 bằng bằng cấp quốc tế (IB, A-Level, SAT/AP). Chương trình thạc sĩ có trang thông tin riêng.', 'Năm 1, chuyển tiếp năm 2–3 hoặc xét bằng cấp quốc tế.'),
    ('Cộng đồng Việt Nam tại XJTLU đang hình thành. Dưới đây là những câu chuyện có thật từ Việt Nam và các nước láng giềng, được tóm tắt từ bài viết chính thức của XJTLU – nhấn "Bài gốc" để đọc đầy đủ.', 'Một số câu chuyện thật từ sinh viên Việt Nam và châu Á tại XJTLU.'),
]
for old, new in replacements:
    replace_once(old, new)

# Compact detail-page handoff blocks: one short title + one short link.
replace_once('''<strong>Đại học Liverpool tại Trung Quốc? Tìm hiểu mô hình XJTLU</strong>\n    <p>Giải thích rõ mối quan hệ với University of Liverpool, chương trình học bằng tiếng Anh và lộ trình 2+2 dành cho sinh viên quốc tế.</p>''', '''<strong>XJTLU &amp; University of Liverpool</strong>''')
replace_once('Tìm hiểu XJTLU & Liverpool →', 'Xem chi tiết →')
replace_once('''<strong>Học phí và học bổng XJTLU 2027</strong>\n    <p>Xem riêng học phí, Entry Scholarship, Early Bird và các khoản chi cần chuẩn bị cho sinh viên Việt Nam.</p>''', '''<strong>Học phí &amp; học bổng XJTLU 2027</strong>''')
replace_once('Xem hướng dẫn học phí →', 'Xem chi tiết →')
replace_once('''<strong>Điều kiện tuyển sinh XJTLU 2027 cho học sinh Việt Nam</strong>\n    <p>Xem yêu cầu THPT, IELTS/TOEFL, hồ sơ, chuyển tiếp năm 2–3 và thời gian xét tuyển.</p>''', '''<strong>Điều kiện tuyển sinh XJTLU 2027</strong>''')
replace_once('Xem điều kiện chi tiết →', 'Xem chi tiết →')

# Compact graduate outcomes while preserving the useful statistics.
old_grad = '''<!-- TNS_GRAD_OUTCOMES_START -->
<div class="tns-grad-outcomes reveal">
  <div class="tns-grad-outcomes-head">
    <div>
      <span class="pill">Kết quả học lên · 2025</span>
      <h3>Sau XJTLU, sinh viên tiếp tục học ở đâu?</h3>
      <p>Dữ liệu XJTLU 2025 cho thấy tỷ lệ học lên rất cao, với các điểm đến như UCL, Imperial, Oxford, Harvard, Cambridge, NUS và nhiều đại học hàng đầu khác.</p>
    </div>
  </div>
  <div class="tns-grad-stats">
    <div class="tns-grad-stat"><b>86,43%</b><span>dự định tiếp tục học tại các đại học trên thế giới</span></div>
    <div class="tns-grad-stat"><b>47,16%</b><span>đi vào nhóm đại học TOP 10 theo dữ liệu XJTLU</span></div>
    <div class="tns-grad-stat"><b>93,40%</b><span>đi vào nhóm đại học TOP 100 theo dữ liệu XJTLU</span></div>
  </div>
  <a class="tns-grad-link" href="/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html">Xem Harvard, Oxford, UCL và toàn bộ điểm đến học lên 2025 →</a>
</div>
<!-- TNS_GRAD_OUTCOMES_END -->'''
new_grad = '''<!-- TNS_GRAD_OUTCOMES_START -->
<div class="tns-grad-outcomes reveal">
  <span class="pill">Kết quả học lên · 2025</span>
  <h3>Sinh viên XJTLU học tiếp ở đâu?</h3>
  <p class="tns-grad-destinations">UCL · Imperial · Oxford · Harvard · Cambridge · NUS…</p>
  <div class="tns-grad-stats">
    <div class="tns-grad-stat"><b>86,43%</b><span>dự định học tiếp</span></div>
    <div class="tns-grad-stat"><b>47,16%</b><span>vào TOP 10</span></div>
    <div class="tns-grad-stat"><b>93,40%</b><span>vào TOP 100</span></div>
  </div>
  <div class="tns-grad-foot"><small>Theo dữ liệu XJTLU 2025.</small><a class="tns-grad-link" href="/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html">Xem điểm đến 2025 →</a></div>
</div>
<!-- TNS_GRAD_OUTCOMES_END -->'''
replace_once(old_grad, new_grad)

# Compact component styling for detail handoffs and graduate outcomes.
old_guide_style = '''<style id="tns-inline-guide-style">
.tns-inline-guide{margin-top:28px;padding:20px 0 0;border-top:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:22px}.tns-inline-guide-copy{max-width:760px}.tns-inline-guide small{display:block;color:var(--gold);font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-bottom:5px}.tns-inline-guide strong{display:block;color:var(--navy);font-family:var(--font-display);font-size:19px;line-height:1.3}.tns-inline-guide p{margin:6px 0 0;color:var(--muted);font-size:13.5px;line-height:1.65}.tns-inline-guide a{flex:none;color:var(--jade);font-size:14px;font-weight:800;white-space:nowrap}.tns-inline-guide a:hover{text-decoration:underline}@media(max-width:700px){.tns-inline-guide{display:block}.tns-inline-guide a{display:inline-block;margin-top:12px;white-space:normal}}
</style>'''
new_guide_style = '''<style id="tns-inline-guide-style">
.tns-inline-guide{width:min(1180px,calc(100% - 40px));margin:22px auto 0;padding:16px 0 0;border-top:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:18px}.tns-inline-guide-copy{max-width:760px}.tns-inline-guide small{display:block;color:var(--gold);font-size:10.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px}.tns-inline-guide strong{display:block;color:var(--navy);font-family:var(--font-display);font-size:18px;line-height:1.25}.tns-inline-guide a{flex:none;color:var(--jade);font-size:13.5px;font-weight:800;white-space:nowrap}.tns-inline-guide a:hover{text-decoration:underline}
.tns-grad-outcomes{width:min(1180px,calc(100% - 40px));margin:26px auto 0;padding:24px 26px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:18px}.tns-grad-outcomes h3{color:#fff;margin:8px 0 4px;font-size:26px}.tns-grad-destinations{color:#b9c2d6;margin:0;font-size:14px}.tns-grad-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:16px 0 12px}.tns-grad-stat{padding:13px 14px;background:rgba(255,255,255,.06);border-radius:12px}.tns-grad-stat b{display:block;color:var(--gold-2);font-family:var(--font-display);font-size:26px;line-height:1}.tns-grad-stat span{display:block;color:#dfe4ef;font-size:12.5px;margin-top:5px}.tns-grad-foot{display:flex;justify-content:space-between;align-items:center;gap:14px}.tns-grad-foot small{color:#8f9ab2}.tns-grad-link{color:var(--gold-2);font-weight:800;font-size:13.5px}
@media(max-width:700px){.tns-inline-guide{width:calc(100% - 32px);margin-top:16px;padding-top:13px;display:flex;align-items:flex-end}.tns-inline-guide strong{font-size:17px}.tns-inline-guide a{font-size:13px}.tns-grad-outcomes{width:calc(100% - 32px);padding:20px 18px;margin-top:20px}.tns-grad-outcomes h3{font-size:23px}.tns-grad-stats{grid-template-columns:1fr;gap:7px}.tns-grad-stat{display:flex;align-items:center;justify-content:space-between;padding:9px 11px}.tns-grad-stat b{font-size:22px}.tns-grad-stat span{margin:0;font-size:12.5px}.tns-grad-foot{align-items:flex-end}.tns-grad-foot small{font-size:11px}.tns-grad-link{font-size:13px;text-align:right}}
</style>'''
replace_once(old_guide_style, new_guide_style)

p.write_text(s, encoding='utf-8')
print('Compacted XJTLU Vietnam homepage copy, detail handoffs and mobile route cards.')
