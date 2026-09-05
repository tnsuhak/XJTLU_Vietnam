from pathlib import Path
import re

INDEX = Path('index.html')

COMBINED = r'''<!-- ===================== VIETNAM RELEVANCE ===================== -->
<style id="tns-vietnam-relevance-combined-20260905">
.vn-relevance-grid{display:grid;grid-template-columns:1.06fr .94fr;gap:16px;margin-top:26px}
.vn-relevance-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;min-width:0;box-shadow:var(--shadow)}
.vn-relevance-card.primary{background:linear-gradient(145deg,#172947,#0d1b35);border-color:rgba(255,255,255,.12);color:#fff}
.vn-relevance-kicker{display:block;font-size:10.5px;font-weight:850;letter-spacing:.13em;text-transform:uppercase;color:var(--gold);margin-bottom:8px}
.vn-relevance-card h3{font-family:var(--font-display);font-size:25px;line-height:1.2;color:var(--navy);margin:0 0 8px}
.vn-relevance-card.primary h3{color:#fff}
.vn-relevance-intro{font-size:13.5px;line-height:1.65;color:var(--muted);margin:0 0 17px}
.vn-relevance-card.primary .vn-relevance-intro{color:#c9d1e0}
.vn-proof-list{display:grid;gap:7px;margin-top:14px}
.vn-proof{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:start;padding:10px 11px;border-radius:11px;background:var(--mist)}
.vn-relevance-card.primary .vn-proof{background:rgba(255,255,255,.065)}
.vn-proof i{font-style:normal;font-size:15px;line-height:1.3}
.vn-proof b{display:block;color:var(--navy);font-size:13.5px;line-height:1.35;margin-bottom:2px}
.vn-proof span{display:block;color:var(--muted);font-size:11.8px;line-height:1.45}
.vn-relevance-card.primary .vn-proof b{color:#fff}.vn-relevance-card.primary .vn-proof span{color:#bfc8d8}
.vn-relevance-link{display:inline-block;margin-top:17px;color:var(--jade);font-size:13.5px;font-weight:850;text-decoration:none}
.vn-relevance-card.primary .vn-relevance-link{color:var(--gold-2)}
.vn-relevance-link:hover{text-decoration:underline}
.vn-relevance-note{margin:12px 0 0;color:#8f9ab2;font-size:10.5px;line-height:1.5}
@media(max-width:820px){.vn-relevance-grid{grid-template-columns:1fr}.vn-relevance-card{padding:20px}.vn-relevance-card h3{font-size:22px}}
@media(max-width:560px){.vn-relevance-grid{gap:10px;margin-top:20px}.vn-relevance-card{padding:17px 16px;border-radius:14px}.vn-relevance-card h3{font-size:20px}.vn-relevance-intro{font-size:13px;margin-bottom:13px}.vn-proof{padding:9px 10px}.vn-proof b{font-size:13px}.vn-proof span{font-size:11.5px}.vn-relevance-link{margin-top:14px;font-size:13px}}
</style>
<section class="section" id="liverpool-vietnam">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Vì sao đáng chú ý với sinh viên Việt Nam?</div>
      <h2>Hai lợi thế XJTLU kết hợp trong một lựa chọn</h2>
      <p class="lead">Kết nối với University of Liverpool và trải nghiệm Trung Quốc tạo nên một hướng đi khác với du học Anh hoặc Trung Quốc theo cách truyền thống.</p>
    </div>

    <div class="vn-relevance-grid">
      <article class="vn-relevance-card primary reveal">
        <span class="vn-relevance-kicker">Liverpool × Việt Nam</span>
        <h3>Liverpool đang ngày càng gần Việt Nam</h3>
        <p class="vn-relevance-intro">Không chỉ là cái tên trên bằng cấp: trong 2025–2026, Liverpool và University of Liverpool xuất hiện rõ hơn trong các kết nối giáo dục, y tế và công nghệ với Việt Nam.</p>
        <div class="vn-proof-list">
          <div class="vn-proof"><i>🇬🇧🇻🇳</i><div><b>UK × Việt Nam</b><span>Đối tác Chiến lược Toàn diện · 10/2025</span></div></div>
          <div class="vn-proof"><i>🏙️</i><div><b>Liverpool × TP.HCM</b><span>Giáo dục · y tế · khoa học-công nghệ</span></div></div>
          <div class="vn-proof"><i>🎓</i><div><b>University of Liverpool × UMP</b><span>AI · dữ liệu · y tế số · 01/2026</span></div></div>
        </div>
        <a class="vn-relevance-link" href="/university-of-liverpool-vietnam.html">Xem Liverpool kết nối với Việt Nam →</a>
        <p class="vn-relevance-note">Các mốc trên không phải thỏa thuận tuyển sinh trực tiếp của XJTLU; trang chi tiết giải thích rõ mối liên hệ.</p>
      </article>

      <article class="vn-relevance-card reveal d1">
        <span class="vn-relevance-kicker">Tiếng Anh + tiếng Trung</span>
        <h3>Học bằng tiếng Anh, thêm lợi thế từ Trung Quốc</h3>
        <p class="vn-relevance-intro">XJTLU cho phép sinh viên học chuyên ngành bằng tiếng Anh tại Tô Châu, đồng thời xây dựng thêm tiếng Trung và hiểu biết về thị trường Trung Quốc.</p>
        <div class="vn-proof-list">
          <div class="vn-proof"><i>EN</i><div><b>Chuyên ngành bằng tiếng Anh</b><span>Phù hợp với sinh viên muốn học chương trình quốc tế mà không cần học chuyên ngành bằng tiếng Trung.</span></div></div>
          <div class="vn-proof"><i>中</i><div><b>Tiếng Trung là năng lực bổ sung</b><span>Có thể học tiếng Trung và Business Chinese trong thời gian học.</span></div></div>
          <div class="vn-proof"><i>🌏</i><div><b>Trải nghiệm Trung Quốc thực tế</b><span>Học và sống tại Tô Châu, gần Thượng Hải và hệ sinh thái doanh nghiệp lớn của Trung Quốc.</span></div></div>
        </div>
        <a class="vn-relevance-link" href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">Xem cách học đại học bằng tiếng Anh tại Trung Quốc →</a>
      </article>
    </div>
  </div>
</section>'''

text = INDEX.read_text(encoding='utf-8')
pattern = re.compile(
    r'<!-- ===================== VIETNAM RELEVANCE ===================== -->.*?(?=<!-- ===================== PROGRAMMES ===================== -->)',
    re.S,
)
text, n = pattern.subn(COMBINED + '\n\n', text, count=1)
if n != 1:
    raise SystemExit('Vietnam relevance section not found')
INDEX.write_text(text, encoding='utf-8')
print('Combined Liverpool × Vietnam and English + Chinese into one light homepage section.')
