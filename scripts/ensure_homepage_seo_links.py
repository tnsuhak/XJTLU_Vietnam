from pathlib import Path
import re

INDEX = Path("index.html")
SITEMAP = Path("sitemap.xml")
NEWS = Path("news/700-sinh-vien-indonesia-xjtlu-dong-nam-a.html")
TODAY = "2026-09-05"

text = INDEX.read_text(encoding="utf-8")
original = text

# Remove any obsolete helper-managed schema block. The homepage already has
# the richer maintained JSON-LD graph.
start = "<!-- TNS_SEO_SCHEMA_START -->"
end = "<!-- TNS_SEO_SCHEMA_END -->"
if start in text and end in text:
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    text = before.rstrip() + "\n" + after.lstrip("\n")

# Do not advertise optional local image/icon assets that are not present.
for pattern in [
    r'^<meta property="og:image"[^>]*>\s*\n?',
    r'^<meta property="og:image:width"[^>]*>\s*\n?',
    r'^<meta property="og:image:height"[^>]*>\s*\n?',
    r'^<meta property="og:image:alt"[^>]*>\s*\n?',
    r'^<meta name="twitter:image"[^>]*>\s*\n?',
    r'^<link rel="icon"[^>]*>\s*\n?',
    r'^<link rel="apple-touch-icon"[^>]*>\s*\n?',
]:
    text = re.sub(pattern, "", text, flags=re.MULTILINE)
text = text.replace(
    '<meta name="twitter:card" content="summary_large_image">',
    '<meta name="twitter:card" content="summary">',
)

# Keep all consultation CTAs on the SOS HCMC representative's Zalo.
zalo_url = "https://zalo.me/0336737617"
text = re.sub(r'ZALO_URL:\s*"https://zalo\.me/[^"]+"', f'ZALO_URL: "{zalo_url}"', text)
text = re.sub(r'href="https://zalo\.me/[^"]+"', f'href="{zalo_url}"', text)

# Keep current academic-unit names visible in the programme section.
text = text.replace(
    "School of Advanced Technology · Taicang",
    "Academy of Artificial Intelligence and Advanced Technology",
)
text = text.replace(
    "School of Science · Academy of Pharmacy",
    "Academy of Life and Natural Sciences",
)

# The Netlify form is not currently registered on the site. Remove the visible
# form rather than collecting inquiries through an unverified route; retain
# the direct Zalo/phone/email consultation block.
text = re.sub(
    r'\n\s*<form class="form reveal d1" id="inquiryForm".*?</form>',
    "",
    text,
    count=1,
    flags=re.DOTALL,
)
text = re.sub(r'<div class="inq(?: tns-contact-only)?">', '<div class="inq tns-contact-only">', text, count=1)
contact_style = '''<style id="tns-contact-only-style">
.inq.tns-contact-only{display:block}.inq.tns-contact-only .inq-side{max-width:820px}
</style>
'''
inquiry_marker = "<!-- ===================== INQUIRY ===================== -->"
if 'id="tns-contact-only-style"' not in text and inquiry_marker in text:
    text = text.replace(inquiry_marker, contact_style + inquiry_marker, 1)
text = re.sub(
    r'\n\s*// ---- Form: Netlify handles POST;[^\n]*\n\s*if\(new URLSearchParams\(location\.search\).*?\n',
    "\n",
    text,
    count=1,
)

# Keep one embedded header logo payload and copy it into the footer at runtime.
footer_marker = "<!-- ===================== FOOTER ===================== -->"
if footer_marker in text:
    before_footer, footer = text.split(footer_marker, 1)
    footer = re.sub(
        r'<div class="brand-mark(?: footer-brand-mark)?"(?: aria-hidden="true")?(?:><img src="data:image/webp;base64,[^"]+"[^>]*></div>|>XJ</div>)',
        '<div class="brand-mark footer-brand-mark" aria-hidden="true">XJ</div>',
        footer,
        count=1,
    )
    footer = re.sub(
        r'\s*<div><h4>Trang chính thức</h4><ul>.*?</ul></div>',
        "",
        footer,
        count=1,
        flags=re.DOTALL,
    )
    footer = footer.replace('<div class="foot-grid">', '<div class="foot-grid tns-three-col">', 1)
    text = before_footer + footer_marker + footer

footer_style = '''<style id="tns-footer-three-col-style">
.foot-grid.tns-three-col{grid-template-columns:minmax(0,1.4fr) repeat(2,minmax(0,1fr))}
@media(max-width:900px){.foot-grid.tns-three-col{grid-template-columns:1fr 1fr}}
@media(max-width:620px){.foot-grid.tns-three-col{grid-template-columns:1fr}}
</style>
'''
if 'id="tns-footer-three-col-style"' not in text and footer_marker in text:
    text = text.replace(footer_marker, footer_style + footer_marker, 1)

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
if "// ---- Keep footer brand mark visually identical to the header logo" not in text:
    nav_marker = "  // ---- Nav scroll state + to-top"
    if nav_marker in text:
        text = text.replace(nav_marker, logo_sync + nav_marker, 1)

# Keep evergreen detail links short and contextual on the homepage instead of
# adding a large repeated guide directory.
text = re.sub(
    r'\n?<!-- TNS_SEO_GUIDES_START -->.*?<!-- TNS_SEO_GUIDES_END -->\n?',
    "\n",
    text,
    count=1,
    flags=re.DOTALL,
)
text = re.sub(
    r'\n?<!-- TNS_INLINE_GUIDE_[A-Z_]+_START -->.*?<!-- TNS_INLINE_GUIDE_[A-Z_]+_END -->\n?',
    "\n",
    text,
    flags=re.DOTALL,
)
text = re.sub(
    r'\n?<style id="tns-inline-guide-style">.*?</style>\n?',
    "\n",
    text,
    count=1,
    flags=re.DOTALL,
)

