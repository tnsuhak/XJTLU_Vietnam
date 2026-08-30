# XJTLU Vietnam — AEO / GEO maintenance rules

Last updated: 2026-08-30

## Principle

AEO/GEO is an extension of the existing SEO strategy, not a replacement for it. Google states that its normal SEO foundations remain applicable to AI Overviews and AI Mode and that no special AI-only markup or machine-readable file is required.

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

## Current answer map

- `/` → What is XJTLU? Brand/entity definition.
- `/du-hoc-trung-quoc-2027.html` → Can students study in China without studying the degree in Chinese?
- `/du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html` → Can students study a university degree in English at XJTLU in China?
- `/xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html` → What does a Vietnamese student need for XJTLU Year 1 entry?
- `/xjtlu-hoc-phi-hoc-bong-2027.html` → Does XJTLU offer scholarships to international undergraduate applicants?
- `/xjtlu-ranking-2027.html` → Does XJTLU have its own ranking or use University of Liverpool's ranking?

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
- Do not repeat the same high-volume keyword across every page; follow the keyword-to-page map in `strategy-2026-08-30.md`.
- Do not use University of Liverpool or Xi'an Jiaotong University rankings as if they were XJTLU's own ranking.
- Do not present volatile fees, scholarships, entry criteria, deadlines, ranking figures, or visa rules without checking the latest primary source or the applicable official 2027 material.

## Measurement

Continue tracking normal Search Console metrics and Lighthouse. Where Google Search Console exposes generative-AI visibility reporting for the property, use it as an additional signal rather than replacing normal impressions, clicks, CTR, queries, landing pages, and average position.

## Editorial goal

Create pages that a Vietnamese student or parent can understand quickly and that an AI system can quote accurately: clear entity names, direct answers, primary-source evidence, useful Vietnam-specific context, and enough detail to satisfy the full intent beyond the short answer.
