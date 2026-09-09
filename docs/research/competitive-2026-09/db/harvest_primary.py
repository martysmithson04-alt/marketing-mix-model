#!/usr/bin/env python3
"""Primary-source harvest for Mcfly niche. Research only. Live fetches."""

from __future__ import annotations

import html as htmlmod
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT
FETCHED = date.today().isoformat()
UA = "McflyResearch/2026-09 (+https://mcflyads.com; primary-source harvest; research only)"
TIMEOUT = 25

# Curated + sitemap-tight handles in analytics / profit / ROAS / ads / reports / LTV.
# Verified by HTTP 200 at fetch time; 404s are dropped, never invented.
SEED_HANDLES = [
    "mcfly-analytics-public",
    "triplewhale-1",
    "polar-analytics",
    "trueprofit",
    "lifetimely-lifetime-value-and-profit-analytics",
    "beprofit-profit-tracker",
    "metorik",
    "margins",
    "betterreports",
    "syncwith",
    "microsoft-clarity",
    "parkour-pixel",
    "wetracked-io-connect",
    "analyzify",
    "gtm-datalayer-by-elevar",
    "a2x",
    "finaloop",
    "klar-analytics",
    "kleio",
    "juicy",
    "go-profit",
    "profitario",
    "profit-calc",
    "bloom-analytics",
    "setpilot",
    "clearprofit",
    "clearprofit-1",
    "cashdash-pro",
    "margn-1",
    "margyn",
    "trackprofit-1",
    "profitiq",
    "marginlens-ai-powered",
    "profit-panel",
    "profitmetrics",
    "report-pundit",
    "advanced-reports",
    "report-toaster",
    "ez-exporter",
    "data-export",
    "littledata",
    "lucky-orange",
    "hotjar",
    "advertising-insights",
    "attribuly",
    "daasity",
    "rockerbox",
    "segmetrics",
    "synder",
    "linkmybooks",
    "metrilo",
    "tiktok",
    "facebook",
    "repeat-customer-insights",
    "glew",
    "simple-reports-and-data-export",
    "ai-profit-analytics",
    "better-profit-dashboard",
    "cmo-analytics-profit-tracker",
    "customer-lifetime-value",
    "customer-analytics-vip-ltv",
    "cohorts",
    "cohortive",
    "cohortly-repeat-tracker",
    "easy-profit-calculator",
    "full-roas-calculations",
    "open-roas",
    "true-roas-ai",
    "churney-roas-ai-estimator",
    "profit-bid-poas",
    "poas-jet",
    "neoprofit",
    "profitvane",
    "profit-agent",
    "profit-ai",
    "profit-analytics-1",
    "profit-peak-analytics",
    "profitlens-analytics",
    "profitpod-analytics",
    "real-profit",
    "real-profit-calculator",
    "realprofit-analytics",
    "rwa-true-profit-analytics",
    "shoprofy-profit-analytics",
    "storehero-profit-analytics",
    "m8trics-profit-analytics",
    "metricflow-analytics-profit",
    "my-profit-app",
    "netlyze-profit-tracking",
    "sellerboard-profit-ltv-customer-lifetime-value-analytics",
    "ltv-analyzer",
    "attribution",
    "blackbox-attribution",
    "fueled-attribution-suite",
    "ordinary-attribution-ab-testing",
    "perforyx-attribution-tracker",
    "ulittle-attribution-engine",
    "whatconverts-marketing-attribution",
    "agencyanalytics",
    "advanced-analytics",
    "advanced-reporting-analytics",
    "elly-analytics",
    "firstbridge-analytics",
    "hawkeai-analytics",
    "keel-analytics",
    "metrixon-ai-analytics",
    "mixtable-analytics",
    "orca-analytics",
    "orderlens-analytics",
    "pivotal-analytics",
    "prism-analytics",
    "sliderule-analytics",
    "syft-analytics",
    "theo-analytics",
    "twik-analytics",
    "utm-ads-analytics",
    "adcohort-smart-ad-spend",
    "skylitee-sales-ads-reports",
    "lebesgue-facebook-audit",
    "nabu-for-facebook-pixel",
    "parkour-tiktok-pixel",
    "segment-com-by-littledata",
    "supermetrics",
    "xero-taxomate",
    "taxjar",
    "peasy-1",
    "foxsell",
    "shoplytics-1",
    "moby-marketing",
    "clearmargin",
    "true-margins",
    "order-margins",
    "returns-margin-analytics",
    "draft-profit-margins",
    "profit-truth",
    "profit-net",
    "profit-x",
    "profit-pulse",
    "profit-pulse-ai",
    "profit-tracker-2",
    "profit-expert",
    "profit-first-v1",
    "profit-leak-detector",
    "code-magic-profitiq",
    "abprofit",
    "analytics-reports-lab",
    "free-reports-analytics",
    "ods-smart-reports",
    "smart-reports-scheduler",
    "report-scheduler",
    "reportgenix-sales-analytics",
    "morning-pulse-daily-reports",
    "daily-orders-refunds-report",
    "ga4-audit-tracking-reports",
    "better-reports-exporter",
    "cube-reports-1",
    "dumb-reports",
    "easy-reports",
    "itk-reporting",
    "dnd-reporting",
    "original-report",
    "z-reports",
    "microsoft-advertising",
    "pinterest",
    "snapchat",
    "google-channel",
    "google-and-youtube",
    "klaviyo",
    "recharge",
    "northbeam",
    "hyros",
    "wicked-reports",
    "glew-io",
    "glewio",
    "profitmetrics-io",
    "lebesgue",
    "nabu",
    "elevar",
    "clarity",
    "we-tracked",
    "wetracked",
    "true-profit",
    "polar",
    "triple-whale",
    "lifetimely",
    "beprofit",
    "reportpundit",
    "mipler",
    "advanced-custom-reports",
    "custom-reports",
    "shopify-reports",
    "analytics-by-shopify",
    "profit-calculator",
    "net-profit",
    "netprofit",
    "blended-roas",
    "mer-tracker",
    "marketing-efficiency",
    "ad-spend-tracker",
    "spend-tracker",
    "cogs-tracker",
    "inventory-planner",
    "prediko",
    "craftybase",
    "cogsy",
    "pos-cogs",
    "tallymeter-labor-cogs-margin",
    "nextcart-ltv-loss-leaders",
    "automatik-ai-analytics",
    "attronaut-analytics",
    "belardi-wong-analytics",
    "cifra-analytics",
    "ecommerce-analytics-goat",
    "ewynk-ai-growth-analytics",
    "heartcoding-essential-product-analytics",
    "icarus-analytics-app",
    "influencer-analytics",
    "modovisa-analytics",
    "narriqo-analytics",
    "nowfluence-analytics",
    "oogwai-analytics",
    "partnercentric-analytics-clo",
    "shopaw-sell-analytics",
    "shopsmart-analytics-pro",
    "store-analytics-1",
    "sweet-analytics-1",
    "trackywise-analytics",
    "wsfy-analytics",
    "zerotohero-analytics",
    "zuko-form-analytics",
    "llm-analytics",
    "flow-analytics-by-databrief-sa",
    "avia-pos-store-analytics",
    "bipeye-orders-analytics",
    "biqli-conversion-analytics",
    "cart-analytics",
    "coupon-analytics-pro",
    "exatom-checkout-analytics",
    "inventory-analytics",
    "manca-quote-analytics",
    "mtl-product-like-analytics",
    "shopai-product-analytics-1",
    "stocking-analytics-dashboard",
    "store-analytics-by-audiosdroid",
    "blackboxng",
    "profit-brain-1",
    "profit-champions-app",
    "profit-cluster",
    "profit-maximization",
    "profit-pages-1",
    "profit-pie",
    "profit-pilot-3",
    "profit-powertools",
    "rios-profit-planning",
    "vizbix-profit-optimizer",
    "amplisio-profit-upsell",
    "nda-profit",
    "nda-profit-global",
    "easy-margin",
    "margin",
    "margin-1",
    "margin-boost",
    "margin-os",
    "margin-mate",
    "mastering-margins-1",
    "real-time-margin-guard",
    "adbreakers-reporting-connecto",
    "ag-reporting-app",
    "businessleague-reports",
    "email-reports",
    "subscriber-reports",
    "supercognit-reports-pro",
    "reporting-by-wip",
    "reporting-saas-public",
    "report-fetcher",
    "report-sales-by-state",
    "uae-vat201-tax-reports",
    "conversios-all-in-one-pixel",
    "avantify-first-party-pixel",
    "facebook-pixel-capi-by-appesy",
    "tiktok-pixel-capi",
    "capi-relay-pro",
    "capisync",
    "omni-pixel",
    "pixel-x-facebook-tiktok-ga4",
    "google-analytics-4",
    "ga4-google-analytics-4",
    "easy-google-analytics-4ga4",
    "analyzely-google-analytics-4",
    "ad-google-analytics-4",
    "pasilobus-google-analytics",
    "wixpa-google-analytics-4",
    "hitsteps-analytics",
    "shinystat-analytics-service",
    "afs-analytics",
    "analytics-5",
    "analytics-app-2",
    "analytics-audit",
    "analertics-analytics-alerts",
    "blufire-analytics",
    "atchoo-analytics",
    "d2c-dashboard",
    "ceo-compass",
    "store-compass",
    "statty-dashboard",
    "pma-analytics-importer",
    "mipler-flow",
    "arcs-data-export-backup",
    "bagpiper-data-export",
    "exportier-advanced-data-export",
    "order-data-exporter",
    "product-data-exporter",
    "ests-data-exporter-pro",
    "data-exporter-tax-compliance",
    "xero-taxomate",
    "combidesk-twinfield-accounting",
    "dashi-accounting-myob-xero",
]

