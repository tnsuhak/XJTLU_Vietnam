## 8. Lighthouse technical SEO & performance

Automated weekly Lighthouse audit of the production homepage.

| Audit | Mobile | Desktop |
| --- | ---: | ---: |
| Performance | 76 | 100 |
| SEO | 100 | 100 |
| Accessibility | 100 | 100 |
| Best Practices | 96 | 96 |

### Core loading metrics (lab data)

| Metric | Mobile | Desktop |
| --- | --- | --- |
| First Contentful Paint | 4.2 s | 0.5 s |
| Largest Contentful Paint | 4.2 s | 0.5 s |
| Total Blocking Time | 0 ms | 0 ms |
| Cumulative Layout Shift | 0.001 | 0.002 |
| Speed Index | 4.2 s | 0.5 s |

### GPT priority flags

- Mobile Performance is 76/100; prioritize mobile loading work before cosmetic SEO changes.
- Mobile LCP is 4.17s (>2.5s target). Inspect the LCP element, image priority/preload, server response and render-blocking resources.

### LCP element / likely LCP-related nodes

- `XJTLU Vietnam cung cấp thông tin dành cho học sinh và phụ huynh Việt Nam về học… | section#hero > div.container > div > p.sub | <p class="sub">`

### CLS / layout-shift culprits

- `Chat Zalo | body > header#nav > div.container > div.nav-cta | <div class="nav-cta">`
- `head > link | head > link | <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">`

### Mobile performance diagnostics

- **Avoids enormous network payloads** — Total size was 272 KiB
- **Avoid long main-thread tasks** — 7 long tasks found
- **Minimize main-thread work** — 3.3 s

### Largest estimated mobile savings opportunities

- Initial server response time was short (~0.12s potential savings)

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

_No failed weighted accessibility audits._

### GPT maintenance rule

When asked to improve technical SEO/performance, inspect the cited DOM selector/snippet and the corresponding repository code before editing. Prefer fixes with measurable impact (LCP/CLS/image weight/render blocking). Re-run this workflow after changes and compare scores/metrics. Do not treat a single Lighthouse run as field performance evidence.

> Lighthouse scores are synthetic lab measurements and can vary between runs. Use them for diagnostics and trend monitoring; use Search Console/CrUX field data for actual organic/user performance when available.
## 9. Deep Lighthouse diagnostics

This section exposes the underlying mobile Lighthouse timing breakdown so future GPT edits can target measured bottlenecks rather than guessed causes.

### Main-thread work breakdown

- Script Evaluation: **1.30s**
- Other: **0.96s**
- Style & Layout: **0.68s**
- Rendering: **0.30s**
- Parse HTML & CSS: **0.03s**
- Script Parsing & Compilation: **0.02s**

### Longest main-thread tasks

- 0.77s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud`
- 0.32s · `Unattributable`
- 0.24s · `xjtlu-vietnam.netlify.app/`
- 0.20s · `xjtlu-vietnam.netlify.app/`
- 0.12s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud`
- 0.06s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud`
- 0.06s · `Unattributable`

### JavaScript boot-up cost

- 1.65s · `xjtlu-vietnam.netlify.app/` (eval 0.46s, parse 0.00s)
- 1.14s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud` (eval 0.83s, parse 0.02s)
- 0.49s · `Unattributable` (eval 0.00s)

### LCP phase timing

_LCP phase detail unavailable in this Lighthouse version/run._

### Interpretation rule

Prioritize the largest measured category/task first. If Style & Layout dominates, reduce above-the-fold DOM/CSS complexity. If Script Evaluation dominates, defer non-critical startup JavaScript. If Rendering/Paint dominates, simplify expensive visual effects in the first viewport. Preserve SEO copy and conversion content unless the data clearly justifies a content change.
