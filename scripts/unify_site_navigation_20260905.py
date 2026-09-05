from pathlib import Path
import re

ROOT = Path('.')
MAIN = ROOT / 'index.html'
STUDENT_LIFE = ROOT / 'xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html'

# Keep the legacy list in the homepage DOM for backwards compatibility, but the
# visible navigation is the same grouped full-width menu used by XJTLU Korea.
NAV_LINKS = [
    ('Trang chủ', '/'),
    ('Tuyển sinh 2027', '/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html'),
    ('Học phí & học bổng', '/xjtlu-hoc-phi-hoc-bong-2027.html'),
    ('Ngành học & nghề nghiệp', '/xjtlu-nganh-hoc-nghe-nghiep.html'),
    ('2+2 & University of Liverpool', '/xjtlu-2plus2-liverpool.html'),
    ('Đời sống sinh viên', '/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html'),
    ('Học bằng tiếng Anh', '/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html'),
    ('XJTLU ranking', '/xjtlu-ranking-2027.html'),
    ('Kết quả học lên', '/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html'),
    ('Du học Trung Quốc 2027', '/du-hoc-trung-quoc-2027.html'),
    ('Tin tức', '/news/'),
]
menu_items = ''.join(f'<li><a href="{href}">{label}</a></li>' for label, href in NAV_LINKS)

GLOBAL_STYLE = r'''
<style id="tns-global-menu-vietnam-20260905">
/* XJTLU Korea-style full-width grouped menu */
.tns-global-menu-btn{display:inline-flex!important;align-items:center;justify-content:center;gap:8px;background:#fff!important;border:1px solid #d9dde6!important;color:#14213d!important;padding:9px 13px!important;border-radius:4px!important;font-family:inherit!important;font-size:13.5px!important;font-weight:800!important;cursor:pointer!important;white-space:nowrap!important;line-height:1!important;height:42px!important;width:auto!important}
.tns-global-menu-btn:hover,.tns-global-menu-btn[aria-expanded="true"]{background:#14213d!important;color:#fff!important;border-color:#14213d!important}
.tns-global-menu-icon{font-size:15px;font-weight:400;line-height:1}
.tns-site-menu{display:none;position:fixed;left:0;right:0;z-index:190;background:#fff;color:#262d40;border-top:1px solid rgba(20,33,61,.1);box-shadow:0 24px 55px rgba(10,18,34,.22);overflow-y:auto}
.tns-site-menu.tns-main-menu{top:calc(var(--topbar,36px) + var(--nav,70px));max-height:calc(100vh - var(--topbar,36px) - var(--nav,70px))}
.tns-site-menu.tns-sub-menu{top:62px;max-height:calc(100vh - 62px)}
.tns-site-menu.open{display:block}
.tns-site-menu-inner{max-width:1200px;margin:0 auto;padding:28px 40px 34px}
.tns-site-menu-head{display:flex;align-items:flex-start;justify-content:space-between;gap:20px;padding-bottom:18px;border-bottom:1px solid #e4e7ec;background:#fff;color:#14213d;min-height:0}
.tns-site-menu-headcopy>span{display:block;color:#9a7827;font-size:10px;font-weight:800;letter-spacing:.13em;margin-bottom:4px}
.tns-site-menu-head h2{font-family:inherit!important;font-size:25px!important;line-height:1.3!important;margin:0!important;color:#14213d!important}
.tns-site-menu-head p{margin:6px 0 0!important;color:#6a7283!important;font-size:13px!important}
.tns-site-menu-close{border:1px solid #d9dde6!important;background:#fff!important;color:#14213d!important;width:38px!important;height:38px!important;border-radius:0!important;cursor:pointer!important;font-size:17px!important;line-height:1!important;flex:none}
.tns-site-menu-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px 30px;padding-top:24px}
.tns-site-menu-group{min-width:0;padding:0;border:0}
.tns-site-menu-group h3{font-family:inherit!important;font-size:16px!important;color:#14213d!important;margin:0 0 7px!important;border-bottom:2px solid #14213d!important}
.tns-site-menu-group h3 a{display:flex!important;align-items:baseline;justify-content:space-between;gap:10px;text-decoration:none!important;color:#14213d!important;padding:0 2px 10px!important;font-weight:800!important}
.tns-site-menu-group h3 a:hover{color:#9a7827!important}
.tns-site-menu-group h3 small{font-size:10.5px!important;font-weight:700!important;color:#9a7827!important;white-space:nowrap!important}
.tns-site-menu-group>a{display:block!important;text-decoration:none!important;color:#4f596e!important;font-size:14px!important;font-weight:600!important;line-height:1.45!important;padding:8px 2px!important;border-bottom:1px solid #eeeae1!important}
.tns-site-menu-group>a:hover{color:#9a7827!important}
.tns-site-menu-group>p{font-size:13px!important;line-height:1.65!important;color:#747c8c!important;margin:10px 2px 0!important}
.tns-guide-nav{position:sticky;top:0;z-index:60;background:#fff;border-bottom:1px solid #e3e6ec;box-shadow:0 2px 14px rgba(20,33,61,.06)}
.tns-guide-nav__inner{width:min(1120px,calc(100% - 36px));margin:auto;min-height:62px;display:flex;align-items:center;justify-content:space-between;gap:18px}
.tns-guide-nav__brand{color:#14213d!important;text-decoration:none!important;font-weight:850!important;font-size:16px!important}
/* Homepage legacy section list is intentionally hidden; the grouped menu is the only visible nav list. */
#nav nav{display:none!important}
#nav .nav-cta>.btn{display:none!important}
#nav .tns-global-menu-btn{display:inline-flex!important}
@media(max-width:960px){
  .tns-site-menu-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .tns-site-menu-inner{padding:22px 20px 30px}
}
@media(max-width:620px){
  .tns-site-menu-grid{grid-template-columns:1fr;gap:22px}
  .tns-site-menu-head h2{font-size:22px!important}
  .tns-site-menu-head p{font-size:12px!important}
  .tns-site-menu-inner{padding:20px 18px 28px}
  .tns-global-menu-btn{height:40px!important;padding:8px 11px!important;font-size:13px!important}
  .tns-guide-nav__inner{min-height:58px}
  .tns-site-menu.tns-sub-menu{top:58px;max-height:calc(100vh - 58px)}
}
</style>
'''

