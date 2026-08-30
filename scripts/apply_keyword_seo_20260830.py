from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

repls = {
    '<title>XJTLU Vietnam (Việt Nam) | Học phí, học bổng & tuyển sinh 2027</title>': '<title>Xi\'an Jiaotong-Liverpool University (XJTLU) | Vietnam 2027</title>',
    '<meta name="description" content="XJTLU Vietnam: thông tin tuyển sinh 2027 dành cho học sinh Việt Nam về học phí XJTLU, học bổng, điều kiện đầu vào, ngành học, ký túc xá và bằng University of Liverpool.">': '<meta name="description" content="Xi\'an Jiaotong-Liverpool University (XJTLU) tại Tô Châu: xếp hạng, học phí, học bổng, điều kiện tuyển sinh 2027, ngành học, ký túc xá và bằng University of Liverpool.">',
    '<meta property="og:title" content="XJTLU Vietnam (Việt Nam) | Học phí, học bổng & tuyển sinh 2027">': '<meta property="og:title" content="Xi\'an Jiaotong-Liverpool University (XJTLU) | Vietnam 2027">',
    '<meta property="og:description" content="XJTLU Vietnam 2027: học phí, học bổng, điều kiện tuyển sinh, ngành học và bằng University of Liverpool dành cho sinh viên Việt Nam.">': '<meta property="og:description" content="XJTLU Vietnam: xếp hạng, học phí, học bổng, tuyển sinh 2027, ngành học và bằng University of Liverpool dành cho sinh viên Việt Nam.">',
    '<meta name="twitter:title" content="XJTLU Vietnam (Việt Nam) | Học phí, học bổng & tuyển sinh 2027">': '<meta name="twitter:title" content="Xi\'an Jiaotong-Liverpool University (XJTLU) | Vietnam 2027">',
    '<meta name="twitter:description" content="XJTLU Vietnam 2027: học phí, học bổng, tuyển sinh và bằng University of Liverpool.">': '<meta name="twitter:description" content="XJTLU Vietnam 2027: ranking, học phí, học bổng, tuyển sinh và bằng University of Liverpool.">',
    '"name": "XJTLU Vietnam (Việt Nam) | Học phí, học bổng & tuyển sinh 2027",': '"name": "Xi\'an Jiaotong-Liverpool University (XJTLU) | Vietnam 2027",',
    '"description": "Thông tin tiếng Việt về XJTLU (Xi\'an Jiaotong-Liverpool University) tại Tô Châu, Trung Quốc: ngành học, học phí, học bổng, ký túc xá và điều kiện tuyển sinh dành cho học sinh Việt Nam.",': '"description": "Thông tin tiếng Việt về Xi\'an Jiaotong-Liverpool University (XJTLU) tại Tô Châu: xếp hạng, ngành học, học phí, học bổng, ký túc xá và điều kiện tuyển sinh 2027.",',
}
for old, new in repls.items():
    if old not in s:
        raise SystemExit(f'Missing expected homepage string: {old[:100]}')
    s = s.replace(old, new, 1)

start = '<!-- TNS_SEO_GUIDES_START -->'
end = '<!-- TNS_SEO_GUIDES_END -->'
if start not in s or end not in s:
    raise SystemExit('SEO guide markers missing')
