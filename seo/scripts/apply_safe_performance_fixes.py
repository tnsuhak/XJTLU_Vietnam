from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "index.html"

OLD_FONT = '<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">'
FONT_URL = 'https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=optional'
NEW_FONT = (
    f'<link rel="preload" as="style" href="{FONT_URL}">\n'
    f'<link href="{FONT_URL}" rel="stylesheet" media="print" onload="this.media=\'all\'">\n'
    f'<noscript><link href="{FONT_URL}" rel="stylesheet"></noscript>'
)

HERO_MARKER = '<!-- ===================== HERO ===================== -->'
FOOTER_MARKER = '<!-- ===================== FOOTER ===================== -->'


def main() -> None:
    html = INDEX.read_text(encoding="utf-8")
    original = html

    # 1) Make Google Fonts non-render-blocking and reduce nonessential variants.
    if OLD_FONT in html:
        html = html.replace(OLD_FONT, NEW_FONT, 1)

    # 2) Add a semantic main landmark without changing visible content.
    if '<main id="main-content">' not in html:
        html = html.replace(HERO_MARKER, '<main id="main-content">\n\n' + HERO_MARKER, 1)
        html = html.replace(FOOTER_MARKER, '</main>\n\n' + FOOTER_MARKER, 1)

    # 3) Fix tab semantics in the admission tablist.
    html = html.replace('<button class="adm-tab active" data-adm=', '<button class="adm-tab active" role="tab" data-adm=')
    html = html.replace('<button class="adm-tab" data-adm=', '<button class="adm-tab" role="tab" data-adm=')

    # 4) Give column headers explicit scope where it is currently omitted.
    html = re.sub(r'<th(?![^>]*\bscope=)', '<th scope="col"', html)

    if html == original:
        print('No safe performance/accessibility changes needed.')
        return

    INDEX.write_text(html, encoding="utf-8")
    print('Applied safe performance/accessibility fixes to index.html')


if __name__ == '__main__':
    main()
