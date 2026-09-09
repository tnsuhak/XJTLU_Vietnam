from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
START='<!-- VIETNAM-MARKET-HOME-LINKS-20260909 -->'
END='<!-- /VIETNAM-MARKET-HOME-LINKS-20260909 -->'
block='''<!-- VIETNAM-MARKET-HOME-LINKS-20260909 -->
<div style="display:flex;flex-wrap:wrap;gap:8px 16px;margin-top:12px;font-size:12.5px;font-weight:700;color:#596273">
  <a href="/xjtlu-to-chau-thuong-hai-viet-nam.html">Tô Châu &amp; Việt Nam →</a>
  <a href="/xjtlu-chi-phi-sinh-hoat-2027.html">Chi phí sinh hoạt 2027 →</a>
  <a href="/xjtlu-ky-tuc-xa-sip-taicang.html">Ký túc xá SIP &amp; Taicang →</a>
</div>
<!-- /VIETNAM-MARKET-HOME-LINKS-20260909 -->'''

# Remove an older generated copy if present, then insert immediately after the
# existing single student-life guide action. Keep the homepage lightweight.
import re
s=re.sub(r'<!-- VIETNAM-MARKET-HOME-LINKS-20260909 -->.*?<!-- /VIETNAM-MARKET-HOME-LINKS-20260909 -->','',s,flags=re.S)
marker='<div class="home-lite-actions"><a href="/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html">Xem đời sống sinh viên XJTLU →</a></div>'
assert marker in s, 'student-life action marker not found'
s=s.replace(marker,marker+'\n'+block,1)
p.write_text(s,encoding='utf-8')

out=p.read_text(encoding='utf-8')
assert out.count(START)==1 and out.count(END)==1
for text in ['Tô Châu &amp; Việt Nam →','Chi phí sinh hoạt 2027 →','Ký túc xá SIP &amp; Taicang →']:
    assert text in out,text
print('homepage Vietnam-market links ensured')
