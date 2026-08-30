from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old_kicker = 'Đại học toàn cầu hợp tác Anh – Trung, tọa lạc tại Tô Châu (30 phút đến Thượng Hải)'
new_kicker = 'Đại học quốc tế Anh – Trung tại Tô Châu'
if old_kicker in s:
    s = s.replace(old_kicker, new_kicker, 1)

old_sub = '''<p class="sub">XJTLU Vietnam cung cấp thông tin dành cho học sinh và phụ huynh Việt Nam về <b>học phí XJTLU, học bổng, điều kiện tuyển sinh 2027, ngành học và ký túc xá</b>. Xi'an Jiaotong-Liverpool University (XJTLU) do <b>University of Liverpool</b> (Anh Quốc) và <b>Đại học Giao thông Tây An</b> (Trung Quốc) đồng sáng lập năm 2006. Sinh viên tốt nghiệp đại học nhận <b>bằng của University of Liverpool (Anh Quốc) và bằng của XJTLU</b>, học hoàn toàn bằng tiếng Anh, và có thể bổ sung tiếng Trung như một lợi thế nghề nghiệp.</p>'''
new_sub = '''<p class="sub"><b>Xi'an Jiaotong-Liverpool University (XJTLU)</b> là đại học quốc tế Anh – Trung tại Tô Châu. Sinh viên học chương trình đại học bằng tiếng Anh và, khi đáp ứng yêu cầu tốt nghiệp, nhận bằng của <b>University of Liverpool</b> cùng bằng XJTLU.</p>'''
if old_sub in s:
    s = s.replace(old_sub, new_sub, 1)

old_mobile = '@media(max-width:560px){.hero{min-height:auto}.hero-actions .btn{width:100%;white-space:normal;text-align:center}.fact b{font-size:28px}}'
new_mobile = '''@media(max-width:560px){
  .hero{min-height:auto}
  .hero .container{padding:40px 0 48px}
  .hero-kicker{margin-bottom:18px;padding:7px 12px 7px 9px;font-size:12px}
  .hero h1 .h1-brand{margin-bottom:11px;font-size:11px;letter-spacing:.11em}
  .hero .sub{margin-top:18px;font-size:15.5px;line-height:1.62}
  .hero-actions{margin-top:24px;gap:8px;flex-direction:column;align-items:stretch}
  .hero-actions .btn{width:100%;white-space:normal;text-align:center}
  .hero-actions .btn-ghost{width:auto;align-self:center;border:0;padding:8px 4px;border-radius:0;font-size:13.5px;color:#dfe4ef;box-shadow:none}
  .hero-actions .btn-ghost::after{content:" →"}
  .hero-facts{margin-top:38px;padding-top:24px;gap:20px 16px}
  .fact b{font-size:28px}
  .route{margin-top:4px}
}'''
if old_mobile in s:
    s = s.replace(old_mobile, new_mobile, 1)

# Keep the mobile 2+2 route card concise so it does not collide visually
# with the adjacent 4+0 card.
s = s.replace('2 năm Trung Quốc → 2 năm Liverpool (tùy ngành)', '2 năm Trung Quốc → 2 năm Liverpool', 1)

p.write_text(s, encoding='utf-8')
print('Compacted XJTLU Vietnam mobile hero and shortened 2+2 route card.')