DOC_URLS = [
    # Kleio
    "https://getkleio.com/",
    "https://www.getkleio.com/docs",
    "https://getkleio.com/docs/getting-started/metrics",
    "https://www.getkleio.com/docs/integrations/ad-integrations",
    "https://getkleio.com/docs/costs/cogs-and-variable-costs",
    # TrueProfit
    "https://helpdesk.trueprofit.io/en/articles/11330282-overview-how-does-marketing-attribution-work-in-trueprofit",
    "https://helpdesk.trueprofit.io/en/articles/11325389-can-i-update-ad-spend-manually",
    "https://helpdesk.trueprofit.io/en/articles/14631734-connect-google-ads-with-trueprofit",
    "https://helpdesk.trueprofit.io/en/articles/11325292-faq-what-are-the-differences-between-taxes-collected-and-taxes-paid",
    "https://helpdesk.trueprofit.io/en/articles/12289182-set-up-custom-costs",
    "https://helpdesk.trueprofit.io/en/articles/11325259-set-up-taxes-paid",
    # Polar
    "https://intercom.help/polar-app/en/articles/8047958-understanding-attribution-models",
    "https://intercom.help/polar-app/en/articles/15551014-understanding-attribution-settings",
    "https://intercom.help/polar-app/en/articles/10861666-data-settings",
    "https://www.polaranalytics.com/integrations/taxjar",
    "https://www.polaranalytics.com/connectors",
    "https://www.polaranalytics.com/integrations/reddit-ads",
    "https://www.polaranalytics.com/vs/triple-whale",
    # Triple Whale
    "https://kb.triplewhale.com/en/collections/19642466-attribution",
    "https://kb.triplewhale.com/en/articles/5960333-understanding-and-utilizing-attribution-models",
    "https://kb.triplewhale.com/en/articles/10201911-is-vat-international-sales-tax-included-in-the-sales-metric",
    "https://triplewhale.readme.io/docs/blended-ad-spend",
    "https://triplewhale.readme.io/docs/blended-stats-table",
    "https://www.triplewhale.com/pricing",
]

