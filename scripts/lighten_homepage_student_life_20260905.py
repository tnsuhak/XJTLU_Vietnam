from pathlib import Path
import re

INDEX = Path('index.html')
SITEMAP = Path('sitemap.xml')
TODAY = '2026-09-05'

text = INDEX.read_text(encoding='utf-8')

STYLE_ID = 'tns-home-lite-20260905'
style = '''<style id="tns-home-lite-20260905">
.home-lite-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:26px}.home-lite-card{background:var(--paper);border:1px solid var(--line);border-radius:var(--r);padding:20px;min-width:0}.home-lite-card b{display:block;color:var(--navy);font-family:var(--font-display);font-size:20px;line-height:1.25;margin-bottom:6px}.home-lite-card span,.home-lite-card p{display:block;color:var(--muted);font-size:13px;line-height:1.55}.home-lite-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px}.home-lite-actions a{font-size:13.5px;font-weight:800;color:var(--jade)}.home-lite-actions a:hover{text-decoration:underline}.home-lite-stat{font-family:var(--font-display);font-size:29px!important;color:var(--navy)!important;font-weight:700}.home-life{background:linear-gradient(135deg,var(--deep),#1c3158);color:#fff}.home-life h2{color:#fff}.home-life .lead{color:#c6cfdf}.home-life .home-lite-card{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.12)}.home-life .home-lite-card b{color:#fff}.home-life .home-lite-card span,.home-life .home-lite-card p{color:#c9d1e0}.home-life .home-lite-actions a{color:var(--gold-2)}.home-lite-video{max-width:760px;margin:24px auto 0}.home-lite-video .video{min-height:0}.home-lite-faq{max-width:850px;margin:24px auto 0}.home-lite-faq details{background:#fff;border-bottom:1px solid var(--line);padding:15px 18px}.home-lite-faq summary{font-weight:700;color:var(--navy);cursor:pointer}.home-lite-faq p{font-size:13.5px;color:var(--muted);margin-top:8px}@media(max-width:760px){.home-lite-grid{grid-template-columns:1fr}.home-lite-card{padding:17px}.home-lite-card b{font-size:18px}.home-lite-stat{font-size:25px!important}.home-lite-actions{margin-top:16px}.home-lite-faq details{padding:14px 15px}}
</style>
'''
if STYLE_ID not in text:
    marker = '<!-- ===================== ABOUT / WHY XJTLU ===================== -->'
    if marker not in text:
        raise SystemExit('About marker missing')
    text = text.replace(marker, style + marker, 1)

