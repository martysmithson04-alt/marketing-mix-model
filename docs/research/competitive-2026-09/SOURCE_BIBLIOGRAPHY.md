# Source bibliography — URLs actually fetched

**Date window:** 2026-09-09
**Rule:** every row is a URL this corpus retrieved (this wave or PRs #5–#13 same-day fetches). If this wave got 429/404/timeout, that is stated. One line = what the page **proves**, not a vibe.
**Do not invent** review counts or installs from these rows.

Fetch mix this wave (`db/fetch_raw.jsonl`): **238 attempted · 103 OK · 50 Shopify HTTP 429 · 65 HTTP 404 · 17 HTTP 403 · 2 network fail**. Reddit threads often returned a bot-challenge page (`FETCH_FAILED` this wave); prior-wave snippets remain cited as `PUBLIC_SNIPPET`.

Counts after assemble: **300 unique URLs** in `db/sources.jsonl`.

## How to use

Query `SELECT url, type, notes, fetch_status FROM sources;` in `db/competitive.sqlite`.
Primary decision docs cite these IDs implicitly by URL. If a number is not on a live page, it is `UNVERIFIED` / `VENDOR_CLAIM` / `MARKET_REPORT`.

## A. Official Shopify (policy / taxonomy / billing)

| # | URL | Proves | Fetch |
| --- | --- | --- | --- |
| 1 | https://help.shopify.com/en/manual/apps/about-apps | BFS merchant-facing badge copy | prior-wave |
| 2 | https://help.shopify.com/en/manual/apps/uninstalling-apps | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 3 | https://help.shopify.com/en/manual/products/details/product-cost | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 4 | https://help.shopify.com/en/manual/products/inventory/transitioning-from-stocky | Stocky sunset 2026-08-31 | prior-wave |
| 5 | https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/marketing-attribution | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 6 | https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/marketing-performance | Cost only Shopify-created activities | prior-wave |
| 7 | https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/finances-reports | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 8 | https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/marketing-reports | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 9 | https://help.shopify.com/en/partners/build-integrate/making-apps | 15% reduced plan framing | prior-wave |
| 10 | https://shopify.dev/changelog/updated-app-store-requirements-13-always-use-honest-and-transparent-review-practices | 1.3 2026-07-06 | prior-wave |
| 11 | https://shopify.dev/docs/api/app-home/apis/user-interface-and-interactions/reviews-api | 24h/60d/3x365 | prior-wave |
| 12 | https://shopify.dev/docs/api/shopifyql/latest/schemas/marketing/shop_campaign_insights | enterprise wave status=200 ok=True err=None | 200 |
| 13 | https://shopify.dev/docs/apps/build/analytics | ShopifyQL / App Events platform | prior-wave |
| 14 | https://shopify.dev/docs/apps/launch/app-store-review | enterprise wave status=200 ok=True err=None | 200 |
| 15 | https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories | Seven top-level categories; Analytics is Store management → Operations, not Marketing navbar. | 200 |
| 16 | https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing | enterprise wave status=200 ok=True err=None | 200 |
| 17 | https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials | Trials configurable; 180-day anti-reinstall window. | 200 |
| 18 | https://shopify.dev/docs/apps/launch/built-for-shopify | enterprise wave status=200 ok=True err=None | 200 |
| 19 | https://shopify.dev/docs/apps/launch/built-for-shopify/requirements | BFS floor includes 50 net paid-plan installs + 5 reviews (rating threshold unpublished). | 200 |
| 20 | https://shopify.dev/docs/apps/launch/distribution/revenue-share | Official take-rate: 2.9% processing; 0% share on first $1M from 2025-01-01 then 15%; refunds do not reduce gross. | 200 |
| 21 | https://shopify.dev/docs/apps/launch/marketing/advertising | first-price CPC | prior-wave |
| 22 | https://shopify.dev/docs/apps/launch/marketing/advertising/ad-billing | 30d or $100 | prior-wave |
| 23 | https://shopify.dev/docs/apps/launch/marketing/advertising/create-ads | relevance + bid | prior-wave |
| 24 | https://shopify.dev/docs/apps/launch/marketing/advertising/faq | $5 min budget; impression-date attribution | prior-wave |
| 25 | https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews | Reviews need installs; AI summary needs 100 written + 4.0; no paid-for-reviews; 45-day post-uninstall window. | 200 |
| 26 | https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements | enterprise wave status=200 ok=True err=None | 200 |
| 27 | https://apps.shopify.com/categories/marketing-and-conversion | enterprise wave status=200 ok=True err=None | 200 |
| 28 | https://apps.shopify.com/categories/store-management | enterprise wave status=200 ok=True err=None | 200 |
| 29 | https://apps.shopify.com/categories/store-management-operations-analytics/all | Analytics aisle states **1,546 apps**; first screen is free pixels/heatmaps, not cash desks. | 200 |

## B. App Store listings (live or 429/404 this wave)

| # | URL | Proves | Fetch |
| --- | --- | --- | --- |
| 30 | https://apps.shopify.com/a2x | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 31 | https://apps.shopify.com/adscale | enterprise wave status=200 ok=True err=None | 200 |
| 32 | https://apps.shopify.com/advanced-profit-reports | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 33 | https://apps.shopify.com/advanced-reports | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 34 | https://apps.shopify.com/adverity | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 35 | https://apps.shopify.com/advertising-insights | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 36 | https://apps.shopify.com/aftership-returns | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 37 | https://apps.shopify.com/agency-analytics | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 38 | https://apps.shopify.com/amazon-channel | enterprise wave status=200 ok=True err=None | 200 |
| 39 | https://apps.shopify.com/analysisgpt | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 40 | https://apps.shopify.com/analytics-king | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 41 | https://apps.shopify.com/analyzify | enterprise wave status=200 ok=True err=None | 200 |
| 42 | https://apps.shopify.com/attentive | enterprise wave status=200 ok=True err=None | 200 |
| 43 | https://apps.shopify.com/attribuly | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 44 | https://apps.shopify.com/beprofit-profit-tracker | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 45 | https://apps.shopify.com/betterreports | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 46 | https://apps.shopify.com/bing-shopping | enterprise wave status=200 ok=True err=None | 200 |
| 47 | https://apps.shopify.com/bloom-analytics | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 48 | https://apps.shopify.com/blotout | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 49 | https://apps.shopify.com/bold-subscriptions | enterprise wave status=200 ok=True err=None | 200 |
| 50 | https://apps.shopify.com/bookkeep | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 51 | https://apps.shopify.com/capi-gateway | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 52 | https://apps.shopify.com/cashdash-pro | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 53 | https://apps.shopify.com/clearprofit | enterprise wave status=200 ok=True err=None | 200 |
| 54 | https://apps.shopify.com/coefficient | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 55 | https://apps.shopify.com/compass-analytics | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 56 | https://apps.shopify.com/conversion-tracking | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 57 | https://apps.shopify.com/coupler-io | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 58 | https://apps.shopify.com/custom-reports | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 59 | https://apps.shopify.com/daasity | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 60 | https://apps.shopify.com/data-export | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 61 | https://apps.shopify.com/databox | enterprise wave status=200 ok=True err=None | 200 |
| 62 | https://apps.shopify.com/enhanced-ecommerce | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 63 | https://apps.shopify.com/ez-exporter | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 64 | https://apps.shopify.com/facebook | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 65 | https://apps.shopify.com/fairing | enterprise wave status=200 ok=True err=None | 200 |
| 66 | https://apps.shopify.com/finaloop | enterprise wave status=200 ok=True err=None | 200 |
| 67 | https://apps.shopify.com/fullstory | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 68 | https://apps.shopify.com/funnel-io | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 69 | https://apps.shopify.com/glew | enterprise wave status=200 ok=True err=None | 200 |
| 70 | https://apps.shopify.com/glew-io | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 71 | https://apps.shopify.com/go-profit | enterprise wave status=200 ok=True err=None | 200 |
| 72 | https://apps.shopify.com/godmode | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 73 | https://apps.shopify.com/google-analytics | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 74 | https://apps.shopify.com/google-channel | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 75 | https://apps.shopify.com/gorgias | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 76 | https://apps.shopify.com/gtm-datalayer-by-elevar | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 77 | https://apps.shopify.com/hotjar | enterprise wave status=200 ok=True err=None | 200 |
| 78 | https://apps.shopify.com/humblytics | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 79 | https://apps.shopify.com/hyros | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 80 | https://apps.shopify.com/judge-me | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 81 | https://apps.shopify.com/juicy | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 82 | https://apps.shopify.com/klar-analytics | enterprise wave status=200 ok=True err=None | 200 |
| 83 | https://apps.shopify.com/klaviyo | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 84 | https://apps.shopify.com/klaviyo-sms | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 85 | https://apps.shopify.com/kleio | Live Kleio: $29/mo Everything, 14-day, 5.0 (20), 100% 5★, Works with Meta/Google, same adjacent rail as Mcfly. | 429 |
| 86 | https://apps.shopify.com/lifetimely-attribution | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 87 | https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 88 | https://apps.shopify.com/linkmybooks | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 89 | https://apps.shopify.com/littledata | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 90 | https://apps.shopify.com/loop-returns | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 91 | https://apps.shopify.com/loox | enterprise wave status=200 ok=True err=None | 200 |
| 92 | https://apps.shopify.com/lucky-orange | enterprise wave status=200 ok=True err=None | 200 |
| 93 | https://apps.shopify.com/madgicx | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 94 | https://apps.shopify.com/marginlens-ai-powered | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 95 | https://apps.shopify.com/margins | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 96 | https://apps.shopify.com/margn-1 | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 97 | https://apps.shopify.com/matrixify | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 98 | https://apps.shopify.com/mcfly-analytics-public | Live Mcfly: $39/mo, 7-day trial, 0.0/0 reviews, launched Sept 7 2026, Total ROAS hero, adjacent Clarity/WeTracked/Parkour. | 429 |
| 99 | https://apps.shopify.com/meta-capi | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 100 | https://apps.shopify.com/metorik | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 101 | https://apps.shopify.com/metrilo | enterprise wave status=200 ok=True err=None | 200 |
| 102 | https://apps.shopify.com/meyoo | enterprise wave status=200 ok=True err=None | 200 |
| 103 | https://apps.shopify.com/microsoft-advertising | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 104 | https://apps.shopify.com/microsoft-clarity | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 105 | https://apps.shopify.com/moby-ai | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 106 | https://apps.shopify.com/nabu | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 107 | https://apps.shopify.com/northbeam | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 108 | https://apps.shopify.com/omnisend | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 109 | https://apps.shopify.com/parkour-pixel | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 110 | https://apps.shopify.com/peaka | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 111 | https://apps.shopify.com/peaklytics | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 112 | https://apps.shopify.com/peel | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 113 | https://apps.shopify.com/pinterest | enterprise wave status=200 ok=True err=None | 200 |
| 114 | https://apps.shopify.com/pixelfy | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 115 | https://apps.shopify.com/plenisher | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 116 | https://apps.shopify.com/polar-analytics | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 117 | https://apps.shopify.com/postscript | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 118 | https://apps.shopify.com/privy | enterprise wave status=200 ok=True err=None | 200 |
| 119 | https://apps.shopify.com/profit-by-product | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 120 | https://apps.shopify.com/profit-calc | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 121 | https://apps.shopify.com/profit-hero | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 122 | https://apps.shopify.com/profit-panel | enterprise wave status=200 ok=True err=None | 200 |
| 123 | https://apps.shopify.com/profitario | enterprise wave status=200 ok=True err=None | 200 |
| 124 | https://apps.shopify.com/profitario-ai | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 125 | https://apps.shopify.com/profitiq | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 126 | https://apps.shopify.com/profitmetrics | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 127 | https://apps.shopify.com/puzzle-bookkeeping | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 128 | https://apps.shopify.com/quickbooks-commerce | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 129 | https://apps.shopify.com/recharge | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 130 | https://apps.shopify.com/redtrack | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 131 | https://apps.shopify.com/repeat | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 132 | https://apps.shopify.com/repeat-customer-insights | enterprise wave status=200 ok=True err=None | 200 |
| 133 | https://apps.shopify.com/report-pundit | enterprise wave status=200 ok=True err=None | 200 |
| 134 | https://apps.shopify.com/report-toaster | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 135 | https://apps.shopify.com/rockerbox | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 136 | https://apps.shopify.com/segmetrics | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 137 | https://apps.shopify.com/server-side-gtm | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 138 | https://apps.shopify.com/setpilot | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 139 | https://apps.shopify.com/shiphero | enterprise wave status=200 ok=True err=None | 200 |
| 140 | https://apps.shopify.com/shopify-flow | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 141 | https://apps.shopify.com/shopify-reports | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 142 | https://apps.shopify.com/skio | enterprise wave status=200 ok=True err=None | 200 |
| 143 | https://apps.shopify.com/smsbump | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 144 | https://apps.shopify.com/snapchat | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 145 | https://apps.shopify.com/sonar | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 146 | https://apps.shopify.com/stape | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 147 | https://apps.shopify.com/stay-ai | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 148 | https://apps.shopify.com/stocky | enterprise wave status=200 ok=True err=None | 200 |
| 149 | https://apps.shopify.com/subscription-payments | Recharge 4.8/3118 | prior-wave |
| 150 | https://apps.shopify.com/sunforce | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 151 | https://apps.shopify.com/supermetrics | enterprise wave status=200 ok=True err=None | 200 |
| 152 | https://apps.shopify.com/syncwith | enterprise wave status=200 ok=True err=None | 200 |
| 153 | https://apps.shopify.com/synder | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 154 | https://apps.shopify.com/taxomate | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 155 | https://apps.shopify.com/tidio | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 156 | https://apps.shopify.com/tiktok | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 157 | https://apps.shopify.com/tiktok-events-api | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 158 | https://apps.shopify.com/trackify | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 159 | https://apps.shopify.com/trackprofit-1 | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 160 | https://apps.shopify.com/triple-pixel | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 161 | https://apps.shopify.com/triplewhale-1 | enterprise wave status=200 ok=True err=None | 200 |
| 162 | https://apps.shopify.com/triquetra | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 163 | https://apps.shopify.com/true-roas | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 164 | https://apps.shopify.com/trueprofit | Live TrueProfit: from $35 + $/order, 5.0 (900 this wave), auto spend + COGS + LTV; 14-day. | 429 |
| 165 | https://apps.shopify.com/trueprofit-attribution | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 166 | https://apps.shopify.com/upprofit | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 167 | https://apps.shopify.com/voluum | enterprise wave status=200 ok=True err=None | 200 |
| 168 | https://apps.shopify.com/webgility | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 169 | https://apps.shopify.com/wetracked-io-connect | enterprise wave status=200 ok=True err=None | 200 |
| 170 | https://apps.shopify.com/whaly | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 171 | https://apps.shopify.com/wicked-reports | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 172 | https://apps.shopify.com/windsor-ai | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 173 | https://apps.shopify.com/xero-taxomate | 5.0/6 Taxomate | prior-wave |
| 174 | https://apps.shopify.com/yotpo-reviews | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 175 | https://apps.shopify.com/zendesk | enterprise wave status=200 ok=True err=None | 200 |

## C. Shopify Community threads

| # | URL | Proves | Fetch |
| --- | --- | --- | --- |
| 176 | https://community.shopify.com/t/anyone-else-notice-that-the-new-returns-system-breaks-all-of-shopify-sales-data/301853/54 | Merchant/staff thread — job language, not a census. | prior-wave |
| 177 | https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628 | Pull TOTAL ad spend not attributed-only; timestamp COGS; TW overkill at $15–20k/mo. | 200 |
| 178 | https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628/3 | TW fighter jet | prior-wave |
| 179 | https://community.shopify.com/t/app-for-p-l-analyse/361631/7 | Merchant/staff thread — job language, not a census. | prior-wave |
| 180 | https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364 | enterprise wave status=200 ok=True err=None | 200 |
| 181 | https://community.shopify.com/t/how-did-you-get-your-first-10-organic-app-installations-in-2026/643974 | 1.4k views first 10 = outreach | prior-wave |
| 182 | https://community.shopify.com/t/how-to-handle-orders-returned-to-sender/306065/1 | Merchant/staff thread — job language, not a census. | prior-wave |
| 183 | https://community.shopify.com/t/i-stopped-looking-at-shopify-metrics-one-by-one/653041/5 | Merchant/staff thread — job language, not a census. | prior-wave |
| 184 | https://community.shopify.com/t/need-help-with-shopify-returns-api-and-analytics/587957/2 | Merchant/staff thread — job language, not a census. | prior-wave |
| 185 | https://community.shopify.com/t/retract-or-modify-conversion-for-google-ads-facebook-when-customer-returns-order/199943 | Merchant/staff thread — job language, not a census. | prior-wave |
| 186 | https://community.shopify.com/t/returns-metric-in-analytics-is-misleading-should-reflect-actual-returns-not-all-refund-events/637409 | Merchant/staff thread — job language, not a census. | prior-wave |
| 187 | https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915 | enterprise wave status=200 ok=True err=None | 200 |
| 188 | https://community.shopify.com/t/tracking-app/581032/14 | Merchant/staff thread — job language, not a census. | prior-wave |
| 189 | https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805 | Revenue is native; true net profit must be assembled; cost-incomplete flag preferred. | 200 |
| 190 | https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4 | Shopify does not ingest Meta/Google/Microsoft spend; third-party app required. | 200 |

## D. Reddit (challenge-blocked this wave)

| # | URL | Proves | Fetch |
| --- | --- | --- | --- |
| 191 | https://www.reddit.com/r/FacebookAds/comments/1c6am9l/any_good_alternatives_to_triple_whale/ | Reddit thread cited in prior waves; this-wave WebFetch hit a bot-challenge page (`FETCH_FAILED`). Treat as PUBLIC_SNIPPET unless re-opened in a browser. | prior-wave |
| 192 | https://www.reddit.com/r/PPC/comments/1ohxwk6/best_triple_whale_alternative/ | Reddit thread cited in prior waves; this-wave WebFetch hit a bot-challenge page (`FETCH_FAILED`). Treat as PUBLIC_SNIPPET unless re-opened in a browser. | prior-wave |
| 193 | https://www.reddit.com/r/PPC/comments/1pqv5kh/how_are_you_handling_ad_attribution/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 194 | https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 195 | https://www.reddit.com/r/PPC/comments/1r2pvgy/question_for_d2c_founders_on_shopify_running_meta/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 196 | https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 197 | https://www.reddit.com/r/dropshipping/comments/1s3mx43/how_do_you_guys_actually_calculate_your_real/ | Reddit thread cited in prior waves; this-wave WebFetch hit a bot-challenge page (`FETCH_FAILED`). Treat as PUBLIC_SNIPPET unless re-opened in a browser. | prior-wave |
| 198 | https://www.reddit.com/r/shopify/comments/1h27sj3/beprofit_vs_lifetimely_vs/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 199 | https://www.reddit.com/r/shopify/comments/1jpb8cy/sales_attribution_tracking/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 200 | https://www.reddit.com/r/shopify/comments/1pzy8iv/app_or_plugin_to_calculate_profit_each_month/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 201 | https://www.reddit.com/r/shopify/comments/1rpjuk0/best_way_to_track_meta_ads_roas_in_shopify/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 202 | https://www.reddit.com/r/triplewhale/comments/1qs7n0s/attribution_app_alternatives/ | Reddit thread cited in prior waves; this-wave WebFetch hit a bot-challenge page (`FETCH_FAILED`). Treat as PUBLIC_SNIPPET unless re-opened in a browser. | prior-wave |

## E. Mcfly + Kleio surfaces

| # | URL | Proves | Fetch |
| --- | --- | --- | --- |
| 203 | https://getkleio.com/ | Kleio site: $29 flat, unlimited users/orders/revenue (VENDOR_CLAIM store counts), Attribution ✗ on purpose, 14-day. | 200 |
| 204 | https://getkleio.com/docs/costs/cogs-and-variable-costs | enterprise wave status=200 ok=True err=None | 200 |
| 205 | https://getkleio.com/docs/getting-started/metrics | Published CM1–CM3 waterfall, tax toggle, order-date vs accounting-date, E(return) forecast. | 200 |
| 206 | https://getkleio.com/docs/getting-started/recommended-setup | enterprise wave status=200 ok=True err=None | 200 |
| 207 | https://getkleio.com/docs/integrations/mcp-server | enterprise wave status=200 ok=True err=None | 200 |
| 208 | https://mcflyads.com | enterprise wave status=200 ok=True err=None | 200 |
| 209 | https://mcflyads.com/pricing | Live site: $39 flat, 7-day, anti-GMV, $79 course side door. | 200 |
| 210 | https://mcflyads.com/product | enterprise wave status=200 ok=True err=None | 200 |
| 211 | https://mcflyads.com/why-pixels-fail | enterprise wave status=200 ok=True err=None | 200 |
| 212 | https://www.getkleio.com/docs/integrations/ad-integrations | OAuth Meta/Google + others; Meta tokens expire 60 days and cannot auto-refresh. | 200 |
| 213 | https://www.getkleio.com/docs/integrations/mcp-server | Kleio MCP | prior-wave |

## F. Competitor sites, docs, market reports

| # | URL | Proves | Fetch |
| --- | --- | --- | --- |
| 214 | https://a2xaccounting.com/pricing/ | enterprise wave status=200 ok=True err=None | 200 |
| 215 | https://ads.tiktok.com/marketing_api/docs | enterprise wave status=200 ok=True err=None | 200 |
| 216 | https://agencyanalytics.com/pricing | enterprise wave status=200 ok=True err=None | 200 |
| 217 | https://apnews.com/press-release/ein-presswire-newsmatics/everest-group-acquires-commerce-data-and-ai-platform-glew-io-an-it-exchangenet-transaction-fe5dbf4a14c4f63a30a289a74311b907 | Glew acquired 2026-03 — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 218 | https://applora.ai/appstore | enterprise wave status=200 ok=True err=None | 200 |
| 219 | https://beprofit.co/resources/competitors/triple-whale-vs-beprofit/ | vendor | prior-wave |
| 220 | https://blotout.io/ | enterprise wave status=200 ok=True err=None | 200 |
| 221 | https://changelog.shopify.com/posts/benchmark-comparisons-in-analytics-will-be-removed-on-may-19th | removed 2026-05-19 | prior-wave |
| 222 | https://coefficient.io/pricing | enterprise wave status=200 ok=True err=None | 200 |
| 223 | https://d2c-times.com/polar-analytics-vs-triplewhale-in-2026-which-dtc-intelligence-layer-wins/ | TW buyer vs Polar CFO — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 224 | https://developers.facebook.com/docs/marketing-api/overview | enterprise wave status=400 ok=False err=HTTP 400 | 400 |
| 225 | https://developers.google.com/google-ads/api/docs/start | enterprise wave status=200 ok=True err=None | 200 |
| 226 | https://docs.northbeam.io/docs/northbeam-apex | enterprise wave status=200 ok=True err=None | 200 |
| 227 | https://ecom-tools.de/en/klar-review/ | OMR 4.8/129 — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 228 | https://eightx.co/blog/cfo-for-shopify-brands | MER blended CAC board language | prior-wave |
| 229 | https://eightx.co/blog/compare/reviews/a2x-for-ecommerce-review | enterprise wave status=200 ok=True err=None | 200 |
| 230 | https://eightx.co/blog/compare/reviews/triple-whale-for-ecommerce-review | TW not books — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 231 | https://funnel.io/pricing | enterprise wave status=200 ok=True err=None | 200 |
| 232 | https://getfairview.com/blog/polar-analytics-vs-triple-whale | Third-party market report — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 233 | https://getklar.com/pricing | €200/€400 net revenue after returns and taxes | prior-wave |
| 234 | https://honestecommerce.com/blogs/episodes/bonus-episode-balancing-trends-and-consistency-how-clean-data-drives-success-with-maxx-blank | TW pixel presale MRR jump | prior-wave |
| 235 | https://hyros.com/ | Sales-led pixel/passback; “15%+ more customers or you don’t pay” — VENDOR_CLAIM; no Shopify listing (404). | 200 |
| 236 | https://hyros.com/updates/blended-roas/ | blended vs MER denominator | prior-wave |
| 237 | https://joinhampton.com/blog/from-internal-tool-to-50m-saas-how-triple-whale-got-its-start | TW Twitter DMs agencies | prior-wave |
| 238 | https://kb.triplewhale.com/en/articles/10201911-is-vat-international-sales-tax-included-in-the-sales-metric | VAT not in Sales; custom expense workaround; dated 2026-07-26 | prior-wave |
| 239 | https://lebesgue.io/pricing | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 240 | https://makometrics.com/blog/mer-vs-roas-ecommerce-meta-ads | MER vs ROAS | prior-wave |
| 241 | https://ocontis.studio/blog/post/the-hidden-cost-of-running-a-shopify-store-when-12-apps-quietly-eat-your-margins/ | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 242 | https://plenisher.ai/ | enterprise wave status=200 ok=True err=None | 200 |
| 243 | https://shopivibe.app/how-to-price-shopify-app | enterprise wave status=200 ok=True err=None | 200 |
| 244 | https://stape.io/ | enterprise wave status=200 ok=True err=None | 200 |
| 245 | https://supermetrics.com/pricing | enterprise wave status=200 ok=True err=None | 200 |
| 246 | https://synder.com/pricing/ | enterprise wave status=200 ok=True err=None | 200 |
| 247 | https://taylorsicard.com/blog/shopify-app-economics-one-chart | enterprise wave status=200 ok=True err=None | 200 |
| 248 | https://taylorsicard.com/blog/shopify-app-listing-conversion | enterprise wave status=200 ok=True err=None | 200 |
| 249 | https://taylorsicard.com/blog/shopify-app-pricing-strategy | enterprise wave status=200 ok=True err=None | 200 |
| 250 | https://taylorsicard.com/blog/shopify-app-review-policy-2026 | 2026 incentivization crackdown — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 251 | https://techcrunch.com/2023/07/18/polar-analytics-9m-shopify-brands-ecommerce/ | 2-day Polar onboard | prior-wave |
| 252 | https://triplewhale.readme.io/docs/order-revenue | Order Revenue includes Taxes | prior-wave |
| 253 | https://triplewhale.readme.io/docs/total-sales | Total Sales includes Taxes | prior-wave |
| 254 | https://trueprofit.io/comparison/trueprofit-vs-triple-whale | vs-page format | prior-wave |
| 255 | https://trueprofit.io/pricing | Official menu $35/$60/$100/$200 + per-order surcharge caps $300–$1000; no annual; 5+ stores sales discount. | 200 |
| 256 | https://venon.io/blog/triple-whale-pricing | enterprise wave status=200 ok=True err=None | 200 |
| 257 | https://whatagraph.com/pricing | enterprise wave status=200 ok=True err=None | 200 |
| 258 | https://windsor.ai/ | enterprise wave status=200 ok=True err=None | 200 |
| 259 | https://www.adsx.com/blog/blended-roas-vs-platform-roas-reconciliation | overlap ratio example | prior-wave |
| 260 | https://www.adsx.com/blog/shopify-app-marketing-first-100-installs | 30/60/90 first 100 — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 261 | https://www.adsx.com/blog/shopify-app-store-ads-guide | first-price; illustrative funnel DO NOT PUBLISH — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 262 | https://www.attribuly.com/pricing | enterprise wave status=None ok=False err=URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'www.attribuly.com'. (_ssl.c:1000)> | URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'www.attribuly.com'. (_ssl.c:1000)> |
| 263 | https://www.bigmoves.marketing/blog/get-more-shopify-app-reviews-without-breaking-shopifys-rules-guide | neutral review ask — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 264 | https://www.brevo.com/blog/sendinblue-acquires-metrilo-chatra-pushowl/ | Metrilo acquired 2021 — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 265 | https://www.coupler.io/pricing | enterprise wave status=200 ok=True err=None | 200 |
| 266 | https://www.daasity.com/pricing | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 267 | https://www.dashthis.com/pricing/ | enterprise wave status=200 ok=True err=None | 200 |
| 268 | https://www.einpresswire.com/article/750779451/viably-announces-strategic-acquisition-of-beprofit-to-enhance-ecommerce-banking-solution | BeProfit acquired 2024-10-14 — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 269 | https://www.finaloop.com/pricing | enterprise wave status=200 ok=True err=None | 200 |
| 270 | https://www.gapquery.com/blog/shopify-app-pricing-by-category | enterprise wave status=200 ok=True err=None | 200 |
| 271 | https://www.getelevar.com/pricing/ | enterprise wave status=200 ok=True err=None | 200 |
| 272 | https://www.getrecast.com/ | enterprise wave status=200 ok=True err=None | 200 |
| 273 | https://www.glew.io/ | enterprise wave status=200 ok=True err=None | 200 |
| 274 | https://www.haus.io/ | enterprise wave status=200 ok=True err=None | 200 |
| 275 | https://www.klar-analytics.com/ | enterprise wave status=None ok=False err=URLError: <urlopen error [Errno -2] Name or service not known> | URLError: <urlopen error [Errno -2] Name or service not known> |
| 276 | https://www.koji.so/blog/mom-test-customer-interviews-2026 | Mom Test recap — MARKET_REPORT, not Mcfly KPI. | prior-wave |
| 277 | https://www.letstalkshop.com/blog/triple-whale-vs-polar-analytics | This-wave re-fetch **HTTP 429** (Shopify rate limit). Prior-wave same-day snapshot still in corpus. enterprise wave status=429 ok=False err=HTTP 429 | 429 |
| 278 | https://www.lifetimely.io/pricing | Free ≤50 orders; $49–$999 by volume; Amazon +$75; Attribution listed on paid plans. | 200 |
| 279 | https://www.loopreturns.com/pricing/ | $155/$340 | prior-wave |
| 280 | https://www.measured.com/ | Incrementality + causal MMM; sales-led; no App Store card. | 200 |
| 281 | https://www.mutinex.co/ | enterprise wave status=200 ok=True err=None | 200 |
| 282 | https://www.nfx.com/post/product-led-growth-principles-triple-whale | TW PLG Slack | prior-wave |
| 283 | https://www.northbeam.io/ | Sales-led; no public price card; vendor claims $130B attributed / 37% ROAS — VENDOR_CLAIM only. | 200 |
| 284 | https://www.polaranalytics.com/blog/mer-marketing-efficiency-ratio | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 285 | https://www.polaranalytics.com/case-studies/rsvp-paris | board pack + Slack | prior-wave |
| 286 | https://www.polaranalytics.com/post/shopify-attribution-models-explained-which-one-should-you-use | Admin no spend any plan | prior-wave |
| 287 | https://www.polaranalytics.com/vs/triple-whale | enterprise wave status=200 ok=True err=None | 200 |
| 288 | https://www.reportpundit.com/post/shopify-cogs-report-profit-margins | enterprise wave status=200 ok=True err=None | 200 |
| 289 | https://www.rockerbox.com/ | enterprise wave status=200 ok=True err=None | 200 |
| 290 | https://www.segmetrics.io/pricing | enterprise wave status=200 ok=True err=None | 200 |
| 291 | https://www.shopify.com/blog/aeo-for-ecommerce | Risley AEO/GEO | prior-wave |
| 292 | https://www.shopify.com/enterprise/blog/marketing-attribution | This-wave **HTTP 404** — handle/site not a live listing. Absence ≠ death. enterprise wave status=404 ok=False err=HTTP 404 | 404 |
| 293 | https://www.shopify.com/partners/blog/a-new-partner-earning-model | referral GMV share Aug 10 2026 — not app SKU | prior-wave |
| 294 | https://www.shopify.com/partners/terms | Partner Program Agreement | prior-wave |
| 295 | https://www.swydo.com/pricing/ | enterprise wave status=200 ok=True err=None | 200 |
| 296 | https://www.thepricegeek.com/profit-analytics/best-shopify-profit-tracker/ | Jul 2026 crowns TP; omits Mcfly | prior-wave |
| 297 | https://www.triplewhale.com/blog/what-is-mer | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 298 | https://www.triplewhale.com/pricing | This-wave **HTTP 403**. Do not treat as a product fact. enterprise wave status=403 ok=False err=HTTP 403 | 403 |
| 299 | https://www.trygodmode.com/blog/shopify-real-profit-2026-dashboard-lies | enterprise wave status=200 ok=True err=None | 200 |
| 300 | https://www.wickedreports.com/ | enterprise wave status=200 ok=True err=None | 200 |

## Failures to say out loud

| What | What we did |
| --- | --- |
| Shopify App Store bulk crawl | ~50 handles **HTTP 429** this wave after ~20 200s. Wave C same-day JSON-LD snapshots remain the rating/review source unless WebFetch re-confirmed (Mcfly, Kleio, TrueProfit 900, aisle 1,546). |
| Guessed handles (hyros, wicked-reports, stape, blotout, godmode, windsor-ai, agency-analytics, …) | **HTTP 404** — recorded. Sales-led sites were fetched instead where they exist. |
| Reddit HTML | Bot challenge / empty. Prior-wave URLs stay in the table as `PUBLIC_SNIPPET`. |
| Triple Whale site pricing | One WebFetch **timed out**. Listing + prior-wave site snapshot still used. |
| Elevar `/pricing` | Resolved to an unexpected Audiense page — **do not cite as Elevar price**. Use App Store listing $225. |
| Northbeam / Hyros / Measured price | **No public card.** Do not invent. |

*Generated from `db/sources.jsonl` after `assemble_enterprise.py`. Re-run assemble after new fetches.*