THREAD_URLS = [
    # Shopify Community (known + harvest extras)
    "https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4",
    "https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805",
    "https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628",
    "https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364",
    "https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915",
    # Reddit (known)
    "https://www.reddit.com/r/shopify/comments/1rpjuk0/best_way_to_track_meta_ads_roas_in_shopify/",
    "https://www.reddit.com/r/shopify/comments/1jpb8cy/sales_attribution_tracking/",
    "https://www.reddit.com/r/shopify/comments/1pzy8iv/app_or_plugin_to_calculate_profit_each_month/",
    "https://www.reddit.com/r/shopify/comments/1h27sj3/beprofit_vs_lifetimely_vs/",
    "https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/",
    "https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/",
    "https://www.reddit.com/r/PPC/comments/1r2pvgy/question_for_d2c_founders_on_shopify_running_meta/",
    "https://www.reddit.com/r/PPC/comments/1pqv5kh/how_are_you_handling_ad_attribution/",
]

REDDIT_SEARCHES = [
    "https://www.reddit.com/r/shopify/search.json?q=MER%20OR%20ROAS%20OR%20%22triple%20whale%22%20OR%20%22profit%20tracker%22&restrict_sr=1&sort=relevance&t=year&limit=25",
    "https://www.reddit.com/r/PPC/search.json?q=Shopify%20MER%20OR%20ROAS%20OR%20%22triple%20whale%22%20OR%20TrueProfit&restrict_sr=1&sort=relevance&t=year&limit=25",
    "https://www.reddit.com/r/ecommerce/search.json?q=Shopify%20MER%20OR%20%22triple%20whale%22%20OR%20ROAS%20OR%20TrueProfit&restrict_sr=1&sort=relevance&t=year&limit=25",
    "https://www.reddit.com/r/shopify/search.json?q=TrueProfit%20OR%20Lifetimely%20OR%20BeProfit%20OR%20Kleio&restrict_sr=1&sort=relevance&t=year&limit=25",
    "https://www.reddit.com/r/digital_marketing/search.json?q=Shopify%20MER%20OR%20blended%20ROAS%20OR%20%22triple%20whale%22&restrict_sr=1&sort=relevance&t=year&limit=15",
]

