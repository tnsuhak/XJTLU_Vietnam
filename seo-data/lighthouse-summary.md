## 8. Lighthouse technical SEO & performance

Automated weekly Lighthouse audit of the production homepage.

| Audit | Mobile | Desktop |
| --- | ---: | ---: |
| Performance | 94 | 100 |
| SEO | 100 | 100 |
| Accessibility | 100 | 100 |
| Best Practices | 96 | 96 |

### Core loading metrics (lab data)

| Metric | Mobile | Desktop |
| --- | --- | --- |
| First Contentful Paint | 2.1 s | 0.5 s |
| Largest Contentful Paint | 2.1 s | 0.5 s |
| Total Blocking Time | 210 ms | 0 ms |
| Cumulative Layout Shift | 0.008 | 0 |
| Speed Index | 2.1 s | 0.5 s |

### GPT priority flags

- Total Blocking Time is elevated; inspect long tasks, unused JavaScript and third-party scripts.

### LCP element / likely LCP-related nodes

- `XJTLU Vietnam cung cấp thông tin dành cho học sinh và phụ huynh Việt Nam về học… | section#hero > div.container > div > p.sub | <p class="sub">`

### CLS / layout-shift culprits

- `body > iframe#nl-badge-frame | body > iframe#nl-badge-frame | <iframe sandbox="allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox" id="nl-badge-frame" srcdoc="&…`

### Mobile performance diagnostics

- **Avoids enormous network payloads** — Total size was 268 KiB
- **Avoid long main-thread tasks** — 8 long tasks found
- **Minimize main-thread work** — 3.7 s

### Largest estimated mobile savings opportunities

- Initial server response time was short (~0.23s potential savings)

### Heaviest network resources (mobile run)

- 38 KiB · Font · `fonts.gstatic.com/s/playfairdisplay/v40/nuFiD-vYSZviVYUb_rj3ij__anPXDTzYgEM86xQ.woff2`
- 36 KiB · Document · `xjtlu-vietnam.netlify.app/`
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

- Style & Layout: **1.27s**
- Other: **1.13s**
- Script Evaluation: **0.62s**
- Rendering: **0.51s**
- Parse HTML & CSS: **0.12s**
- Script Parsing & Compilation: **0.01s**

### Longest main-thread tasks

- 0.31s · `xjtlu-vietnam.netlify.app/`
- 0.25s · `xjtlu-vietnam.netlify.app/`
- 0.18s · `Unattributable`
- 0.14s · `xjtlu-vietnam.netlify.app/`
- 0.13s · `xjtlu-vietnam.netlify.app/`
- 0.08s · `xjtlu-vietnam.netlify.app/`
- 0.06s · `xjtlu-vietnam.netlify.app/`
- 0.05s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud`

### JavaScript boot-up cost

- 3.15s · `xjtlu-vietnam.netlify.app/` (eval 0.54s, parse 0.00s)
- 0.39s · `Unattributable` (eval 0.02s)
- 0.06s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud` (eval 0.05s, parse 0.01s)

### LCP phase timing

_LCP phase detail unavailable in this Lighthouse version/run._

### Interpretation rule

Prioritize the largest measured category/task first. If Style & Layout dominates, reduce above-the-fold DOM/CSS complexity. If Script Evaluation dominates, defer non-critical startup JavaScript. If Rendering/Paint dominates, simplify expensive visual effects in the first viewport. Preserve SEO copy and conversion content unless the data clearly justifies a content change.
