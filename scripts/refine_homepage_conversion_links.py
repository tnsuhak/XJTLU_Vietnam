from __future__ import annotations

import re
from pathlib import Path

INDEX = Path("index.html")
SITEMAP = Path("sitemap.xml")
TODAY = "2026-08-30"
GRAD_URL = "https://xjtlu-vietnam.netlify.app/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html"

text = INDEX.read_text(encoding="utf-8")
original = text

# ---------------------------------------------------------------------------
# 1) Keep student-story source links, but reduce other homepage exit paths.
#    Homepage should lead to internal guides and consultation; detailed source
#    links belong on detail pages. Student stories are an explicit exception.
# ---------------------------------------------------------------------------
stories_match = re.search(
    r'(<section\b[^>]*\bid="stories"[^>]*>.*?</section>)',
    text,
    flags=re.DOTALL,
)
stories_html = stories_match.group(1) if stories_match else None
placeholder = "<!-- TNS_STORIES_PRESERVED -->"
if stories_html:
    text = text.replace(stories_html, placeholder, 1)

# Remove programme-level links to XJTLU from the main page; programme names
# remain visible and users can ask through Zalo or use internal detail guides.
text = re.sub(
    r'<a\s+href="https://www\.xjtlu\.edu\.cn/[^"]+"[^>]*>(?:Chi tiết|Danh sách)\s*↗</a>',
    "",
    text,
)

# Remove a late-added Business Chinese external news CTA from the programme
# block. The underlying message stays in the page copy and student stories.
text = re.sub(
    r'<a\s+class="src"\s+href="https://www\.xjtlu\.edu\.cn/en/news/2024/12/business-chinese-boosts-international-students-career-prospects"[^>]*>.*?</a>',
    "",
    text,
    flags=re.DOTALL,
)

# Replace the full-programme external link with non-clickable copy.
text = re.sub(
    r'<p class="note">Danh sách đầy đủ hơn 50 ngành đại học, 55\+ ngành thạc sĩ:\s*<a[^>]+>.*?</a>\.\s*Chương trình thạc sĩ dành cho sinh viên Việt Nam sẽ được giới thiệu tại một trang riêng\.</p>',
    '<p class="note">XJTLU có hơn 50 ngành đại học và 55+ ngành thạc sĩ. Chương trình thạc sĩ dành cho sinh viên Việt Nam sẽ được giới thiệu tại một trang riêng.</p>',
    text,
    flags=re.DOTALL,
)

# Convert source links outside the student-story area into plain source labels.
# This applies to market-signal sources, partnership sources, admissions source
# notes, faculty-profile source links, etc. Facts remain visible without giving
# the homepage another exit path.
def src_to_span(match: re.Match[str]) -> str:
    label = re.sub(r'\s*↗\s*$', '', match.group(1).strip())
    return f'<span class="src">{label}</span>'

text = re.sub(
    r'<a\s+class="src"[^>]*href="https?://[^"]+"[^>]*>(.*?)</a>',
    src_to_span,
    text,
    flags=re.DOTALL,
)

# Remove the remaining direct University of Liverpool link inside the homepage
# FAQ while preserving the factual guidance.
text = re.sub(
    r'Điều kiện cụ thể theo từng ngành xem tại\s*<a\s+href="https://www\.liverpool\.ac\.uk/[^"]+"[^>]*>trang của University of Liverpool</a>\.',
    'Điều kiện cụ thể theo từng ngành nên được kiểm tra lại trước khi nộp hồ sơ.',
    text,
)

# Restore student stories unchanged: their official-original links are useful
# attribution and the user explicitly wants to keep them.
if stories_html:
    text = text.replace(placeholder, stories_html, 1)

# Any remaining clickable external link on the homepage must open in a new tab
# and protect window.opener. (This covers story originals and Zalo links.)
def harden_external_anchor(match: re.Match[str]) -> str:
    tag = match.group(0)
    if 'target="_blank"' not in tag:
        tag = tag[:-1] + ' target="_blank">'
    if 'rel="noopener"' not in tag:
        tag = tag[:-1] + ' rel="noopener">'
    return tag

text = re.sub(
    r'<a\b[^>]*href="https?://[^"]+"[^>]*>',
    harden_external_anchor,
    text,
)

