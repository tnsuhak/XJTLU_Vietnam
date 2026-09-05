from pathlib import Path
import re
import subprocess

ROOT = Path('.')
INDEX = ROOT / 'index.html'
DETAIL = ROOT / 'university-of-liverpool-vietnam.html'
SITEMAP = ROOT / 'sitemap.xml'
DETAIL_URL = 'https://xjtlu-vietnam.netlify.app/university-of-liverpool-vietnam.html'

HOME_SECTION = r'''<!-- ===================== VIETNAM RELEVANCE ===================== -->
<style id="tns-liverpool-vietnam-home-20260905">
.lv-home-cards .home-lite-card{background:rgba(255,255,255,.065);border-color:rgba(255,255,255,.13);padding:18px 19px}
.lv-home-cards .home-lite-card b{color:#fff;font-size:18px;margin-bottom:5px}
.lv-home-cards .home-lite-card span{color:#c9d1e0;font-size:12.5px;line-height:1.55}
.lv-home-note{margin-top:10px;color:#8f9ab2;font-size:11px;line-height:1.55}
@media(max-width:700px){.lv-home-cards{gap:8px}.lv-home-cards .home-lite-card{padding:14px 15px}.lv-home-cards .home-lite-card b{font-size:16.5px}.lv-home-note{font-size:10.5px}}
</style>
<section class="section deep" id="liverpool-vietnam">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Liverpool × Việt Nam</div>
      <h2>University of Liverpool đang ngày càng gần Việt Nam</h2>
      <p class="lead">Ba kết nối đáng chú ý trong giáo dục, y tế và công nghệ — xem nhanh ở đây, chi tiết ở trang riêng.</p>
    </div>
    <div class="home-lite-grid lv-home-cards">
      <div class="home-lite-card reveal"><b>UK × Việt Nam</b><span>Đối tác Chiến lược Toàn diện · 10/2025</span></div>
      <div class="home-lite-card reveal d1"><b>Liverpool × TP.HCM</b><span>Y tế · giáo dục · khoa học-công nghệ</span></div>
      <div class="home-lite-card reveal d2"><b>University of Liverpool × UMP</b><span>AI · dữ liệu · y tế số · 01/2026</span></div>
    </div>
    <div class="home-lite-actions"><a href="/university-of-liverpool-vietnam.html">Xem Liverpool kết nối với Việt Nam như thế nào →</a></div>
    <p class="lv-home-note">Các hợp tác trên là của Anh/Liverpool/University of Liverpool với Việt Nam, không phải thỏa thuận tuyển sinh trực tiếp của XJTLU.</p>
  </div>
</section>'''

