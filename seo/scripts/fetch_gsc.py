#!/usr/bin/env python3
import csv
import json
import os
from datetime import date, timedelta
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "seo" / "config.json"
OUT_DIR = ROOT / "seo-data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

with CONFIG_PATH.open("r", encoding="utf-8") as f:
    cfg = json.load(f)

SITE_URL = os.getenv("GSC_SITE_URL", cfg["site_url"])
TARGET_COUNTRY = cfg.get("target_country")
TARGET_COUNTRY_NAME = cfg.get("target_country_name", TARGET_COUNTRY or "All")
DAYS = int(cfg.get("days", 28))
LAG_DAYS = int(cfg.get("data_lag_days", 3))
REPORT_LIMIT = int(cfg.get("report_limit", 20))

secret = os.getenv("GSC_SERVICE_ACCOUNT_JSON")
if not secret:
    raise RuntimeError(
        "Missing GitHub secret GSC_SERVICE_ACCOUNT_JSON. "
        "Add the Google service-account JSON as a repository Actions secret."
    )

try:
    service_account_info = json.loads(secret)
except json.JSONDecodeError as exc:
    raise RuntimeError("GSC_SERVICE_ACCOUNT_JSON is not valid JSON") from exc

credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
)
service = build("searchconsole", "v1", credentials=credentials, cache_discovery=False)

end_date = date.today() - timedelta(days=LAG_DAYS)
start_date = end_date - timedelta(days=DAYS - 1)
prev_end_date = start_date - timedelta(days=1)
prev_start_date = prev_end_date - timedelta(days=DAYS - 1)


def country_filter():
    if not TARGET_COUNTRY:
        return None
    return [
        {
            "filters": [
                {
                    "dimension": "country",
                    "operator": "equals",
                    "expression": TARGET_COUNTRY,
                }
            ]
        }
    ]


def query_gsc(start, end, dimensions=None, use_country_filter=True):
    all_rows = []
    start_row = 0
    row_limit = 25000
    while True:
        body = {
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
            "rowLimit": row_limit,
            "startRow": start_row,
            "dataState": "final",
        }
        if dimensions:
            body["dimensions"] = dimensions
        if use_country_filter and TARGET_COUNTRY:
            body["dimensionFilterGroups"] = country_filter()

        response = (
            service.searchanalytics()
            .query(siteUrl=SITE_URL, body=body)
            .execute()
        )
        rows = response.get("rows", [])
        all_rows.extend(rows)
        if len(rows) < row_limit:
            break
        start_row += row_limit
    return all_rows


def one_total(start, end, filtered):
    rows = query_gsc(start, end, dimensions=None, use_country_filter=filtered)
    if not rows:
        return {"clicks": 0, "impressions": 0, "ctr": 0.0, "position": 0.0}
    row = rows[0]
    return {
        "clicks": row.get("clicks", 0),
        "impressions": row.get("impressions", 0),
        "ctr": row.get("ctr", 0.0),
        "position": row.get("position", 0.0),
    }


def rows_to_map(rows, dimensions):
    result = {}
    for row in rows:
        keys = row.get("keys", [])
        key = tuple(keys)
        result[key] = {
            "keys": keys,
            "clicks": row.get("clicks", 0),
            "impressions": row.get("impressions", 0),
            "ctr": row.get("ctr", 0.0),
            "position": row.get("position", 0.0),
        }
    return result


def merged_rows(current_rows, previous_rows, dimensions):
    cur = rows_to_map(current_rows, dimensions)
    prev = rows_to_map(previous_rows, dimensions)
    merged = []
    for key in set(cur) | set(prev):
        c = cur.get(key, {"keys": list(key), "clicks": 0, "impressions": 0, "ctr": 0.0, "position": 0.0})
        p = prev.get(key, {"keys": list(key), "clicks": 0, "impressions": 0, "ctr": 0.0, "position": 0.0})
        row = {dimensions[i]: key[i] if i < len(key) else "" for i in range(len(dimensions))}
        row.update(
            {
                "clicks": c["clicks"],
                "impressions": c["impressions"],
                "ctr": c["ctr"],
                "position": c["position"],
                "prev_clicks": p["clicks"],
                "prev_impressions": p["impressions"],
                "prev_ctr": p["ctr"],
                "prev_position": p["position"],
                "delta_clicks": c["clicks"] - p["clicks"],
                "delta_impressions": c["impressions"] - p["impressions"],
                "position_improvement": (p["position"] - c["position"]) if c["position"] and p["position"] else 0.0,
            }
        )
        merged.append(row)
    merged.sort(key=lambda r: (r["impressions"], r["clicks"]), reverse=True)
    return merged


