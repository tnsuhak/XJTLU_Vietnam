from pathlib import Path
import re

STYLE_ID = "tns-spacing-compact-20260908"
STYLE_RE = re.compile(rf'\n?<style id="{STYLE_ID}">.*?</style>\n?', re.S)

HOME_STYLE = f'''<style id="{STYLE_ID}">
/* Tighter site-wide vertical rhythm. Keep content readable while reducing empty space. */
.section{{padding:clamp(52px,6vw,82px) 0!important}}
.section-head{{margin-bottom:30px!important}}
@media(max-width:900px){{
  .section{{padding:32px 0!important}}
  body>.section+.section{{padding-top:18px!important}}
  .section-head{{margin-bottom:18px!important}}
  .tns-news-top{{margin-bottom:18px!important}}
  #faq{{padding-bottom:22px!important}}
  #faq + .tns-news-section{{padding-top:18px!important}}
  #inquiry{{padding-top:28px!important;padding-bottom:30px!important}}
}}
@media(max-width:640px){{
  .section{{padding:26px 0!important}}
  body>.section+.section{{padding-top:14px!important}}
  .section-head{{margin-bottom:16px!important}}
  .tns-news-top{{margin-bottom:16px!important}}
  #faq{{padding-bottom:18px!important}}
  #faq + .tns-news-section{{padding-top:16px!important}}
  #inquiry{{padding-top:26px!important;padding-bottom:28px!important}}
  .home-lite-grid{{margin-top:18px!important}}
  .home-lite-actions{{margin-top:16px!important}}
}}
</style>'''

SUBPAGE_STYLE = f'''<style id="{STYLE_ID}">
/* Tighter guide/news rhythm across desktop, tablet and mobile. */
main,.main{{padding-top:42px!important;padding-bottom:54px!important}}
.main .section,main .section{{margin-bottom:28px!important}}
.main h2,main h2{{margin-top:32px!important;margin-bottom:10px!important}}
.main h3,main h3{{margin-top:20px!important;margin-bottom:8px!important}}
.answer{{margin-bottom:26px!important}}
.source,.sources{{margin-top:28px!important}}
.cta{{margin-top:26px!important}}
@media(max-width:900px){{
  .hero{{padding-top:38px!important;padding-bottom:42px!important}}
  main,.main{{padding-top:28px!important;padding-bottom:38px!important}}
  .main .section,main .section{{margin-bottom:20px!important}}
  .main .section>h2:first-child,main .section>h2:first-child{{margin-top:0!important}}
  .main h2,main h2{{margin-top:24px!important;margin-bottom:8px!important}}
  .main h3,main h3{{margin-top:16px!important;margin-bottom:7px!important}}
  .answer{{margin-bottom:20px!important}}
  .source,.sources{{margin-top:22px!important}}
  .cta{{margin-top:20px!important}}
}}
@media(max-width:640px){{
  .hero{{padding-top:32px!important;padding-bottom:36px!important}}
  main,.main{{padding-top:24px!important;padding-bottom:32px!important}}
  .main .section,main .section{{margin-bottom:16px!important}}
  .main h2,main h2{{margin-top:20px!important;margin-bottom:7px!important}}
  .main h3,main h3{{margin-top:14px!important;margin-bottom:6px!important}}
  .answer{{margin-bottom:18px!important}}
  .grid,.related,.dates{{gap:10px!important}}
  .source,.sources{{margin-top:18px!important}}
  .cta{{margin-top:18px!important}}
}}
</style>'''

pages = sorted(Path('.').glob('*.html')) + sorted(Path('news').glob('*.html'))
changed = 0
for page in pages:
    text = page.read_text(encoding='utf-8')
    text = STYLE_RE.sub('\n', text)
    style = HOME_STYLE if page.as_posix() == 'index.html' else SUBPAGE_STYLE
    if '</head>' not in text:
        raise SystemExit(f'Missing </head> in {page}')
    text = text.replace('</head>', style + '\n</head>', 1)
    page.write_text(text, encoding='utf-8')
    changed += 1

print(f'Normalized responsive spacing on {changed} HTML pages')