MEGA_INNER = r'''
<div class="tns-site-menu-inner">
  <div class="tns-site-menu-head">
    <div class="tns-site-menu-headcopy"><span>XJTLU VIỆT NAM</span><h2>Menu</h2><p>Trang chính và các hướng dẫn chi tiết được nhóm theo chủ đề.</p></div>
    <button type="button" class="tns-site-menu-close" onclick="closeSiteMenu()" aria-label="Đóng menu">✕</button>
  </div>
  <div class="tns-site-menu-grid">
    <section class="tns-site-menu-group"><h3><a href="/">Giới thiệu XJTLU <small>Trang chính →</small></a></h3><a href="/xjtlu-2plus2-liverpool.html">Bằng University of Liverpool & lộ trình 2+2</a><a href="/xjtlu-ranking-2027.html">Xếp hạng XJTLU</a></section>
    <section class="tns-site-menu-group"><h3><a href="/xjtlu-nganh-hoc-nghe-nghiep.html">Ngành học & nghề nghiệp <small>Xem chi tiết →</small></a></h3><a href="/xjtlu-nganh-hoc-nghe-nghiep.html">Ngành học, nghề nghiệp & lựa chọn chương trình</a><a href="/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html">Kết quả học lên sau tốt nghiệp</a></section>
    <section class="tns-site-menu-group"><h3><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí & học bổng <small>2027 →</small></a></h3><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí, học bổng & các mốc quan trọng 2027</a></section>
    <section class="tns-site-menu-group"><h3><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html">Đời sống sinh viên <small>Xem chi tiết →</small></a></h3><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html#the-thao">Thể thao & cơ sở thể thao</a><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html#cau-lac-bo">Câu lạc bộ & tổ chức sinh viên</a><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html#video">Video đời sống XJTLU</a></section>
    <section class="tns-site-menu-group"><h3><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Tuyển sinh 2027 <small>Xem chi tiết →</small></a></h3><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Điều kiện dành cho học sinh Việt Nam</a></section>
    <section class="tns-site-menu-group"><h3><a href="/du-hoc-trung-quoc-2027.html">Du học Trung Quốc <small>2027 →</small></a></h3><a href="/du-hoc-trung-quoc-2027.html">Hướng dẫn du học Trung Quốc 2027</a><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Học đại học bằng tiếng Anh tại XJTLU</a></section>
    <section class="tns-site-menu-group"><h3><a href="/news/">Tin tức XJTLU <small>Xem tin →</small></a></h3><p>Tin chính thức đáng chú ý được chọn lọc và tóm tắt bằng tiếng Việt.</p></section>
  </div>
</div>
'''