COMMUNITY_SEARCHES = [
    "https://community.shopify.com/search?q=profit%20tracking%20ROAS",
    "https://community.shopify.com/search?q=Triple%20Whale",
    "https://community.shopify.com/search?q=MER%20ad%20spend",
    "https://community.shopify.com/search?q=TrueProfit",
]

MONTHS = {
    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "may": "05",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12",
}

NICHE_RE = re.compile(
    r"\b(profit|roas|poas|ltv|lifetime value|analytics|attribution|report|cohort|"
    r"cogs|margin|mer\b|ad spend|ads? manager|pixel|capi|p&l|pnl|"
    r"blended|marketing efficiency|true profit|net profit)\b",
    re.I,
)

SKIP_PATHS = {
    "search",
    "sitemap",
    "categories",
    "cdn",
    "extensions",
    "partner",
    "partners",
    "stories",
    "set",
    "compare",
    "collections",
    "login",
    "signup",
}


def fetch(url: str, accept: str | None = None) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": accept or "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.8",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            return resp.status, raw.decode(charset, errors="replace")
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return e.code, body
    except Exception as e:
        return 0, str(e)


def unescape(s: str) -> str:
    return htmlmod.unescape(s).replace("\u0026", "&").strip()


def parse_ldjson(page: str) -> dict:
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', page, re.S):
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and data.get("@type") == "SoftwareApplication":
            return data
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get("@type") == "SoftwareApplication":
                    return item
    return {}


def parse_launched(page: str) -> str | None:
    m = re.search(
        r"Launched\s*</p>\s*<p[^>]*>\s*([A-Za-z]+)\s+(\d{1,2}),\s+(20\d{2})",
        page,
        re.S,
    )
    if not m:
        m = re.search(
            r"Launched.{0,120}?([A-Za-z]+)\s+(\d{1,2}),\s+(20\d{2})",
            page,
            re.S,
        )
    if not m:
        return None
    mon = MONTHS.get(m.group(1).lower())
    if not mon:
        return None
    return f"{m.group(3)}-{mon}-{int(m.group(2)):02d}"


def parse_trial(page: str) -> int | None:
    days = []
    for n in re.findall(r"(\d{1,2})[-\s]?day(?:s)?(?:\s+free)?\s+trial", page, re.I):
        days.append(int(n))
    if days:
        # listing cards usually repeat the same trial; take the mode-ish min paid-plan trial
        return min(days)
    if re.search(r"Free trial available", page, re.I) and not days:
        return None
    return None