# ---------------------------------------------------------------------------
# 2) Add a compact 2025 graduate-destination summary inside #opportunity and
#    link to the new Vietnamese evergreen detail guide.
# ---------------------------------------------------------------------------
text = re.sub(
    r'\n?<!-- TNS_GRAD_OUTCOMES_START -->.*?<!-- TNS_GRAD_OUTCOMES_END -->\n?',
    "\n",
    text,
    flags=re.DOTALL,
)
text = re.sub(
    r'\n?<style id="tns-grad-outcomes-style">.*?</style>\n?',
    "\n",
    text,
    flags=re.DOTALL,
)

grad_style = '''<style id="tns-grad-outcomes-style">
.tns-grad-outcomes{margin-top:34px;background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:26px;box-shadow:var(--shadow)}.tns-grad-outcomes-head{display:flex;align-items:end;justify-content:space-between;gap:22px;margin-bottom:18px}.tns-grad-outcomes-head h3{margin:5px 0 0;font-size:25px}.tns-grad-outcomes-head p{margin:6px 0 0;color:var(--muted);font-size:14px;max-width:700px}.tns-grad-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.tns-grad-stat{background:var(--ivory);border:1px solid var(--line);border-radius:14px;padding:18px}.tns-grad-stat b{display:block;font-family:var(--font-display);font-size:31px;color:var(--navy);line-height:1}.tns-grad-stat span{display:block;margin-top:7px;color:var(--muted);font-size:12.5px}.tns-grad-link{display:inline-flex;margin-top:18px;color:var(--jade);font-weight:800;font-size:14px}.tns-grad-link:hover{text-decoration:underline}@media(max-width:720px){.tns-grad-outcomes-head{display:block}.tns-grad-stats{grid-template-columns:1fr}.tns-grad-outcomes{padding:20px}}
</style>
'''
opportunity_marker = '<section class="section ivory" id="opportunity">'
if opportunity_marker in text and 'id="tns-grad-outcomes-style"' not in text:
    text = text.replace(opportunity_marker, grad_style + opportunity_marker, 1)

grad_block = '''
<!-- TNS_GRAD_OUTCOMES_START -->
<div class="tns-grad-outcomes reveal">
  <div class="tns-grad-outcomes-head">
    <div>
      <span class="pill">Kết quả học lên · 2025</span>
      <h3>Sau XJTLU, sinh viên tiếp tục học ở đâu?</h3>
      <p>Dữ liệu XJTLU 2025 cho thấy tỷ lệ học lên rất cao, với các điểm đến như UCL, Imperial, Oxford, Harvard, Cambridge, NUS và nhiều đại học hàng đầu khác.</p>
    </div>
  </div>
  <div class="tns-grad-stats">
    <div class="tns-grad-stat"><b>86,43%</b><span>dự định tiếp tục học tại các đại học trên thế giới</span></div>
    <div class="tns-grad-stat"><b>47,16%</b><span>đi vào nhóm đại học TOP 10 theo dữ liệu XJTLU</span></div>
    <div class="tns-grad-stat"><b>93,40%</b><span>đi vào nhóm đại học TOP 100 theo dữ liệu XJTLU</span></div>
  </div>
  <a class="tns-grad-link" href="/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html">Xem Harvard, Oxford, UCL và toàn bộ điểm đến học lên 2025 →</a>
</div>
<!-- TNS_GRAD_OUTCOMES_END -->
'''
pattern = r'(<section\b[^>]*\bid="opportunity"[^>]*>.*?)(</section>)'
text, count = re.subn(
    pattern,
    lambda m: m.group(1).rstrip() + grad_block + m.group(2),
    text,
    count=1,
    flags=re.DOTALL,
)
if count != 1:
    raise SystemExit("Could not place 2025 graduate outcomes in #opportunity")

if text != original:
    INDEX.write_text(text, encoding="utf-8")
    print("Homepage conversion links and graduate outcomes updated")
else:
    print("Homepage conversion links and graduate outcomes already current")

# ---------------------------------------------------------------------------
# 3) Ensure the new indexable detail page is present in the sitemap.
# ---------------------------------------------------------------------------
sitemap = SITEMAP.read_text(encoding="utf-8")
sitemap_original = sitemap
if GRAD_URL not in sitemap:
    entry = f'  <url><loc>{GRAD_URL}</loc><lastmod>{TODAY}</lastmod></url>\n'
    sitemap = sitemap.replace('</urlset>', entry + '</urlset>')
else:
    sitemap = re.sub(
        rf'(<loc>{re.escape(GRAD_URL)}</loc><lastmod>)[^<]+(</lastmod>)',
        rf'\g<1>{TODAY}\2',
        sitemap,
        count=1,
    )
if sitemap != sitemap_original:
    SITEMAP.write_text(sitemap, encoding="utf-8")
    print("Graduate destinations URL added to sitemap")