MEGA_MAIN = '<!-- TNS_GLOBAL_MENU_START --><div id="siteMenu" class="tns-site-menu tns-main-menu" aria-label="Menu XJTLU Việt Nam" aria-hidden="true">' + MEGA_INNER + '</div><!-- TNS_GLOBAL_MENU_END -->'
MEGA_SUB = '<!-- TNS_GLOBAL_MENU_START --><div id="siteMenu" class="tns-site-menu tns-sub-menu" aria-label="Menu XJTLU Việt Nam" aria-hidden="true">' + MEGA_INNER + '</div><!-- TNS_GLOBAL_MENU_END -->'

GLOBAL_SCRIPT = r'''
<!-- TNS_GLOBAL_MENU_SCRIPT_START -->
<script id="tns-global-menu-script-20260905">
function setSiteMenuOpen(open){
  var menu=document.getElementById('siteMenu');
  var buttons=document.querySelectorAll('.tns-global-menu-btn');
  if(!menu)return;
  menu.classList.toggle('open',open);
  menu.setAttribute('aria-hidden',open?'false':'true');
  buttons.forEach(function(btn){
    btn.setAttribute('aria-expanded',open?'true':'false');
    var icon=btn.querySelector('.tns-global-menu-icon');
    if(icon)icon.textContent=open?'✕':'☰';
  });
}
function openSiteMenu(){var menu=document.getElementById('siteMenu');setSiteMenuOpen(!(menu&&menu.classList.contains('open')));}
function closeSiteMenu(){setSiteMenuOpen(false);}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeSiteMenu();});
document.addEventListener('click',function(e){
  var menu=document.getElementById('siteMenu');
  if(menu&&menu.classList.contains('open')&&!e.target.closest('#siteMenu')&&!e.target.closest('.tns-global-menu-btn'))closeSiteMenu();
});
document.addEventListener('DOMContentLoaded',function(){document.querySelectorAll('#siteMenu a').forEach(function(a){a.addEventListener('click',closeSiteMenu);});});
</script>
<!-- TNS_GLOBAL_MENU_SCRIPT_END -->
'''

SUB_HEADER = r'''<header class="tns-guide-nav"><div class="tns-guide-nav__inner"><a class="tns-guide-nav__brand" href="/">XJTLU Việt Nam</a><button type="button" class="tns-global-menu-btn" onclick="openSiteMenu()" aria-controls="siteMenu" aria-expanded="false">Menu <span class="tns-global-menu-icon">☰</span></button></div></header>'''

VIDEO_STYLE = r'''
<style id="tns-studentlife-video-20260905">
.studentlife-video-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px}
.studentlife-video-card{background:#0e1a2e;border-radius:14px;overflow:hidden;box-shadow:0 16px 34px rgba(14,26,46,.15)}
.studentlife-video-frame{position:relative;padding-top:56.25%;background:#000}
.studentlife-video-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.studentlife-video-copy{padding:17px 18px 19px;color:#d9e0ec}
.studentlife-video-copy b{display:block;color:#fff;font-size:14px;line-height:1.45;margin-bottom:6px}
.studentlife-video-copy p{font-size:12.5px;line-height:1.6;margin:0 0 9px;color:#bfc8d8}
.studentlife-video-copy a{font-size:12px;font-weight:800;color:#e8d9a8;text-decoration:none}
@media(max-width:850px){.studentlife-video-grid{grid-template-columns:1fr}}
</style>
'''

