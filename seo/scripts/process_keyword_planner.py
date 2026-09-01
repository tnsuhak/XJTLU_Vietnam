from __future__ import annotations

import csv
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "seo-keywords" / "raw"
OUT_CSV = ROOT / "seo-keywords" / "latest-keywords.csv"
OUT_MD = ROOT / "seo-keywords" / "keyword-strategy.md"

ALIASES = {
    "keyword": ["keyword", "từ khóa"],
    "avg_monthly": [
        "avg. monthly searches",
        "average monthly searches",
        "số lượt tìm kiếm trung bình hằng tháng",
        "số lượt tìm kiếm trung bình hàng tháng",
    ],
    "competition": ["competition", "mức độ cạnh tranh"],
    "competition_index": ["competition (indexed value)", "mức độ cạnh tranh (giá trị được lập chỉ mục)"],
    "three_month": ["three month change", "thay đổi trong 3 tháng"],
    "yoy": ["yoy change", "year over year change", "thay đổi so với cùng kỳ năm trước"],
    "bid_low": ["top of page bid (low range)", "giá thầu đầu trang (phạm vi thấp)"],
    "bid_high": ["top of page bid (high range)", "giá thầu đầu trang (phạm vi cao)"],
}


def norm(s: str) -> str:
    return " ".join((s or "").strip().lower().split())


def find_column(headers: list[str], names: list[str]) -> str | None:
    lookup = {norm(h): h for h in headers}
    for n in names:
        if norm(n) in lookup:
            return lookup[norm(n)]
    return None


def parse_num(text: str | None) -> float | None:
    if text is None:
        return None
    s = str(text).strip().replace("\u00a0", " ")
    if not s or s in {"-", "—", "--"}:
        return None
    s = s.replace(",", "")
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    return float(m.group()) if m else None


def parse_volume(text: str | None) -> tuple[str, float | None, float | None, float | None]:
    raw = (text or "").strip()
    if not raw:
        return "", None, None, None
    s = raw.lower().replace(",", "").replace("–", "-").replace("—", "-")

    def unit(v: float, suffix: str | None) -> float:
        if suffix == "k":
            return v * 1_000
        if suffix == "m":
            return v * 1_000_000
        return v

    rm = re.match(r"\s*(\d+(?:\.\d+)?)\s*([km])?\s*-\s*(\d+(?:\.\d+)?)\s*([km])?\s*$", s)
    if rm:
        lo = unit(float(rm.group(1)), rm.group(2))
        hi = unit(float(rm.group(3)), rm.group(4))
        return raw, lo, hi, (lo + hi) / 2

    sm = re.match(r"\s*(\d+(?:\.\d+)?)\s*([km])?\s*$", s)
    if sm:
        v = unit(float(sm.group(1)), sm.group(2))
        return raw, v, v, v

    v = parse_num(raw)
    return raw, v, v, v


def basic_intent(keyword: str) -> str:
    k = keyword.lower()
    commercial = ["học phí", "học bổng", "tuyển sinh", "điều kiện", "chi phí", "admission", "apply", "visa"]
    brand = ["xjtlu", "jiaotong-liverpool", "liverpool china"]
    info = ["du học", "ngành học", "ranking", "đại học", "tô châu", "suzhou"]
    if any(x in k for x in commercial):
        return "high-intent"
    if any(x in k for x in brand):
        return "brand"
    if any(x in k for x in info):
        return "informational"
    return "mixed"


