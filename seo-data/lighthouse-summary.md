## 8. Lighthouse technical SEO & performance

Automated weekly Lighthouse audit of the production homepage.

| Audit | Mobile | Desktop |
| --- | ---: | ---: |
| Performance | 98 | 93 |
| SEO | 100 | 100 |
| Accessibility | 96 | 96 |
| Best Practices | 100 | 100 |

### Core loading metrics (lab data)

| Metric | Mobile | Desktop |
| --- | --- | --- |
| First Contentful Paint | 1.9 s | 1.3 s |
| Largest Contentful Paint | 1.9 s | 1.3 s |
| Total Blocking Time | 0 ms | 0 ms |
| Cumulative Layout Shift | 0.036 | 0.004 |
| Speed Index | 1.9 s | 1.3 s |

### GPT priority flags

_No priority performance thresholds exceeded._

### LCP element / likely LCP-related nodes

- `Xi'an Jiaotong–Liverpool University (XJTLU) là đại học Anh–Trung tại Tô Châu. S… | section#hero > div.container > div > p.sub | <p class="sub">`

### CLS / layout-shift culprits

- `28.000+ sinh viên 100+ chương trình đào tạo 90+ quốc gia có sinh viên theo học … | section#hero > div.container > div > div.hero-facts | <div class="hero-facts">`
- `Powered by Netlify | body > div.nl-wrap | <div class="nl-wrap">`
- `+ | div.hero-facts > div.fact > b > span.g | <span class="g">`

### Mobile performance diagnostics

- **Avoids enormous network payloads** — Total size was 257 KiB
- **Avoid long main-thread tasks** — 4 long tasks found
- **Minimizes main-thread work** — 1.9 s

### Largest estimated mobile savings opportunities

- Initial server response time was short (~0.06s potential savings)

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
- 423 B · `xjtlu-vietnam.netlify.app/favicon.svg`

### Failed SEO audits

_None — Lighthouse SEO category passed._

### Accessibility issues worth reviewing

- Background and foreground colors do not have a sufficient contrast ratio.

### GPT maintenance rule

When asked to improve technical SEO/performance, inspect the cited DOM selector/snippet and the corresponding repository code before editing. Prefer fixes with measurable impact (LCP/CLS/image weight/render blocking). Re-run this workflow after changes and compare scores/metrics. Do not treat a single Lighthouse run as field performance evidence.

> Lighthouse scores are synthetic lab measurements and can vary between runs. Use them for diagnostics and trend monitoring; use Search Console/CrUX field data for actual organic/user performance when available.
## 9. Deep Lighthouse diagnostics

This section exposes the underlying mobile Lighthouse timing breakdown so future GPT edits can target measured bottlenecks rather than guessed causes.

### Main-thread work breakdown

- Style & Layout: **0.75s**
- Other: **0.56s**
- Rendering: **0.34s**
- Script Evaluation: **0.23s**
- Parse HTML & CSS: **0.04s**
- Script Parsing & Compilation: **0.02s**

### Longest main-thread tasks

- 0.13s · `xjtlu-vietnam.netlify.app/`
- 0.07s · `xjtlu-vietnam.netlify.app/`
- 0.06s · `xjtlu-vietnam.netlify.app/`
- 0.06s · `xjtlu-vietnam.netlify.app/`

### JavaScript boot-up cost

- 1.55s · `xjtlu-vietnam.netlify.app/` (eval 0.18s, parse 0.00s)
- 0.23s · `Unattributable` (eval 0.01s)
- 0.15s · `xjtlu-vietnam.netlify.app/.netlify/scripts/hud` (eval 0.03s, parse 0.01s)

### LCP phase timing

_LCP phase detail unavailable in this Lighthouse version/run._

### Interpretation rule

Prioritize the largest measured category/task first. If Style & Layout dominates, reduce above-the-fold DOM/CSS complexity. If Script Evaluation dominates, defer non-critical startup JavaScript. If Rendering/Paint dominates, simplify expensive visual effects in the first viewport. Preserve SEO copy and conversion content unless the data clearly justifies a content change.
