from pathlib import Path

INDEX = Path('index.html')
START = '<!-- TNS_AUTO_NEWS_START -->'
END = '<!-- TNS_AUTO_NEWS_END -->'

SECTION = r'''
<!-- TNS_AUTO_NEWS_START -->
<section class="section mist tns-news-section" id="news">
  <style>
    .tns-news-top{display:flex;align-items:end;justify-content:space-between;gap:20px;margin-bottom:34px}.tns-news-top .section-head{margin-bottom:0}.tns-news-all{font-size:14px;font-weight:800;color:var(--jade);white-space:nowrap}.tns-news-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.tns-news-card{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow);display:flex;flex-direction:column;min-height:100%}.tns-news-thumb{aspect-ratio:16/9;background:linear-gradient(135deg,var(--navy),#31517e);display:grid;place-items:center;color:var(--gold);font-family:var(--font-display);font-size:28px}.tns-news-thumb img{width:100%;height:100%;object-fit:cover}.tns-news-body{padding:22px;display:flex;flex-direction:column;gap:10px;flex:1}.tns-news-meta{font-size:12px;color:var(--muted);font-weight:700}.tns-news-body h3{font-size:21px;line-height:1.3}.tns-news-body p{font-size:14px;color:var(--ink-2);margin:0}.tns-news-link{margin-top:auto;color:var(--jade);font-weight:800;font-size:14px}.tns-news-empty{grid-column:1/-1;padding:34px;border:1px dashed #c8cfda;border-radius:var(--r-lg);background:#fff;text-align:center;color:var(--muted)}@media(max-width:900px){.tns-news-grid{grid-template-columns:1fr 1fr}}@media(max-width:640px){.tns-news-top{align-items:start;flex-direction:column}.tns-news-grid{grid-template-columns:1fr}}
  </style>
  <div class="container">
    <div class="tns-news-top reveal">
      <div class="section-head">
        <div class="eyebrow">Tin tức XJTLU</div>
        <h2>Cập nhật mới nhất từ XJTLU</h2>
        <p class="lead">Tin chính thức được chọn lọc và tóm tắt bằng tiếng Việt cho học sinh và phụ huynh Việt Nam.</p>
      </div>
      <a class="tns-news-all" href="/news/">Xem tất cả tin tức →</a>
    </div>
    <div class="tns-news-grid" id="tnsNewsGrid"><div class="tns-news-empty">Đang tải tin tức…</div></div>
  </div>
  <script>
  (async()=>{const g=document.getElementById('tnsNewsGrid');if(!g)return;const esc=s=>String(s??'').replace(/[&<>'\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','\"':'&quot;'}[c]));try{const r=await fetch('/news/news-data.json',{cache:'no-store'});const d=await r.json();const a=(Array.isArray(d.items)?d.items:[]).slice(0,3);if(!a.length){g.innerHTML='<div class="tns-news-empty"><b>Chưa có bản tin được chọn.</b><br>Hệ thống kiểm tra nguồn chính thức của XJTLU vào mỗi thứ Hai.</div>';return;}g.innerHTML=a.map(x=>`<article class="tns-news-card"><div class="tns-news-thumb">${x.image?`<img src="${esc(x.image)}" alt="" loading="lazy">`:'XJTLU'}</div><div class="tns-news-body"><div class="tns-news-meta">${esc(x.date||'XJTLU Official News')}</div><h3>${esc(x.title)}</h3><p>${esc(x.summary||'')}</p><a class="tns-news-link" href="${esc(x.url||x.source_url||'/news/')}">Đọc thêm →</a></div></article>`).join('');}catch(e){g.innerHTML='<div class="tns-news-empty">Không thể tải tin tức lúc này.</div>';}})();
  </script>
</section>
<!-- TNS_AUTO_NEWS_END -->
'''.strip()


def main():
    html = INDEX.read_text(encoding='utf-8')
    changed = False
    if START not in html:
        marker = '<!-- ===================== FOOTER ===================== -->'
        if marker not in html:
            marker = '<footer'
        if marker not in html:
            raise SystemExit('Footer marker not found')
        html = html.replace(marker, SECTION + '\n\n' + marker, 1)
        changed = True

    nav_after = '<li><a href="#stories">Câu chuyện</a></li>'
    nav_news = '<li><a href="#news">Tin tức</a></li>'
    if nav_news not in html and nav_after in html:
        html = html.replace(nav_after, nav_after + '\n        ' + nav_news, 1)
        changed = True

    footer_pair = '<li><a href="#stories">Câu chuyện</a></li><li><a href="#reviews">Video</a></li>'
    footer_repl = '<li><a href="#stories">Câu chuyện</a></li><li><a href="#news">Tin tức</a></li><li><a href="#reviews">Video</a></li>'
    if footer_pair in html:
        html = html.replace(footer_pair, footer_repl, 1)
        changed = True

    if changed:
        INDEX.write_text(html, encoding='utf-8')
        print('Installed XJTLU news section into index.html')
    else:
        print('News section already installed; no changes')

if __name__ == '__main__':
    main()