def parse_price(page: str) -> str:
    # Prefer explicit monthly plans. Do not treat "Free trial" as a free SKU.
    prices = re.findall(r"\$[0-9]+(?:\.[0-9]+)?(?:/month|/mo)?", page)
    # Shopify chrome says "Free to install" / "Free trial" on almost every paid app.
    # Only treat as a free SKU when a plan is actually free.
    free = bool(re.search(r"Free Forever|Forever Free(?: Plan)?", page, re.I))
    if re.search(r">\s*Free\s*<", page) and not re.search(r">\s*Free trial", page, re.I):
        # A pricing-card title that is exactly "Free" (Lifetimely / TW / Clarity).
        free = True
    # Dedup preserving order; drop bare $0.xx surcharge crumbs if monthly exists
    seen: list[str] = []
    for p in prices:
        if p not in seen:
            seen.append(p)
    monthly = [p for p in seen if "/month" in p or "/mo" in p]
    if monthly and free:
        return "Free; " + "; ".join(monthly[:4])
    if monthly:
        return "; ".join(monthly[:4])
    if seen and free:
        return "Free; " + "; ".join(seen[:3])
    if seen:
        return "; ".join(seen[:4])
    if free:
        return "Free"
    return "unlisted"


def parse_adjacent(page: str, self_handle: str) -> list[str]:
    hrefs = re.findall(r"https://apps\.shopify\.com/([a-z0-9][a-z0-9-]{1,80})", page)
    out: list[str] = []
    for h in hrefs:
        if h in SKIP_PATHS or h == self_handle:
            continue
        if h not in out:
            out.append(h)
    return out[:8]


def parse_hero(page: str, ld: dict) -> str:
    og = re.search(r'property="og:description" content="(.*?)"', page)
    if og:
        return unescape(og.group(1))[:280]
    desc = ld.get("description")
    if isinstance(desc, str) and desc.strip():
        return unescape(desc)[:280]
    return ""


def parse_title(page: str, ld: dict) -> str:
    name = ld.get("name")
    if isinstance(name, str) and name.strip():
        return unescape(name)
    t = re.search(r"<title>(.*?)</title>", page, re.S)
    if t:
        return unescape(re.sub(r"\s+", " ", t.group(1))).split("|")[0].strip()
    return ""


def parse_listing(handle: str, url: str, page: str, status: int) -> dict:
    ld = parse_ldjson(page)
    rating = None
    reviews = None
    agg = ld.get("aggregateRating") if isinstance(ld.get("aggregateRating"), dict) else {}
    if agg:
        try:
            rating = float(agg.get("ratingValue"))
        except (TypeError, ValueError):
            rating = None
        try:
            reviews = int(agg.get("ratingCount") or agg.get("reviewCount") or 0)
        except (TypeError, ValueError):
            reviews = None
    hero = parse_hero(page, ld)
    title = parse_title(page, ld)
    return {
        "handle": handle,
        "url": url,
        "title": title,
        "positioning": hero,
        "price": parse_price(page),
        "trial_days": parse_trial(page),
        "rating": rating,
        "review_count": reviews,
        "launched": parse_launched(page),
        "adjacent": parse_adjacent(page, handle),
        "http_status": status,
        "fetched": FETCHED,
        "confidence": "live" if status == 200 and title else "fetch_fail",
    }


def is_niche(card: dict) -> bool:
    blob = " ".join(
        [
            card.get("handle") or "",
            card.get("title") or "",
            card.get("positioning") or "",
        ]
    )
    return bool(NICHE_RE.search(blob))


def harvest_listings(handles: list[str]) -> list[dict]:
    cards: list[dict] = []
    seen: set[str] = set()
    queue: list[str] = []
    for h in handles:
        if h not in seen:
            seen.add(h)
            queue.append(h)

    def one(handle: str) -> dict:
        url = f"https://apps.shopify.com/{handle}"
        status, body = fetch(url)
        if status != 200 or "<title>" not in body:
            return {
                "handle": handle,
                "url": url,
                "title": "",
                "positioning": "",
                "price": "unlisted",
                "trial_days": None,
                "rating": None,
                "review_count": None,
                "launched": None,
                "adjacent": [],
                "http_status": status,
                "fetched": FETCHED,
                "confidence": "fetch_fail",
            }
        return parse_listing(handle, url, body, status)

    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(one, h): h for h in queue}
        for fut in as_completed(futs):
            card = fut.result()
            cards.append(card)
            print(f"listing {card['handle']} {card['http_status']} {card.get('title','')[:50]}", flush=True)
    return cards


