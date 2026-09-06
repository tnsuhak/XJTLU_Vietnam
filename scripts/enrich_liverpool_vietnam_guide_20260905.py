from pathlib import Path

PAGE = Path('university-of-liverpool-vietnam.html')
text = PAGE.read_text(encoding='utf-8')

text = text.replace(
    'Ba kết nối nổi bật giữa UK/Liverpool/University of Liverpool và Việt Nam trong giáo dục, y tế, AI và khoa học-công nghệ.',
    'Năm kết nối nổi bật giữa UK, Liverpool, University of Liverpool và Việt Nam trong giáo dục, y tế, AI, khoa học-công nghệ và văn hóa.',
)
text = text.replace(
    '"description":"Hợp tác UK–Việt Nam, Liverpool–TP.HCM và University of Liverpool–UMP HCMC"',
    '"description":"Các kết nối UK–Việt Nam, Liverpool–TP.HCM và University of Liverpool với Việt Nam trong giáo dục, y tế, AI và đổi mới"',
)
text = text.replace(
    '<p>Ba sự kiện dưới đây là quan hệ <b>UK–Việt Nam</b>, hợp tác giữa <b>TP.HCM và Vùng Đô thị Liverpool</b>, và hợp tác giữa <b>University of Liverpool với UMP TP.HCM</b>. Chúng đáng chú ý với người tìm hiểu XJTLU vì XJTLU có quan hệ học thuật và bằng cấp sâu với University of Liverpool — nhưng không nên hiểu thành một thỏa thuận tuyển sinh trực tiếp của XJTLU tại Việt Nam.</p>',
    '<p>Các mốc dưới đây cho thấy kết nối giữa <b>Việt Nam, Liverpool và University of Liverpool</b> đang mở rộng từ giáo dục, y tế và khoa học-công nghệ sang đổi mới và văn hóa. Đây là bối cảnh đáng chú ý với người tìm hiểu XJTLU vì XJTLU có quan hệ học thuật và bằng cấp sâu với University of Liverpool.</p>',
)
text = text.replace('Ba mốc kết nối đáng chú ý', 'Năm mốc kết nối đáng chú ý')

anchor_first = '<article class="event"><div class="event-dot"></div><div class="event-card"><span class="event-date">29/10/2025</span><h3>UK × Việt Nam</h3>'
new_first = '''<article class="event"><div class="event-dot"></div><div class="event-card"><span class="event-date">03/2025</span><h3>Hệ sinh thái y tế Liverpool × TP.HCM</h3><div class="event-tag">Nhi khoa · đổi mới y tế · nghiên cứu</div><p>Alder Hey Children’s Hospital tại Liverpool ký thỏa thuận hợp tác với Bệnh viện Nhi Đồng 1 TP.HCM về dịch vụ lâm sàng, nghiên cứu và phát triển trung tâm đổi mới y tế nhi khoa. Cùng giai đoạn này, các chuyên gia thuộc hệ sinh thái đổi mới y tế Liverpool tăng cường làm việc với TP.HCM.</p><a class="src" href="https://www.alderhey.nhs.uk/alder-hey-sign-ground-breaking-agreement-with-childrens-hospital-in-vietnam/" target="_blank" rel="noopener">Nguồn: Alder Hey Children’s Hospital ↗</a></div></article>\n''' + anchor_first
if anchor_first not in text:
    raise SystemExit('First timeline anchor not found')
text = text.replace(anchor_first, new_first, 1)

anchor_last = '<article class="event"><div class="event-dot"></div><div class="event-card"><span class="event-date">30/01/2026</span><h3>University of Liverpool × UMP TP.HCM</h3>'
new_last = '''<article class="event"><div class="event-dot"></div><div class="event-card"><span class="event-date">29/01/2026</span><h3>Liverpool Culture Festival tại TP.HCM</h3><div class="event-tag">City2City · văn hóa · giao lưu cộng đồng</div><p>Liverpool và TP.HCM khởi động giai đoạn hợp tác City2City dài hạn bằng Liverpool Culture Festival tại Việt Nam, với sự tham gia của Liverpool City Council, Tổng Lãnh sự quán Anh và British Council. Sự kiện đưa âm nhạc, nghệ thuật và hình ảnh thành phố Liverpool đến gần công chúng Việt Nam hơn.</p><a class="src" href="https://cultureliverpool.co.uk/2026/liverpool-and-ho-chi-minh-city-mark-twinning-partnership-with-cultural-festival/" target="_blank" rel="noopener">Nguồn: Culture Liverpool ↗</a></div></article>\n''' + anchor_last
if anchor_last not in text:
    raise SystemExit('Final timeline anchor not found')
text = text.replace(anchor_last, new_last, 1)

PAGE.write_text(text, encoding='utf-8')
print('Added two distinct Liverpool–Vietnam milestones to the detail guide.')
