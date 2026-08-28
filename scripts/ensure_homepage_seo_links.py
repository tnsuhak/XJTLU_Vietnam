from pathlib import Path

PATH = Path("index.html")
text = PATH.read_text(encoding="utf-8")
original = text

schema = r'''<!-- TNS_SEO_SCHEMA_START -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://xjtlu-vietnam.netlify.app/#website",
      "url": "https://xjtlu-vietnam.netlify.app/",
      "name": "XJTLU Vietnam",
      "alternateName": "XJTLU Việt Nam",
      "inLanguage": "vi-VN"
    },
    {
      "@type": "WebPage",
      "@id": "https://xjtlu-vietnam.netlify.app/#webpage",
      "url": "https://xjtlu-vietnam.netlify.app/",
      "name": "XJTLU Vietnam (Việt Nam) | Học phí, học bổng & tuyển sinh 2027",
      "isPartOf": {"@id": "https://xjtlu-vietnam.netlify.app/#website"},
      "inLanguage": "vi-VN",
      "about": {
        "@type": "CollegeOrUniversity",
        "name": "Xi'an Jiaotong-Liverpool University",
        "alternateName": "XJTLU",
        "url": "https://www.xjtlu.edu.cn/"
      }
    }
  ]
}
</script>
<!-- TNS_SEO_SCHEMA_END -->'''

if "<!-- TNS_SEO_SCHEMA_START -->" not in text:
    if "</head>" not in text:
        raise SystemExit("Could not find </head>")
    text = text.replace("</head>", schema + "\n</head>", 1)

links_section = r'''<!-- TNS_SEO_GUIDES_START -->
<section class="section ivory tns-seo-guides" id="xjtlu-guides">
  <style>
    .tns-seo-guide-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.tns-seo-guide{display:flex;flex-direction:column;gap:12px;background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:26px;box-shadow:var(--shadow);transition:transform .2s,box-shadow .2s}.tns-seo-guide:hover{transform:translateY(-3px);box-shadow:0 18px 40px rgba(20,33,61,.12)}.tns-seo-guide h3{font-size:22px}.tns-seo-guide p{font-size:14px;color:var(--ink-2);margin:0}.tns-seo-guide .go{margin-top:auto;color:var(--jade);font-weight:800;font-size:14px}@media(max-width:900px){.tns-seo-guide-grid{grid-template-columns:1fr}} 
  </style>
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Hướng dẫn XJTLU 2027</div>
      <h2>Thông tin XJTLU dành cho học sinh Việt Nam</h2>
      <p class="lead">Xem nhanh các hướng dẫn chuyên sâu về học phí, học bổng, điều kiện tuyển sinh và lựa chọn du học Trung Quốc bằng tiếng Anh.</p>
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
        <p>Yêu cầu THPT, IELTS/TOEFL, lộ trình năm 1 và các lựa chọn chuyển tiếp dành cho hồ sơ từ Việt Nam.</p>
        <span class="go">Xem điều kiện →</span>
      </a>
      <a class="tns-seo-guide reveal d2" href="/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html">
        <span class="pill navy">English-taught</span>
        <h3>Du học Trung Quốc bằng tiếng Anh tại XJTLU</h3>
        <p>Vì sao XJTLU là lựa chọn khác biệt giữa giáo dục Anh Quốc, cơ hội tại Trung Quốc và môi trường quốc tế.</p>
        <span class="go">Tìm hiểu thêm →</span>
      </a>
    </div>
  </div>
</section>
<!-- TNS_SEO_GUIDES_END -->'''

if "<!-- TNS_SEO_GUIDES_START -->" not in text:
    marker = "<!-- TNS_AUTO_NEWS_START -->"
    if marker not in text:
        raise SystemExit("Could not find news insertion marker")
    text = text.replace(marker, links_section + "\n\n" + marker, 1)

if text != original:
    PATH.write_text(text, encoding="utf-8")
    print("Homepage SEO structure updated")
else:
    print("Homepage SEO structure already current")
