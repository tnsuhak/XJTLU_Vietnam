# XJTLU Vietnam — AEO / GEO maintenance rules

Last updated: 2026-09-05

## Principle

AEO/GEO is an extension of the existing SEO strategy, not a replacement for it. Google states that its normal SEO foundations remain applicable to AI Overviews and AI Mode and that no special AI-only markup or machine-readable file is required.

## Homepage architecture rule

Keep the homepage light. It should introduce XJTLU, show the most important proof points, and route users to dedicated evergreen guides. Do not rebuild long tuition, admissions, programme, 2+2, student-life, ranking, or graduate-destination explanations inside the homepage once a dedicated page exists.

Homepage pattern:

1. Short section title.
2. One short explanatory line.
3. 3–6 compact facts/cards where useful.
4. One clear internal link to the detail guide.

This improves mobile usability and preserves one primary search intent per detail page.

## Required content pattern for priority pages

For each important search-intent page:

1. Keep one clear primary search intent per page.
2. Near the top of the visible page, include one concise direct-answer block where it genuinely helps users.
3. Use a natural question that matches the page intent, followed by a factual answer in roughly 2–5 sentences.
4. Put important facts in static HTML, not only in JavaScript, images, tabs, or hidden UI.
5. Link volatile factual claims to an official or primary source whenever practical.
6. Show a visible last-updated date for answer blocks that depend on changing admissions, fees, scholarships, rankings, visa rules, or deadlines.
7. Continue with detailed explanation, tables, comparisons, and Vietnam-specific context below the short answer.
8. Maintain meaningful internal links to the next relevant page in the user journey.

## Current page map

- `/` → XJTLU brand/entity definition and light navigation hub.
- `/du-hoc-trung-quoc-2027.html` → Generic China-study hub.
- `/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html` → English-taught study in China / XJTLU-Liverpool relationship.
- `/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html` → Vietnam admissions intent.
- `/xjtlu-hoc-phi-hoc-bong-2027.html` → Tuition, scholarship and cost intent.
- `/xjtlu-2plus2-liverpool.html` → Dual degree vs 2+2 / Liverpool route.
- `/xjtlu-nganh-hoc-nghe-nghiep.html` → Programmes, careers and graduate-direction intent.
- `/xjtlu-doi-song-sinh-vien-the-thao-cau-lac-bo.html` → Student life, sports, clubs, accommodation and Suzhou context.
- `/xjtlu-ranking-2027.html` → Ranking intent.
- `/xjtlu-ket-qua-hoc-len-sau-tot-nghiep-2025.html` → Graduate destination / postgraduate outcome intent.

## Source hierarchy

Prefer, in order:

1. XJTLU official pages and official admissions publications.
2. University of Liverpool official pages for Liverpool-specific partnership/degree facts.
3. Official ranking publisher pages for ranking claims (QS, THE, ARWU).
4. Chinese government / embassy / visa-centre sources for visa rules.
5. TNS/SOS first-party experience only when it is clearly labelled as experience, not as an official university rule.

## Do not do

- Do not add `llms.txt` or AI-only text files merely for Google visibility.
- Do not invent a special GEO schema. Structured data must match visible page content.
- Do not mass-produce thin FAQ pages or near-duplicate pages for every query variation.
- Do not repeat the same high-volume keyword across every page; follow the keyword-to-page map in `strategy-2026-08-30.md` and `config.json`.
- Do not use University of Liverpool or Xi'an Jiaotong University rankings as if they were XJTLU's own ranking.
- Do not present volatile fees, scholarships, entry criteria, deadlines, ranking figures, visa rules, club counts, or facility details without checking the latest primary source or applicable official material.
- Do not move full detail-page copy back into the homepage merely to increase word count.

## Measurement

Continue tracking normal Search Console metrics and Lighthouse. Where Google Search Console exposes generative-AI visibility reporting for the property, use it as an additional signal rather than replacing normal impressions, clicks, CTR, queries, landing pages, and average position.

## Editorial goal

Create pages that a Vietnamese student or parent can understand quickly and that an AI system can quote accurately: clear entity names, direct answers, primary-source evidence, useful Vietnam-specific context, and enough detail to satisfy the full intent beyond the short answer.
