from __future__ import annotations

import html
import json
from pathlib import Path
from urllib.parse import urljoin

INDEX = Path("index.html")
NEWS_INDEX = Path("news/index.html")
NEWS_DATA = Path("news/news-data.json")
START = "<!-- TNS_AUTO_NEWS_START -->"
END = "<!-- TNS_AUTO_NEWS_END -->"
BASE = "https://xjtlu-vietnam.netlify.app/"
HOMEPAGE_LATEST_COUNT = 4


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def load_items() -> tuple[dict, list[dict]]:
    data = json.loads(NEWS_DATA.read_text(encoding="utf-8"))
    items = data.get("items") if isinstance(data, dict) else []
    if not isinstance(items, list):
        items = []
    return data, items


def homepage_card(item: dict) -> str:
    image = item.get("image")
    image_html = ""
    if image:
        image_html = f'<div class="tns-news-thumb"><img src="{esc(image)}" alt="" loading="lazy" decoding="async"></div>'
    return (
        '<article class="tns-news-card">'
        f'{image_html}'
        '<div class="tns-news-body">'
        f'<div class="tns-news-meta">{esc(item.get("date") or "XJTLU Official News")}</div>'
        f'<h3>{esc(item.get("title"))}</h3>'
        f'<p>{esc(item.get("summary"))}</p>'
        f'<a class="tns-news-link" href="{esc(item.get("url") or item.get("source_url") or "/news/")}">Đọc thêm →</a>'
        '</div></article>'
    )


def render_homepage(items: list[dict]) -> None:
    cards = "".join(homepage_card(x) for x in items[:HOMEPAGE_LATEST_COUNT])
    if not cards:
        cards = '<div class="tns-news-empty"><b>Chưa có bản tin được chọn.</b><br>Hệ thống kiểm tra nguồn chính thức của XJTLU vào mỗi thứ Hai.</div>'

    section = f'''{START}
<section class="section mist tns-news-section" id="news">
  <style>
    .tns-news-top{{display:flex;align-items:end;justify-content:space-between;gap:20px;margin-bottom:34px}}.tns-news-top .section-head{{margin-bottom:0}}.tns-news-all{{font-size:14px;font-weight:800;color:var(--jade);white-space:nowrap}}.tns-news-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}}.tns-news-card{{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow);display:flex;flex-direction:column;min-height:100%}}.tns-news-thumb{{aspect-ratio:16/9;background:var(--navy);overflow:hidden}}.tns-news-thumb img{{width:100%;height:100%;object-fit:cover}}.tns-news-body{{padding:22px;display:flex;flex-direction:column;gap:10px;flex:1}}.tns-news-meta{{font-size:12px;color:var(--muted);font-weight:700}}.tns-news-body h3{{font-size:21px;line-height:1.3}}.tns-news-body p{{font-size:14px;color:var(--ink-2);margin:0}}.tns-news-link{{margin-top:auto;color:var(--jade);font-weight:800;font-size:14px}}.tns-news-empty{{grid-column:1/-1;padding:34px;border:1px dashed #c8cfda;border-radius:var(--r-lg);background:#fff;text-align:center;color:var(--muted)}}@media(max-width:1050px){{.tns-news-grid{{grid-template-columns:1fr 1fr}}}}@media(max-width:640px){{.tns-news-top{{align-items:start;flex-direction:column}}.tns-news-grid{{grid-template-columns:1fr}}}}
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
    <div class="tns-news-grid">{cards}</div>
  </div>
</section>
{END}'''

    text = INDEX.read_text(encoding="utf-8")
    if START in text and END in text:
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        text = before.rstrip() + "\n\n" + section + "\n\n" + after.lstrip()
    else:
        marker = "<!-- ===================== FOOTER ===================== -->"
        if marker not in text:
            marker = "<footer"
        if marker not in text:
            raise SystemExit("Footer marker not found")
        text = text.replace(marker, section + "\n\n" + marker, 1)

    nav_after = '<li><a href="#stories">Câu chuyện</a></li>'
    nav_news = '<li><a href="#news">Tin tức</a></li>'
    if nav_news not in text and nav_after in text:
        text = text.replace(nav_after, nav_after + "\n        " + nav_news, 1)

    footer_pair = '<li><a href="#stories">Câu chuyện</a></li><li><a href="#reviews">Video</a></li>'
    footer_repl = '<li><a href="#stories">Câu chuyện</a></li><li><a href="#news">Tin tức</a></li><li><a href="#reviews">Video</a></li>'
    if footer_pair in text:
        text = text.replace(footer_pair, footer_repl, 1)

    INDEX.write_text(text, encoding="utf-8")


def news_card(item: dict) -> str:
    image = item.get("image")
    image_html = ""
    if image:
        image_html = f'<div class="thumb"><img src="{esc(image)}" alt="" loading="lazy" decoding="async"></div>'
    return (
        '<article class="card">'
        f'{image_html}'
        '<div class="body">'
        f'<div class="meta">{esc(item.get("date") or "XJTLU Official News")}</div>'
        f'<h2><a href="{esc(item.get("url") or item.get("source_url") or "#")}">{esc(item.get("title"))}</a></h2>'
        f'<p>{esc(item.get("summary"))}</p>'
        f'<a class="more" href="{esc(item.get("url") or item.get("source_url") or "#")}">Đọc bản tóm tắt →</a>'
        '</div></article>'
    )


