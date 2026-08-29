from pathlib import Path
import re

PATH = Path("index.html")
text = PATH.read_text(encoding="utf-8")
original = text

# The homepage already contains a richer JSON-LD graph maintained in the
# main source. Remove any older helper-managed schema block so WebSite/WebPage
# entities are not duplicated.
start = "<!-- TNS_SEO_SCHEMA_START -->"
end = "<!-- TNS_SEO_SCHEMA_END -->"
if start in text and end in text:
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    text = before.rstrip() + "\n" + after.lstrip("\n")

# Do not advertise local social/icon assets that do not actually exist.
optional_asset_patterns = [
    r'^<meta property="og:image"[^>]*>\s*\n?',
    r'^<meta property="og:image:width"[^>]*>\s*\n?',
    r'^<meta property="og:image:height"[^>]*>\s*\n?',
    r'^<meta property="og:image:alt"[^>]*>\s*\n?',
    r'^<meta name="twitter:image"[^>]*>\s*\n?',
    r'^<link rel="icon"[^>]*>\s*\n?',
    r'^<link rel="apple-touch-icon"[^>]*>\s*\n?',
]
for pattern in optional_asset_patterns:
    text = re.sub(pattern, "", text, flags=re.MULTILINE)
text = text.replace('<meta name="twitter:card" content="summary_large_image">', '<meta name="twitter:card" content="summary">')

# Use the SOS International Ho Chi Minh City representative as the single
# Zalo destination across the Vietnam site so every consultation CTA reaches
# the same local admissions contact.
zalo_url = "https://zalo.me/0336737617"
text = re.sub(r'ZALO_URL:\s*"https://zalo\.me/[^"]+"', f'ZALO_URL: "{zalo_url}"', text)
text = re.sub(r'href="https://zalo\.me/[^"]+"', f'href="{zalo_url}"', text)

# Keep the header logo as the single embedded Base64 payload. The footer uses
# a small fallback mark in raw HTML, then copies the exact header logo at
# runtime so both locations look identical without duplicating the image data.
footer_marker = "<!-- ===================== FOOTER ===================== -->"
if footer_marker in text:
    before_footer, footer = text.split(footer_marker, 1)
    footer = re.sub(
        r'<div class="brand-mark(?: footer-brand-mark)?"(?: aria-hidden="true")?(?:><img src="data:image/webp;base64,[^"]+"[^>]*></div>|>XJ</div>)',
        '<div class="brand-mark footer-brand-mark" aria-hidden="true">XJ</div>',
        footer,
        count=1,
    )
    text = before_footer + footer_marker + footer

logo_sync = '''  // ---- Keep footer brand mark visually identical to the header logo
  const headerBrandLogo=document.querySelector('header.nav .brand-mark img');
  const footerBrandMark=document.querySelector('footer .footer-brand-mark');
  if(headerBrandLogo&&footerBrandMark){
    const footerLogo=headerBrandLogo.cloneNode(true);
    footerLogo.alt='';
    footerLogo.setAttribute('aria-hidden','true');
    footerBrandMark.textContent='';
    footerBrandMark.appendChild(footerLogo);
  }

'''
logo_sync_marker = "  // ---- Keep footer brand mark visually identical to the header logo"
nav_marker = "  // ---- Nav scroll state + to-top"
if logo_sync_marker not in text and nav_marker in text:
    text = text.replace(nav_marker, logo_sync + nav_marker, 1)

# Keep separate landing pages only when search intent is clearly different.
# General FAQ content is merged into the homepage/admissions content rather
# than maintained as a thin overlapping page.
links_section = r'''<!-- TNS_SEO_GUIDES_START -->
<section class="section ivory tns-seo-guides" id="xjtlu-guides">
  <style>
    .tns-seo-guide-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.tns-seo-guide{display:flex;flex-direction:column;gap:12px;background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:26px;box-shadow:var(--shadow);transition:transform .2s,box-shadow .2s}.tns-seo-guide:hover{transform:translateY(-3px);box-shadow:0 18px 40px rgba(20,33,61,.12)}.tns-seo-guide h3{font-size:22px}.tns-seo-guide p{font-size:14px;color:var(--ink-2);margin:0}.tns-seo-guide .go{margin-top:auto;color:var(--jade);font-weight:800;font-size:14px}@media(max-width:900px){.tns-seo-guide-grid{grid-template-columns:1fr}}
  </style>
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Hướng dẫn XJTLU 2027</div>
      <h2>Thông tin chuyên sâu dành cho học sinh Việt Nam</h2>
      <p class="lead">Chỉ tách thành trang riêng cho ba chủ đề có ý định tìm kiếm rõ ràng: học phí – học bổng, điều kiện tuyển sinh và du học Trung Quốc bằng tiếng Anh.</p>
    </div>
    <div class="tns-seo-guide-grid">
      <a class="tns-seo-guide reveal" href="/xjtlu-hoc-phi-hoc-bong-2027.html">
        <span class="pill">Học phí · Học bổng</span>
        <h3>Học phí XJTLU 2027 & học bổng</h3>
        <p>Mức học phí, Entry Scholarship, ưu đãi nộp sớm và các khoản chi cần chuẩn bị cho sinh viên Việt Nam.</p>
        <span class="go">Xem hướng dẫn →</span>
      </a>
      <a class="tns-seo-guide reveal d1" href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">
        <span class="pill jade">Tuyển sinh</span>
        <h3>Điều kiện vào XJTLU cho học sinh Việt Nam</h3>
        <p>Yêu cầu THPT, IELTS/TOEFL, chuyển tiếp, hồ sơ và thời gian xét tuyển dành cho ứng viên Việt Nam.</p>
        <span class="go">Xem điều kiện →</span>
      </a>
      <a class="tns-seo-guide reveal d2" href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">
        <span class="pill navy">English-taught</span>
        <h3>Du học Trung Quốc bằng tiếng Anh tại XJTLU</h3>
        <p>Vì sao XJTLU kết hợp môi trường Trung Quốc, chương trình tiếng Anh và bằng cấp gắn với University of Liverpool.</p>
        <span class="go">Tìm hiểu thêm →</span>
      </a>
    </div>
  </div>
</section>
<!-- TNS_SEO_GUIDES_END -->'''

guide_start = "<!-- TNS_SEO_GUIDES_START -->"
guide_end = "<!-- TNS_SEO_GUIDES_END -->"
if guide_start in text and guide_end in text:
    before, rest = text.split(guide_start, 1)
    _, after = rest.split(guide_end, 1)
    text = before.rstrip() + "\n" + links_section + after
else:
    marker = "<!-- TNS_AUTO_NEWS_START -->"
    if marker not in text:
        raise SystemExit("Could not find news insertion marker")
    text = text.replace(marker, links_section + "\n\n" + marker, 1)

if text != original:
    PATH.write_text(text, encoding="utf-8")
    print("Homepage SEO/performance structure updated")
else:
    print("Homepage SEO/performance structure already current")
