## 8. Lighthouse technical SEO & performance

Automated weekly Lighthouse audit of the production homepage.

| Audit | Mobile | Desktop |
| --- | ---: | ---: |
| Performance | 97 | 100 |
| SEO | 100 | 100 |
| Accessibility | 100 | 100 |
| Best Practices | 96 | 96 |

### Core loading metrics (lab data)

| Metric | Mobile | Desktop |
| --- | --- | --- |
| First Contentful Paint | 1.8 s | 0.6 s |
| Largest Contentful Paint | 1.8 s | 0.6 s |
| Total Blocking Time | 140 ms | 0 ms |
| Cumulative Layout Shift | 0.007 | 0.001 |
| Speed Index | 1.8 s | 0.6 s |

### GPT priority flags

_No priority performance thresholds exceeded._

### LCP element / likely LCP-related nodes

- `Xi'an Jiaotong-Liverpool University (XJTLU) là đại học quốc tế Anh – Trung tại … | section#hero > div.container > div > p.sub | <p class="sub">`

### CLS / layout-shift culprits

- `Powered by Netlify | body > div.nl-wrap | <div class="nl-wrap">`
- `+ | div.hero-facts > div.fact > b > span.g | <span class="g">`
- `body > iframe#nl-badge-frame | body > iframe#nl-badge-frame | <iframe id="nl-badge-frame" srcdoc="&lt;!doctype html&gt;&lt;html class=&quot;nl-narrow&quot;&gt;&lt;head&gt;&lt;meta…`

### Mobile performance diagnostics

- **Avoids enormous network payloads** — Total size was 268 KiB
- **Avoid long main-thread tasks** — 12 long tasks found
- **Minimize main-thread work** — 3.4 s

### Largest estimated mobile savings opportunities

- Initial server response time was short (~0.13s potential savings)

### Heaviest network resources (mobile run)

- 38 KiB · Font · `fonts.gstatic.com/s/playfairdisplay/v40/nuFiD-vYSZviVYUb_rj3ij__anPXDTzYgEM86xQ.woff2`
- 26 KiB · Document · `xjtlu-vietnam.netlify.app/`
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

_No failed weighted accessibility audits._

### GPT maintenance rule

When asked to improve technical SEO/performance, inspect the cited DOM selector/snippet and the corresponding repository code before editing. Prefer fixes with measurable impact (LCP/CLS/image weight/render blocking). Re-run this workflow after changes and compare scores/metrics. Do not treat a single Lighthouse run as field performance evidence.

> Lighthouse scores are synthetic lab measurements and can vary between runs. Use them for diagnostics and trend monitoring; use Search Console/CrUX field data for actual organic/user performance when available.
## 9. Deep Lighthouse diagnostics

This section exposes the underlying mobile Lighthouse timing breakdown so future GPT edits can target measured bottlenecks rather than guessed causes.

### Main-thread work breakdown

- Other: **1.10s**
- Style & Layout: **0.87s**
- Script Evaluation: **0.84s**
- Rendering: **0.42s**
- Parse HTML & CSS: **0.18s**
- Script Parsing & Compilation: **0.01s**
- Garbage Collection: **0.00s**

### Longest main-thread tasks

- 0.31s · `xjtlu-vietnam.netlify.app/`
- 0.25s · `xjtlu-vietnam.netlify.app/`
- 0.18s · `Unattributable`
- 0.09s · `xjtlu-vietnam.netlify.app/`
- 0.09s · `xjtlu-vietnam.netlify.app/`
- 0.09s · `xjtlu-vietnam.netlify.app/`
- 0.09s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud`
- 0.07s · `xjtlu-vietnam.netlify.app/`
- 0.06s · `Unattributable`
- 0.06s · `Unattributable`

### JavaScript boot-up cost

- 2.64s · `xjtlu-vietnam.netlify.app/` (eval 0.66s, parse 0.00s)
- 0.44s · `Unattributable` (eval 0.03s)
- 0.31s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud` (eval 0.14s, parse 0.01s)

### LCP phase timing

_LCP phase detail unavailable in this Lighthouse version/run._

### Interpretation rule

Prioritize the largest measured category/task first. If Style & Layout dominates, reduce above-the-fold DOM/CSS complexity. If Script Evaluation dominates, defer non-critical startup JavaScript. If Rendering/Paint dominates, simplify expensive visual effects in the first viewport. Preserve SEO copy and conversion content unless the data clearly justifies a content change.