VIDEO_SECTION = r'''
<section class="section" id="video"><h2>Video: xem đời sống XJTLU thực tế</h2><p class="lead">Các video đã dùng trên trang XJTLU Việt Nam được giữ lại ở trang đời sống sinh viên, cùng video về cơ sở thể thao Taicang.</p><div class="studentlife-video-grid">
  <article class="studentlife-video-card"><div class="studentlife-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/XciLskXWwIU" title="Trải nghiệm sinh viên quốc tế tại XJTLU" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div><div class="studentlife-video-copy"><b>Trải nghiệm sinh viên quốc tế tại XJTLU</b><p>Không khí học tập và trải nghiệm thực tế của sinh viên quốc tế.</p><a href="https://www.youtube.com/watch?v=XciLskXWwIU" target="_blank" rel="noopener">Mở trên YouTube ↗</a></div></article>
  <article class="studentlife-video-card"><div class="studentlife-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/T8g0zoI9rO4" title="Cuộc sống sinh viên tại XJTLU" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div><div class="studentlife-video-copy"><b>Cuộc sống sinh viên tại XJTLU</b><p>Một góc nhìn trực quan hơn về môi trường và sinh hoạt của sinh viên.</p><a href="https://www.youtube.com/watch?v=T8g0zoI9rO4" target="_blank" rel="noopener">Mở trên YouTube ↗</a></div></article>
  <article class="studentlife-video-card"><div class="studentlife-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/nVirGEvdcT8" title="Cơ sở thể thao XJTLU Taicang" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div><div class="studentlife-video-copy"><b>Cơ sở thể thao tại Taicang (XEC)</b><p>Xem trực tiếp không gian và cơ sở thể thao của khuôn viên Taicang.</p><a href="https://www.youtube.com/watch?v=nVirGEvdcT8" target="_blank" rel="noopener">Mở trên YouTube ↗</a></div></article>
</div></section>
'''


def strip_old_injections(text: str) -> str:
    text = re.sub(r'\n?<style id="tns-subpage-navigation-20260905">.*?</style>\n?', '\n', text, flags=re.S)
    text = re.sub(r'\n?<style id="tns-guide-navigation-20260905">.*?</style>\n?', '\n', text, flags=re.S)
    text = re.sub(r'\n?<style id="tns-global-menu-vietnam-20260905">.*?</style>\n?', '\n', text, flags=re.S)
    text = re.sub(r'\n?<!-- TNS_GLOBAL_MENU_START -->.*?<!-- TNS_GLOBAL_MENU_END -->\n?', '\n', text, flags=re.S)
    text = re.sub(r'\n?<!-- TNS_GLOBAL_MENU_SCRIPT_START -->.*?<!-- TNS_GLOBAL_MENU_SCRIPT_END -->\n?', '\n', text, flags=re.S)
    return text


def update_student_life():
    if not STUDENT_LIFE.exists():
        raise SystemExit('Student-life guide not found')
    text = STUDENT_LIFE.read_text(encoding='utf-8')
    text = re.sub(r'\n?<style id="tns-studentlife-video-20260905">.*?</style>\n?', '\n', text, flags=re.S)
    text = re.sub(r'<section class="section" id="video">.*?</section>', '', text, flags=re.S)
    text = text.replace('<section class="section"><h2>Thể thao tại XJTLU</h2>', '<section class="section" id="the-thao"><h2>Thể thao tại XJTLU</h2>', 1)
    text = text.replace('<section class="section"><h2>Câu lạc bộ và tổ chức sinh viên</h2>', '<section class="section" id="cau-lac-bo"><h2>Câu lạc bộ và tổ chức sinh viên</h2>', 1)
    # Preserve the former homepage student videos on the detail page; add the Korea sports-facilities video as well.
    anchor = '<section class="section"><h2>Sự kiện sinh viên</h2>'
    if anchor not in text:
        raise SystemExit('Student-life events anchor not found')
    text = text.replace(anchor, VIDEO_SECTION + '\n' + anchor, 1)
    text = text.replace('</head>', VIDEO_STYLE + '</head>', 1)
    STUDENT_LIFE.write_text(text, encoding='utf-8')


