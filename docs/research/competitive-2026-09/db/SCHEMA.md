# Competitive research DB schema

**Built:** 2026-09-09  
**Rule:** every numeric field is from a live fetch or explicitly `confidence=market_report|vendor_claim|commenter_claim|approx_from_percent`.

## Tables / JSONL files

### competitors.jsonl
One row per product.

| field | type | notes |
| --- | --- | --- |
| id | string | slug |
| name | string | |
| kind | string | suite\|profit\|pixel\|reports\|pipe\|finance\|native\|diy\|mcfly |
| listing_url | string? | |
| site_url | string? | |
| launched | string? | ISO date if listing showed it |
| price_scan | string | listing header |
| price_notes | string | |
| rating | number? | |
| review_count | integer? | |
| star5_pct | integer? | Shopify UI % |
| star1_pct | integer? | |
| trial_days | integer? | |
| fetched | date | |
| confidence | string | live\|mixed\|market_report |

### listings.jsonl
Listing copy snapshot.

### problems.jsonl
From PROBLEM_BANK.

### review_quotes.jsonl
Only **visible** written reviews we actually saw (usually 3/app).

### sources.jsonl
URLs used.

### opportunities.jsonl
From OPPORTUNITY_MAP.

### religion.jsonl
From RELIGION_FLEX.

### harvest_listings.jsonl
PRIMARY_SOURCE_HARVEST cards (append-only; does not replace `listings.jsonl`).

| field | type | notes |
| --- | --- | --- |
| handle | string | App Store handle |
| url | string | `https://apps.shopify.com/{handle}` |
| title | string | listing / JSON-LD name |
| positioning | string | og:description one-liner |
| price | string | listing header scan |
| trial_days | integer? | if listing printed a N-day trial |
| rating | number? | JSON-LD aggregateRating |
| review_count | integer? | JSON-LD ratingCount |
| launched | string? | ISO if “Launched Month D, YYYY” present |
| adjacent | list | “more like this” handles observed on page |
| http_status | integer | live fetch |
| fetched | date | |
| confidence | string | live\|fetch_fail |

### harvest_threads.jsonl
Shopify Community + public Reddit. Paraphrase + URL only.

### harvest_docs.jsonl
Kleio / TrueProfit / Polar / Triple Whale public docs. Claims tagged spend / tax / attribution.

### harvest_sources.jsonl
URLs used by PRIMARY_SOURCE_HARVEST. Do not clobber `sources.jsonl`.

SQLite: `competitive.sqlite` built by `build_db.py`.