def write_csv(filename, rows, dimensions):
    fields = dimensions + [
        "clicks",
        "impressions",
        "ctr",
        "position",
        "prev_clicks",
        "prev_impressions",
        "prev_ctr",
        "prev_position",
        "delta_clicks",
        "delta_impressions",
        "position_improvement",
    ]
    path = OUT_DIR / filename
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def pct_change(cur, prev):
    if prev == 0:
        return None if cur == 0 else 100.0
    return ((cur - prev) / prev) * 100


def fmt_change(cur, prev):
    value = pct_change(cur, prev)
    if value is None:
        return "0.0%"
    return f"{value:+.1f}%"


def md_table(headers, rows):
    if not rows:
        return "_No data yet._\n"
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        safe = [str(v).replace("|", "\\|") for v in row]
        lines.append("| " + " | ".join(safe) + " |")
    return "\n".join(lines) + "\n"


# Country-filtered data is the primary dataset for XJTLU Vietnam.
cur_queries = query_gsc(start_date, end_date, ["query"], True)
prev_queries = query_gsc(prev_start_date, prev_end_date, ["query"], True)
cur_pages = query_gsc(start_date, end_date, ["page"], True)
prev_pages = query_gsc(prev_start_date, prev_end_date, ["page"], True)
cur_query_pages = query_gsc(start_date, end_date, ["query", "page"], True)
prev_query_pages = query_gsc(prev_start_date, prev_end_date, ["query", "page"], True)

queries = merged_rows(cur_queries, prev_queries, ["query"])
pages = merged_rows(cur_pages, prev_pages, ["page"])
query_pages = merged_rows(cur_query_pages, prev_query_pages, ["query", "page"])

write_csv("google-search-console-queries.csv", queries, ["query"])
write_csv("google-search-console-pages.csv", pages, ["page"])
write_csv("google-search-console-query-pages.csv", query_pages, ["query", "page"])

cur_target_total = one_total(start_date, end_date, True)
prev_target_total = one_total(prev_start_date, prev_end_date, True)
cur_all_total = one_total(start_date, end_date, False)
prev_all_total = one_total(prev_start_date, prev_end_date, False)

min_imp = int(cfg.get("opportunity_min_impressions", 10))
min_pos = float(cfg.get("opportunity_min_position", 4))
max_pos = float(cfg.get("opportunity_max_position", 20))
low_ctr_pos = float(cfg.get("low_ctr_max_position", 10))
low_ctr = float(cfg.get("low_ctr_threshold", 0.03))

opportunities = [
    r for r in queries
    if r["impressions"] >= min_imp and min_pos <= r["position"] <= max_pos
]
opportunities.sort(key=lambda r: (r["impressions"], -r["position"]), reverse=True)

low_ctr_queries = [
    r for r in queries
    if r["impressions"] >= min_imp and 0 < r["position"] <= low_ctr_pos and r["ctr"] < low_ctr
]
low_ctr_queries.sort(key=lambda r: r["impressions"], reverse=True)

growing = [
    r for r in queries
    if r["impressions"] >= min_imp and r["delta_impressions"] > 0
]
growing.sort(key=lambda r: r["delta_impressions"], reverse=True)

top_queries = [r for r in queries if r["impressions"] > 0][:REPORT_LIMIT]
top_pages = [r for r in pages if r["impressions"] > 0][:REPORT_LIMIT]

report = []
report.append("# XJTLU Vietnam — Weekly Google Search Console SEO Report\n")
report.append(f"- Property: `{SITE_URL}`")
report.append(f"- Primary market filter: **{TARGET_COUNTRY_NAME}** (`{TARGET_COUNTRY}`)")
report.append(f"- Current period: **{start_date.isoformat()} → {end_date.isoformat()}**")
report.append(f"- Comparison period: **{prev_start_date.isoformat()} → {prev_end_date.isoformat()}**")
report.append(f"- Search Console settling lag applied: **{LAG_DAYS} days**\n")

