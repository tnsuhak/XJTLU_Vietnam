# XJTLU Vietnam — Google keyword research

This folder is the input layer for data-driven SEO planning.

## Target
- Search engine: Google
- Country: Vietnam
- Language: Vietnamese
- Production site: https://xjtlu-vietnam.netlify.app/

## Workflow
1. In Google Ads Keyword Planner, use **Discover new keywords**.
2. Set location to **Vietnam**, language to **Vietnamese**, and use Google search.
3. Start with the seed keywords in `config.json`.
4. Download the keyword ideas as CSV.
5. Put the CSV in `seo-keywords/raw/` (or upload the CSV to ChatGPT and let GPT add it here).
6. GitHub Actions normalizes the export and builds:
   - `seo-keywords/latest-keywords.csv`
   - `seo-keywords/keyword-strategy.md`
7. GPT should then combine this observed demand data with:
   - current Google SERP/search intent,
   - existing page content,
   - Google Search Console query/page data,
   - Lighthouse technical data.
8. Only after that should GPT propose or apply title/H1/H2/body/FAQ/internal-link/new-page changes.

## Important rules
- Never fabricate monthly search volume.
- Keyword Planner ranges (for example 100–1K) are estimates; preserve the original value and use midpoint only for sorting.
- Search Console is site-specific observed performance, not market-wide search volume.
- Do not stuff every keyword into the homepage. Map distinct search intents to distinct pages when justified.
- Major content changes should preserve factual accuracy and existing conversion intent.
