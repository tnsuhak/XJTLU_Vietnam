from pathlib import Path
import re

PAGE = Path('xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html')
text = PAGE.read_text(encoding='utf-8')

text = text.replace(
    '.studentlife-video-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px}',
    '.studentlife-video-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:22px}',
)

new_section = '''<section class="section" id="video"><h2>Video: cơ sở thể thao SIP & Taicang</h2><p class="lead">Hai video tiếng Anh dưới đây cho thấy trực tiếp cơ sở thể thao tại hai khuôn viên chính của XJTLU.</p><div class="studentlife-video-grid">
  <article class="studentlife-video-card"><div class="studentlife-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/drOy9rzNmlE" title="Cơ sở thể thao XJTLU SIP Suzhou" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div><div class="studentlife-video-copy"><b>Cơ sở thể thao tại SIP (Suzhou)</b><p>Khám phá trực tiếp các không gian và tiện ích thể thao tại khuôn viên SIP ở Tô Châu.</p></div></article>
  <article class="studentlife-video-card"><div class="studentlife-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/T8g0zoI9rO4" title="Cơ sở thể thao XJTLU Taicang XEC" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div><div class="studentlife-video-copy"><b>Cơ sở thể thao tại Taicang (XEC)</b><p>Xem không gian thể thao và các tiện ích của khuôn viên Taicang bằng video tiếng Anh.</p></div></article>
</div></section>'''

pattern = re.compile(r'<section class="section" id="video">.*?</div></section>(?=\s*<section class="section"><h2>Sự kiện sinh viên)', re.S)
text, n = pattern.subn(new_section, text, count=1)
if n != 1:
    raise SystemExit('Video section not found')

for old_id in ('XciLskXWwIU', 'nVirGEvdcT8'):
    if old_id in text:
        raise SystemExit(f'Old video id still present: {old_id}')

for new_id in ('drOy9rzNmlE', 'T8g0zoI9rO4'):
    if new_id not in text:
        raise SystemExit(f'New video id missing: {new_id}')

if 'Mở trên YouTube' in text:
    raise SystemExit('YouTube text links should not remain')

PAGE.write_text(text, encoding='utf-8')
print('Kept only English SIP and Taicang sports videos and removed YouTube text links.')
