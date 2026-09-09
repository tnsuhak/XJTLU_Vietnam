from pathlib import Path
import re

RANK_HREF = '/xjtlu-ranking-2027.html'
PAGES = sorted(Path('.').glob('*.html')) + sorted(Path('news').glob('*.html'))

GRID = '''<div class="tns-site-menu-grid">
<section class="tns-site-menu-group"><h3><a href="/">Giới thiệu XJTLU <small>Trang chính →</small></a></h3><a href="/xjtlu-2plus2-liverpool.html">Bằng University of Liverpool &amp; lộ trình 2+2</a><a href="/university-of-liverpool-vietnam.html">Liverpool &amp; Việt Nam</a><a href="/xjtlu-to-chau-thuong-hai-viet-nam.html">Tô Châu, Thượng Hải &amp; Việt Nam</a></section>
<section class="tns-site-menu-group"><h3><a href="/xjtlu-nganh-hoc-nghe-nghiep.html">Ngành học &amp; nghề nghiệp <small>Xem chi tiết →</small></a></h3><a href="/xjtlu-nganh-hoc-nghe-nghiep.html">Ngành học, nghề nghiệp &amp; lựa chọn chương trình</a><a href="/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html">Kết quả học lên sau tốt nghiệp</a></section>
<section class="tns-site-menu-group"><h3><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí &amp; học bổng <small>2027 →</small></a></h3><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí, học bổng &amp; các mốc quan trọng 2027</a><a href="/xjtlu-chi-phi-sinh-hoat-2027.html">Chi phí sinh hoạt XJTLU 2027</a></section>
<section class="tns-site-menu-group"><h3><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html">Đời sống sinh viên <small>Xem chi tiết →</small></a></h3><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html#the-thao">Thể thao &amp; cơ sở thể thao</a><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html#cau-lac-bo">Câu lạc bộ &amp; tổ chức sinh viên</a><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html#video">Video đời sống XJTLU</a><a href="/xjtlu-ky-tuc-xa-sip-taicang.html">Ký túc xá SIP &amp; Taicang</a></section>
<section class="tns-site-menu-group"><h3><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Tuyển sinh 2027 <small>Xem chi tiết →</small></a></h3><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Điều kiện dành cho học sinh Việt Nam</a></section>
<section class="tns-site-menu-group"><h3><a href="/du-hoc-trung-quoc-2027.html">Du học Trung Quốc <small>2027 →</small></a></h3><a href="/du-hoc-trung-quoc-2027.html">Hướng dẫn du học Trung Quốc 2027</a><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Học đại học bằng tiếng Anh tại XJTLU</a></section>
<section class="tns-site-menu-group"><h3><a href="/news/">Tin tức XJTLU <small>Xem tin →</small></a></h3><a href="/news/">Tin chính thức đáng chú ý được chọn lọc và tóm tắt bằng tiếng Việt →</a></section>
</div>'''

GRID_RE = re.compile(r'<div class=["\']tns-site-menu-grid["\']>.*?</div>', re.I | re.S)
EXPECTED = {
    '/xjtlu-to-chau-thuong-hai-viet-nam.html',
    '/xjtlu-chi-phi-sinh-hoat-2027.html',
    '/xjtlu-ky-tuc-xa-sip-taicang.html',
}

changed=[]
for p in PAGES:
    text=p.read_text(encoding='utf-8')
    matches=list(GRID_RE.finditer(text))
    if not matches:
        raise RuntimeError(f'{p}: grouped menu grid not found')
    # Some generated pages can contain more than one menu copy. Normalize all copies.
    new_text=GRID_RE.sub(GRID,text)
    for href in EXPECTED:
        if href not in new_text:
            raise RuntimeError(f'{p}: missing {href}')
    if RANK_HREF in GRID:
        raise RuntimeError('ranking link unexpectedly present in canonical grid')
    if new_text!=text:
        p.write_text(new_text,encoding='utf-8')
        changed.append(str(p))

print('Canonical Vietnamese grouped menu applied:',len(changed),'pages changed')
