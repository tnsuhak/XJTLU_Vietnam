from pathlib import Path
import re

ROOT = Path('.')
MAIN = ROOT / 'index.html'

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
sub_links = ''.join(f'<a href="{href}">{label}</a>' for label, href in NAV_LINKS)

MAIN_STYLE = '''
<style id="tns-subpage-navigation-20260905">
/* UIS-style navigation: homepage at left, one Menu control at right, direct links to subpages. */
#menu.tns-subpage-menu{
  position:fixed!important;
  top:calc(var(--topbar) + var(--nav))!important;
  right:24px!important;left:auto!important;
  width:min(390px,calc(100vw - 32px))!important;
  max-height:calc(100vh - var(--topbar) - var(--nav) - 18px)!important;
  overflow-y:auto!important;
  display:flex!important;flex-direction:column!important;
  gap:2px!important;padding:12px!important;
  background:#fff!important;border:1px solid var(--line)!important;
  border-radius:0 0 16px 16px!important;
  box-shadow:0 24px 60px rgba(20,33,61,.18)!important;
  transform:translateY(-8px)!important;opacity:0!important;
  pointer-events:none!important;z-index:80!important;
}
#menu.tns-subpage-menu.open{transform:none!important;opacity:1!important;pointer-events:auto!important}
#menu.tns-subpage-menu li{width:100%}
#menu.tns-subpage-menu a{display:block!important;padding:12px 14px!important;border-radius:10px!important;font-size:14px!important;line-height:1.35!important}
#menu.tns-subpage-menu a:hover{background:var(--mist)!important}
.nav-cta>.btn{display:none!important}
.hamburger.tns-menu-toggle{display:flex!important;align-items:center!important;justify-content:center!important;gap:10px!important;width:auto!important;height:44px!important;padding:0 13px!important;border:1px solid var(--line)!important;background:#fff!important;border-radius:12px!important}
.hamburger.tns-menu-toggle b{font-size:14px;font-weight:800;color:var(--navy);line-height:1}
.hamburger.tns-menu-toggle span{width:20px!important;flex:none}
@media(max-width:640px){
  #menu.tns-subpage-menu{left:16px!important;right:16px!important;width:auto!important;padding:10px!important}
  #menu.tns-subpage-menu a{font-size:14px!important;padding:12px!important}
  .hamburger.tns-menu-toggle{height:42px!important;padding:0 11px!important}
}
</style>
'''

SUB_STYLE = '''
<style id="tns-guide-navigation-20260905">
.tns-guide-nav{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--line,#e3e6ec);box-shadow:0 2px 14px rgba(20,33,61,.06)}
.tns-guide-nav__inner{min-height:62px;display:flex;align-items:center;justify-content:space-between;gap:18px}
.tns-guide-nav__brand{color:var(--navy,#14213d)!important;text-decoration:none!important;font-weight:800!important;font-size:16px!important}
.tns-guide-nav__menu{position:relative}
.tns-guide-nav__menu summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:8px;padding:9px 13px;border:1px solid var(--line,#e3e6ec);border-radius:10px;color:var(--navy,#14213d);font-weight:800;font-size:14px;background:#fff;user-select:none}
.tns-guide-nav__menu summary::-webkit-details-marker{display:none}
.tns-guide-nav__menu summary::after{content:'☰';font-size:17px;line-height:1}
.tns-guide-nav__menu[open] summary::after{content:'×';font-size:22px}
.tns-guide-nav__menu nav{position:absolute;right:0;top:calc(100% + 8px);width:min(380px,calc(100vw - 36px));max-height:calc(100vh - 88px);overflow:auto;background:#fff;border:1px solid var(--line,#e3e6ec);border-radius:14px;padding:10px;box-shadow:0 20px 48px rgba(20,33,61,.18)}
.tns-guide-nav__menu nav a{display:block!important;color:var(--navy,#14213d)!important;text-decoration:none!important;font-size:14px!important;font-weight:700!important;line-height:1.35!important;padding:11px 12px!important;border-radius:9px!important}
.tns-guide-nav__menu nav a:hover{background:var(--mist,#eef0f4)!important}
@media(max-width:620px){.tns-guide-nav__inner{min-height:58px}.tns-guide-nav__brand{font-size:15px!important}.tns-guide-nav__menu nav{position:fixed;left:18px;right:18px;top:66px;width:auto;max-height:calc(100vh - 84px)}}
</style>
'''