# Merge two explanatory sections into one compact Vietnam-relevance section.
compact_vietnam = '''<!-- ===================== VIETNAM RELEVANCE ===================== -->
<section class="section deep" id="liverpool-vietnam">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">XJTLU × Việt Nam</div>
      <h2>Học bằng tiếng Anh, hiểu thêm thị trường Trung Quốc</h2>
      <p class="lead">XJTLU phù hợp với học sinh muốn kết hợp bằng cấp quốc tế với trải nghiệm học tập tại Trung Quốc.</p>
    </div>
    <div class="home-lite-grid">
      <div class="home-lite-card reveal"><b>University of Liverpool</b><span>Bằng Liverpool + XJTLU cho sinh viên đủ điều kiện tốt nghiệp.</span></div>
      <div class="home-lite-card reveal d1"><b>Tiếng Anh + tiếng Trung</b><span>Học chuyên ngành bằng tiếng Anh; tiếng Trung là lợi thế bổ sung.</span></div>
      <div class="home-lite-card reveal d2"><b>Việt Nam ↔ Trung Quốc</b><span>Phù hợp với kinh doanh, công nghệ, logistics và các ngành gắn với châu Á.</span></div>
    </div>
    <div class="home-lite-actions"><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">XJTLU & Liverpool →</a><a href="/xjtlu-2plus2-liverpool.html">Lộ trình 2+2 →</a><a href="/du-hoc-trung-quoc-2027.html">Du học Trung Quốc 2027 →</a></div>
  </div>
</section>

'''
text, n = re.subn(
    r'<!-- ===================== LIVERPOOL x VIETNAM ===================== -->.*?(?=<!-- ===================== PROGRAMMES ===================== -->)',
    compact_vietnam,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('Could not compact Liverpool/Vietnam sections')

compact_programmes = '''<!-- ===================== PROGRAMMES ===================== -->
<section class="section ivory" id="major">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Ngành học</div>
      <h2>5 nhóm ngành nổi bật</h2>
      <p class="lead">Xem nhanh trên trang chính; chương trình và hướng nghề nghiệp được tách sang hướng dẫn riêng.</p>
    </div>
    <div class="home-lite-grid">
      <div class="home-lite-card"><b>Kinh doanh & tài chính</b><span>Accounting · Economics & Finance · Marketing</span></div>
      <div class="home-lite-card"><b>AI · Data · Computing</b><span>AI · Computer Science · Data Science</span></div>
      <div class="home-lite-card"><b>Kỹ thuật & công nghệ</b><span>Robotics · Electrical · Microelectronics</span></div>
      <div class="home-lite-card"><b>Khoa học sự sống</b><span>Biomedical · Biopharmaceuticals · Chemistry</span></div>
      <div class="home-lite-card"><b>Design & Media</b><span>Architecture · Film · Digital Media</span></div>
      <div class="home-lite-card"><b>Taicang</b><span>Supply Chain · Manufacturing · IoT và các ngành kết hợp doanh nghiệp</span></div>
    </div>
    <div class="home-lite-actions"><a href="/xjtlu-nganh-hoc-nghe-nghiep.html">Xem toàn bộ ngành & nghề nghiệp →</a></div>
  </div>
</section>

'''
text, n = re.subn(
    r'<!-- ===================== PROGRAMMES ===================== -->.*?(?=<!-- ===================== TUITION ===================== -->)',
    compact_programmes,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('Could not compact programmes section')

compact_tuition = '''<!-- ===================== TUITION ===================== -->
<section class="section" id="tuition">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Học phí & Học bổng</div>
      <h2>Chi phí chính cho kỳ 2027</h2>
      <p class="lead">Chỉ giữ số liệu cần biết trên trang chính; điều kiện chi tiết nằm ở trang học phí riêng.</p>
    </div>
    <div class="home-lite-grid">
      <div class="home-lite-card"><span class="home-lite-stat">99.000 RMB</span><span>học phí đại học / năm</span></div>
      <div class="home-lite-card"><span class="home-lite-stat">Đến 50%</span><span>Entry Scholarship cho ứng viên quốc tế xuất sắc</span></div>
      <div class="home-lite-card"><span class="home-lite-stat">10%</span><span>Early Bird theo điều kiện và thời hạn của kỳ tuyển sinh</span></div>
    </div>
    <div class="home-lite-actions"><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Xem học phí, học bổng & chi phí chi tiết →</a></div>
  </div>
</section>

'''
text, n = re.subn(
    r'<!-- ===================== TUITION ===================== -->.*?(?=<!-- ===================== ACCOMMODATION ===================== -->)',
    compact_tuition,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('Could not compact tuition section')

compact_life = '''<!-- ===================== STUDENT LIFE ===================== -->
<section class="section home-life" id="rooms">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Đời sống sinh viên</div>
      <h2>Không chỉ có lớp học</h2>
      <p class="lead">Ký túc xá, thể thao, hơn 200 tổ chức & câu lạc bộ, cùng cuộc sống tại Tô Châu.</p>
    </div>
    <div class="home-lite-grid">
      <div class="home-lite-card"><b>Thể thao</b><span>SIP và Taicang có trung tâm thể thao với nhiều môn trong nhà và ngoài trời.</span></div>
      <div class="home-lite-card"><b>CLB & hoạt động</b><span>Thể thao, nghệ thuật, học thuật, tình nguyện và nhiều nhóm sở thích.</span></div>
      <div class="home-lite-card"><b>Ký túc xá & Tô Châu</b><span>Nhiều lựa chọn chỗ ở và môi trường sinh viên quốc tế gần Thượng Hải.</span></div>
    </div>
    <div class="home-lite-actions"><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html">Xem đời sống sinh viên XJTLU →</a></div>
  </div>
</section>

'''
text, n = re.subn(
    r'<!-- ===================== ACCOMMODATION ===================== -->.*?(?=<!-- ===================== ADMISSION ===================== -->)',
    compact_life,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('Could not compact accommodation/student-life section')

compact_admission = '''<!-- ===================== ADMISSION ===================== -->
<section class="section" id="admission">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Tuyển sinh 2027</div>
      <h2>Điều kiện chính cho học sinh Việt Nam</h2>
      <p class="lead">Tóm tắt để kiểm tra nhanh trước khi xem hướng dẫn hồ sơ chi tiết.</p>
    </div>
    <div class="home-lite-grid">
      <div class="home-lite-card"><span class="home-lite-stat">7,0/10</span><span>mức học lực THPT tham khảo cho lộ trình năm 1</span></div>
      <div class="home-lite-card"><span class="home-lite-stat">IELTS 5.0</span><span>năm 1 · mỗi kỹ năng từ 4.5</span></div>
      <div class="home-lite-card"><span class="home-lite-stat">31/05/2027</span><span>hạn hồ sơ đại học quốc tế theo brochure 2027</span></div>
    </div>
    <div class="home-lite-actions"><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Xem điều kiện tuyển sinh 2027 →</a></div>
  </div>
</section>

'''
text, n = re.subn(
    r'<!-- ===================== ADMISSION ===================== -->.*?(?=<!-- ===================== STORIES ===================== -->)',
    compact_admission,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('Could not compact admission section')

compact_video = '''<!-- ===================== VIDEO ===================== -->
<section class="section" id="reviews">
  <div class="container">
    <div class="section-head center reveal">
      <div class="eyebrow">Campus</div>
      <h2>Xem nhanh khuôn viên XJTLU</h2>
      <p class="lead">Một video là đủ trên trang chính; thông tin đời sống sinh viên nằm ở trang riêng.</p>
    </div>
    <div class="home-lite-video"><div class="video reveal" data-yt="2PyruJRbV5c" role="button" tabindex="0" aria-label="Phát video khuôn viên XJTLU"><img src="https://img.youtube.com/vi/2PyruJRbV5c/hqdefault.jpg" alt="Khuôn viên XJTLU và thành phố Tô Châu" width="480" height="360" loading="lazy" decoding="async"><div class="play"><i><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></i></div><div class="cap">Khuôn viên & cuộc sống tại Tô Châu</div></div></div>
    <div class="home-lite-actions" style="justify-content:center"><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html">Thể thao, CLB & đời sống sinh viên →</a></div>
  </div>
</section>

'''
text, n = re.subn(
    r'<!-- ===================== VIDEO ===================== -->.*?(?=<!-- ===================== FAQ ===================== -->)',
    compact_video,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('Could not compact video section')

compact_faq = '''<!-- ===================== FAQ ===================== -->
<section class="section mist" id="faq">
  <div class="container">
    <div class="section-head center reveal">
      <div class="eyebrow">Hỏi đáp nhanh</div>
      <h2>4 câu hỏi quan trọng nhất</h2>
    </div>
    <div class="home-lite-faq">
      <details><summary>XJTLU có dạy bằng tiếng Anh không?</summary><p>Có. Các chương trình cấp bằng dành cho sinh viên quốc tế được giảng dạy bằng tiếng Anh.</p></details>
      <details><summary>Học 4 năm ở Trung Quốc có nhận bằng University of Liverpool không?</summary><p>Sinh viên đại học đáp ứng yêu cầu tốt nghiệp của chương trình có thể nhận bằng XJTLU và bằng University of Liverpool; 2+2 là lộ trình học, không phải điều kiện duy nhất để nhận bằng Liverpool.</p></details>
      <details><summary>Học sinh Việt Nam có thể vào năm 1 không?</summary><p>Có. XJTLU công bố tiêu chí riêng cho Việt Nam; hãy xem trang điều kiện 2027 để kiểm tra học lực, môn liên quan và tiếng Anh.</p></details>
      <details><summary>2+2 có bắt buộc không?</summary><p>Không. Nhiều sinh viên học toàn bộ chương trình tại Trung Quốc; 2+2 chỉ áp dụng với các chương trình đủ điều kiện và cần kiểm tra theo ngành.</p></details>
    </div>
  </div>
</section>

'''
text, n = re.subn(
    r'<!-- ===================== FAQ ===================== -->.*?(?=<style id="tns-contact-only-style">)',
    compact_faq,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('Could not compact FAQ section')

INDEX.write_text(text, encoding='utf-8')
print('Homepage compacted and student-life preview added')

# Add/refresh sitemap entry for the student-life page and homepage.
sitemap = SITEMAP.read_text(encoding='utf-8')
student_url = 'https://xjtlu-vietnam.netlify.app/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html'
if student_url not in sitemap:
    sitemap = sitemap.replace('</urlset>', f'  <url><loc>{student_url}</loc><lastmod>{TODAY}</lastmod></url>\n</urlset>')
else:
    sitemap = re.sub(rf'(<loc>{re.escape(student_url)}</loc>\s*<lastmod>)[^<]+', rf'\g<1>{TODAY}', sitemap, count=1)
sitemap = re.sub(r'(<loc>https://xjtlu-vietnam\.netlify\.app/</loc>\s*<lastmod>)[^<]+', rf'\g<1>{TODAY}', sitemap, count=1)
SITEMAP.write_text(sitemap, encoding='utf-8')
print('Sitemap updated')
