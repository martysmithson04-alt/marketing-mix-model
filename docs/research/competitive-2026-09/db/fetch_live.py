#!/usr/bin/env python3
"""Live-fetch competitor listings, docs, and community URLs. Research only.

Writes:
  fetch_raw.jsonl   — one row per URL (status, excerpt, extracted fields)
  fetch_quotes.jsonl — visible review-like snippets when present
"""

from __future__ import annotations

import json
import re
import ssl
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)
CTX = ssl.create_default_context()

# Shopify App Store handles to fetch (listing pages).
SHOPIFY_HANDLES = [
    "mcfly-analytics-public",
    "trueprofit",
    "lifetimely-lifetime-value-and-profit-analytics",
    "beprofit-profit-tracker",
    "metorik",
    "margins",
    "kleio",
    "juicy",
    "go-profit",
    "profitario",
    "profit-calc",
    "bloom-analytics",
    "repeat-customer-insights",
    "cashdash-pro",
    "clearprofit",
    "profitmetrics",
    "setpilot",
    "repeat",
    "margn-1",
    "trackprofit-1",
    "profitiq",
    "marginlens-ai-powered",
    "profit-panel",
    "triplewhale-1",
    "polar-analytics",
    "attribuly",
    "advertising-insights",
    "daasity",
    "rockerbox",
    "klar-analytics",
    "segmetrics",
    "microsoft-clarity",
    "lucky-orange",
    "analyzify",
    "parkour-pixel",
    "gtm-datalayer-by-elevar",
    "littledata",
    "wetracked-io-connect",
    "hotjar",
    "fullstory",
    "betterreports",
    "report-pundit",
    "data-export",
    "advanced-reports",
    "report-toaster",
    "ez-exporter",
    "syncwith",
    "coupler-io",
    "coefficient",
    "supermetrics",
    "a2x",
    "synder",
    "finaloop",
    "linkmybooks",
    "tiktok",
    "facebook",
    "adscale",
    "microsoft-advertising",
    "madgicx",
    "metrilo",
    "taxomate",
    "matrixify",
    "nabu",
    "klaviyo",
    "omnisend",
    "recharge",
    "loop-returns",
    "aftership-returns",
    "peel",
    "fairing",
    "pixelfy",
    "trackify",
    "stape",
    "blotout",
    "meyoo",
    "profitario-ai",
    "upprofit",
    "godmode",
    "peaklytics",
    "profit-hero",
    "true-roas",
    "adverity",
    "windsor-ai",
    "funnel-io",
    "agency-analytics",
    "databox",
    "glew",
    "glew-io",
    "hyros",
    "wicked-reports",
    "northbeam",
    "redtrack",
    "voluum",
    "humblytics",
    "analysisgpt",
    "whaly",
    "triquetra",
    "sunforce",
    "peaka",
    "bookkeep",
    "puzzle-bookkeeping",
    "webgility",
    "quickbooks-commerce",
    "shopify-flow",
    "google-channel",
    "pinterest",
    "snapchat",
    "bing-shopping",
    "amazon-channel",
    "judge-me",
    "loox",
    "yotpo-reviews",
    "gorgias",
    "tidio",
    "zendesk",
    "shiphero",
    "stocky",
    "plenisher",
    "skio",
    "bold-subscriptions",
    "stay-ai",
    "postscript",
    "attentive",
    "smsbump",
    "privy",
    "klaviyo-sms",
    "triple-pixel",
    "sonar",
    "compass-analytics",
    "moby-ai",
    "trueprofit-attribution",
    "lifetimely-attribution",
    "profit-by-product",
    "advanced-profit-reports",
    "shopify-reports",
    "custom-reports",
    "analytics-king",
    "google-analytics",
    "enhanced-ecommerce",
    "server-side-gtm",
    "conversion-tracking",
    "capi-gateway",
    "meta-capi",
    "tiktok-events-api",
]

