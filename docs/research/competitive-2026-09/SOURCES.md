# Sources — review mining (2026-09-09)

Primary evidence is **public merchant reviews** and **public community posts**. Secondary editorial (Eightx, Fairview, Talk Shop) is used only as context, never as invented quotes.

## Method

1. Pull Shopify App Store listing + 1-star (and 2-star where volume exists) for profit / ROAS / ads-analytics apps.
2. Recover truncated listing text from aggregators that reprint Shopify reviews (Taranker, AppNavigator). Treat those as reprints of the same listing review, not a second independent quote.
3. Add G2 cons clusters for Triple Whale (on-store + off-store volume).
4. Add Shopify Community + Trustpilot where they name a real operator problem.
5. Paraphrase in the bank. Short verbatim snippets only when the full sentence was captured. Never fabricate reviewer voice.
6. Shopify star distributions are **inflated** (profit apps sit at 4.8–5.0). Pain signal lives in the 1-star tail + the *job* hidden in 5-star praise.

## Listing snapshot (fetched 2026-09-09)

| App | Handle / URL | Rating (this fetch) | n | 1★ share |
| --- | --- | --- | --- | --- |
| TrueProfit | https://apps.shopify.com/trueprofit | 5.0 | 880–899 | ~1% (7–8) |
| Lifetimely (AMP) | https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics | 4.9 | 460–535 | ~1–2% (5–10) |
| BeProfit | https://apps.shopify.com/beprofit-profit-tracker | 4.4–4.5 | 173–202 | ~6% (11) |
| Analyzify | https://apps.shopify.com/analyzify | 4.7 | 271–313 | ~4% (10) |
| Triple Whale | https://apps.shopify.com/triplewhale-1 | 4.0–4.1 | 85–92 | **16–17%** (14–16) |
| Polar Analytics | https://apps.shopify.com/polar-analytics | 4.9 | 103–116 | ~3% (3) |
| GoProfit | https://apps.shopify.com/go-profit | 4.8 | 85 | ~2% (2) |
| Kleio | https://apps.shopify.com/kleio | 5.0 | 20 | 0% (tiny n) |

Counts moved during the day; use ranges. Triple Whale is the only on-store suite with a **material 1-star cluster**.

Northbeam is **not** a Shopify App Store listing in this pass. Treated as off-store context only.

## Primary pages fetched

| Source | URL | Used for |
| --- | --- | --- |
| Shopify 1★ TrueProfit | https://apps.shopify.com/trueprofit/reviews?ratings%5B%5D=1 | Billing, VAT, variant sync, ad-spend errors |
| Shopify 1★ BeProfit | https://apps.shopify.com/beprofit-profit-tracker/reviews?ratings%5B%5D=1 | Attributed-only spend, cancel/refund |
| Shopify 1★ Analyzify | https://apps.shopify.com/analyzify/reviews?ratings%5B%5D=1 | Tracking breakage, paid setup |
| Shopify 1★ Triple Whale | https://apps.shopify.com/triplewhale-1/reviews?ratings%5B%5D=1 | VAT-in-revenue, support cliff, pixel, cancel |
| Shopify 1★ Lifetimely | https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics/reviews?ratings%5B%5D=1 | Volume tax, AMP acquisition, upsell math |
| Shopify 1★ Polar | https://apps.shopify.com/polar-analytics/reviews?ratings%5B%5D=1 | Sales-gated trial |
| Shopify 2★ Triple Whale | https://apps.shopify.com/triplewhale-1/reviews?ratings%5B%5D=2 | Setup + no support |
| Taranker BeProfit | https://taranker.com/shopify-beprofit-profit-tracker-app-customer-reviews | Full A Farley Country Attire quote |
| Taranker Analyzify | https://taranker.com/shopify-analyzify-app-customer-reviews | Full 1★ + 5★ job quotes |
| Taranker Lifetimely 1★ | https://taranker.com/shopify-lifetimely-lifetime-value-and-profit-analytics-app-customer-reviews?filter-by=1 | Chef Preserve $600/mo + support |
| Taranker TrueProfit 1★ | https://taranker.com/shopify-trueprofit-app-customer-reviews?filter-by=1 | Legacy 400% hike, overage, Google Ads connect |
| AppNavigator Analyzify 1★ | https://appnavigator.io/app/analyzify/reviews/?rating=1 | Duckfeet / Tameson / MakeMyGift full text |
| AppNavigator TW 1★ | https://appnavigator.io/app/triplewhale-1/reviews/2272366 | Kove Footwear VAT full text |
| AppNavigator Polar 1★ | https://appnavigator.io/app/polar-analytics/reviews/1550354 | dryoasisplants sales-call gate |
| G2 TW cons (IT mirror) | https://www.g2.com/it/products/triple-whale/reviews?qs=pros-and-cons | Agency 50% mis-attribution; $600/mo no support |
| Shopify Community | https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628 | Spreadsheet + TW-overkill + total-spend checklist |
| Trustpilot Polar | https://www.trustpilot.com/reviews/690da52c91938d8e1b9286b7 | Price bait + inventory × stores |
| Kleio listing | https://apps.shopify.com/kleio | “goodbye TripleWhale” at $29 |
| GoProfit listing | https://apps.shopify.com/go-profit | Category undercut / overage contrast |

## Secondary (context, not quote-invention)

| Source | URL | Note |
| --- | --- | --- |
| Eightx Lifetimely CFO review | https://eightx.co/blog/compare/reviews/lifetimely-for-ecommerce-review | Intraday MER lag; order-volume pricing |
| Eightx Triple Whale | https://eightx.co/blog/compare/reviews/triple-whale-for-ecommerce-review | “Not a system of record” |
| Triple Whale docs | https://triplewhale.readme.io/docs/why-do-my-order-based-sales-metrics-not-match-between-shopify-and-triple-whale | Vendor admits Shopify date/edit mismatch |
| Northbeam docs | https://docs.northbeam.io/docs/setting-up-google-ads-for-northbeam | Vendor admits platform discrepancies expected |
| Fairview profit-app roundup | https://getfairview.com/blog/best-shopify-profit-tracking-apps | Category map |
| EcommRumble Lifetimely | https://ecommrumble.com/fighters/lifetimely | Aggregated “5.71× hike” claim — treat as secondary until primary quote found |

## What was not used

- Invented composite quotes.
- Vendor marketing testimonials as “reviews” unless they also appear on the App Store.
- Granola / internal meetings (MCP unauthenticated this run).