SUB_HEADER = f'''<header class="tns-guide-nav"><div class="wrap tns-guide-nav__inner"><a class="tns-guide-nav__brand" href="/">XJTLU Việt Nam</a><details class="tns-guide-nav__menu"><summary>Menu</summary><nav aria-label="Các trang hướng dẫn XJTLU">{sub_links}</nav></details></div></header>'''


def update_main():
    text = MAIN.read_text(encoding='utf-8')

    # Left-side brand always returns to homepage, including when this markup is reused.
    text = re.sub(r'<a class="brand" href="[^"]*" aria-label="XJTLU Việt Nam">',
                  '<a class="brand" href="/" aria-label="Trang chủ XJTLU Việt Nam">', text, count=1)

    # Remove consultation actions from the fixed header/top bar. In-page and floating consultation remain untouched.
    text = re.sub(r'\s*<a class="zalo-link" href="#">💬\s*Zalo tư vấn</a>', '', text, count=1)
    text = re.sub(r'\s*<a class="btn btn-outline" href="#admission">.*?</a>', '', text, count=1, flags=re.S)
    text = re.sub(r'\s*<a class="btn btn-zalo zalo-link" href="#">.*?</a>', '', text, count=1, flags=re.S)

    # Replace section-anchor navigation with direct links to useful subpages.
    text, n = re.subn(r'<ul class="menu(?: [^"]*)?" id="menu">.*?</ul>',
                      f'<ul class="menu tns-subpage-menu" id="menu">{menu_items}</ul>',
                      text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit('Homepage menu markup not found')

    # One visible Menu control on the right at all viewport sizes.
    text = re.sub(
        r'<button class="hamburger(?: [^"]*)?" id="hamburger" aria-label="[^"]*" aria-expanded="false"><span></span></button>',
        '<button class="hamburger tns-menu-toggle" id="hamburger" aria-label="Mở menu trang" aria-expanded="false"><b>Menu</b><span></span></button>',
        text, count=1,
    )

    if 'id="tns-subpage-navigation-20260905"' not in text:
        text = text.replace('</head>', MAIN_STYLE + '</head>', 1)

    # Old scroll-spy assumes every menu href is a CSS #selector. It must ignore direct subpage URLs.
    spy_pattern = re.compile(
        r"  // ---- Active section highlighting\n  const links=\[\.\.\.menu\.querySelectorAll\('a'\)\];\n  const sections=links\.map\(a=>document\.querySelector\(a\.getAttribute\('href'\)\)\)\.filter\(Boolean\);\n  const spy=new IntersectionObserver\(entries=>\{.*?\n  sections\.forEach\(s=>spy\.observe\(s\)\);",
        re.S,
    )
    safe_spy = """  // ---- Active section highlighting (only for in-page # anchors)
  const links=[...menu.querySelectorAll('a')];
  const sectionLinks=links.filter(a=>(a.getAttribute('href')||'').startsWith('#'));
  const sections=sectionLinks.map(a=>document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if(sections.length){
    const spy=new IntersectionObserver(entries=>{
      entries.forEach(e=>{if(e.isIntersecting){sectionLinks.forEach(l=>l.classList.toggle('active',l.getAttribute('href')==='#'+e.target.id));}});
    },{rootMargin:'-40% 0px -55% 0px'});
    sections.forEach(s=>spy.observe(s));
  }"""
    text, n = spy_pattern.subn(safe_spy, text, count=1)
    if n == 0 and 'const sectionLinks=links.filter' not in text:
        raise SystemExit('Homepage nav scroll-spy block not found')

    MAIN.write_text(text, encoding='utf-8')


def update_subpage(path: Path):
    text = path.read_text(encoding='utf-8')
    if '<body' not in text:
        return

    if 'id="tns-guide-navigation-20260905"' not in text:
        text = text.replace('</head>', SUB_STYLE + '</head>', 1)

    # Most guide/news pages currently use a simple one-link .top bar. Replace it with the shared navigation.
    text, n = re.subn(r'<div class="top"><div class="wrap">.*?</div></div>', SUB_HEADER, text, count=1, flags=re.S)
    if n == 0 and 'class="tns-guide-nav"' not in text:
        # For a standalone page without the old .top block, add the common header immediately after <body>.
        text = re.sub(r'(<body[^>]*>)', r'\1' + SUB_HEADER, text, count=1)

    path.write_text(text, encoding='utf-8')


update_main()
for path in sorted(list(ROOT.glob('*.html')) + list((ROOT / 'news').glob('*.html'))):
    if path == MAIN:
        continue
    update_subpage(path)

print('Unified XJTLU Vietnam navigation: homepage brand -> /, Menu -> subpages, no header Zalo CTA.')
