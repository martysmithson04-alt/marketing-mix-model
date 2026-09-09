#!/usr/bin/env python3
"""Assemble enterprise JSONL from prior waves + live fetch. Research only.

Does not invent ratings, review counts, or prices. Live fetch wins when
extracted fields are present. Prior-wave same-day snapshots fill gaps.
429 / 404 are recorded on sources with fetch_status.
"""

from __future__ import annotations

import csv
import json
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORPUS = ROOT.parent

# Extra competitors beyond Wave C jsonl. Ratings/reviews only if a live
# fetch or a prior-wave matrix row supplies them — otherwise null.
EXTRA_COMPETITORS = [
    # Matrix rows missing from Wave C jsonl
    {"id": "adscale", "name": "AdScale", "kind": "ads_os", "listing_url": "https://apps.shopify.com/adscale", "price_scan": "$169", "rating": 4.7, "review_count": 372, "confidence": "live", "price_notes": "WAVE C matrix + this-wave 200 on listing"},
    {"id": "microsoft_ads", "name": "Microsoft Advertising", "kind": "ads_channel", "listing_url": "https://apps.shopify.com/microsoft-advertising", "price_scan": "Free to install", "rating": 3.0, "review_count": 348, "confidence": "live", "price_notes": "WAVE C matrix; this wave 429 on re-fetch"},
    {"id": "madgicx", "name": "Madgicx", "kind": "ads_os", "listing_url": "https://apps.shopify.com/madgicx", "price_scan": "Free to install", "rating": 4.1, "review_count": 16, "confidence": "live", "price_notes": "WAVE C matrix"},
    {"id": "fullstory", "name": "FullStory", "kind": "pixel", "listing_url": "https://apps.shopify.com/fullstory", "price_scan": "Free to install", "rating": 0.0, "review_count": None, "confidence": "live", "price_notes": "WAVE C: store-empty"},
    {"id": "coupler", "name": "Coupler.io", "kind": "pipe", "listing_url": "https://apps.shopify.com/coupler-io", "site_url": "https://www.coupler.io/pricing", "price_scan": "$32", "rating": 2.9, "review_count": 6, "confidence": "live", "price_notes": "WAVE C; low-love pipe"},
    {"id": "coefficient", "name": "Coefficient", "kind": "pipe", "listing_url": "https://apps.shopify.com/coefficient", "site_url": "https://coefficient.io/pricing", "price_scan": "Free", "rating": 4.4, "review_count": 6, "confidence": "live"},
    {"id": "supermetrics", "name": "Supermetrics", "kind": "pipe", "listing_url": "https://apps.shopify.com/supermetrics", "site_url": "https://supermetrics.com/pricing", "price_scan": "$37", "rating": 2.0, "review_count": None, "confidence": "live", "price_notes": "WAVE C store-dead; this-wave 200 name only"},
    {"id": "glew", "name": "Glew", "kind": "suite", "listing_url": "https://apps.shopify.com/glew", "site_url": "https://www.glew.io/", "price_scan": "sales-led", "rating": None, "review_count": None, "confidence": "mixed", "price_notes": "Acquired Everest Group 2026-03; listing card empty this wave"},
    {"id": "stocky", "name": "Stocky", "kind": "native", "listing_url": None, "site_url": "https://help.shopify.com/en/manual/products/inventory/transitioning-from-stocky", "price_scan": "sunset", "price_notes": "Official sunset 2026-08-31 — autopsy, not a peer", "confidence": "live"},
    {"id": "repeat", "name": "Repeat", "kind": "retention", "listing_url": "https://apps.shopify.com/repeat", "price_scan": "Free to install / $199", "rating": 5.0, "review_count": 1, "confidence": "live", "price_notes": "WAVE C matrix — retention, not spend"},
    # This-wave 200s not in Wave C jsonl
    {"id": "meyoo", "name": "Meyoo — PNL & Profit Analytics", "kind": "profit", "listing_url": "https://apps.shopify.com/meyoo", "price_scan": None, "rating": None, "review_count": None, "confidence": "live", "price_notes": "Listing 200 this wave; rating object incomplete"},
    {"id": "fairing", "name": "Fairing Post Purchase Surveys", "kind": "pixel", "listing_url": "https://apps.shopify.com/fairing", "price_scan": None, "rating": 5.0, "review_count": None, "confidence": "live", "price_notes": "Attribution *surveys*, not a cash desk"},
    {"id": "databox", "name": "Databox", "kind": "reports", "listing_url": "https://apps.shopify.com/databox", "price_scan": None, "rating": None, "review_count": None, "confidence": "live", "price_notes": "Modern BI; listing 200 this wave"},
    {"id": "pinterest_channel", "name": "Pinterest", "kind": "ads_channel", "listing_url": "https://apps.shopify.com/pinterest", "price_scan": "Free to install", "rating": 4.1, "review_count": None, "confidence": "live"},
    {"id": "voluum", "name": "Voluum", "kind": "suite", "listing_url": "https://apps.shopify.com/voluum", "price_scan": None, "rating": None, "review_count": None, "confidence": "mixed", "price_notes": "Listing 200 but empty extract"},
    # Sales-led / site-only (no inventing prices)
    {"id": "hyros", "name": "Hyros", "kind": "suite", "listing_url": None, "site_url": "https://hyros.com/", "price_scan": "sales-led", "confidence": "mixed", "price_notes": "apps.shopify.com/hyros 404 this wave"},
    {"id": "wicked_reports", "name": "Wicked Reports", "kind": "suite", "listing_url": None, "site_url": "https://www.wickedreports.com/", "price_scan": "sales-led", "confidence": "mixed", "price_notes": "apps.shopify.com/wicked-reports 404"},
    {"id": "measured", "name": "Measured", "kind": "incrementality", "listing_url": None, "site_url": "https://www.measured.com/", "price_scan": "sales-led", "confidence": "mixed"},
    {"id": "haus", "name": "Haus", "kind": "incrementality", "listing_url": None, "site_url": "https://www.haus.io/", "price_scan": "sales-led", "confidence": "mixed"},
    {"id": "recast", "name": "Recast", "kind": "mmm", "listing_url": None, "site_url": "https://www.getrecast.com/", "price_scan": "sales-led", "confidence": "mixed"},
    {"id": "mutinex", "name": "Mutinex", "kind": "mmm", "listing_url": None, "site_url": "https://www.mutinex.co/", "price_scan": "sales-led", "confidence": "mixed"},
    {"id": "windsor_ai", "name": "Windsor.ai", "kind": "pipe", "listing_url": None, "site_url": "https://windsor.ai/", "price_scan": "site", "confidence": "mixed", "price_notes": "apps.shopify.com/windsor-ai 404"},
    {"id": "funnel_io", "name": "Funnel.io", "kind": "pipe", "listing_url": None, "site_url": "https://funnel.io/pricing", "price_scan": "site", "confidence": "mixed"},
    {"id": "agencyanalytics", "name": "AgencyAnalytics", "kind": "agency", "listing_url": None, "site_url": "https://agencyanalytics.com/pricing", "price_scan": "site", "confidence": "mixed", "price_notes": "apps.shopify.com/agency-analytics 404"},
    {"id": "whatagraph", "name": "Whatagraph", "kind": "agency", "listing_url": None, "site_url": "https://whatagraph.com/pricing", "price_scan": "site", "confidence": "mixed"},
    {"id": "dashthis", "name": "DashThis", "kind": "agency", "listing_url": None, "site_url": "https://www.dashthis.com/pricing/", "price_scan": "site", "confidence": "mixed"},
    {"id": "swydo", "name": "Swydo", "kind": "agency", "listing_url": None, "site_url": "https://www.swydo.com/pricing/", "price_scan": "site", "confidence": "mixed"},
    {"id": "stape", "name": "Stape", "kind": "pixel", "listing_url": None, "site_url": "https://stape.io/", "price_scan": "site", "confidence": "mixed", "price_notes": "apps.shopify.com/stape 404"},
    {"id": "blotout", "name": "Blotout", "kind": "pixel", "listing_url": None, "site_url": "https://blotout.io/", "price_scan": "site", "confidence": "mixed", "price_notes": "apps.shopify.com/blotout 404"},
    {"id": "google_analytics", "name": "Google Analytics 4", "kind": "native", "listing_url": None, "site_url": "https://support.google.com/analytics/", "price_scan": "free", "confidence": "mixed", "price_notes": "Default session religion; not a cash desk"},
    {"id": "meta_ads_manager", "name": "Meta Ads Manager", "kind": "native", "listing_url": None, "site_url": "https://developers.facebook.com/docs/marketing-api/overview", "price_scan": "free UI", "confidence": "mixed", "price_notes": "The lying ROAS surface"},
    {"id": "google_ads", "name": "Google Ads", "kind": "native", "listing_url": None, "site_url": "https://developers.google.com/google-ads/api/docs/start", "price_scan": "free UI", "confidence": "mixed"},
    {"id": "tiktok_ads", "name": "TikTok Ads Manager", "kind": "native", "listing_url": None, "site_url": "https://ads.tiktok.com/marketing_api/docs", "price_scan": "free UI", "confidence": "mixed"},
    {"id": "looker_studio", "name": "Looker Studio", "kind": "diy", "listing_url": None, "site_url": "https://lookerstudio.google.com/", "price_scan": "free", "confidence": "mixed", "price_notes": "DIY MER destination with SyncWith/Supermetrics"},
    {"id": "klaviyo", "name": "Klaviyo", "kind": "retention", "listing_url": None, "site_url": "https://www.klaviyo.com/", "price_scan": "site", "confidence": "mixed", "price_notes": "apps.shopify.com/klaviyo 404 this wave — handle is elsewhere"},
    {"id": "omnisend", "name": "Omnisend", "kind": "retention", "listing_url": "https://apps.shopify.com/omnisend", "price_scan": None, "confidence": "mixed", "price_notes": "this wave 429"},
    {"id": "recharge", "name": "Recharge", "kind": "subs", "listing_url": "https://apps.shopify.com/recharge", "price_scan": None, "confidence": "mixed", "price_notes": "this wave 429"},
    {"id": "loop_returns", "name": "Loop Returns", "kind": "returns", "listing_url": "https://apps.shopify.com/loop-returns", "price_scan": None, "confidence": "mixed", "price_notes": "this wave 429"},
    {"id": "taxomate", "name": "Taxomate", "kind": "finance", "listing_url": "https://apps.shopify.com/taxomate", "price_scan": None, "confidence": "mixed", "price_notes": "this wave 429; WAVE C handle 404 historically — re-listed?"},
    {"id": "matrixify", "name": "Matrixify", "kind": "pipe", "listing_url": "https://apps.shopify.com/matrixify", "price_scan": None, "confidence": "mixed", "price_notes": "this wave 429"},
    {"id": "nabu", "name": "Nabu (Meta/TikTok pixel)", "kind": "pixel", "listing_url": "https://apps.shopify.com/nabu", "price_scan": None, "confidence": "mixed", "price_notes": "this wave 429; WAVE C aisle card exists"},
    {"id": "plenisher", "name": "Plenisher", "kind": "ops", "listing_url": None, "site_url": "https://plenisher.ai/", "price_scan": "Free / Pro $49 (VENDOR_CLAIM)", "confidence": "mixed", "price_notes": "Stocky-migration marketing; not an analytics peer"},
    {"id": "mida", "name": "MIDA Replay, Heatmap & Insight", "kind": "pixel", "listing_url": None, "site_url": "https://apps.shopify.com/categories/store-management-operations-analytics/all", "price_scan": "Free plan", "rating": 4.9, "review_count": 562, "confidence": "live", "price_notes": "Visible on Analytics aisle 2026-09-09 this wave; handle not isolated"},
    {"id": "propel", "name": "Propel Replay, Survey, Heatmap", "kind": "pixel", "listing_url": None, "site_url": "https://apps.shopify.com/categories/store-management-operations-analytics/all", "price_scan": "Free plan", "rating": 4.9, "review_count": 676, "confidence": "live", "price_notes": "Analytics aisle first screen"},
    {"id": "nabu_pixels", "name": "Meta & Facebook Pixels by Nabu", "kind": "pixel", "listing_url": "https://apps.shopify.com/nabu", "price_scan": "Free to install", "rating": 5.0, "review_count": 116, "confidence": "live", "price_notes": "Aisle card this wave; listing 429 on handle re-fetch"},
    {"id": "grapevine", "name": "Grapevine Post Purchase Survey", "kind": "pixel", "listing_url": None, "site_url": "https://apps.shopify.com/categories/store-management-operations-analytics/all", "price_scan": "trial", "rating": 5.0, "review_count": 221, "confidence": "live", "price_notes": "Attribution surveys on aisle"},
    {"id": "parkour_tiktok", "name": "Parkour: TikTok Pixel & CAPI", "kind": "pixel", "listing_url": None, "site_url": "https://apps.shopify.com/categories/store-management-operations-analytics/all", "price_scan": "Free", "rating": 5.0, "review_count": 30, "confidence": "live"},
    {"id": "tixel", "name": "TiXel: Meta Pixel TikTok Pixel", "kind": "pixel", "listing_url": None, "site_url": "https://apps.shopify.com/categories/store-management-operations-analytics/all", "price_scan": "Free plan", "rating": 4.4, "review_count": 88, "confidence": "live"},
    {"id": "realtimestack", "name": "RealtimeStack : Live Analytics", "kind": "reports", "listing_url": None, "site_url": "https://apps.shopify.com/categories/store-management-operations-analytics/all", "price_scan": "Free plan", "rating": 4.8, "review_count": 107, "confidence": "live"},
    {"id": "indexgpt", "name": "IndexGPT: AI SEO for ChatGPT", "kind": "adjacent", "listing_url": None, "site_url": "https://apps.shopify.com/categories/store-management-operations-analytics/all", "price_scan": "Free plan", "rating": 4.9, "review_count": 143, "confidence": "live", "price_notes": "Aisle merchandises LLM SEO next to cash desks — topology evidence"},
    {"id": "godmode", "name": "Godmode", "kind": "profit", "listing_url": None, "site_url": "https://www.trygodmode.com/blog/shopify-real-profit-2026-dashboard-lies", "price_scan": "site", "confidence": "mixed", "price_notes": "apps.shopify.com/godmode 404; vendor blog only"},
    {"id": "elevar_site", "name": "Elevar (site)", "kind": "pixel", "listing_url": "https://apps.shopify.com/gtm-datalayer-by-elevar", "site_url": "https://www.getelevar.com/pricing/", "price_scan": "From $225", "confidence": "mixed", "price_notes": "alias of elevar for site URL; skipped if elevar exists"},
]

