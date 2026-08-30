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
| Cumulative Layout Shift | 0 | 0.003 |
| Speed Index | 4.2 s | 0.5 s |

### GPT priority flags

- Mobile Performance is 76/100; prioritize mobile loading work before cosmetic SEO changes.
- Mobile LCP is 4.20s (>2.5s target). Inspect the LCP element, image priority/preload, server response and render-blocking resources.

### LCP element / likely LCP-related nodes

- `XJTLU Vietnam cung cấp thông tin dành cho học sinh và phụ huynh Việt Nam về học… | section#hero > div.container > div > p.sub | <p class="sub">`

### CLS / layout-shift culprits

_No specific layout-shift node was exposed in this run._

### Mobile performance diagnostics

- **Avoids enormous network payloads** — Total size was 268 KiB
- **Avoid long main-thread tasks** — 8 long tasks found
- **Minimize main-thread work** — 6.3 s

### Largest estimated mobile savings opportunities

- Initial server response time was short (~0.15s potential savings)

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