# Non-listing primary URLs that must be fetched for bibliography / landscape.
PRIMARY_URLS = [
    # Mcfly
    "https://apps.shopify.com/mcfly-analytics-public",
    "https://mcflyads.com",
    "https://mcflyads.com/pricing",
    "https://mcflyads.com/product",
    "https://mcflyads.com/why-pixels-fail",
    # Official Shopify
    "https://shopify.dev/docs/apps/launch/app-store-review",
    "https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews",
    "https://shopify.dev/docs/apps/launch/built-for-shopify",
    "https://shopify.dev/docs/apps/launch/built-for-shopify/requirements",
    "https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements",
    "https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials",
    "https://shopify.dev/docs/apps/launch/distribution/revenue-share",
    "https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories",
    "https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing",
    "https://shopify.dev/docs/api/shopifyql/latest/schemas/marketing/shop_campaign_insights",
    "https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/marketing-reports",
    "https://help.shopify.com/en/manual/apps/uninstalling-apps",
    "https://help.shopify.com/en/manual/products/details/product-cost",
    "https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/finances-reports",
    "https://apps.shopify.com/categories/store-management-operations-analytics/all",
    "https://apps.shopify.com/categories/marketing-and-conversion",
    "https://apps.shopify.com/categories/store-management",
    # Community
    "https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4",
    "https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805",
    "https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628",
    "https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364",
    "https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915",
    # Reddit
    "https://www.reddit.com/r/shopify/comments/1rpjuk0/best_way_to_track_meta_ads_roas_in_shopify/",
    "https://www.reddit.com/r/shopify/comments/1jpb8cy/sales_attribution_tracking/",
    "https://www.reddit.com/r/shopify/comments/1pzy8iv/app_or_plugin_to_calculate_profit_each_month/",
    "https://www.reddit.com/r/shopify/comments/1h27sj3/beprofit_vs_lifetimely_vs/",
    "https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/",
    "https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/",
    "https://www.reddit.com/r/PPC/comments/1r2pvgy/question_for_d2c_founders_on_shopify_running_meta/",
    "https://www.reddit.com/r/PPC/comments/1pqv5kh/how_are_you_handling_ad_attribution/",
    # Competitor sites / docs
    "https://www.northbeam.io/",
    "https://docs.northbeam.io/docs/northbeam-apex",
    "https://www.triplewhale.com/pricing",
    "https://www.polaranalytics.com/vs/triple-whale",
    "https://getkleio.com/",
    "https://getkleio.com/docs/getting-started/metrics",
    "https://getkleio.com/docs/getting-started/recommended-setup",
    "https://www.getkleio.com/docs/integrations/ad-integrations",
    "https://getkleio.com/docs/integrations/mcp-server",
    "https://getkleio.com/docs/costs/cogs-and-variable-costs",
    "https://trueprofit.io/pricing",
    "https://www.lifetimely.io/pricing",
    "https://www.glew.io/",
    "https://hyros.com/",
    "https://www.wickedreports.com/",
    "https://www.measured.com/",
    "https://www.haus.io/",
    "https://www.getrecast.com/",
    "https://www.mutinex.co/",
    "https://windsor.ai/",
    "https://supermetrics.com/pricing",
    "https://www.coupler.io/pricing",
    "https://coefficient.io/pricing",
    "https://funnel.io/pricing",
    "https://agencyanalytics.com/pricing",
    "https://whatagraph.com/pricing",
    "https://www.dashthis.com/pricing/",
    "https://www.swydo.com/pricing/",
    "https://stape.io/",
    "https://blotout.io/",
    "https://www.getelevar.com/pricing/",
    "https://a2xaccounting.com/pricing/",
    "https://www.finaloop.com/pricing",
    "https://synder.com/pricing/",
    "https://www.rockerbox.com/",
    "https://www.daasity.com/pricing",
    "https://www.attribuly.com/pricing",
    "https://lebesgue.io/pricing",
    "https://www.segmetrics.io/pricing",
    "https://www.klar-analytics.com/",
    "https://plenisher.ai/",
    "https://www.reportpundit.com/post/shopify-cogs-report-profit-margins",
    "https://www.trygodmode.com/blog/shopify-real-profit-2026-dashboard-lies",
    "https://applora.ai/appstore",
    "https://taylorsicard.com/blog/shopify-app-listing-conversion",
    "https://taylorsicard.com/blog/shopify-app-pricing-strategy",
    "https://taylorsicard.com/blog/shopify-app-economics-one-chart",
    "https://shopivibe.app/how-to-price-shopify-app",
    "https://www.gapquery.com/blog/shopify-app-pricing-by-category",
    "https://venon.io/blog/triple-whale-pricing",
    "https://eightx.co/blog/compare/reviews/a2x-for-ecommerce-review",
    "https://www.letstalkshop.com/blog/triple-whale-vs-polar-analytics",
    "https://ocontis.studio/blog/post/the-hidden-cost-of-running-a-shopify-store-when-12-apps-quietly-eat-your-margins/",
    "https://developers.facebook.com/docs/marketing-api/overview",
    "https://developers.google.com/google-ads/api/docs/start",
    "https://ads.tiktok.com/marketing_api/docs",
    "https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/marketing-attribution",
    "https://www.shopify.com/enterprise/blog/marketing-attribution",
    "https://www.triplewhale.com/blog/what-is-mer",
    "https://www.polaranalytics.com/blog/mer-marketing-efficiency-ratio",
]


def fetch(url: str, timeout: int = 25) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
            raw = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            text = raw.decode(charset, errors="replace")
            return {
                "url": url,
                "ok": True,
                "status": resp.status,
                "final_url": resp.geturl(),
                "bytes": len(raw),
                "html": text,
                "error": None,
            }
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return {
            "url": url,
            "ok": False,
            "status": e.code,
            "final_url": url,
            "bytes": len(body),
            "html": body,
            "error": f"HTTP {e.code}",
        }
    except Exception as e:  # noqa: BLE001 — research fetcher must record any failure
        return {
            "url": url,
            "ok": False,
            "status": None,
            "final_url": url,
            "bytes": 0,
            "html": "",
            "error": f"{type(e).__name__}: {e}",
        }