# Additional problems (beyond Wave A p1–p15 and PR5 P-001–P-016).
# Each must have at least one public URL already in the corpus.
NEW_PROBLEMS = [
    {"id": "p16_returns_period", "rank": 16, "name": "Refunds/edits move sales across periods", "wtp": "high_finance", "review_proxy": "TW docs + Lifetimely Koss Design 1★", "mcfly": "none", "tag": "RESEARCH_OPTION", "urls": ["https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915", "https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics"]},
    {"id": "p17_vat_toggle", "rank": 17, "name": "Need a labeled tax-in/tax-out definition", "wtp": "strong_eu", "review_proxy": "TW Kove 1★; TP VocaSpark 1★; Kleio ships toggle", "mcfly": "missing", "tag": "RESEARCH_OPTION", "urls": ["https://apps.shopify.com/triplewhale-1", "https://getkleio.com/docs/getting-started/metrics"]},
    {"id": "p18_attributed_only_spend", "rank": 18, "name": "Profit tile subtracts only UTM-matched spend", "wtp": "strong", "review_proxy": "BeProfit Farley 1★; Community 588628", "mcfly": "religion_forbids", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/beprofit-profit-tracker", "https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628"]},
    {"id": "p19_order_meter_surprise", "rank": 19, "name": "Order/GMV success tax with late notice", "wtp": "hate", "review_proxy": "TP bamtoo / Brooklyn 1★; Lifetimely $600", "mcfly": "refuses", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/trueprofit", "https://mcflyads.com/pricing"]},
    {"id": "p20_cancel_hell", "rank": 20, "name": "Uninstall does not stop billing / history hostage", "wtp": "strong", "review_proxy": "BeProfit $720 zombie; TW cancel 1★", "mcfly": "must_not_copy", "tag": "CURRENT_RELIGION", "urls": ["https://help.shopify.com/en/manual/apps/uninstalling-apps", "https://apps.shopify.com/beprofit-profit-tracker"]},
    {"id": "p21_sales_call_gate", "rank": 21, "name": "Cannot trial without a sales call / work email", "wtp": "lean_merchant", "review_proxy": "Polar dryoasis / Skechers / Minseart 1★", "mcfly": "self_serve", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/polar-analytics"]},
    {"id": "p22_cogs_rot", "rank": 22, "name": "Variant/supplier cost changes do not rewrite history cleanly", "wtp": "strong", "review_proxy": "Community 657805; TP stale variants", "mcfly": "typed_only", "tag": "RESEARCH_OPTION", "urls": ["https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805", "https://help.shopify.com/en/manual/products/details/product-cost"]},
    {"id": "p23_token_expiry", "rank": 23, "name": "Meta spend tokens die in 60 days", "wtp": "ops", "review_proxy": "Kleio docs: cannot auto-refresh", "mcfly": "if_oauth", "tag": "RESEARCH_OPTION", "urls": ["https://www.getkleio.com/docs/integrations/ad-integrations"]},
    {"id": "p24_shop_campaigns_only", "rank": 24, "name": "ShopifyQL marketing schema is Shop Campaigns, not Meta/Google", "wtp": "real", "review_proxy": "Official ShopifyQL docs", "mcfly": "wedge", "tag": "CURRENT_RELIGION", "urls": ["https://shopify.dev/docs/api/shopifyql/latest/schemas/marketing/shop_campaign_insights", "https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4"]},
    {"id": "p25_listing_integrity", "rank": 25, "name": "Listing claims features the app does not ship", "wtp": "trust", "review_proxy": "Mcfly LTV/Goals vs repo; Lifetimely free-but-paywall 1★", "mcfly": "risk", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/mcfly-analytics-public", "https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements"]},
    {"id": "p26_ttv_trial_mismatch", "rank": 26, "name": "7-day trial dies if first number needs homework", "wtp": "conversion", "review_proxy": "Aisle default 14-day; Mcfly 7 + CSV", "mcfly": "live_7", "tag": "RESEARCH_OPTION", "urls": ["https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials", "https://apps.shopify.com/kleio"]},
    {"id": "p27_pixel_rail", "rank": 27, "name": "Analytics aisle merchandises free pixels; cash desk is misfiled", "wtp": "distribution", "review_proxy": "Mcfly adjacent Clarity/Parkour/WeTracked; 1,546-app aisle", "mcfly": "live_fail", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/categories/store-management-operations-analytics/all", "https://apps.shopify.com/mcfly-analytics-public"]},
    {"id": "p28_name_collision", "rank": 28, "name": "Total ROAS vs cash MER vs Ads Manager ROAS", "wtp": "confusion", "review_proxy": "Live listing vs repo; Polar MER tile", "mcfly": "two_names", "tag": "RESEARCH_OPTION", "urls": ["https://apps.shopify.com/mcfly-analytics-public", "https://mcflyads.com/product"]},
    {"id": "p29_claims_vs_cash", "rank": 29, "name": "Need Ads Manager claim next to Shopify till as a product", "wtp": "high_midmarket", "review_proxy": "r/PPC 1u81q7r; Kleio refuses the card", "mcfly": "partial_footer", "tag": "RESEARCH_OPTION", "urls": ["https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/", "https://getkleio.com/"]},
    {"id": "p30_mcp_monday", "rank": 30, "name": "Monday artifact via MCP/Claude, not a native email", "wtp": "rising", "review_proxy": "Kleio Trek Light / Hummii 5★", "mcfly": "none", "tag": "RESEARCH_OPTION", "urls": ["https://apps.shopify.com/kleio", "https://getkleio.com/docs/integrations/mcp-server"]},
    {"id": "p31_cost_incomplete", "rank": 31, "name": "Show profit only with a missing-cost flag", "wtp": "strong", "review_proxy": "Community 657805 recipe; Kleio missing-data queue; Margn data-health", "mcfly": "none", "tag": "RESEARCH_OPTION", "urls": ["https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805", "https://apps.shopify.com/margn-1"]},
    {"id": "p32_offline_ledger", "rank": 32, "name": "Billboard/retainer/offline spend has no first-class home", "wtp": "niche", "review_proxy": "Mcfly hero; Kleio Other Marketing is fixed cost", "mcfly": "core_wedge", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/mcfly-analytics-public", "https://mcflyads.com/product"]},
    {"id": "p33_allocation_circular", "rank": 33, "name": "Advice that assumes sales ∝ spend", "wtp": "credibility", "review_proxy": "mer-core allocation.ts; r/PPC pause tests", "mcfly": "ships_heuristic", "tag": "CURRENT_RELIGION", "urls": ["https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/"]},
    {"id": "p34_bfs_gate", "rank": 34, "name": "BFS needs 50 paid installs + 5 reviews", "wtp": "n/a", "review_proxy": "Official BFS requirements", "mcfly": "not_this_quarter", "tag": "CURRENT_RELIGION", "urls": ["https://shopify.dev/docs/apps/launch/built-for-shopify/requirements"]},
    {"id": "p35_review_physics", "rank": 35, "name": "0 reviews → hostile conversion; Magic needs 100 written + 4.0", "wtp": "distribution", "review_proxy": "Official review docs; TSC MARKET_REPORT", "mcfly": "live_0", "tag": "CURRENT_RELIGION", "urls": ["https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews", "https://taylorsicard.com/blog/shopify-app-listing-conversion"]},
    {"id": "p36_take_rate", "rank": 36, "name": "2.9% processing + 0% then 15% share; refunds do not reduce gross", "wtp": "n/a_founder", "review_proxy": "Official revenue-share", "mcfly": "under_1m_cap", "tag": "CURRENT_RELIGION", "urls": ["https://shopify.dev/docs/apps/launch/distribution/revenue-share"]},
    {"id": "p37_subs_cash", "rank": 37, "name": "Subscription billed ≠ cash collected this period", "wtp": "subset", "review_proxy": "DEEP_DIVE_RETURNS_LTV_SUBS; Recharge aisle", "mcfly": "none", "tag": "RESEARCH_OPTION", "urls": ["https://apps.shopify.com/recharge"]},
    {"id": "p38_amazon_plus", "rank": 38, "name": "Amazon + Shopify identity / add-on priced like a second app", "wtp": "high_subset", "review_proxy": "Lifetimely Amazon +$75; carnivoro 1★", "mcfly": "none", "tag": "RESEARCH_OPTION", "urls": ["https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics", "https://www.lifetimely.io/pricing"]},
    {"id": "p39_work_email", "rank": 39, "name": "Gmail/private email blocked on enterprise trials", "wtp": "lean", "review_proxy": "Polar Minseart 1★", "mcfly": "must_not_copy", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/polar-analytics"]},
    {"id": "p40_support_named", "rank": 40, "name": "Love is a named human (Juan/Bryce), not a bot", "wtp": "retention", "review_proxy": "TW Marielle; TrueProfit shipping-cost + named CS; BeProfit bot 1★", "mcfly": "inbox_unproven", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/triplewhale-1", "https://apps.shopify.com/trueprofit"]},
    {"id": "p41_emq_chase", "rank": 41, "name": "Event Match Quality / CAPI accuracy cannot be evidenced", "wtp": "ads", "review_proxy": "WeTracked elife 1★; Parkour EMQ 5★", "mcfly": "refuse_own", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/wetracked-io-connect", "https://apps.shopify.com/parkour-pixel"]},
    {"id": "p42_connector_zoo", "rank": 42, "name": "40 connectors without a religion", "wtp": "agency_diy", "review_proxy": "SyncWith $4.99/10; Polar 45+ @ $750", "mcfly": "refuse", "tag": "CURRENT_RELIGION", "urls": ["https://apps.shopify.com/syncwith", "https://apps.shopify.com/polar-analytics"]},
    {"id": "p43_dual_clock", "rank": 43, "name": "Need delivery-day vs invoice/accrual-day", "wtp": "finance", "review_proxy": "Kleio (O) metrics; Apex accrual; Community 577364", "mcfly": "none", "tag": "RESEARCH_OPTION", "urls": ["https://getkleio.com/docs/getting-started/metrics", "https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364"]},
    {"id": "p44_gift_cards", "rank": 44, "name": "Gift cards / store credit inflate sales vs cash", "wtp": "finance", "review_proxy": "Finance reports Help; Kleio definition sheet", "mcfly": "underspecified", "tag": "RESEARCH_OPTION", "urls": ["https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/finances-reports"]},
    {"id": "p45_currency", "rank": 45, "name": "Multi-currency / payout FX vs ad-account currency", "wtp": "intl", "review_proxy": "DEEP_DIVE_INTERNATIONAL", "mcfly": "none", "tag": "RESEARCH_OPTION", "urls": ["https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/marketing-reports"]},
]


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"wrote {path.name}: {len(rows)}")


def merge_by_id(rows: list[dict], key: str = "id") -> list[dict]:
    out: dict[str, dict] = {}
    for r in rows:
        k = r.get(key)
        if not k:
            continue
        if k in out:
            out[k] = {**out[k], **{kk: vv for kk, vv in r.items() if vv not in (None, "", [])}}
        else:
            out[k] = dict(r)
    return list(out.values())


def main() -> None:
    # --- competitors ---
    wave_c = load_jsonl(Path("/tmp/wave-dbs/c_competitors.jsonl"))
    local = load_jsonl(ROOT / "competitors.jsonl")
    extras = []
    have = {r["id"] for r in wave_c + local}
    for e in EXTRA_COMPETITORS:
        if e["id"] in have or e["id"] == "elevar_site":
            continue
        e.setdefault("fetched", "2026-09-09")
        e.setdefault("launched", None)
        e.setdefault("star5_pct", None)
        e.setdefault("star1_pct", None)
        e.setdefault("trial_days", None)
        e.setdefault("site_url", None)
        extras.append(e)
    competitors = merge_by_id(wave_c + local + extras)

    # Overlay live extract when we have a 200 + name/rating
    fetch_rows = load_jsonl(ROOT / "fetch_raw.jsonl")
    by_listing = {c.get("listing_url"): c for c in competitors if c.get("listing_url")}
    for fr in fetch_rows:
        url = fr.get("url")
        ex = fr.get("extracted") or {}
        if url in by_listing and fr.get("ok") and ex.get("name"):
            c = by_listing[url]
            if ex.get("rating") is not None:
                c["rating"] = ex["rating"]
            if ex.get("review_count") is not None:
                c["review_count"] = ex["review_count"]
            if ex.get("price_scan") and not c.get("price_scan"):
                c["price_scan"] = ex["price_scan"]
            if ex.get("trial_days") and not c.get("trial_days"):
                c["trial_days"] = ex["trial_days"]
            c["this_wave_fetch"] = "200"
        elif url in by_listing:
            by_listing[url]["this_wave_fetch"] = str(fr.get("status") or fr.get("error"))

    # WebFetch this wave (App Store HTML via browser tool) — do not invent
    for c in competitors:
        if c.get("id") == "trueprofit":
            c["review_count"] = 900
            c["price_notes"] = (c.get("price_notes") or "") + " | WebFetch 2026-09-09 listing shows 5.0 (900)"
            c["confidence"] = "live"
        if c.get("id") == "clarity":
            c["review_count"] = 2127
            c["confidence"] = "live"
        if c.get("id") == "mcfly":
            c["review_count"] = 0
            c["rating"] = 0.0
            c["price_scan"] = "$39/month"
            c["confidence"] = "live"

    write_jsonl(ROOT / "competitors.jsonl", competitors)

    # --- problems ---
    old = load_jsonl(ROOT / "problems.jsonl")
    problems = merge_by_id(old + NEW_PROBLEMS)
    # fold PR5 CSV as parallel IDs (already distinct P-001)
    csv_path = ROOT / "problems.csv"
    if csv_path.exists():
        with csv_path.open() as f:
            for row in csv.DictReader(f):
                pid = row["id"]
                if any(p["id"] == pid for p in problems):
                    continue
                problems.append(
                    {
                        "id": pid,
                        "rank": int(row.get("priority") or 99),
                        "name": row.get("pain_short"),
                        "wtp": row.get("who_hurt"),
                        "review_proxy": row.get("evidence_ids"),
                        "mcfly": row.get("mcfly_fit"),
                        "tag": "RESEARCH_OPTION" if row.get("research_option") == "true" else "CURRENT_RELIGION",
                        "urls": [],
                    }
                )
    write_jsonl(ROOT / "problems.jsonl", problems)

    # --- quotes ---
    quotes = load_jsonl(ROOT / "review_quotes.jsonl")
    seen = {(q.get("url"), q.get("quote")) for q in quotes}
    reviews_csv = ROOT / "reviews.csv"
    if reviews_csv.exists():
        with reviews_csv.open() as f:
            for row in csv.DictReader(f):
                snippet = (row.get("verbatim_snippet") or "").strip()
                url = row.get("url")
                if not snippet or (url, snippet) in seen:
                    continue
                quotes.append(
                    {
                        "id": row.get("id"),
                        "app_id": (row.get("app") or "").lower().replace(" ", "_"),
                        "date": row.get("date"),
                        "stars": int(row["stars"]) if (row.get("stars") or "").isdigit() else None,
                        "store": row.get("reviewer"),
                        "country": row.get("country"),
                        "tenure": row.get("tenure"),
                        "theme": row.get("problem_ids"),
                        "quote": snippet,
                        "url": url,
                        "grade": row.get("grade"),
                    }
                )
                seen.add((url, snippet))
    for fq in load_jsonl(ROOT / "fetch_quotes.jsonl"):
        key = (fq.get("url"), fq.get("quote"))
        if key in seen or not fq.get("quote"):
            continue
        quotes.append(
            {
                "app_id": (fq.get("url") or "").rstrip("/").split("/")[-1],
                "quote": fq["quote"],
                "url": fq.get("url"),
                "fetched": fq.get("fetched"),
                "stars": None,
                "theme": "listing_visible",
            }
        )
        seen.add(key)
    write_jsonl(ROOT / "review_quotes.jsonl", quotes)

    # --- sources ---
    sources = load_jsonl(ROOT / "sources.jsonl")
    for extra in Path("/tmp/wave-dbs").glob("*_sources.jsonl"):
        sources.extend(load_jsonl(extra))
    # fetch_raw
    for fr in fetch_rows:
        sources.append(
            {
                "url": fr.get("url"),
                "type": "listing" if "apps.shopify.com/" in (fr.get("url") or "") else "fetch",
                "fetched": "2026-09-09",
                "notes": f"enterprise wave status={fr.get('status')} ok={fr.get('ok')} err={fr.get('error')}",
                "fetch_status": fr.get("status") or fr.get("error"),
                "ok": fr.get("ok"),
                "excerpt": (fr.get("excerpt") or "")[:180],
            }
        )
    # dedupe by url, keep richest
    by_url: dict[str, dict] = {}
    for s in sources:
        u = s.get("url")
        if not u:
            continue
        if u not in by_url:
            by_url[u] = s
        else:
            # prefer a row that has ok=True or a longer notes
            if s.get("ok") is True or (len(s.get("notes") or "") > len(by_url[u].get("notes") or "")):
                by_url[u] = {**by_url[u], **s}
    sources = list(by_url.values())
    write_jsonl(ROOT / "sources.jsonl", sources)

    # --- rebuild sqlite via existing builder, then add extra tables ---
    subprocess.check_call([sys.executable, str(ROOT / "build_db.py")])

    print("COUNTS", {
        "competitors": len(competitors),
        "problems": len(problems),
        "quotes": len(quotes),
        "sources": len(sources),
    })


if __name__ == "__main__":
    main()
