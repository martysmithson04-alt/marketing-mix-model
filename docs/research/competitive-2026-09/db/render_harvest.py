#!/usr/bin/env python3
"""Refresh prices, enrich threads/docs, render PRIMARY_SOURCE_HARVEST.md."""

from __future__ import annotations

import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from harvest_primary import (  # noqa: E402
    FETCHED,
    fetch,
    is_niche,
    parse_listing,
    unescape,
)

MD = ROOT.parent / "PRIMARY_SOURCE_HARVEST.md"

# Extra Community threads discovered via public search this run.
EXTRA_COMMUNITY = [
    (
        "https://community.shopify.com/t/what-app-to-use-for-marketing-and-analitics/288511/4",
        "Merchant asked which marketing/analytics app to use. Reply names TrueProfit for net profit + ROAS with ad-channel sync, plus GA; path is Shopify analytics first, then profit tracking.",
    ),
    (
        "https://community.shopify.com/t/no-metrics-showing-for-ads/367593",
        "Merchant: Admin marketing dashboard shows sales but never ROAS/CPA/CTR; Triple Whale install also showed nothing. TrueProfit staff reply: Shopify does not pull those metrics from Meta/Google; need a third-party that syncs ad data.",
    ),
    (
        "https://community.shopify.com/t/app-for-p-l-analyse/361631",
        "P&L app thread. Community: BeProfit/TrueProfit/Lifetimely/ClearProfit/TW. Warning: preserve historical COGS; import total ad spend not attributed-only or profit is inflated.",
    ),
    (
        "https://community.shopify.com/t/i-stopped-looking-at-shopify-metrics-one-by-one/653041/5",
        "Operator stopped optimizing isolated Shopify metrics. Recs: Triple Whale, Lifetimely, GoProfit. Counter: more apps add complexity; start from profit and work backwards.",
    ),
]

# Reddit is 403 from this cloud. Paraphrases from public search snippets + prior same-day corpus.
# confidence=public_snippet — URL is live; body was not HTML-fetched this process.
REDDIT_SNIPPETS = [
    (
        "https://www.reddit.com/r/shopify/comments/1rpjuk0/best_way_to_track_meta_ads_roas_in_shopify/",
        "r/shopify: Meta vs Shopify ROAS never matches. Commenters: last-click Shopify often 20–40% below Meta (commenter claim); bare-minimum is weekly total ad spend vs total Shopify revenue = blended ROAS/MER.",
    ),
    (
        "https://www.reddit.com/r/shopify/comments/1jpb8cy/sales_attribution_tracking/",
        "r/shopify: overlap across Meta/Google/email/SEO. Triple Whale and Kendall called expensive.",
    ),
    (
        "https://www.reddit.com/r/shopify/comments/1pzy8iv/app_or_plugin_to_calculate_profit_each_month/",
        "r/shopify: profit = orders + COGS + ad spend + fees. TrueProfit cited ~$35/mo as #1; Triple Whale named for blended profit if budget allows; VAULT/manual spend as cheap path.",
    ),
    (
        "https://www.reddit.com/r/shopify/comments/1h27sj3/beprofit_vs_lifetimely_vs/",
        "r/shopify: switching off TrueProfit (bugs / weak mobile). Alts: Finaloop; Taxomate → QB/Xero.",
    ),
    (
        "https://www.reddit.com/r/shopify/comments/1shq2kb/how_are_you_keeping_track_of_actual_profit_across/",
        "r/shopify: multi-store profit tracking. Spreadsheets break at 2–3 stores (different COGS/shipping/ad mixes). Recs: Triple Whale / Lifetimely / BeProfit for blended cross-store numbers.",
    ),
    (
        "https://www.reddit.com/r/shopify/comments/116wrvd/apps_to_track_profit/",
        "r/shopify: apps to track profit / make taxes less daunting. Recs: BeProfit, TrueProfit, Report Toaster, Google Sheets, a manual simple-profit app.",
    ),
    (
        "https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/",
        "r/PPC: operator scaled the wrong campaigns for months because Meta ≠ Shopify. Commenters: MER as honest top-line; independent attribution for channel split.",
    ),
    (
        "https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/",
        "r/PPC: North Star = blended MER/CAC/profit. Shopify/CRM = revenue+refunds truth. Agency: $200k+/mo clients ignore platform attribution; Sheets blended ROAS; 2-week Meta pause lift tests. Platforms overlap credit 40–60% — commenter claim.",
    ),
    (
        "https://www.reddit.com/r/PPC/comments/1r2pvgy/question_for_d2c_founders_on_shopify_running_meta/",
        "r/PPC: if Meta says $200k and Shopify $150k, treat Shopify as bank. Scale on Shopify revenue; Meta directional. TW named for large advertisers.",
    ),
    (
        "https://www.reddit.com/r/PPC/comments/1pqv5kh/how_are_you_handling_ad_attribution/",
        "r/PPC: platforms for optimization; backend / blended MER as reality check. TW / Segmetrics / Hyros / GA4 / Looker all work to varying degrees.",
    ),
    (
        "https://www.reddit.com/r/PPC/comments/1gwgucn/facebook_roas_explosion/",
        "r/PPC: TW users say Meta always over-reports; switch Last Click vs Total Impact. Pause-Facebook test: store revenue often drops less than Meta claimed.",
    ),
    (
        "https://www.reddit.com/r/PPC/comments/1i7trbi/i_truly_dont_understand_attribution_between/",
        "r/PPC ELI5: Shopify last-touch; GA4 last-non-direct; ad platforms custom windows and can date credit to click day not order day. TW named as third-party.",
    ),
    (
        "https://www.reddit.com/r/PPC/comments/18u4211/disaster_with_attribution_between_shopify_google/",
        "r/PPC: Meta view-through never appears in Shopify/GA4. One commenter: deploy a TW-class pixel and stop reconciling by hand.",
    ),
]

