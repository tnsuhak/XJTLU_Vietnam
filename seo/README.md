# XJTLU Vietnam — Free Google Search Console automation

This repository collects Google Search Console data automatically with GitHub Actions and stores GPT-readable reports under `/seo-data/`.

## One-time setup

1. Create or select a Google Cloud project.
2. Enable **Google Search Console API**.
3. Create a service account (suggested name: `tns-seo-bot`).
4. Create a JSON key for that service account.
5. In Google Search Console, add the service-account email as a user for `https://xjtlu-vietnam.netlify.app/` with read access.
6. In this GitHub repository, add the full JSON key as an Actions secret named exactly `GSC_SERVICE_ACCOUNT_JSON`.
7. Run **Actions → GSC SEO Monitor → Run workflow** once to test.

## Automatic schedule

The workflow runs every Monday at 09:15 Korea time (00:15 UTC).

## Generated files

- `/seo-data/latest-report.md` — GPT-friendly weekly SEO report
- `/seo-data/google-search-console-queries.csv` — Vietnam query performance
- `/seo-data/google-search-console-pages.csv` — Vietnam landing-page performance
- `/seo-data/google-search-console-query-pages.csv` — query-to-page mapping
- `/seo-data/gsc-run-metadata.json` — run metadata

The script compares the latest settled 28 days against the prior 28 days, using a 3-day data-settling lag. The primary dataset is filtered to Vietnam (`vnm`), while the Markdown report also includes an all-country summary.

## Security

Never commit the Google service-account JSON key into the repository. Store it only in GitHub Actions Secrets. The collector requests the read-only Search Console scope.

## GPT rule

Treat Search Console data as observed performance for this site, not as market-wide keyword search volume. Do not invent missing search-volume numbers. Use `/seo-data/latest-report.md` first, then inspect the CSVs and live SERPs before making material SEO changes.
