from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

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


def audit(report: dict, audit_id: str) -> dict:
    return report.get("audits", {}).get(audit_id, {}) or {}


def metric(report: dict, audit_id: str) -> str:
    item = audit(report, audit_id)
    return item.get("displayValue") or "n/a"


def numeric(report: dict, audit_id: str) -> float | None:
    value = audit(report, audit_id).get("numericValue")
    return float(value) if isinstance(value, (int, float)) else None


def short(text: object, limit: int = 180) -> str:
    value = " ".join(str(text or "").split())
    return value if len(value) <= limit else value[: limit - 1] + "…"


def human_bytes(value: object) -> str:
    if not isinstance(value, (int, float)):
        return ""
    value = float(value)
    if value >= 1024 * 1024:
        return f"{value / (1024 * 1024):.1f} MiB"
    if value >= 1024:
        return f"{value / 1024:.0f} KiB"
    return f"{value:.0f} B"


def collect_nodes(value: object, out: list[str], limit: int = 5) -> None:
    if len(out) >= limit:
        return
    if isinstance(value, dict):
        if any(k in value for k in ("selector", "snippet", "nodeLabel")):
            pieces = []
            if value.get("nodeLabel"):
                pieces.append(str(value["nodeLabel"]))
            if value.get("selector"):
                pieces.append(str(value["selector"]))
            if value.get("snippet"):
                pieces.append(str(value["snippet"]))
            text = short(" | ".join(pieces))
            if text and text not in out:
                out.append(text)
        for child in value.values():
            collect_nodes(child, out, limit)
    elif isinstance(value, list):
        for child in value:
            collect_nodes(child, out, limit)


def audit_nodes(report: dict, audit_ids: list[str], limit: int = 5) -> list[str]:
    nodes: list[str] = []
    for audit_id in audit_ids:
        collect_nodes(audit(report, audit_id).get("details"), nodes, limit)
        if nodes:
            break
    return nodes


def opportunities(report: dict, limit: int = 8) -> list[str]:
    rows: list[tuple[float, str]] = []
    for item in report.get("audits", {}).values():
        details = item.get("details") or {}
        ms = details.get("overallSavingsMs")
        b = details.get("overallSavingsBytes")
        weight = 0.0
        suffix = ""
        if isinstance(ms, (int, float)) and ms > 0:
            weight += float(ms)
            suffix += f" (~{float(ms) / 1000:.2f}s potential savings)"
        if isinstance(b, (int, float)) and b > 0:
            weight += float(b) / 1000
            suffix += f" ({human_bytes(b)} potential transfer savings)"
        if weight <= 0:
            continue
        title = item.get("title")
        if title:
            rows.append((weight, f"{title}{suffix}"))
    rows.sort(reverse=True)
    return [text for _, text in rows[:limit]]


