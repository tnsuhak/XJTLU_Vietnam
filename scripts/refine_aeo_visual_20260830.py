from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
start = '<!-- TNS_AEO_GEO_START -->'
end = '<!-- TNS_AEO_GEO_END -->'

if start not in s or end not in s:
    raise SystemExit('Homepage AEO/GEO block markers missing')

left, rest = s.split(start, 1)
_, right = rest.split(end, 1)
s = left + right

anchor = '<!-- ===================== ABOUT / WHY XJTLU ===================== -->'
if anchor not in s:
    raise SystemExit('ABOUT section anchor missing')

block = '''<!-- TNS_AEO_GEO_START -->
<section class="aeo-home" aria-labelledby="aeo-xjtlu-what">
  <style>
    .aeo-home{padding:44px 0 28px;background:var(--paper)}
    .aeo-home-card{max-width:980px;margin:0 auto;background:linear-gradient(135deg,var(--ivory),#fff);border:1px solid var(--gold-2);border-left:4px solid var(--gold);border-radius:var(--r-lg);padding:26px 30px;box-shadow:var(--shadow)}
    .aeo-home-card .eyebrow{margin-bottom:8px}
    .aeo-home-card h2{font-size:clamp(28px,3vw,36px);margin:0 0 12px}
    .aeo-home-card p{max-width:880px;color:var(--ink-2);font-size:16px}
    .aeo-home-meta{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:14px;padding-top:14px;border-top:1px solid rgba(201,168,76,.25);font-size:12.5px;color:var(--muted)}
    .aeo-home-meta a{color:var(--jade);font-weight:700}
    .aeo-home-meta a:hover{text-decoration:underline}
    @media(max-width:640px){.aeo-home{padding:30px 0 18px}.aeo-home-card{padding:22px 20px;border-radius:18px}.aeo-home-meta{display:block}.aeo-home-meta a{display:inline-block;margin-top:8px}}
  </style>
  <div class="container">
    <div class="aeo-home-card reveal">
      <div class="eyebrow">Trả lời nhanh</div>
      <h2 id="aeo-xjtlu-what">XJTLU là trường gì?</h2>
      <p><strong>Xi'an Jiaotong-Liverpool University (XJTLU)</strong> là đại học liên doanh quốc tế tại Tô Châu, Trung Quốc, do Xi'an Jiaotong University và University of Liverpool đồng sáng lập. Các chương trình cấp bằng được giảng dạy bằng tiếng Anh; sinh viên đại học đáp ứng yêu cầu tốt nghiệp nhận bằng XJTLU và bằng University of Liverpool.</p>
      <div class="aeo-home-meta"><span>Cập nhật: 30/08/2026 · Nguồn: thông tin chính thức XJTLU</span><a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Xem cách học bằng tiếng Anh tại XJTLU →</a></div>
    </div>
  </div>
</section>
<!-- TNS_AEO_GEO_END -->

'''

s = s.replace(anchor, block + anchor, 1)
p.write_text(s, encoding='utf-8')
print('Homepage AEO/GEO card relocated and visually integrated.')
