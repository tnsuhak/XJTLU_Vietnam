from pathlib import Path
import re

p = Path('index.html')
text = p.read_text(encoding='utf-8')

compact_stories = '''<!-- ===================== STORIES ===================== -->
<section class="section ivory" id="stories">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Câu chuyện & kết quả</div>
      <h2>3 điểm đáng xem về sinh viên XJTLU</h2>
      <p class="lead">Chỉ giữ những ví dụ tiêu biểu trên trang chính; hồ sơ và kết quả chi tiết nằm ở các trang riêng.</p>
    </div>
    <div class="home-lite-grid">
      <div class="home-lite-card"><b>Sinh viên Việt Nam</b><span>Mai Anh Ngô đạt Giải Nhì cuộc thi hùng biện tiếng Trung Hoa Đông 2025 khi tham gia từ XJTLU.</span></div>
      <div class="home-lite-card"><b>Đông Nam Á</b><span>XJTLU công bố cộng đồng sinh viên Indonesia lớn và đang mở rộng kết nối tuyển sinh trong khu vực.</span></div>
      <div class="home-lite-card"><b>Học lên quốc tế</b><span>Dữ liệu 2025 cho thấy tỷ lệ học lên cao với nhiều điểm đến như UCL, Imperial, Oxford, Cambridge và NUS.</span></div>
    </div>
    <div class="home-lite-actions"><a href="/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html">Xem kết quả học lên 2025 →</a><a href="/news/">Xem câu chuyện & tin tức →</a></div>
  </div>
</section>

'''
text, n = re.subn(
    r'<!-- ===================== STORIES ===================== -->.*?(?=<!-- ===================== VIDEO ===================== -->)',
    compact_stories,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('Could not compact stories section')

# Rename navigation/footer label now that #rooms is a broader student-life section.
text = text.replace('href="#rooms">Ký túc xá', 'href="#rooms">Đời sống sinh viên')

# Mobile homepage should not become long again because of four full news cards.
news_style = '''<style id="tns-mobile-news-lite-20260905">
@media(max-width:640px){.tns-news-grid .tns-news-card:nth-child(n+4){display:none}.tns-news-body p{display:none}.tns-news-body h3{font-size:19px;line-height:1.32;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}.tns-news-body{padding:18px}.tns-news-section .section-head{margin-bottom:0}}
</style>
'''
if 'tns-mobile-news-lite-20260905' not in text:
    marker = '<!-- TNS_AUTO_NEWS_START -->'
    if marker not in text:
        raise SystemExit('News marker missing')
    text = text.replace(marker, news_style + marker, 1)

p.write_text(text, encoding='utf-8')
print('Stories and mobile news compacted')