def top_network_requests(report: dict, limit: int = 8) -> list[str]:
    details = audit(report, "network-requests").get("details") or {}
    items = details.get("items") or []
    rows: list[tuple[float, str]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        url = item.get("url")
        size = item.get("transferSize") or item.get("resourceSize") or 0
        if not url or not isinstance(size, (int, float)):
            continue
        kind = item.get("resourceType") or item.get("mimeType") or "resource"
        parsed = urlparse(str(url))
        label = parsed.netloc + parsed.path if parsed.netloc else str(url)
        rows.append((float(size), f"{human_bytes(size)} · {kind} · `{short(label, 135)}`"))
    rows.sort(reverse=True)
    return [text for _, text in rows[:limit]]


def image_requests(report: dict, limit: int = 8) -> list[str]:
    details = audit(report, "network-requests").get("details") or {}
    items = details.get("items") or []
    rows: list[tuple[float, str]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        kind = str(item.get("resourceType") or "").lower()
        mime = str(item.get("mimeType") or "").lower()
        if kind != "image" and not mime.startswith("image/"):
            continue
        url = item.get("url")
        size = item.get("transferSize") or item.get("resourceSize") or 0
        if not url or not isinstance(size, (int, float)):
            continue
        parsed = urlparse(str(url))
        label = parsed.netloc + parsed.path if parsed.netloc else str(url)
        rows.append((float(size), f"{human_bytes(size)} · `{short(label, 145)}`"))
    rows.sort(reverse=True)
    return [text for _, text in rows[:limit]]


def failed_category_audits(report: dict, category: str, limit: int = 8) -> list[str]:
    refs = report.get("categories", {}).get(category, {}).get("auditRefs", []) or []
    rows: list[str] = []
    for ref in refs:
        audit_id = ref.get("id") if isinstance(ref, dict) else None
        if not audit_id:
            continue
        item = audit(report, str(audit_id))
        raw_score = item.get("score")
        if raw_score is None or raw_score == 1:
            continue
        title = item.get("title") or audit_id
        display = item.get("displayValue")
        rows.append(f"{title}" + (f" — {display}" if display else ""))
        if len(rows) >= limit:
            break
    return rows


def selected_diagnostics(report: dict) -> list[str]:
    ids = [
        "render-blocking-resources",
        "render-blocking-insight",
        "image-delivery-insight",
        "uses-optimized-images",
        "uses-responsive-images",
        "modern-image-formats",
        "offscreen-images",
        "unsized-images",
        "font-display",
        "unused-css-rules",
        "unused-javascript",
        "total-byte-weight",
        "dom-size",
        "third-party-summary",
        "long-tasks",
        "mainthread-work-breakdown",
    ]
    rows: list[str] = []
    for audit_id in ids:
        item = audit(report, audit_id)
        if not item:
            continue
        raw_score = item.get("score")
        display = item.get("displayValue")
        details = item.get("details") or {}
        savings_ms = details.get("overallSavingsMs")
        savings_b = details.get("overallSavingsBytes")
        important = raw_score not in (None, 1) or bool(display) or bool(savings_ms) or bool(savings_b)
        if not important:
            continue
        extras = []
        if display:
            extras.append(str(display))
        if isinstance(savings_ms, (int, float)) and savings_ms > 0:
            extras.append(f"save ~{float(savings_ms) / 1000:.2f}s")
        if isinstance(savings_b, (int, float)) and savings_b > 0:
            extras.append(f"save {human_bytes(savings_b)}")
        title = item.get("title") or audit_id
        rows.append(f"**{title}**" + (" — " + "; ".join(extras) if extras else ""))
    return rows[:12]


def build_action_flags(mobile: dict) -> list[str]:
    flags: list[str] = []
    lcp = numeric(mobile, "largest-contentful-paint")
    cls = numeric(mobile, "cumulative-layout-shift")
    perf = score(mobile, "performance")
    if perf and perf < 90:
        flags.append(f"Mobile Performance is {perf}/100; prioritize mobile loading work before cosmetic SEO changes.")
    if lcp is not None and lcp > 2500:
        flags.append(f"Mobile LCP is {lcp / 1000:.2f}s (>2.5s target). Inspect the LCP element, image priority/preload, server response and render-blocking resources.")
    if cls is not None and cls > 0.1:
        flags.append(f"Mobile CLS is {cls:.3f} (>0.10 target). Reserve dimensions for images/embeds and inspect late-loading fonts or injected content.")
    if numeric(mobile, "total-blocking-time") is not None and (numeric(mobile, "total-blocking-time") or 0) > 200:
        flags.append("Total Blocking Time is elevated; inspect long tasks, unused JavaScript and third-party scripts.")
    return flags


def build_section(mobile: dict, desktop: dict) -> str:
    section = [
        "## 8. Lighthouse technical SEO & performance",
        "",
        "Automated weekly Lighthouse audit of the production homepage.",
        "",
        "| Audit | Mobile | Desktop |",
        "| --- | ---: | ---: |",
        f"| Performance | {score(mobile, 'performance')} | {score(desktop, 'performance')} |",
        f"| SEO | {score(mobile, 'seo')} | {score(desktop, 'seo')} |",
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
        "### GPT priority flags",
        "",
    ]

    flags = build_action_flags(mobile)
    section.extend([f"- {item}" for item in flags] if flags else ["_No priority performance thresholds exceeded._"])

    section.extend(["", "### LCP element / likely LCP-related nodes", ""])
    lcp_nodes = audit_nodes(mobile, [
        "largest-contentful-paint-element",
        "lcp-discovery-insight",
        "lcp-breakdown-insight",
        "lcp-phases",
    ])
    section.extend([f"- `{short(item, 220)}`" for item in lcp_nodes] if lcp_nodes else ["_Lighthouse did not expose a specific LCP node in this run._"])

    section.extend(["", "### CLS / layout-shift culprits", ""])
    cls_nodes = audit_nodes(mobile, ["layout-shifts", "cls-culprits-insight", "unsized-images"], limit=8)
    section.extend([f"- `{short(item, 220)}`" for item in cls_nodes] if cls_nodes else ["_No specific layout-shift node was exposed in this run._"])

    section.extend(["", "### Mobile performance diagnostics", ""])
    diagnostics = selected_diagnostics(mobile)
    section.extend([f"- {item}" for item in diagnostics] if diagnostics else ["_No additional failed diagnostics reported._"])

    section.extend(["", "### Largest estimated mobile savings opportunities", ""])
    ops = opportunities(mobile)
    section.extend([f"- {item}" for item in ops] if ops else ["_No material time/transfer savings opportunities reported._"])

    section.extend(["", "### Heaviest network resources (mobile run)", ""])
    resources = top_network_requests(mobile)
    section.extend([f"- {item}" for item in resources] if resources else ["_Network request details unavailable._"])

    section.extend(["", "### Heaviest image resources (mobile run)", ""])
    images = image_requests(mobile)
    section.extend([f"- {item}" for item in images] if images else ["_Image request details unavailable._"])

    section.extend(["", "### Failed SEO audits", ""])
    seo_failures = failed_category_audits(mobile, "seo")
    section.extend([f"- {item}" for item in seo_failures] if seo_failures else ["_None — Lighthouse SEO category passed._"])

    section.extend(["", "### Accessibility issues worth reviewing", ""])
    accessibility_failures = failed_category_audits(mobile, "accessibility", limit=6)
    section.extend([f"- {item}" for item in accessibility_failures] if accessibility_failures else ["_No failed weighted accessibility audits._"])

    section.extend([
        "",
        "### GPT maintenance rule",
        "",
        "When asked to improve technical SEO/performance, inspect the cited DOM selector/snippet and the corresponding repository code before editing. Prefer fixes with measurable impact (LCP/CLS/image weight/render blocking). Re-run this workflow after changes and compare scores/metrics. Do not treat a single Lighthouse run as field performance evidence.",
        "",
        "> Lighthouse scores are synthetic lab measurements and can vary between runs. Use them for diagnostics and trend monitoring; use Search Console/CrUX field data for actual organic/user performance when available.",
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
