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

SQLite: `competitive.sqlite` built by `build_db.py`.

Wave 2 (2026-09-09) appended competitors `report_pundit` `kleio` `recharge` `loop_returns` `repeat_customer_insights` `taxomate` and deepened `klar`. Rebuild after JSONL edits: `python3 db/build_db.py`.
