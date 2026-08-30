# XJTLU Vietnam — Weekly Google Search Console SEO Report

- Property: `https://xjtlu-vietnam.netlify.app/`
- Primary market filter: **Vietnam** (`vnm`)
- Current period: **2026-07-31 → 2026-08-27**
- Comparison period: **2026-07-03 → 2026-07-30**
- Search Console settling lag applied: **3 days**

## 1. Vietnam organic search summary

| Metric | Current | Previous | Change |
| --- | --- | --- | --- |
| Clicks | 0 | 0 | 0.0% |
| Impressions | 0 | 0 | 0.0% |
| CTR | 0.00% | 0.00% | +0.00 pp |
| Avg position | 0.00 | 0.00 | +0.00 better |

## 2. All-country summary

| Metric | Current | Previous | Change |
| --- | --- | --- | --- |
| Clicks | 0 | 0 | 0.0% |
| Impressions | 0 | 0 | 0.0% |
| CTR | 0.00% | 0.00% | +0.00 pp |
| Avg position | 0.00 | 0.00 | +0.00 better |

## 3. SEO opportunities — positions 4–20

_No data yet._

## 4. High-ranking but low-CTR queries

_No data yet._

## 5. Growing queries

_No data yet._

## 6. Top Vietnam queries

_No data yet._

## 7. Top Vietnam landing pages

_No data yet._

## GPT maintenance instructions

Use this report as observed Search Console data, not as market-wide keyword volume. Prioritize real query/page data over guessed SEO metrics. Before changing content, inspect the target page and current SERP/search intent. Do not fabricate search volume. Large SEO changes should be reviewed before production deployment.
## 8. Lighthouse technical SEO & performance

Automated weekly Lighthouse audit of the production homepage.

| Audit | Mobile | Desktop |
| --- | ---: | ---: |
| Performance | 70 | 86 |
| SEO | 100 | 100 |
| Accessibility | 95 | 95 |
| Best Practices | 96 | 96 |

### Core loading metrics (lab data)

| Metric | Mobile | Desktop |
| --- | --- | --- |
| First Contentful Paint | 3.6 s | 1.3 s |
| Largest Contentful Paint | 3.6 s | 1.3 s |
| Total Blocking Time | 0 ms | 0 ms |
| Cumulative Layout Shift | 0.257 | 0.17 |
| Speed Index | 3.6 s | 1.3 s |

### GPT priority flags

- Mobile Performance is 70/100; prioritize mobile loading work before cosmetic SEO changes.
- Mobile LCP is 3.57s (>2.5s target). Inspect the LCP element, image priority/preload, server response and render-blocking resources.
- Mobile CLS is 0.257 (>0.10 target). Reserve dimensions for images/embeds and inspect late-loading fonts or injected content.

### LCP element / likely LCP-related nodes

- `XJTLU Vietnam cung cấp thông tin dành cho học sinh và phụ huynh Việt Nam về học… | section#hero > div.container > div > p.sub | <p class="sub">`

### CLS / layout-shift culprits

- `XJTLU Vietnam cung cấp thông tin dành cho học sinh và phụ huynh Việt Nam về học… | section#hero > div.container > div > p.sub | <p class="sub">`

### Mobile performance diagnostics

- **Render-blocking requests** — Est savings of 2,140 ms
- **Avoids enormous network payloads** — Total size was 270 KiB
- **Avoid long main-thread tasks** — 7 long tasks found
- **Minimize main-thread work** — 3.0 s

### Largest estimated mobile savings opportunities

- Initial server response time was short (~0.31s potential savings)

### Heaviest network resources (mobile run)

- 38 KiB · Font · `fonts.gstatic.com/s/playfairdisplay/v40/nuFiD-vYSZviVYUb_rj3ij__anPXDTzYgEM86xQ.woff2`
- 35 KiB · Document · `xjtlu-vietnam.netlify.app/`
- 23 KiB · Font · `fonts.gstatic.com/s/playfairdisplay/v40/nuFRD-vYSZviVYUb_rj3ij__anPXDTnCjmHKM4nYO7KN_pqTXtHA-X-oE0o.woff2`
- 21 KiB · Font · `fonts.gstatic.com/s/playfairdisplay/v40/nuFiD-vYSZviVYUb_rj3ij__anPXDTLYgEM86xRbPQ.woff2`
- 13 KiB · Font · `fonts.gstatic.com/s/bevietnampro/v12/QdVMSTAyLFyeg_IDWvOJmVES_HToIW81Rb0JcBao.woff2`
- 13 KiB · Font · `fonts.gstatic.com/s/bevietnampro/v12/QdVMSTAyLFyeg_IDWvOJmVES_HSQI281Rb0JcBao.woff2`
- 13 KiB · Font · `fonts.gstatic.com/s/bevietnampro/v12/QdVMSTAyLFyeg_IDWvOJmVES_HSMIG81Rb0JcBao.woff2`
- 13 KiB · Font · `fonts.gstatic.com/s/bevietnampro/v12/QdVMSTAyLFyeg_IDWvOJmVES_HTEJm81Rb0JcBao.woff2`

### Heaviest image resources (mobile run)

- 2 KiB · `data:image/webp;base64,UklGRggHAABXRUJQVlA4IPwGAAAQLQCdASqAAIAAPjEYi0QiIaERySRsIAMEsracq6LnBzP8QPnb…`
- 183 B · `data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke…`

### Failed SEO audits

_None — Lighthouse SEO category passed._

### Accessibility issues worth reviewing

- Elements with an ARIA `[role]` that require children to contain a specific `[role]` are missing some or all of those required children.
- Document does not have a main landmark.
- `<td>` elements in a large `<table>` do not have table headers.

### GPT maintenance rule

When asked to improve technical SEO/performance, inspect the cited DOM selector/snippet and the corresponding repository code before editing. Prefer fixes with measurable impact (LCP/CLS/image weight/render blocking). Re-run this workflow after changes and compare scores/metrics. Do not treat a single Lighthouse run as field performance evidence.

> Lighthouse scores are synthetic lab measurements and can vary between runs. Use them for diagnostics and trend monitoring; use Search Console/CrUX field data for actual organic/user performance when available.