def update_main():
    text = strip_old_injections(MAIN.read_text(encoding='utf-8'))
    text = re.sub(r'<a class="brand" href="[^"]*" aria-label="[^"]*">', '<a class="brand" href="/" aria-label="Trang chủ XJTLU Việt Nam">', text, count=1)
    text = re.sub(r'\s*<a class="zalo-link" href="#">💬\s*Zalo tư vấn</a>', '', text, count=1)
    text = re.sub(r'\s*<a class="btn btn-outline" href="#admission">.*?</a>', '', text, count=1, flags=re.S)
    text = re.sub(r'\s*<a class="btn btn-zalo zalo-link" href="#">.*?</a>', '', text, count=1, flags=re.S)

    text, n = re.subn(r'<ul class="menu(?: [^"]*)?" id="menu">.*?</ul>', f'<ul class="menu" id="menu">{menu_items}</ul>', text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit('Homepage legacy menu markup not found')

    button = '<button type="button" class="tns-global-menu-btn" onclick="openSiteMenu()" aria-controls="siteMenu" aria-expanded="false">Menu <span class="tns-global-menu-icon">☰</span></button>'
    text, n = re.subn(r'<button class="hamburger(?: [^"]*)?" id="hamburger"[^>]*>.*?</button>', button, text, count=1, flags=re.S)
    if n == 0:
        # idempotent path when the Korea-style button already exists
        text = re.sub(r'<button type="button" class="tns-global-menu-btn".*?</button>', button, text, count=1, flags=re.S)

    # Disable the legacy mobile dropdown JS so only the Korea-style full menu controls the header.
    text = re.sub(r'\n\s*// ---- Mobile menu.*?\n\s*// ---- Reveal on scroll', '\n\n  // ---- Korea-style global menu replaces the legacy dropdown\n\n  // ---- Reveal on scroll', text, count=1, flags=re.S)

    text = text.replace('</head>', GLOBAL_STYLE + '</head>', 1)
    if '<main id="main-content">' not in text:
        raise SystemExit('Homepage main-content anchor not found')
    text = text.replace('<main id="main-content">', MEGA_MAIN + '\n<main id="main-content">', 1)
    text = text.replace('</body>', GLOBAL_SCRIPT + '</body>', 1)
    MAIN.write_text(text, encoding='utf-8')


def update_subpage(path: Path):
    text = strip_old_injections(path.read_text(encoding='utf-8'))
    if '<body' not in text:
        return
    text = re.sub(r'<header class="tns-guide-nav">.*?</header>', '', text, count=1, flags=re.S)
    # Remove the old simple top/back bar where present; the shared header replaces it.
    text = re.sub(r'<div class="top"><div class="wrap">.*?</div></div>', '', text, count=1, flags=re.S)
    text = text.replace('</head>', GLOBAL_STYLE + '</head>', 1)
    text = re.sub(r'(<body[^>]*>)', r'\1' + SUB_HEADER + MEGA_SUB, text, count=1)
    text = text.replace('</body>', GLOBAL_SCRIPT + '</body>', 1)
    path.write_text(text, encoding='utf-8')


# Add/restore media first, then apply the same shared navigation to every HTML page.
update_student_life()
update_main()
for path in sorted(list(ROOT.glob('*.html')) + list((ROOT / 'news').glob('*.html'))):
    if path == MAIN:
        continue
    update_subpage(path)

print('Applied XJTLU Korea-style mega menu and restored student-life YouTube videos on the Vietnam preview.')
