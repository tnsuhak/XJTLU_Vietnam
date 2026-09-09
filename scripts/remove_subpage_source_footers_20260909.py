from pathlib import Path
import re

RANKING = 'xjtlu-ranking-2027.html'

# Remove the small source/citation footer blocks from ordinary guide pages only.
# News articles are intentionally excluded because their original source links
# must remain visible.
guide_pages = [p for p in Path('.').glob('*.html') if p.name not in {'index.html', RANKING}]
removed_total = 0
patterns = [
    r'\n?\s*<(?:div|section|p)\b[^>]*class=["\'][^"\']*\bsources\b[^"\']*["\'][^>]*>.*?</(?:div|section|p)>\s*',
    r'\n?\s*<(?:div|section|p)\b[^>]*class=["\'][^"\']*\bsource-footer\b[^"\']*["\'][^>]*>.*?</(?:div|section|p)>\s*',
]
for page in guide_pages:
    text = page.read_text(encoding='utf-8')
    original = text
    for pattern in patterns:
        text, count = re.subn(pattern, '\n', text, flags=re.I | re.S)
        removed_total += count
    if text != original:
        page.write_text(text, encoding='utf-8')

# Remove every visible/internal link to the retired ranking guide, including
# homepage cards and grouped-menu links. This runs after menu generators.
all_html = sorted(Path('.').glob('*.html')) + sorted(Path('news').glob('*.html'))
link_re = re.compile(
    r'<a\b[^>]*href=["\'](?:https?://[^"\']+)?/?xjtlu-ranking-2027\.html(?:#[^"\']*)?["\'][^>]*>.*?</a>',
    re.I | re.S,
)
for page in all_html:
    if page.name == RANKING:
        continue
    text = page.read_text(encoding='utf-8')
    text = link_re.sub('', text)
    page.write_text(text, encoding='utf-8')

# Remove from sitemap and delete the page itself.
sitemap = Path('sitemap.xml')
if sitemap.exists():
    text = sitemap.read_text(encoding='utf-8')
    text = re.sub(r'\s*<url>.*?xjtlu-ranking-2027\.html.*?</url>\s*', '\n', text, flags=re.I | re.S)
    sitemap.write_text(text, encoding='utf-8')
ranking = Path(RANKING)
if ranking.exists():
    ranking.unlink()

# Guards.
assert not ranking.exists()
for page in sorted(Path('.').glob('*.html')) + sorted(Path('news').glob('*.html')):
    raw = page.read_text(encoding='utf-8')
    assert RANKING not in raw, page
for page in guide_pages:
    if page.exists():
        raw = page.read_text(encoding='utf-8')
        assert not re.search(r'class=["\'][^"\']*\b(?:sources|source-footer)\b', raw, re.I), page
if sitemap.exists():
    assert RANKING not in sitemap.read_text(encoding='utf-8')
print('ranking guide removed; guide source footers removed:', removed_total)
