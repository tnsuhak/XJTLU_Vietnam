from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "seo-data"
REPORT_PATH = DATA_DIR / "latest-report.md"


def load_json(name: str) -> dict:
    path = DATA_DIR / name
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def score(report: dict, category: str) -> int:
    raw = report.get("categories", {}).get(category, {}).get("score")
    if raw is None:
        return 0
    return round(raw * 100)


def metric(report: dict, audit_id: str) -> str:
    audit = report.get("audits", {}).get(audit_id, {})
    return audit.get("displayValue") or "n/a"


def opportunities(report: dict, limit: int = 6) -> list[str]:
    rows: list[tuple[float, str]] = []
    for audit in report.get("audits", {}).values():
        details = audit.get("details") or {}
        savings = details.get("overallSavingsMs")
        if not isinstance(savings, (int, float)) or savings <= 0:
            continue
        title = audit.get("title")
        if title:
            rows.append((float(savings), str(title)))
    rows.sort(reverse=True)
    return [title for _, title in rows[:limit]]


def build_section(mobile: dict, desktop: dict) -> str:
    mobile_perf = score(mobile, "performance")
    desktop_perf = score(desktop, "performance")
    mobile_seo = score(mobile, "seo")
    desktop_seo = score(desktop, "seo")

    section = [
        "## 8. Lighthouse technical SEO & performance",
        "",
        "Automated weekly Lighthouse audit of the production homepage.",
        "",
        "| Audit | Mobile | Desktop |",
        "| --- | ---: | ---: |",
        f"| Performance | {mobile_perf} | {desktop_perf} |",
        f"| SEO | {mobile_seo} | {desktop_seo} |",
        f"| Accessibility | {score(mobile, 'accessibility')} | {score(desktop, 'accessibility')} |",
        f"| Best Practices | {score(mobile, 'best-practices')} | {score(desktop, 'best-practices')} |",
        "",
        "### Core loading metrics (lab data)",
        "",
        "| Metric | Mobile | Desktop |",
        "| --- | --- | --- |",
        f"| First Contentful Paint | {metric(mobile, 'first-contentful-paint')} | {metric(desktop, 'first-contentful-paint')} |",
        f"| Largest Contentful Paint | {metric(mobile, 'largest-contentful-paint')} | {metric(desktop, 'largest-contentful-paint')} |",
        f"| Total Blocking Time | {metric(mobile, 'total-blocking-time')} | {metric(desktop, 'total-blocking-time')} |",
        f"| Cumulative Layout Shift | {metric(mobile, 'cumulative-layout-shift')} | {metric(desktop, 'cumulative-layout-shift')} |",
        f"| Speed Index | {metric(mobile, 'speed-index')} | {metric(desktop, 'speed-index')} |",
        "",
        "### Largest estimated mobile savings opportunities",
        "",
    ]

    ops = opportunities(mobile)
    if ops:
        section.extend([f"- {item}" for item in ops])
    else:
        section.append("_No material time-saving opportunities reported._")

    section.extend([
        "",
        "> Lighthouse scores are synthetic lab measurements and can vary between runs. Use them for diagnostics and trend monitoring; use Search Console/field data for actual organic performance.",
        "",
    ])
    return "\n".join(section)


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    mobile = load_json("lighthouse-mobile.json")
    desktop = load_json("lighthouse-desktop.json")
    section = build_section(mobile, desktop)

    existing = REPORT_PATH.read_text(encoding="utf-8") if REPORT_PATH.exists() else "# SEO Report\n\n"
    marker = "## 8. Lighthouse technical SEO & performance"
    if marker in existing:
        existing = existing.split(marker, 1)[0].rstrip() + "\n\n"

    REPORT_PATH.write_text(existing + section, encoding="utf-8")
    (DATA_DIR / "lighthouse-summary.md").write_text(section, encoding="utf-8")


if __name__ == "__main__":
    main()
