from pathlib import Path
import re

STYLE_ID = "tns-spacing-compact-20260908"
STYLE_RE = re.compile(rf'\n?<style id="{STYLE_ID}">.*?</style>\n?', re.S)

HOME_STYLE = f'''<style id="{STYLE_ID}">
/* Compact section rhythm for tablets and phones. Desktop spacing stays unchanged. */
@media(max-width:900px){{
  .section{{padding:46px 0!important}}
  .section-head{{margin-bottom:24px!important}}
  .tns-news-top{{margin-bottom:24px!important}}
  #faq{{padding-bottom:40px!important}}
  #faq + .tns-news-section{{padding-top:40px!important}}
  #inquiry{{padding-top:44px!important;padding-bottom:44px!important}}
}}
@media(max-width:640px){{
  .section{{padding:38px 0!important}}
  .section-head{{margin-bottom:20px!important}}
  .tns-news-top{{margin-bottom:20px!important}}
  #faq{{padding-bottom:34px!important}}
  #faq + .tns-news-section{{padding-top:34px!important}}
  #inquiry{{padding-top:38px!important;padding-bottom:38px!important}}
}}
</style>'''

SUBPAGE_STYLE = f'''<style id="{STYLE_ID}">
/* Compact guide/news rhythm on tablets and phones without changing desktop layout. */
@media(max-width:900px){{
  .hero{{padding-top:48px!important;padding-bottom:56px!important}}
  main,.main{{padding-top:42px!important;padding-bottom:52px!important}}
  .section{{margin-bottom:34px!important}}
  .answer{{margin-bottom:32px!important}}
  .section h2{{margin-bottom:10px!important}}
}}
@media(max-width:640px){{
  .hero{{padding-top:42px!important;padding-bottom:48px!important}}
  main,.main{{padding-top:36px!important;padding-bottom:44px!important}}
  .section{{margin-bottom:30px!important}}
  .answer{{margin-bottom:28px!important}}
  .grid,.related,.dates{{gap:12px!important}}
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