def opportunity_score(volume_mid: float | None, competition_index: float | None, intent: str) -> float:
    vol = 0.0 if not volume_mid or volume_mid <= 0 else min(60.0, math.log10(volume_mid + 1) * 20)
    comp = 50.0 if competition_index is None else max(0.0, min(100.0, competition_index))
    ease = (100.0 - comp) * 0.20
    intent_bonus = {"high-intent": 20.0, "brand": 16.0, "informational": 8.0, "mixed": 5.0}[intent]
    return round(vol + ease + intent_bonus, 1)


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(RAW_DIR.glob("*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        raise SystemExit("No Keyword Planner CSV found in seo-keywords/raw/")
    src = files[0]

    text = src.read_text(encoding="utf-8-sig", errors="replace")
    sample = text[:10000]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel

    reader = csv.DictReader(text.splitlines(), dialect=dialect)
    headers = reader.fieldnames or []
    cols = {key: find_column(headers, aliases) for key, aliases in ALIASES.items()}
    if not cols["keyword"]:
        raise SystemExit(f"Could not find keyword column. Headers: {headers}")

    rows = []
    for r in reader:
        kw = (r.get(cols["keyword"] or "") or "").strip()
        if not kw:
            continue
        raw_vol, lo, hi, mid = parse_volume(r.get(cols["avg_monthly"] or "") if cols["avg_monthly"] else "")
        ci = parse_num(r.get(cols["competition_index"] or "") if cols["competition_index"] else None)
        intent = basic_intent(kw)
        rows.append({
            "keyword": kw,
            "avg_monthly_searches_raw": raw_vol,
            "volume_low": "" if lo is None else round(lo),
            "volume_high": "" if hi is None else round(hi),
            "volume_mid_for_sorting": "" if mid is None else round(mid),
            "competition": (r.get(cols["competition"] or "") or "").strip() if cols["competition"] else "",
            "competition_index": "" if ci is None else ci,
            "three_month_change": (r.get(cols["three_month"] or "") or "").strip() if cols["three_month"] else "",
            "yoy_change": (r.get(cols["yoy"] or "") or "").strip() if cols["yoy"] else "",
            "top_page_bid_low": (r.get(cols["bid_low"] or "") or "").strip() if cols["bid_low"] else "",
            "top_page_bid_high": (r.get(cols["bid_high"] or "") or "").strip() if cols["bid_high"] else "",
            "basic_intent": intent,
            "opportunity_score": opportunity_score(mid, ci, intent),
        })

    rows.sort(key=lambda x: (float(x["opportunity_score"]), float(x["volume_mid_for_sorting"] or 0)), reverse=True)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys()) if rows else ["keyword"]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    top = rows[:40]
    lines = [
        "# XJTLU Vietnam — Google keyword demand report",
        "",
        f"- Source file: `{src.name}`",
        "- Market: Vietnam",
        "- Language: Vietnamese",
        "- Search engine: Google",
        "- Important: Keyword Planner values are estimates/ranges. `volume_mid_for_sorting` is only a sorting aid, not a claimed exact search volume.",
        "",
        "## Top keyword opportunities from observed Keyword Planner data",
        "",
        "| Keyword | Planner volume | Competition | Intent | Opportunity |",
        "| --- | ---: | --- | --- | ---: |",
    ]
    for r in top:
        lines.append(f"| {r['keyword'].replace('|','/')} | {r['avg_monthly_searches_raw'] or 'n/a'} | {r['competition'] or r['competition_index'] or 'n/a'} | {r['basic_intent']} | {r['opportunity_score']} |")

    lines += [
        "",
        "## GPT SEO planning instructions",
        "",
        "1. Treat this file as market-demand evidence from Google Keyword Planner, not as exact ground truth.",
        "2. Before editing the site, inspect the live Google SERP for the strongest candidate keywords and identify search intent and ranking page types.",
        "3. Compare candidates against current XJTLU Vietnam pages and existing GSC query/page data.",
        "4. Build a keyword-to-page map. Do not force unrelated intents onto the homepage.",
        "5. Prioritize high-intent queries (fees, scholarships, admissions, requirements) and broader discovery queries only when the site can satisfy the intent well.",
        "6. Then optimize Title, H1/H2, copy, FAQ, internal links and/or create a dedicated landing page when justified.",
        "7. Re-check factual claims against official XJTLU / University of Liverpool sources before publishing.",
        "8. After deployment, use Search Console to validate impressions, CTR and average position over time.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Processed {len(rows)} keywords from {src}")


if __name__ == "__main__":
    main()