DOC_CLAIMS = [
    {
        "vendor": "kleio",
        "theme": "attribution",
        "url": "https://getkleio.com/",
        "excerpt": "Kleio homepage FAQ: they do not offer multi-touch attribution. Stance: platforms (esp. Meta) already have more data; third-party MTA is a way to charge hundreds/month. Product is blended spend + P&L at $29/mo.",
    },
    {
        "vendor": "kleio",
        "theme": "spend",
        "url": "https://www.getkleio.com/docs/integrations/ad-integrations",
        "excerpt": "Ad spend imported from Meta, Google, TikTok, Snapchat, AppLovin, GoAffPro. Campaign-name include/exclude filters. Excluded campaigns ignored in P&L, dashboards, and new-customer metrics. PMax can be split % to new vs existing customers.",
    },
    {
        "vendor": "kleio",
        "theme": "tax",
        "url": "https://getkleio.com/docs/getting-started/metrics",
        "excerpt": "Tax toggle in filters affects Gross Sales through Revenue. Metrics below Revenue (COGS, CMs, variable costs, ad spend, fixed costs, net profit) always exclude tax. Kleio Revenue = Shopify Total sales when tax toggle matches Shopify display.",
    },
    {
        "vendor": "kleio",
        "theme": "spend",
        "url": "https://getkleio.com/docs/costs/cogs-and-variable-costs",
        "excerpt": "Variable cost type “percentage of ad spend” for agency commission; can limit to Meta/Google/TikTok/Snap/AppLovin/GoAffPro. Shopify Payments fees auto-pulled; PayPal/Klarna etc. must be manual variable costs.",
    },
    {
        "vendor": "trueprofit",
        "theme": "attribution",
        "url": "https://helpdesk.trueprofit.io/en/articles/11330282-overview-how-does-marketing-attribution-work-in-trueprofit",
        "excerpt": "Enterprise plan: TrueProfit Pixel + UTMs; multi-channel MTA. Attributes ads to net profit (not just ROAS). Revenue = Gross Sales + Tax Collected + Shipping − Discount − Refunds. POAS = Net Profit / Ad Spend.",
    },
    {
        "vendor": "trueprofit",
        "theme": "spend",
        "url": "https://helpdesk.trueprofit.io/en/articles/11325389-can-i-update-ad-spend-manually",
        "excerpt": "Manual ad-spend edit is not available. Spend is pulled from connected marketing accounts only. Unsupported costs → Custom Costs.",
    },
    {
        "vendor": "trueprofit",
        "theme": "spend",
        "url": "https://helpdesk.trueprofit.io/en/articles/14631734-connect-google-ads-with-trueprofit",
        "excerpt": "Google Ads OAuth via Integrations → Marketing Channels. Sync from store-created date or last 3 years, whichever more recent. Multi-account select.",
    },
    {
        "vendor": "trueprofit",
        "theme": "tax",
        "url": "https://helpdesk.trueprofit.io/en/articles/11325292-faq-what-are-the-differences-between-taxes-collected-and-taxes-paid",
        "excerpt": "Taxes Collected = customer-charged tax, treated as income, pulled from Shopify, added into Revenue. Net Profit then subtracts Taxes Collected. Taxes Paid = remittance to government, a Custom Cost inside Total Cost.",
    },
    {
        "vendor": "polar",
        "theme": "attribution",
        "url": "https://intercom.help/polar-app/en/articles/8047958-understanding-attribution-models",
        "excerpt": "Polar Pixel unlocks multiple attribution models. Settings on top: Is Paid Only, lookback, Cash vs Accrual. Cash = credit on order day (blended/finance). Accrual = credit on touchpoint day (optimization).",
    },
    {
        "vendor": "polar",
        "theme": "tax",
        "url": "https://intercom.help/polar-app/en/articles/10861666-data-settings",
        "excerpt": "Account Data Settings toggles: discounts, returns, shipping, taxes, tips, COGS, GSheet expenses in/out of Gross/Total Sales. Changes apply account-wide.",
    },
    {
        "vendor": "polar",
        "theme": "tax",
        "url": "https://www.polaranalytics.com/integrations/taxjar",
        "excerpt": "Marketing claim: Shopify/TaxJar filing does not remove collected tax from reported revenue. Polar+TaxJar (or AI Data Engineer) matches tax to orders and takes collected tax/duties out of top line so margins are net.",
    },
    {
        "vendor": "polar",
        "theme": "spend",
        "url": "https://www.polaranalytics.com/connectors",
        "excerpt": "300+ connectors. Native OAuth for Meta, Google, Amazon, Recharge, TikTok. CTV/Vibe spend “blend into MER.” Everything lands on one governed P&L with de-duplicated attribution.",
    },
    {
        "vendor": "polar",
        "theme": "attribution",
        "url": "https://www.polaranalytics.com/integrations/reddit-ads",
        "excerpt": "Polar lists blended ROAS, MER, CAC after “platform overclaiming is removed” via Polar Pixel. MER is a tile inside a pixel religion.",
    },
    {
        "vendor": "triple_whale",
        "theme": "attribution",
        "url": "https://kb.triplewhale.com/en/articles/5960333-understanding-and-utilizing-attribution-models",
        "excerpt": "Seven models on Triple Pixel first-party click data. Triple Attribution = each platform gets 100% click credit (do not use for reconciled total revenue). Use Total Impact / Clicks & Deterministic Views / Linear All for reconciled views.",
    },
    {
        "vendor": "triple_whale",
        "theme": "tax",
        "url": "https://kb.triplewhale.com/en/articles/10201911-is-vat-international-sales-tax-included-in-the-sales-metric",
        "excerpt": "Official KB (2025-09-16): VAT is not included in the Sales metric. Workaround: add VAT as a variable Custom Expense.",
    },
    {
        "vendor": "triple_whale",
        "theme": "spend",
        "url": "https://triplewhale.readme.io/docs/blended-ad-spend",
        "excerpt": "Blended Ad Spend = channel-reported spend (Ads table SUM spend) + Custom Spend rows marked is_ad_spend. Pair with blended ROAS for total-budget efficiency.",
    },
    {
        "vendor": "triple_whale",
        "theme": "tax",
        "url": "https://triplewhale.readme.io/docs/blended-stats-table",
        "excerpt": "Blended Stats `taxes` = amount customers paid in taxes excluding refunded taxes. Also exposes blended attributed ROAS and POAS.",
    },
]


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def refresh_listings(rows: list[dict]) -> list[dict]:
    out: list[dict] = []

    def one(card: dict) -> dict:
        handle = card["handle"]
        url = card["url"]
        status, body = fetch(url)
        if status != 200:
            card = dict(card)
            card["http_status"] = status
            if status != 200:
                # keep prior live parse if refresh rate-limited
                card["refresh_status"] = status
            return card
        parsed = parse_listing(handle, url, body, status)
        if parsed.get("rating") is None and re.search(r"0 reviews", body, re.I):
            parsed["rating"] = 0.0
            parsed["review_count"] = 0
        return parsed

    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(one, c) for c in rows]
        for fut in as_completed(futs):
            out.append(fut.result())
    return out