new_guides = '''<!-- TNS_SEO_GUIDES_START -->
<section class="section ivory tns-seo-guides" id="xjtlu-guides">
  <style>
    .tns-seo-guide-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.tns-seo-guide{display:flex;flex-direction:column;gap:12px;background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:26px;box-shadow:var(--shadow);transition:transform .2s,box-shadow .2s}.tns-seo-guide:hover{transform:translateY(-3px);box-shadow:0 18px 40px rgba(20,33,61,.12)}.tns-seo-guide h3{font-size:21px}.tns-seo-guide p{font-size:14px;color:var(--ink-2);margin:0}.tns-seo-guide .go{margin-top:auto;color:var(--jade);font-weight:800;font-size:14px}.tns-ranking-link{display:inline-block;margin-top:22px;color:var(--jade);font-weight:800;font-size:14px}@media(max-width:1100px){.tns-seo-guide-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:700px){.tns-seo-guide-grid{grid-template-columns:1fr}}
  </style>
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Hướng dẫn 2027</div>
      <h2>Từ du học Trung Quốc đến lựa chọn XJTLU</h2>
      <p class="lead">Bắt đầu bằng bức tranh tổng thể về điều kiện, chi phí, học bổng và visa du học Trung Quốc; sau đó đi sâu vào học phí, tuyển sinh và chương trình tiếng Anh của Xi'an Jiaotong-Liverpool University.</p>
    </div>
    <div class="tns-seo-guide-grid">
      <a class="tns-seo-guide reveal" href="/du-hoc-trung-quoc-2027.html">
        <span class="pill navy">Cẩm nang Trung Quốc</span>
        <h3>Du học Trung Quốc 2027: điều kiện, chi phí, học bổng & visa</h3>
        <p>Tổng quan dành cho học sinh Việt Nam trước khi chọn trường: yêu cầu, ngân sách, học bổng, visa X1/X2 và chương trình tiếng Anh.</p>
        <span class="go">Đọc cẩm nang →</span>
      </a>
      <a class="tns-seo-guide reveal d1" href="/xjtlu-hoc-phi-hoc-bong-2027.html">
        <span class="pill">Học phí · Học bổng</span>
        <h3>Học phí XJTLU 2027 & học bổng</h3>
        <p>Mức học phí, Entry Scholarship, ưu đãi nộp sớm và các khoản chi cần chuẩn bị cho sinh viên Việt Nam.</p>
        <span class="go">Xem hướng dẫn →</span>
      </a>
      <a class="tns-seo-guide reveal d2" href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">
        <span class="pill jade">Tuyển sinh</span>
        <h3>Điều kiện vào XJTLU cho học sinh Việt Nam</h3>
        <p>Yêu cầu THPT, IELTS/TOEFL, chuyển tiếp, hồ sơ và thời gian xét tuyển dành cho ứng viên Việt Nam.</p>
        <span class="go">Xem điều kiện →</span>
      </a>
      <a class="tns-seo-guide reveal d3" href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">
        <span class="pill navy">English-taught</span>
        <h3>Du học Trung Quốc bằng tiếng Anh tại XJTLU</h3>
        <p>Vì sao XJTLU kết hợp môi trường Trung Quốc, chương trình tiếng Anh và bằng cấp gắn với University of Liverpool.</p>
        <span class="go">Tìm hiểu thêm →</span>
      </a>
    </div>
    <a class="tns-ranking-link" href="/xjtlu-ranking-2027.html">Xem XJTLU ranking 2027: QS, THE & ARWU →</a>
  </div>
</section>
<!-- TNS_SEO_GUIDES_END -->'''
left, rest = s.split(start, 1)
_, right = rest.split(end, 1)
s = left + new_guides + right

old_visa = 'Thủ tục visa du học Trung Quốc rất đơn giản và tỷ lệ đậu cao. Sau khi đóng cọc, XJTLU cấp form JW202/DQ để bạn xin visa du học X1 tại Trung tâm tiếp nhận hồ sơ visa Trung Quốc ở Hà Nội hoặc TP.HCM. Sau khi nhập cảnh, trường hỗ trợ khám sức khỏe và đổi sang thẻ cư trú dài hạn. SOS hướng dẫn từng bước và kiểm tra hồ sơ trước khi nộp.'
new_visa = 'Với chương trình học dài hạn, sinh viên thường cần visa X1. Sau khi hoàn tất các bước tuyển sinh, trường cung cấp tài liệu liên quan để bạn chuẩn bị hồ sơ visa theo hướng dẫn hiện hành của cơ quan lãnh sự Trung Quốc. Kết quả visa phụ thuộc hồ sơ và cơ quan xét duyệt; SOS có thể hỗ trợ kiểm tra giấy tờ và quy trình trước khi nộp.'
if old_visa in s:
    s = s.replace(old_visa, new_visa, 1)

old_footer = '<div><h4>Nội dung</h4><ul><li><a href="#information">Giới thiệu</a></li><li><a href="#opportunity">Cơ hội</a></li><li><a href="#major">Ngành học</a></li><li><a href="#tuition">Học phí &amp; học bổng</a></li><li><a href="#rooms">Ký túc xá</a></li></ul></div>'
new_footer = '<div><h4>Nội dung</h4><ul><li><a href="/du-hoc-trung-quoc-2027.html">Du học Trung Quốc 2027</a></li><li><a href="/xjtlu-ranking-2027.html">XJTLU ranking 2027</a></li><li><a href="#information">Giới thiệu</a></li><li><a href="#major">Ngành học</a></li><li><a href="#tuition">Học phí &amp; học bổng</a></li><li><a href="#rooms">Ký túc xá</a></li></ul></div>'
if old_footer not in s:
    raise SystemExit('Footer content block missing')
s = s.replace(old_footer, new_footer, 1)

p.write_text(s, encoding='utf-8')
print('Keyword-demand SEO patch applied to index.html')
