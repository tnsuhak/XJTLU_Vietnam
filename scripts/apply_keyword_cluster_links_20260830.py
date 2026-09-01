from pathlib import Path

replacements = {
    'xjtlu-hoc-phi-hoc-bong-2027.html': (
        '<div class="navlinks"><a href="/#tuition">Xem bảng học phí chi tiết</a><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Điều kiện tuyển sinh</a><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Du học Trung Quốc bằng tiếng Anh</a><a href="/news/">Tin tức XJTLU</a></div>',
        '<div class="navlinks"><a href="/du-hoc-trung-quoc-2027.html">Du học Trung Quốc 2027</a><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Điều kiện tuyển sinh XJTLU</a><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Du học Trung Quốc bằng tiếng Anh</a><a href="/xjtlu-ranking-2027.html">XJTLU ranking 2027</a></div>'
    ),
    'xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html': (
        '<div class="navlinks"><a href="/#admission">Xem bảng điều kiện chi tiết</a><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí & học bổng</a><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Du học bằng tiếng Anh tại Trung Quốc</a><a href="/news/">Tin tức XJTLU</a></div>',
        '<div class="navlinks"><a href="/du-hoc-trung-quoc-2027.html">Điều kiện du học Trung Quốc 2027</a><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí & học bổng XJTLU</a><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Du học Trung Quốc bằng tiếng Anh</a><a href="/xjtlu-ranking-2027.html">XJTLU ranking 2027</a></div>'
    ),
    'du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html': (
        '<div class="navlinks"><a href="/#information">Xem XJTLU là trường gì</a><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí & học bổng</a><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Điều kiện tuyển sinh</a><a href="/news/">Tin tức XJTLU</a></div>',
        '<div class="navlinks"><a href="/du-hoc-trung-quoc-2027.html">Cẩm nang du học Trung Quốc 2027</a><a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí & học bổng XJTLU</a><a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Điều kiện tuyển sinh XJTLU</a><a href="/xjtlu-ranking-2027.html">XJTLU ranking 2027</a></div>'
    )
}

changed = []
for filename, (old, new) in replacements.items():
    p = Path(filename)
    s = p.read_text(encoding='utf-8')
    if new in s:
        print(f'{filename}: already optimized')
        continue
    if old not in s:
        raise SystemExit(f'{filename}: expected navlinks block not found')
    p.write_text(s.replace(old, new, 1), encoding='utf-8')
    changed.append(filename)
    print(f'{filename}: internal links optimized')

print('Changed:', ', '.join(changed) if changed else 'none')