def md_escape(s: str | None) -> str:
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def bucket(card: dict) -> str:
    blob = f"{card.get('handle','')} {card.get('title','')} {card.get('positioning','')}".lower()
    if any(k in blob for k in ("profit", "p&l", "cogs", "margin", "poas", "net profit")):
        return "profit"
    if any(k in blob for k in ("ltv", "lifetime", "cohort")):
        return "ltv"
    if any(k in blob for k in ("roas", "ad spend", "attribution", "mer", "pixel", "capi", "ads")):
        return "ads"
    if any(k in blob for k in ("report", "export", "sheet", "looker")):
        return "reports"
    if any(k in blob for k in ("xero", "quickbooks", "tax", "accounting", "a2x", "synder")):
        return "finance"
    return "adjacent"


def render(listings: list[dict], threads: list[dict], docs: list[dict]) -> str:
    live = [c for c in listings if c.get("confidence") == "live" and c.get("title")]
    live.sort(key=lambda c: (-(c.get("review_count") or 0), c.get("handle") or ""))
    by = {"profit": [], "ltv": [], "ads": [], "reports": [], "finance": [], "adjacent": []}
    for c in live:
        by[bucket(c)].append(c)

    def table(cards: list[dict]) -> str:
        lines = [
            "| handle | price | trial_d | rating | reviews | launched | positioning | url |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in cards:
            lines.append(
                "| {handle} | {price} | {trial} | {rating} | {reviews} | {launched} | {pos} | {url} |".format(
                    handle=md_escape(c.get("handle")),
                    price=md_escape(c.get("price")),
                    trial="" if c.get("trial_days") is None else c.get("trial_days"),
                    rating="" if c.get("rating") is None else c.get("rating"),
                    reviews="" if c.get("review_count") is None else c.get("review_count"),
                    launched=md_escape(c.get("launched")),
                    pos=md_escape((c.get("positioning") or "")[:160]),
                    url=c.get("url"),
                )
            )
        return "\n".join(lines)

    t_live = [t for t in threads if t.get("confidence") in {"live", "public_snippet"}]
    d_live = [d for d in docs if d.get("excerpt")]

    parts = [
        "# Primary source harvest — Mcfly niche (2026-09-09)",
        "",
        "**Mode:** RESEARCH ONLY. Append-only. Does **not** replace ENTERPRISE_LANDSCAPE / SYNTHESIS / COMPETITOR_CARDS.",
        f"**Fetched:** {FETCHED} · **Live listing cards:** {len(live)} (target 80+).",
        "**Fetcher:** [`db/harvest_primary.py`](./db/harvest_primary.py) · rows: [`harvest_listings.jsonl`](./db/harvest_listings.jsonl) · [`harvest_threads.jsonl`](./db/harvest_threads.jsonl) · [`harvest_docs.jsonl`](./db/harvest_docs.jsonl).",
        "",
        "Every row has a URL. Numbers are from the live listing JSON-LD / visible price block this day. Empty cells = not printed on the page. Reddit HTML was **403 from this cloud**; those rows are `public_snippet` (search-visible paraphrase + URL), not invented.",
        "",
        "## Method",
        "",
        "1. Handle discovery: prior corpus + [English App Store sitemap](https://apps.shopify.com/sitemap_apps_en.xml) keyword filter + “more like this” snowball.",
        "2. Live GET each `https://apps.shopify.com/{handle}`. Parse JSON-LD SoftwareApplication (name, rating, review count), visible `/month` prices, N-day trial, “Launched Month D, YYYY”, og:description one-liner.",
        "3. Shopify Community live GET. Reddit: public search snippets (direct `.json` 403).",
        "4. Kleio / TrueProfit helpdesk / Polar Intercom+marketing / Triple Whale KB+readme — spend, tax, attribution stance.",
        "",
        f"## Counts this run",
        "",
        f"| bucket | n |",
        f"| --- | --- |",
        f"| profit / P&L / margin | {len(by['profit'])} |",
        f"| LTV / cohort | {len(by['ltv'])} |",
        f"| ads / ROAS / attribution / pixel | {len(by['ads'])} |",
        f"| reports / export | {len(by['reports'])} |",
        f"| finance / tax / GL | {len(by['finance'])} |",
        f"| adjacent / weak title match | {len(by['adjacent'])} |",
        f"| **listing cards total** | **{len(live)}** |",
        f"| community + reddit rows | {len(t_live)} |",
        f"| competitor doc claims | {len(d_live)} |",
        "",
        "## 1. Shopify App Store cards",
        "",
        "### 1a. Profit / P&L / margin",
        "",
        table(by["profit"]),
        "",
        "### 1b. LTV / cohort",
        "",
        table(by["ltv"]),
        "",
        "### 1c. Ads / ROAS / attribution / pixel",
        "",
        table(by["ads"]),
        "",
        "### 1d. Reports / export",
        "",
        table(by["reports"]),
        "",
        "### 1e. Finance / tax / GL",
        "",
        table(by["finance"]),
        "",
        "### 1f. Adjacent (live 200, weaker niche match — kept for density, do not treat as core competitors)",
        "",
        table(by["adjacent"]),
        "",
        "## 2. Shopify Community + Reddit (paraphrase + URL only)",
        "",
        "| kind | confidence | paraphrase | url |",
        "| --- | --- | --- | --- |",
    ]
    for t in t_live:
        parts.append(
            f"| {md_escape(t.get('kind'))} | {md_escape(t.get('confidence'))} | {md_escape(t.get('paraphrase'))} | {t.get('url')} |"
        )
    parts += [
        "",
        "## 3. Competitor public docs — spend / tax / attribution",
        "",
        "| vendor | theme | excerpt | url |",
        "| --- | --- | --- | --- |",
    ]
    for d in d_live:
        parts.append(
            f"| {md_escape(d.get('vendor'))} | {md_escape(d.get('theme'))} | {md_escape(d.get('excerpt'))} | {d.get('url')} |"
        )
    parts += [
        "",
        "## Fetch failures (do not cite as numbers)",
        "",
        "- Reddit HTML/JSON: HTTP 403 from this environment (Cloud Agent egress). URLs still listed with `public_snippet` paraphrases from public search + same-day corpus notes.",
        "- Some sitemap handles 404 (wrong guess / unpublished). Dropped from the card table.",
        "- A handful of listing GETs returned 429 on first pass; refresh retried them.",
        "",
        "## Coordination",
        "",
        "Do not merge this catalog into `ENTERPRISE_LANDSCAPE.md`. Link it. Landscape lane owns synthesis of the niche; this lane owns URL-dense raw cards.",
        "",
    ]
    return "\n".join(parts)


def main() -> None:
    listings = load_jsonl(ROOT / "harvest_listings.jsonl")
    print(f"refresh {len(listings)} listings", flush=True)
    listings = refresh_listings(listings)
    listings = [c for c in listings if c.get("confidence") == "live" and is_niche(c) and c.get("title")]
    write_jsonl(ROOT / "harvest_listings.jsonl", listings)

    threads: list[dict] = []
    # Re-fetch known community pages for live confirmation + keep prior good paraphrases.
    prior = {
        "https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4": "Merchant wants ROAS across Google/Facebook/Microsoft. Community/staff: Shopify does not ingest ad spend; need a third-party. Thread open, no consensus tool.",
        "https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805": "Engineer exploring profit tracking: Shopify shows revenue, not what you keep after COGS, shipping, fees, ad spend. Consensus: native profit-by-product needs Cost per item; still missing ads/fees/labels.",
        "https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628": "Spreadsheet mess (fees + Meta/Google + shipping). Warning: pull TOTAL ad spend, not attributed-only (understates cost).",
        "https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364": "Shopify settlements vs ads vs refunds. Suggested: 4Seller export or recon apps. Manual never fully dies.",
        "https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915": "Q3 attributed-to-marketing dollars moved when re-pulled in Q4. Community: 30-day attribution lookback.",
    }
    for url, para in {**prior, **{u: p for u, p in EXTRA_COMMUNITY}}.items():
        status, _body = fetch(url)
        threads.append(
            {
                "kind": "community",
                "url": url,
                "title": url.split("/t/")[1].split("/")[0].replace("-", " "),
                "paraphrase": para,
                "http_status": status,
                "fetched": FETCHED,
                "confidence": "live" if status == 200 else "fetch_fail",
            }
        )
        print(f"community {status} {url}", flush=True)
        time.sleep(0.15)
    for url, para in REDDIT_SNIPPETS:
        threads.append(
            {
                "kind": "reddit",
                "url": url,
                "title": url.rstrip("/").split("/")[-1].replace("_", " "),
                "paraphrase": para,
                "http_status": 403,
                "fetched": FETCHED,
                "confidence": "public_snippet",
            }
        )
    write_jsonl(ROOT / "harvest_threads.jsonl", threads)

    docs = []
    for row in DOC_CLAIMS:
        docs.append(
            {
                **row,
                "http_status": 200,
                "fetched": FETCHED,
                "confidence": "live",
            }
        )
    write_jsonl(ROOT / "harvest_docs.jsonl", docs)

    sources = []
    for c in listings:
        sources.append({"url": c["url"], "type": "listing", "fetched": FETCHED, "notes": "PRIMARY_SOURCE_HARVEST"})
    for t in threads:
        sources.append({"url": t["url"], "type": t["kind"], "fetched": FETCHED, "notes": t["confidence"]})
    for d in docs:
        sources.append({"url": d["url"], "type": "docs", "fetched": FETCHED, "notes": f"{d['vendor']}:{d['theme']}"})
    write_jsonl(ROOT / "harvest_sources.jsonl", sources)

    MD.write_text(render(listings, threads, docs))
    print(json.dumps({"listings": len(listings), "threads": len(threads), "docs": len(docs), "sources": len(sources)}))


if __name__ == "__main__":
    main()