report.append("## 1. Vietnam organic search summary\n")
report.append(md_table(
    ["Metric", "Current", "Previous", "Change"],
    [
        ["Clicks", cur_target_total["clicks"], prev_target_total["clicks"], fmt_change(cur_target_total["clicks"], prev_target_total["clicks"])],
        ["Impressions", cur_target_total["impressions"], prev_target_total["impressions"], fmt_change(cur_target_total["impressions"], prev_target_total["impressions"])],
        ["CTR", f"{cur_target_total['ctr']*100:.2f}%", f"{prev_target_total['ctr']*100:.2f}%", f"{(cur_target_total['ctr']-prev_target_total['ctr'])*100:+.2f} pp"],
        ["Avg position", f"{cur_target_total['position']:.2f}", f"{prev_target_total['position']:.2f}", f"{prev_target_total['position']-cur_target_total['position']:+.2f} better"],
    ]
))

report.append("## 2. All-country summary\n")
report.append(md_table(
    ["Metric", "Current", "Previous", "Change"],
    [
        ["Clicks", cur_all_total["clicks"], prev_all_total["clicks"], fmt_change(cur_all_total["clicks"], prev_all_total["clicks"])],
        ["Impressions", cur_all_total["impressions"], prev_all_total["impressions"], fmt_change(cur_all_total["impressions"], prev_all_total["impressions"])],
        ["CTR", f"{cur_all_total['ctr']*100:.2f}%", f"{prev_all_total['ctr']*100:.2f}%", f"{(cur_all_total['ctr']-prev_all_total['ctr'])*100:+.2f} pp"],
        ["Avg position", f"{cur_all_total['position']:.2f}", f"{prev_all_total['position']:.2f}", f"{prev_all_total['position']-cur_all_total['position']:+.2f} better"],
    ]
))

report.append("## 3. SEO opportunities — positions 4–20\n")
report.append(md_table(
    ["Query", "Impr.", "Clicks", "CTR", "Position", "Δ Impr."],
    [[r["query"], r["impressions"], r["clicks"], f"{r['ctr']*100:.2f}%", f"{r['position']:.1f}", f"{r['delta_impressions']:+d}"] for r in opportunities[:REPORT_LIMIT]]
))

report.append("## 4. High-ranking but low-CTR queries\n")
report.append(md_table(
    ["Query", "Impr.", "Clicks", "CTR", "Position"],
    [[r["query"], r["impressions"], r["clicks"], f"{r['ctr']*100:.2f}%", f"{r['position']:.1f}"] for r in low_ctr_queries[:REPORT_LIMIT]]
))

report.append("## 5. Growing queries\n")
report.append(md_table(
    ["Query", "Impr.", "Prev. Impr.", "Δ Impr.", "Position"],
    [[r["query"], r["impressions"], r["prev_impressions"], f"{r['delta_impressions']:+d}", f"{r['position']:.1f}"] for r in growing[:REPORT_LIMIT]]
))

report.append("## 6. Top Vietnam queries\n")
report.append(md_table(
    ["Query", "Impr.", "Clicks", "CTR", "Position"],
    [[r["query"], r["impressions"], r["clicks"], f"{r['ctr']*100:.2f}%", f"{r['position']:.1f}"] for r in top_queries]
))

report.append("## 7. Top Vietnam landing pages\n")
report.append(md_table(
    ["Page", "Impr.", "Clicks", "CTR", "Position"],
    [[r["page"], r["impressions"], r["clicks"], f"{r['ctr']*100:.2f}%", f"{r['position']:.1f}"] for r in top_pages]
))

report.append("## GPT maintenance instructions\n")
report.append(
    "Use this report as observed Search Console data, not as market-wide keyword volume. "
    "Prioritize real query/page data over guessed SEO metrics. Before changing content, inspect the target page and current SERP/search intent. "
    "Do not fabricate search volume. Large SEO changes should be reviewed before production deployment.\n"
)

(OUT_DIR / "latest-report.md").write_text("\n".join(report), encoding="utf-8")

metadata = {
    "site_url": SITE_URL,
    "target_country": TARGET_COUNTRY,
    "current_period": [start_date.isoformat(), end_date.isoformat()],
    "previous_period": [prev_start_date.isoformat(), prev_end_date.isoformat()],
    "generated_on": date.today().isoformat(),
    "query_rows": len(queries),
    "page_rows": len(pages),
    "query_page_rows": len(query_pages),
}
(OUT_DIR / "gsc-run-metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"GSC report generated for {SITE_URL}")
print(f"Current period: {start_date} to {end_date}")
print(f"Vietnam queries: {len(queries)}")
