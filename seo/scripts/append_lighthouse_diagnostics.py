from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "seo-data"
REPORTS = [DATA_DIR / "latest-report.md", DATA_DIR / "lighthouse-summary.md"]
MARKER = "## 9. Deep Lighthouse diagnostics"


def load_mobile() -> dict:
    with (DATA_DIR / "lighthouse-mobile.json").open("r", encoding="utf-8") as f:
        return json.load(f)


def audit(report: dict, audit_id: str) -> dict:
    return report.get("audits", {}).get(audit_id, {}) or {}


def seconds(ms: object) -> str:
    if not isinstance(ms, (int, float)):
        return "n/a"
    return f"{float(ms) / 1000:.2f}s"


def short_url(value: object, limit: int = 120) -> str:
    text = str(value or "")
    if not text:
        return "unattributed"
    try:
        p = urlparse(text)
        label = (p.netloc + p.path) if p.netloc else text
    except Exception:
        label = text
    return label if len(label) <= limit else label[: limit - 1] + "…"


def mainthread_rows(report: dict) -> list[str]:
    items = (audit(report, "mainthread-work-breakdown").get("details") or {}).get("items") or []
    rows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        duration = item.get("duration")
        if not isinstance(duration, (int, float)):
            continue
        label = item.get("groupLabel") or item.get("group") or "Other"
        rows.append((float(duration), f"{label}: **{seconds(duration)}**"))
    rows.sort(reverse=True)
    return [text for _, text in rows[:10]]


def long_task_rows(report: dict) -> list[str]:
    items = (audit(report, "long-tasks").get("details") or {}).get("items") or []
    rows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        duration = item.get("duration")
        if not isinstance(duration, (int, float)):
            continue
        url = item.get("url") or item.get("source") or ""
        rows.append((float(duration), f"{seconds(duration)} · `{short_url(url)}`"))
    rows.sort(reverse=True)
    return [text for _, text in rows[:10]]


def bootup_rows(report: dict) -> list[str]:
    items = (audit(report, "bootup-time").get("details") or {}).get("items") or []
    rows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        total = item.get("total")
        if not isinstance(total, (int, float)):
            continue
        url = item.get("url") or ""
        eval_ms = item.get("scripting") or item.get("scriptEvaluation") or 0
        parse_ms = item.get("scriptParseCompile") or 0
        extra = []
        if isinstance(eval_ms, (int, float)) and eval_ms:
            extra.append(f"eval {seconds(eval_ms)}")
        if isinstance(parse_ms, (int, float)) and parse_ms:
            extra.append(f"parse {seconds(parse_ms)}")
        suffix = f" ({', '.join(extra)})" if extra else ""
        rows.append((float(total), f"{seconds(total)} · `{short_url(url)}`{suffix}"))
    rows.sort(reverse=True)
    return [text for _, text in rows[:8]]


def lcp_breakdown(report: dict) -> list[str]:
    rows: list[str] = []
    for audit_id in ("lcp-breakdown-insight", "lcp-phases", "largest-contentful-paint-element"):
        item = audit(report, audit_id)
        details = item.get("details") or {}
        items = details.get("items") or []
        for obj in items:
            if not isinstance(obj, dict):
                continue
            for key, value in obj.items():
                if isinstance(value, (int, float)) and any(token in key.lower() for token in ("time", "delay", "duration", "ttfb", "load", "render")):
                    rows.append(f"{key}: **{seconds(value)}**")
            if rows:
                return rows[:10]
    return rows


def build(report: dict) -> str:
    main_rows = mainthread_rows(report)
    long_rows = long_task_rows(report)
    boot_rows = bootup_rows(report)
    lcp_rows = lcp_breakdown(report)

    out = [
        MARKER,
        "",
        "This section exposes the underlying mobile Lighthouse timing breakdown so future GPT edits can target measured bottlenecks rather than guessed causes.",
        "",
        "### Main-thread work breakdown",
        "",
    ]
    out.extend([f"- {x}" for x in main_rows] if main_rows else ["_Breakdown unavailable in this run._"])
    out += ["", "### Longest main-thread tasks", ""]
    out.extend([f"- {x}" for x in long_rows] if long_rows else ["_No long-task detail available._"])
    out += ["", "### JavaScript boot-up cost", ""]
    out.extend([f"- {x}" for x in boot_rows] if boot_rows else ["_No meaningful boot-up detail available._"])
    out += ["", "### LCP phase timing", ""]
    out.extend([f"- {x}" for x in lcp_rows] if lcp_rows else ["_LCP phase detail unavailable in this Lighthouse version/run._"])
    out += [
        "",
        "### Interpretation rule",
        "",
        "Prioritize the largest measured category/task first. If Style & Layout dominates, reduce above-the-fold DOM/CSS complexity. If Script Evaluation dominates, defer non-critical startup JavaScript. If Rendering/Paint dominates, simplify expensive visual effects in the first viewport. Preserve SEO copy and conversion content unless the data clearly justifies a content change.",
        "",
    ]
    return "\n".join(out)


def append_to(path: Path, section: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if MARKER in text:
        text = text.split(MARKER, 1)[0].rstrip() + "\n\n"
    path.write_text(text + section, encoding="utf-8")


def main() -> None:
    report = load_mobile()
    section = build(report)
    for path in REPORTS:
        append_to(path, section)


if __name__ == "__main__":
    main()