def harvest_docs() -> list[dict]:
    rows = []
    for url in DOC_URLS:
        status, body = fetch(url)
        title = ""
        m = re.search(r"<title>(.*?)</title>", body, re.S | re.I)
        if m:
            title = unescape(re.sub(r"\s+", " ", m.group(1)))[:200]
        text = re.sub(r"<script[\s\S]*?</script>", " ", body, flags=re.I)
        text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
        text = unescape(re.sub(r"<[^>]+>", " ", text))
        text = re.sub(r"\s+", " ", text)
        claims = []
        for pat, label in [
            (r".{0,90}\b(ad spend|spend import|sync.{0,20}spend|manual.{0,20}spend|OAuth|connect.{0,20}ads).{0,90}", "spend"),
            (r".{0,90}\b(VAT|tax(?:es)?|TaxJar|tax toggle|taxes collected|taxes paid).{0,90}", "tax"),
            (r".{0,90}\b(attribution|pixel|multi-touch|MTA|last click|first click|blended|MER).{0,90}", "attribution"),
        ]:
            hits = re.findall(pat, text, re.I)
            for h in hits[:3]:
                claims.append({"theme": label, "excerpt": h.strip()[:220]})
        vendor = "unknown"
        if "kleio" in url:
            vendor = "kleio"
        elif "trueprofit" in url:
            vendor = "trueprofit"
        elif "polar" in url:
            vendor = "polar"
        elif "triplewhale" in url or "triple whale" in url.lower() or "triplewhale" in body.lower():
            vendor = "triple_whale"
        rows.append(
            {
                "vendor": vendor,
                "url": url,
                "title": title,
                "http_status": status,
                "claims": claims,
                "fetched": FETCHED,
                "confidence": "live" if status == 200 else "fetch_fail",
            }
        )
        print(f"doc {status} {url}", flush=True)
        time.sleep(0.15)
    return rows


def harvest_reddit_search() -> list[dict]:
    rows = []
    seen = set()
    for url in REDDIT_SEARCHES:
        status, body = fetch(url, accept="application/json")
        print(f"reddit-search {status} {url[:80]}", flush=True)
        if status != 200:
            rows.append(
                {
                    "kind": "reddit_search",
                    "url": url,
                    "title": "",
                    "paraphrase": f"search fetch http {status}",
                    "http_status": status,
                    "fetched": FETCHED,
                    "confidence": "fetch_fail",
                }
            )
            continue
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            continue
        for child in data.get("data", {}).get("children", []):
            d = child.get("data") or {}
            permalink = d.get("permalink")
            if not permalink:
                continue
            full = "https://www.reddit.com" + permalink
            if full in seen:
                continue
            seen.add(full)
            title = d.get("title") or ""
            selftext = (d.get("selftext") or "")[:400]
            paraphrase = (title + ". " + selftext).strip()
            paraphrase = re.sub(r"\s+", " ", paraphrase)[:320]
            rows.append(
                {
                    "kind": "reddit",
                    "url": full,
                    "title": title,
                    "paraphrase": paraphrase,
                    "subreddit": d.get("subreddit"),
                    "score": d.get("score"),
                    "num_comments": d.get("num_comments"),
                    "http_status": 200,
                    "fetched": FETCHED,
                    "confidence": "live",
                }
            )
        time.sleep(0.4)
    return rows