def render_news_index(data: dict, items: list[dict]) -> None:
    cards = "".join(news_card(x) for x in items)
    if not cards:
        cards = '<div class="empty"><b>Chưa có bản tin được chọn.</b><br>Hệ thống sẽ kiểm tra nguồn chính thức của XJTLU vào mỗi thứ Hai.</div>'

    item_list = []
    for pos, item in enumerate(items, start=1):
        target = item.get("url") or item.get("source_url")
        if not target:
            continue
        item_list.append({"@type": "ListItem", "position": pos, "url": urljoin(BASE, target), "name": item.get("title") or "XJTLU News"})

    schema = {"@context": "https://schema.org", "@graph": [{"@type": "CollectionPage", "@id": BASE + "news/#webpage", "url": BASE + "news/", "name": "Tin tức XJTLU | XJTLU Việt Nam", "description": "Tin tức và cập nhật chính thức từ XJTLU, được chọn lọc và tóm tắt bằng tiếng Việt cho học sinh và phụ huynh Việt Nam.", "inLanguage": "vi-VN"}, {"@type": "ItemList", "name": "Tin tức XJTLU dành cho Việt Nam", "itemListElement": item_list}]}
    schema_json = json.dumps(schema, ensure_ascii=False, separators=(",", ":"))

    page = f'''<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Tin tức XJTLU | XJTLU Việt Nam</title><meta name="description" content="Tin tức và cập nhật chính thức từ Xi'an Jiaotong-Liverpool University (XJTLU), được chọn lọc và tóm tắt bằng tiếng Việt cho học sinh và phụ huynh Việt Nam."><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large"><link rel="canonical" href="{BASE}news/"><script type="application/ld+json">{schema_json}</script><style>:root{{--navy:#14213d;--deep:#0b1630;--gold:#c9a84c;--ivory:#f6f2e8;--mist:#eef0f4;--ink:#1a1d26;--muted:#6b7280;--line:#e3e6ec;--jade:#1f6f78}}*{{box-sizing:border-box}}body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:#fff;line-height:1.65}}.wrap{{width:min(1120px,calc(100% - 36px));margin:auto}}.top{{background:var(--deep);color:#fff;padding:18px 0}}.top a{{color:#fff;text-decoration:none;font-weight:700}}.hero{{background:linear-gradient(135deg,var(--deep),#1d2d52);color:#fff;padding:72px 0}}.hero h1{{font-family:Georgia,serif;font-size:clamp(36px,6vw,60px);margin:0 0 14px}}.hero p{{max-width:760px;color:#d6dcea;font-size:18px}}.badge{{display:inline-block;color:var(--gold);font-weight:800;letter-spacing:.12em;text-transform:uppercase;font-size:12px}}.main{{padding:64px 0}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}.card{{border:1px solid var(--line);border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 10px 28px rgba(20,33,61,.07);display:flex;flex-direction:column}}.thumb{{aspect-ratio:16/9;background:var(--navy);overflow:hidden}}.thumb img{{width:100%;height:100%;object-fit:cover}}.body{{padding:22px;display:flex;flex-direction:column;gap:10px;flex:1}}.meta{{font-size:12px;color:var(--muted);font-weight:700}}.body h2{{font-family:Georgia,serif;color:var(--navy);font-size:22px;line-height:1.25;margin:0}}.body h2 a{{color:inherit;text-decoration:none}}.body p{{margin:0;color:#3d4353;font-size:14px}}.more{{margin-top:auto;color:var(--jade);font-weight:800;text-decoration:none}}.empty{{grid-column:1/-1;padding:42px;border:1px dashed #cbd1dc;border-radius:18px;text-align:center;background:var(--mist);color:var(--muted)}}.note{{margin-top:36px;padding:18px 20px;background:var(--ivory);border-radius:14px;color:#5d6370;font-size:13px}}.footer{{margin-top:50px;padding:28px 0;border-top:1px solid var(--line);color:var(--muted);font-size:13px}}@media(max-width:900px){{.grid{{grid-template-columns:1fr 1fr}}}}@media(max-width:620px){{.grid{{grid-template-columns:1fr}}.hero{{padding:52px 0}}}}</style></head><body><div class="top"><div class="wrap"><a href="/">← XJTLU Việt Nam</a></div></div><header class="hero"><div class="wrap"><span class="badge">Official News · Selected for Vietnam</span><h1>Tin tức XJTLU</h1><p>Các cập nhật đáng chú ý từ nguồn chính thức của XJTLU, được chọn lọc và tóm tắt bằng tiếng Việt. Mỗi bài đều dẫn về nguồn gốc để bạn kiểm tra thông tin đầy đủ.</p></div></header><main class="main"><div class="wrap"><div class="grid">{cards}</div><div class="note">Trang này là nội dung biên tập dành cho người đọc Việt Nam, không phải trang chính thức của XJTLU. Nội dung gốc luôn được liên kết trong từng bài.</div><div class="footer">TNS Worldwide · XJTLU Việt Nam</div></div></main></body></html>'''
    NEWS_INDEX.write_text(page, encoding="utf-8")


def main() -> None:
    data, items = load_items()
    render_homepage(items)
    render_news_index(data, items)
    print(f"Rendered crawlable static news content from {len(items)} item(s)")


if __name__ == "__main__":
    main()
