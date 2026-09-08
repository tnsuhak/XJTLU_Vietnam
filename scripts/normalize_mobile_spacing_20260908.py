from pathlib import Path
import re

STYLE_ID = "tns-spacing-compact-20260908"
STYLE_RE = re.compile(rf'\n?<style id="{STYLE_ID}">.*?</style>\n?', re.S)

HOME_STYLE = f'''<style id="{STYLE_ID}">
/* Balanced section rhythm: remove stacked vertical whitespace on smaller screens. */
@media(max-width:900px){{
  .section{{padding:42px 0!important}}
  body>.section+.section{{padding-top:24px!important}}
  .section-head{{margin-bottom:22px!important}}
  .tns-news-top{{margin-bottom:22px!important}}
  #faq{{padding-bottom:26px!important}}
  #faq + .tns-news-section{{padding-top:24px!important}}
  #inquiry{{padding-top:36px!important;padding-bottom:38px!important}}
}}
@media(max-width:640px){{
  .section{{padding:32px 0!important}}
  body>.section+.section{{padding-top:18px!important}}
  .section-head{{margin-bottom:18px!important}}
  .tns-news-top{{margin-bottom:18px!important}}
  #faq{{padding-bottom:24px!important}}
  #faq + .tns-news-section{{padding-top:22px!important}}
  #inquiry{{padding-top:32px!important;padding-bottom:34px!important}}
}}
</style>'''

SUBPAGE_STYLE = f'''<style id="{STYLE_ID}">
/* Compact guide/news rhythm while keeping cards and text comfortably readable. */
@media(max-width:900px){{
  .hero{{padding-top:44px!important;padding-bottom:48px!important}}
  main,.main{{padding-top:34px!important;padding-bottom:46px!important}}
  .main .section,main .section{{margin-bottom:26px!important}}
  .main .section>h2:first-child,main .section>h2:first-child{{margin-top:0!important}}
  .answer{{margin-bottom:26px!important}}
  .section h2{{margin-bottom:9px!important}}
  .source,.sources{{margin-top:30px!important}}
  .cta{{margin-top:28px!important}}
}}
@media(max-width:640px){{
  .hero{{padding-top:36px!important;padding-bottom:42px!important}}
  main,.main{{padding-top:28px!important;padding-bottom:38px!important}}
  .main .section,main .section{{margin-bottom:22px!important}}
  .answer{{margin-bottom:22px!important}}
  .grid,.related,.dates{{gap:12px!important}}
  .source,.sources{{margin-top:26px!important}}
  .cta{{margin-top:24px!important}}
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