DETAIL_HTML = r'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>University of Liverpool & Việt Nam: giáo dục, AI, y tế | XJTLU Vietnam</title>
<meta name="description" content="University of Liverpool và Việt Nam đang kết nối ra sao? Xem hợp tác UK–Việt Nam, Liverpool–TP.HCM và University of Liverpool–UMP trong giáo dục, AI, dữ liệu và y tế.">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="https://xjtlu-vietnam.netlify.app/university-of-liverpool-vietnam.html">
<meta property="og:type" content="article"><meta property="og:locale" content="vi_VN"><meta property="og:site_name" content="XJTLU Việt Nam"><meta property="og:title" content="University of Liverpool & Việt Nam"><meta property="og:description" content="Ba kết nối nổi bật giữa UK/Liverpool/University of Liverpool và Việt Nam trong giáo dục, y tế, AI và khoa học-công nghệ."><meta property="og:url" content="https://xjtlu-vietnam.netlify.app/university-of-liverpool-vietnam.html">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"University of Liverpool và Việt Nam: kết nối trong giáo dục, AI và y tế","description":"Hợp tác UK–Việt Nam, Liverpool–TP.HCM và University of Liverpool–UMP HCMC","dateModified":"2026-09-05","inLanguage":"vi-VN","mainEntityOfPage":"https://xjtlu-vietnam.netlify.app/university-of-liverpool-vietnam.html","publisher":{"@type":"Organization","name":"TNS Worldwide","url":"https://xjtlu-vietnam.netlify.app/"},"about":[{"@type":"CollegeOrUniversity","name":"University of Liverpool"},{"@type":"CollegeOrUniversity","name":"Xi'an Jiaotong-Liverpool University","alternateName":"XJTLU"}]}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Đây có phải hợp tác trực tiếp giữa XJTLU và Việt Nam không?","acceptedAnswer":{"@type":"Answer","text":"Không. Các sự kiện trên là quan hệ UK–Việt Nam, hợp tác giữa TP.HCM và Vùng Đô thị Liverpool, và hợp tác giữa University of Liverpool với UMP TP.HCM. Chúng không phải thỏa thuận tuyển sinh trực tiếp của XJTLU."}},{"@type":"Question","name":"Vậy vì sao nội dung này liên quan đến XJTLU?","acceptedAnswer":{"@type":"Answer","text":"XJTLU được University of Liverpool và Xi'an Jiaotong University đồng sáng lập và có quan hệ học thuật, bằng cấp và lộ trình 2+2 với University of Liverpool. Vì vậy sự hiện diện ngày càng rõ của Liverpool tại Việt Nam là bối cảnh đáng chú ý với học sinh đang tìm hiểu XJTLU."}},{"@type":"Question","name":"Học XJTLU có bắt buộc phải sang Liverpool không?","acceptedAnswer":{"@type":"Answer","text":"Không. 2+2 là một lộ trình học dành cho các chương trình đủ điều kiện; sinh viên có thể có lựa chọn học toàn bộ chương trình tại Trung Quốc tùy ngành và cấu trúc chương trình."}}]}</script>
<style>
:root{--navy:#14213d;--deep:#0b1630;--gold:#c9a84c;--cream:#faf8f4;--paper:#fff;--mist:#eef0f4;--ink:#171b26;--muted:#667085;--line:#e3e6ec;--jade:#1f6f78}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--cream);color:var(--ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.68}.wrap{width:min(1000px,calc(100% - 36px));margin:auto}.top{background:var(--deep);padding:15px 0}.top a{color:#fff;text-decoration:none;font-weight:750}.hero{background:radial-gradient(900px 480px at 80% 18%,#294d86 0,transparent 62%),linear-gradient(135deg,var(--deep),#172b4d);color:#fff;padding:68px 0 80px}.eyebrow{color:var(--gold);font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}.hero h1{font-family:Georgia,serif;font-size:clamp(35px,6vw,58px);line-height:1.1;margin:10px 0 15px;max-width:860px}.hero p{margin:0;color:#d8deeb;font-size:17px;max-width:800px}.updated{margin-top:16px;color:#aeb8ca;font-size:12px}.answer{margin-top:-38px;background:#fff;border:1px solid var(--line);box-shadow:0 20px 55px rgba(20,33,61,.12);padding:24px 26px;position:relative}.answer small{display:block;color:var(--jade);font-size:11px;font-weight:850;letter-spacing:.09em;text-transform:uppercase}.answer h2{font-family:Georgia,serif;color:var(--navy);font-size:25px;margin:6px 0 9px}.answer p{margin:0;color:#4b5565}.main{padding:58px 0 76px}.section{margin-bottom:54px}.section h2{font-family:Georgia,serif;color:var(--navy);font-size:30px;line-height:1.22;margin:0 0 12px}.lead{color:#4b5565;max-width:850px;margin:0 0 20px}.timeline{display:grid;gap:16px;position:relative}.timeline::before{content:"";position:absolute;left:31px;top:18px;bottom:18px;width:1px;background:#d7c98e}.event{display:grid;grid-template-columns:64px 1fr;gap:16px;position:relative}.event-dot{width:14px;height:14px;border-radius:50%;background:var(--gold);border:4px solid #fff;box-shadow:0 0 0 1px #d7c98e;margin:24px auto 0;z-index:1}.event-card{background:#fff;border:1px solid var(--line);padding:23px 24px}.event-date{display:inline-block;background:#f3ead0;color:#7b6220;border-radius:999px;padding:5px 9px;font-size:11px;font-weight:850;letter-spacing:.05em}.event-card h3{color:var(--navy);font-size:20px;margin:10px 0 5px}.event-tag{color:#8a6d22;font-size:12px;font-weight:800}.event-card p{color:#4b5565;font-size:14px;margin:10px 0 0}.src{display:inline-block;margin-top:11px;color:var(--jade);font-size:12px;font-weight:800;text-decoration:none}.src:hover{text-decoration:underline}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.card{background:#fff;border:1px solid var(--line);padding:21px}.card h3{color:var(--navy);font-size:17px;margin:0 0 7px}.card p{font-size:13.5px;color:#4b5565;margin:0}.note{background:#fff7df;border-left:4px solid var(--gold);padding:18px 20px;color:#596273;font-size:14px}.faq details{background:#fff;border-bottom:1px solid var(--line);padding:16px 19px}.faq summary{font-weight:800;color:var(--navy);cursor:pointer}.faq p{font-size:14px;color:#596273}.related{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.related a{background:#fff;border:1px solid var(--line);padding:17px;color:var(--navy);text-decoration:none;font-weight:800}.related span{display:block;color:var(--muted);font-size:12px;font-weight:500;margin-top:5px}.sources{border-top:1px solid var(--line);padding-top:15px;color:#8a92a2;font-size:12px;line-height:1.75}.sources a{color:#667085}.cta{background:var(--navy);color:#fff;padding:32px 28px;text-align:center}.cta h2{color:#fff;margin:0 0 7px}.cta p{margin:0;color:#d7ddea}.btn{display:inline-block;margin-top:13px;background:var(--gold);color:#17130a;text-decoration:none;padding:11px 19px;border-radius:999px;font-weight:800}
@media(max-width:760px){.hero{padding:52px 0 64px}.hero p{font-size:15px}.answer{padding:20px 19px}.answer h2{font-size:22px}.main{padding:48px 0 62px}.section{margin-bottom:44px}.section h2{font-size:27px}.grid,.related{grid-template-columns:1fr}.timeline::before{left:20px}.event{grid-template-columns:42px 1fr;gap:10px}.event-dot{margin-top:22px}.event-card{padding:18px 17px}.event-card h3{font-size:18px}}
</style>
</head>
<body>
<div class="top"><div class="wrap"><a href="/">← XJTLU Việt Nam</a></div></div>
<header class="hero"><div class="wrap"><div class="eyebrow">Liverpool × Việt Nam</div><h1>University of Liverpool đang kết nối với Việt Nam như thế nào?</h1><p>Trong 2025–2026, các mối liên kết giữa Anh, Liverpool và Việt Nam mở rộng rõ rệt trong giáo dục, y tế, khoa học-công nghệ, dữ liệu và AI.</p><div class="updated">Cập nhật: 05/09/2026</div></div></header>
<div class="wrap"><section class="answer"><small>Điểm cần hiểu trước</small><h2>Đây không phải là “hợp tác trực tiếp XJTLU × Việt Nam”</h2><p>Ba sự kiện dưới đây là quan hệ <b>UK–Việt Nam</b>, hợp tác giữa <b>TP.HCM và Vùng Đô thị Liverpool</b>, và hợp tác giữa <b>University of Liverpool với UMP TP.HCM</b>. Chúng đáng chú ý với người tìm hiểu XJTLU vì XJTLU có quan hệ học thuật và bằng cấp sâu với University of Liverpool — nhưng không nên hiểu thành một thỏa thuận tuyển sinh trực tiếp của XJTLU tại Việt Nam.</p></section></div>
<main class="main"><div class="wrap">
<section class="section"><h2>Ba mốc kết nối đáng chú ý</h2><p class="lead">Từ quan hệ cấp quốc gia đến hợp tác thành phố và đại học, Liverpool đang xuất hiện rõ hơn trong hệ sinh thái giáo dục – đổi mới của Việt Nam.</p><div class="timeline">
<article class="event"><div class="event-dot"></div><div class="event-card"><span class="event-date">29/10/2025</span><h3>UK × Việt Nam</h3><div class="event-tag">Đối tác Chiến lược Toàn diện</div><p>Việt Nam và Vương quốc Anh nâng cấp quan hệ lên Đối tác Chiến lược Toàn diện, với các trụ cột hợp tác bao gồm thương mại, giáo dục, khoa học-công nghệ và nhiều lĩnh vực khác.</p><a class="src" href="https://www.gov.uk/government/news/joint-declaration-on-the-elevation-of-uk-viet-nam-relations-to-comprehensive-strategic-partnership" target="_blank" rel="noopener">Nguồn: Chính phủ Anh ↗</a></div></article>
<article class="event"><div class="event-dot"></div><div class="event-card"><span class="event-date">30/10/2025</span><h3>Liverpool × TP. Hồ Chí Minh</h3><div class="event-tag">Y tế · giáo dục – đào tạo · khoa học – công nghệ</div><p>TP.HCM và Vùng Đô thị Liverpool ký Biên bản ghi nhớ hợp tác trong ba nhóm lĩnh vực trên, mở rộng kết nối giữa hai địa phương.</p><a class="src" href="https://mofahcm.gov.vn/tin-tuc/hoat-dong-doi-ngoai-tai-tphcm/thanh-pho-ho-chi-minh-ky-ket-ban-ghi-nho-hop-tac-voi-vung-do-thi-liverpool-vuong-quoc-anh" target="_blank" rel="noopener">Nguồn: Sở Ngoại vụ TP.HCM ↗</a></div></article>
<article class="event"><div class="event-dot"></div><div class="event-card"><span class="event-date">30/01/2026</span><h3>University of Liverpool × UMP TP.HCM</h3><div class="event-tag">Data Science · AI · Digital Health · nghiên cứu chung</div><p>University of Liverpool và Đại học Y Dược TP.HCM (UMP HCMC) ký MoU cho hợp tác dài hạn, gồm nghiên cứu chung về y tế công cộng, y tế số, tin học y sinh, trao đổi chuyên môn và đổi mới AI – dữ liệu cho chăm sóc sức khỏe.</p><a class="src" href="https://news.liverpool.ac.uk/2026/01/30/liverpool-partners-with-university-of-medicine-and-pharmacy-at-ho-chi-minh-city/" target="_blank" rel="noopener">Nguồn: University of Liverpool ↗</a></div></article>
</div></section>
<section class="section"><h2>Vì sao điều này đáng chú ý với học sinh Việt Nam?</h2><div class="grid"><div class="card"><h3>Liverpool không còn quá xa Việt Nam</h3><p>Quan hệ địa phương và đại học đang tạo thêm điểm chạm giữa Liverpool và Việt Nam trong những lĩnh vực có giá trị học thuật thực tế.</p></div><div class="card"><h3>AI · dữ liệu · y tế là lĩnh vực thật</h3><p>Hợp tác UMP tập trung vào dữ liệu, AI và y tế số — những chủ đề gần với các nhóm ngành công nghệ và khoa học sự sống mà nhiều sinh viên quốc tế quan tâm.</p></div><div class="card"><h3>Hệ sinh thái Liverpool có ý nghĩa với XJTLU</h3><p>XJTLU được University of Liverpool và Xi'an Jiaotong University đồng sáng lập. Vì vậy bối cảnh Liverpool mở rộng kết nối tại Việt Nam là một điểm đáng theo dõi, dù không phải cam kết việc làm hay tuyển sinh.</p></div></div></section>
<section class="section"><h2>XJTLU liên quan như thế nào?</h2><p class="lead">Điểm kết nối không nằm ở việc XJTLU ký ba thỏa thuận trên, mà ở quan hệ học thuật của XJTLU với University of Liverpool.</p><div class="note"><b>Hiểu đơn giản:</b> sinh viên XJTLU học trong mô hình đại học Anh–Trung gắn với University of Liverpool. Tùy chương trình và khi đáp ứng yêu cầu tốt nghiệp, sinh viên có cấu trúc bằng cấp liên quan đến University of Liverpool; một số ngành còn có lộ trình 2+2 sang Liverpool. Vì vậy “Liverpool × Việt Nam” là bối cảnh bổ sung cho câu chuyện XJTLU, không phải bằng chứng rằng XJTLU có thỏa thuận trực tiếp với Việt Nam.</div></section>
<section class="section"><h2>Hỏi nhanh</h2><div class="faq"><details><summary>Đây có phải hợp tác trực tiếp giữa XJTLU và Việt Nam không?</summary><p>Không. Các hợp tác nêu trên thuộc UK–Việt Nam, TP.HCM–Liverpool và University of Liverpool–UMP HCMC.</p></details><details><summary>Vậy vì sao trang XJTLU Việt Nam lại giới thiệu?</summary><p>Vì XJTLU được University of Liverpool và Xi'an Jiaotong University đồng sáng lập, có quan hệ học thuật và lộ trình bằng cấp/2+2 gắn với Liverpool. Đây là bối cảnh có ích cho học sinh Việt Nam khi đánh giá mô hình của XJTLU.</p></details><details><summary>Học XJTLU có bắt buộc sang Liverpool không?</summary><p>Không. 2+2 là lựa chọn học tập của các chương trình đủ điều kiện; cấu trúc cụ thể cần kiểm tra theo ngành.</p></details></div></section>
<section class="section"><h2>Xem tiếp</h2><div class="related"><a href="/xjtlu-2plus2-liverpool.html">Bằng Liverpool & 2+2<span>4+0, 2+2, học phí và điều kiện</span></a><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Học bằng tiếng Anh tại XJTLU<span>Vì sao có thể học đại học ở Trung Quốc bằng tiếng Anh</span></a><a href="/xjtlu-nganh-hoc-nghe-nghiep.html">Ngành học & nghề nghiệp<span>AI, Data, Business, Life Sciences và các nhóm ngành khác</span></a></div></section>
<div class="sources"><b>Thông tin nguồn:</b> UK Government, Sở Ngoại vụ TP.HCM và University of Liverpool. Các đường dẫn trên đi tới đúng trang thông tin của từng sự kiện. Trang này giải thích ý nghĩa trong bối cảnh XJTLU; không mô tả các hợp tác trên như thỏa thuận trực tiếp của XJTLU.</div>
<section class="cta"><h2>Muốn xem XJTLU có phù hợp với bạn?</h2><p>Kiểm tra ngành học, điều kiện 2027 và lộ trình 2+2 trước khi quyết định.</p><a class="btn" href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Xem điều kiện tuyển sinh 2027 →</a></section>
</div></main>
</body>
</html>'''


def replace_home_section():
    text = INDEX.read_text(encoding='utf-8')
    pattern = re.compile(r'<!-- ===================== VIETNAM RELEVANCE ===================== -->.*?(?=<!-- ===================== PROGRAMMES ===================== -->)', re.S)
    text, n = pattern.subn(HOME_SECTION + '\n\n', text, count=1)
    if n != 1:
        raise SystemExit('Vietnam relevance section not found')
    INDEX.write_text(text, encoding='utf-8')


def write_detail():
    DETAIL.write_text(DETAIL_HTML, encoding='utf-8')


def update_sitemap():
    text = SITEMAP.read_text(encoding='utf-8')
    if DETAIL_URL not in text:
        block = f'''  <url>\n    <loc>{DETAIL_URL}</loc>\n    <lastmod>2026-09-05</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.65</priority>\n  </url>\n'''
        text = text.replace('</urlset>', block + '</urlset>')
        SITEMAP.write_text(text, encoding='utf-8')


def apply_shared_nav():
    # The shared navigation generator runs before this script in the workflow.
    # Run it once more so the newly-created detail page receives the same header/menu.
    subprocess.run(['python', 'scripts/unify_site_navigation_20260905.py'], check=True)


def add_menu_link_everywhere():
    root_pages = list(ROOT.glob('*.html'))
    news_pages = list((ROOT / 'news').glob('*.html')) if (ROOT / 'news').exists() else []
    for path in root_pages + news_pages:
        text = path.read_text(encoding='utf-8')
        if '/university-of-liverpool-vietnam.html' in text:
            continue
        # Visible mega-menu: place the Vietnam connection guide next to the Liverpool/2+2 guide.
        text = text.replace(
            '<a href="/xjtlu-2plus2-liverpool.html">Bằng University of Liverpool & lộ trình 2+2</a><a href="/xjtlu-ranking-2027.html">Xếp hạng XJTLU</a>',
            '<a href="/xjtlu-2plus2-liverpool.html">Bằng University of Liverpool & lộ trình 2+2</a><a href="/university-of-liverpool-vietnam.html">Liverpool & Việt Nam</a><a href="/xjtlu-ranking-2027.html">Xếp hạng XJTLU</a>'
        )
        # Hidden legacy homepage list, retained for backwards compatibility.
        text = text.replace(
            '<li><a href="/xjtlu-2plus2-liverpool.html">2+2 & University of Liverpool</a></li><li><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html">Đời sống sinh viên</a></li>',
            '<li><a href="/xjtlu-2plus2-liverpool.html">2+2 & University of Liverpool</a></li><li><a href="/university-of-liverpool-vietnam.html">Liverpool & Việt Nam</a></li><li><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html">Đời sống sinh viên</a></li>'
        )
        path.write_text(text, encoding='utf-8')


replace_home_section()
write_detail()
update_sitemap()
apply_shared_nav()
add_menu_link_everywhere()
print('Added compact Liverpool × Vietnam homepage block and detailed University of Liverpool × Vietnam guide.')