def first(pattern: str, text: str, flags: int = re.I | re.S) -> str | None:
    m = re.search(pattern, text, flags)
    return m.group(1).strip() if m else None


def extract_listing(html: str) -> dict:
    name = first(r'<h1[^>]*>(.*?)</h1>', html)
    if name:
        name = re.sub(r"<[^>]+>", "", name).strip()
    rating = None
    reviews = None
    # JSON-LD aggregateRating
    ld = first(r'<script type="application/ld\+json">(.*?)</script>', html)
    if ld:
        try:
            data = json.loads(ld)
            if isinstance(data, list):
                data = next((x for x in data if isinstance(x, dict) and x.get("@type") in {"SoftwareApplication", "Product"}), data[0] if data else {})
            agg = data.get("aggregateRating") or {}
            if agg.get("ratingValue") is not None:
                rating = float(agg["ratingValue"])
            if agg.get("reviewCount") is not None:
                reviews = int(agg["reviewCount"])
            if not name:
                name = data.get("name")
        except Exception:
            pass
    if rating is None:
        r = first(r'"ratingValue"\s*:\s*"?([0-9.]+)"?', html)
        if r:
            rating = float(r)
    if reviews is None:
        rc = first(r'"reviewCount"\s*:\s*"?([0-9]+)"?', html)
        if rc:
            reviews = int(rc)
    price_scan = first(
        r'((?:Free to install|Free forever|Free|From\s+)?\$[0-9]+(?:\.[0-9]{2})?(?:\s*/\s*month)?)',
        html,
    )
    launched = first(r'Launched\s*</[^>]+>\s*<[^>]+>([^<]+)', html)
    if not launched:
        launched = first(r'Launched[:\s]+([A-Z][a-z]+ \d{1,2}, \d{4})', html)
    trial = first(r'(\d+)\s*-?\s*day free trial', html)
    desc = first(r'<meta name="description" content="([^"]+)"', html)
    quotes = []
    # Visible review cards often include reviewBody in JSON-LD
    for m in re.finditer(r'"reviewBody"\s*:\s*"((?:\\.|[^"\\])*)"', html):
        q = m.group(1).encode("utf-8").decode("unicode_escape")
        q = q.replace("\\n", " ").strip()
        if 20 <= len(q) <= 400:
            quotes.append(q)
    # fallback: quoted review snippets
    if len(quotes) < 2:
        for m in re.finditer(r'data-review-content="([^"]{20,400})"', html):
            quotes.append(m.group(1))
    return {
        "name": name,
        "rating": rating,
        "review_count": reviews,
        "price_scan": price_scan or price,
        "launched": launched,
        "trial_days": int(trial) if trial else None,
        "meta_description": desc,
        "quotes": quotes[:6],
    }


def excerpt(html: str, n: int = 240) -> str:
    text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:n]


def main() -> None:
    urls: list[str] = []
    seen: set[str] = set()
    for h in SHOPIFY_HANDLES:
        u = f"https://apps.shopify.com/{h}"
        if u not in seen:
            urls.append(u)
            seen.add(u)
    for u in PRIMARY_URLS:
        if u not in seen:
            urls.append(u)
            seen.add(u)

    raw_path = ROOT / "fetch_raw.jsonl"
    quotes_path = ROOT / "fetch_quotes.jsonl"
    # resume-safe: skip already fetched urls
    done: set[str] = set()
    if raw_path.exists():
        for line in raw_path.read_text().splitlines():
            if not line.strip():
                continue
            try:
                done.add(json.loads(line)["url"])
            except Exception:
                continue

    print(f"queued {len(urls)} urls; already have {len(done)}")
    with raw_path.open("a") as raw_f, quotes_path.open("a") as q_f:
        for i, url in enumerate(urls, 1):
            if url in done:
                continue
            rec = fetch(url)
            html = rec.pop("html")
            extracted = {}
            quotes: list[str] = []
            if rec.get("ok") or rec.get("status") in {200, 301, 302}:
                if "apps.shopify.com/" in url and "/categories/" not in url:
                    try:
                        extracted = extract_listing(html)
                        quotes = extracted.pop("quotes", [])
                    except Exception as exc:  # noqa: BLE001
                        extracted = {"parse_error": str(exc)}
                        quotes = []
            row = {
                **rec,
                "fetched": "2026-09-09",
                "excerpt": excerpt(html) if html else "",
                "extracted": extracted,
            }
            raw_f.write(json.dumps(row, ensure_ascii=False) + "\n")
            raw_f.flush()
            for qi, quote in enumerate(quotes, 1):
                q_f.write(
                    json.dumps(
                        {
                            "url": url,
                            "quote": quote,
                            "i": qi,
                            "fetched": "2026-09-09",
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
            status = rec.get("status") or rec.get("error")
            name = (extracted or {}).get("name") or ""
            print(f"[{i}/{len(urls)}] {status} {url} {name}")
            time.sleep(0.35)
    print("done")


if __name__ == "__main__":
    main()