def harvest_named_threads() -> list[dict]:
    rows = []
    for url in THREAD_URLS:
        status, body = fetch(url)
        title = ""
        m = re.search(r"<title>(.*?)</title>", body, re.S | re.I)
        if m:
            title = unescape(re.sub(r"\s+", " ", m.group(1)))[:200]
        text = re.sub(r"<script[\s\S]*?</script>", " ", body, flags=re.I)
        text = unescape(re.sub(r"<[^>]+>", " ", text))
        text = re.sub(r"\s+", " ", text)
        # Take a short paraphrase from visible title + first meaty sentence.
        sent = ""
        for chunk in re.split(r"(?<=[.!?])\s+", text):
            if 40 < len(chunk) < 240 and not chunk.lower().startswith("skip to"):
                sent = chunk
                break
        kind = "community" if "community.shopify.com" in url else "reddit"
        rows.append(
            {
                "kind": kind,
                "url": url,
                "title": title,
                "paraphrase": (title + " — " + sent).strip(" —")[:320],
                "http_status": status,
                "fetched": FETCHED,
                "confidence": "live" if status == 200 else "fetch_fail",
            }
        )
        print(f"thread {status} {url}", flush=True)
        time.sleep(0.2)
    return rows


def harvest_community_search() -> list[dict]:
    rows = []
    seen = set()
    for url in COMMUNITY_SEARCHES:
        status, body = fetch(url)
        print(f"community-search {status} {url}", flush=True)
        hrefs = re.findall(r"https://community\.shopify\.com/t/([a-z0-9-]+)/(\d+)", body, re.I)
        for slug, tid in hrefs:
            full = f"https://community.shopify.com/t/{slug}/{tid}"
            if full in seen:
                continue
            seen.add(full)
            rows.append(
                {
                    "kind": "community_search_hit",
                    "url": full,
                    "title": slug.replace("-", " "),
                    "paraphrase": f"Shopify Community search hit: {slug.replace('-', ' ')}",
                    "http_status": status,
                    "fetched": FETCHED,
                    "confidence": "live" if status == 200 else "fetch_fail",
                }
            )
        time.sleep(0.3)
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def main() -> None:
    listings = harvest_listings(SEED_HANDLES)
    # Snowball adjacent niche handles not already fetched (cap extra 40).
    have = {c["handle"] for c in listings}
    extra: list[str] = []
    for c in listings:
        if c.get("confidence") != "live":
            continue
        for h in c.get("adjacent") or []:
            if h not in have and h not in extra and NICHE_RE.search(h.replace("-", " ")):
                extra.append(h)
    extra = extra[:40]
    if extra:
        print(f"snowball {len(extra)} adjacent handles", flush=True)
        listings.extend(harvest_listings(extra))

    live = [c for c in listings if c.get("confidence") == "live"]
    niche = [c for c in live if is_niche(c)]
    # Prefer niche; if still short, keep remaining live cards.
    keep = niche if len(niche) >= 80 else live

    docs = harvest_docs()
    threads = harvest_named_threads() + harvest_reddit_search() + harvest_community_search()
    # Dedup threads by URL
    tseen: set[str] = set()
    threads_u = []
    for t in threads:
        if t["url"] in tseen:
            continue
        tseen.add(t["url"])
        threads_u.append(t)

    write_jsonl(OUT_DIR / "harvest_listings.jsonl", keep)
    write_jsonl(OUT_DIR / "harvest_docs.jsonl", docs)
    write_jsonl(OUT_DIR / "harvest_threads.jsonl", threads_u)

    # Append unique sources (do not rewrite existing sources.jsonl here).
    src_path = OUT_DIR / "harvest_sources.jsonl"
    sources = []
    for c in keep:
        sources.append({"url": c["url"], "type": "listing", "fetched": FETCHED, "notes": "PRIMARY_SOURCE_HARVEST"})
    for d in docs:
        sources.append({"url": d["url"], "type": "docs", "fetched": FETCHED, "notes": f"vendor={d['vendor']}"})
    for t in threads_u:
        sources.append({"url": t["url"], "type": t.get("kind", "thread"), "fetched": FETCHED, "notes": "paraphrase+url"})
    write_jsonl(src_path, sources)

    print(
        json.dumps(
            {
                "listings_attempted": len(listings),
                "listings_live": len(live),
                "listings_niche": len(niche),
                "listings_kept": len(keep),
                "docs": len(docs),
                "threads": len(threads_u),
                "sources": len(sources),
            }
        )
    )


if __name__ == "__main__":
    main()