inline_style = '''<style id="tns-inline-guide-style">
.tns-inline-guide{margin-top:28px;padding:20px 0 0;border-top:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:22px}.tns-inline-guide-copy{max-width:760px}.tns-inline-guide small{display:block;color:var(--gold);font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-bottom:5px}.tns-inline-guide strong{display:block;color:var(--navy);font-family:var(--font-display);font-size:19px;line-height:1.3}.tns-inline-guide p{margin:6px 0 0;color:var(--muted);font-size:13.5px;line-height:1.65}.tns-inline-guide a{flex:none;color:var(--jade);font-size:14px;font-weight:800;white-space:nowrap}.tns-inline-guide a:hover{text-decoration:underline}@media(max-width:700px){.tns-inline-guide{display:block}.tns-inline-guide p{font-size:13px}.tns-inline-guide a{display:inline-block;margin-top:10px;white-space:normal}}
</style>
'''
about_marker = "<!-- ===================== ABOUT / WHY XJTLU ===================== -->"
if about_marker not in text:
    raise SystemExit("Could not find homepage About marker")
text = text.replace(about_marker, inline_style + about_marker, 1)


def add_context_link(section_id, marker_name, href, title, description, action):
    global text
    block = f'''\n<!-- TNS_INLINE_GUIDE_{marker_name}_START -->
<div class="tns-inline-guide reveal">
  <div class="tns-inline-guide-copy">
    <small>Hướng dẫn chi tiết</small>
    <strong>{title}</strong>
    <p>{description}</p>
  </div>
  <a href="{href}">{action} →</a>
</div>
<!-- TNS_INLINE_GUIDE_{marker_name}_END -->\n'''
    pattern = rf'(<section\b[^>]*\bid="{re.escape(section_id)}"[^>]*>.*?)(</section>)'
    text, count = re.subn(
        pattern,
        lambda m: m.group(1).rstrip() + block + m.group(2),
        text,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise SystemExit(f"Could not place contextual guide in section #{section_id}")


add_context_link(
    "information",
    "LIVERPOOL",
    "/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html",
    "XJTLU & University of Liverpool",
    "Mô hình Anh - Trung, học bằng tiếng Anh và bằng University of Liverpool.",
    "Xem chi tiết",
)
add_context_link(
    "major",
    "PROGRAMMES",
    "/xjtlu-nganh-hoc-nghe-nghiep.html",
    "Ngành học XJTLU & hướng nghề nghiệp",
    "So sánh nhóm ngành, hướng học lên, việc làm và khả năng 2+2.",
    "Xem ngành & nghề nghiệp",
)
add_context_link(
    "tuition",
    "TUITION",
    "/xjtlu-hoc-phi-hoc-bong-2027.html",
    "Học phí và học bổng XJTLU 2027",
    "Học phí, Entry Scholarship, Early Bird và các khoản chi chính.",
    "Xem học phí",
)
add_context_link(
    "admission",
    "ADMISSION",
    "/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html",
    "Điều kiện tuyển sinh XJTLU 2027",
    "THPT, IELTS/TOEFL, chuyển tiếp và mốc hồ sơ dành cho Việt Nam.",
    "Xem điều kiện",
)

if text != original:
    INDEX.write_text(text, encoding="utf-8")
    print("Homepage UX/SEO structure updated")
else:
    print("Homepage UX/SEO structure already current")

# Update sitemap lastmod for pages changed in this review batch.
sitemap = SITEMAP.read_text(encoding="utf-8")
sitemap_original = sitemap
for url in [
    "https://xjtlu-vietnam.netlify.app/",
    "https://xjtlu-vietnam.netlify.app/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html",
    "https://xjtlu-vietnam.netlify.app/news/700-sinh-vien-indonesia-xjtlu-dong-nam-a.html",
]:
    pattern = rf'(<loc>{re.escape(url)}</loc>\s*<lastmod>)[^<]+(</lastmod>)'
    sitemap = re.sub(pattern, rf'\g<1>{TODAY}\2', sitemap, count=1)
if sitemap != sitemap_original:
    SITEMAP.write_text(sitemap, encoding="utf-8")
    print("Sitemap lastmod updated")

# Strengthen internal linking from the news article back to evergreen guides.
news = NEWS.read_text(encoding="utf-8")
news_original = news
news = news.replace('"dateModified":"2026-08-28"', f'"dateModified":"{TODAY}"')
if 'class="related-guides"' not in news:
    news_style = '.related-guides{margin-top:30px;padding:22px 24px;border:1px solid var(--line);border-radius:16px;background:#fff}.related-guides b{display:block;color:var(--navy);margin-bottom:10px}.related-guides a{display:inline-block;margin:6px 12px 0 0;color:var(--jade);font-weight:800;text-decoration:none}'
    news = news.replace('</style>', news_style + '\n</style>', 1)
    related = '''    <div class="related-guides">
      <b>Tìm hiểu thêm về XJTLU</b>
      <a href="/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html">Điều kiện tuyển sinh 2027 →</a>
      <a href="/xjtlu-hoc-phi-hoc-bong-2027.html">Học phí & học bổng →</a>
      <a href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">XJTLU & University of Liverpool →</a>
      <a href="/xjtlu-nganh-hoc-nghe-nghiep.html">Ngành học & nghề nghiệp →</a>
    </div>
'''
    news = news.replace('    <a class="back" href="/news/">', related + '    <a class="back" href="/news/">', 1)
if news != news_original:
    NEWS.write_text(news, encoding="utf-8")
    print("News internal links updated")
