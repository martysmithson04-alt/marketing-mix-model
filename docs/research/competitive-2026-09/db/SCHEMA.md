# Competitive research DB schema

**Built:** 2026-09-09 (enterprise landscape assemble)  
**Rule:** every numeric field is from a live fetch or explicitly `confidence=market_report|vendor_claim|commenter_claim|approx_from_percent`.  
**Rebuild:** `python3 assemble_enterprise.py && python3 build_db.py`

## Counts (after assemble)

| Table / JSONL | Rows | Door |
| --- | --- | --- |
| `competitors` | **106** | ≥80 |
| `problems` | **61** | ≥40 |
| `review_quotes` | **80** | ≥80 |
| `sources` | **300** | ≥120 |
| `opportunities` | 22 | Wave A map |
| `religion` | 12 | Wave A R1–R12 |
| `listings` | 4 | copy snapshots |
| `objections` / `positioning` / `content_topics` / `interviews` / `first_customer_plays` | Wave D JSONL | not yet in sqlite builder |

`fetch_raw.jsonl`: 238 attempted URLs this wave (103 OK). Not a table — audit log.

---

## Tables / JSONL files

### competitors.jsonl
One row per product (App Store, sales-led, native, DIY, autopsy).

| field | type | notes |
| --- | --- | --- |
| id | string | slug |
| name | string | |
| kind | string | suite\|profit\|pixel\|reports\|pipe\|finance\|native\|diy\|mcfly\|ads_channel\|ads_os\|incrementality\|mmm\|agency\|retention\|subs\|returns\|ops\|adjacent |
| listing_url | string? | `apps.shopify.com/…` or null |
| site_url | string? | |
| launched | string? | ISO date if listing showed it |
| price_scan | string | listing header / “sales-led” / “sunset” |
| price_notes | string | |
| rating | number? | JSON-LD or listing UI |
| review_count | integer? | **null if not on a live page** |
| star5_pct | integer? | Shopify UI % |
| star1_pct | integer? | |
| trial_days | integer? | |
| fetched | date | |
| confidence | string | live\|mixed\|market_report |
| this_wave_fetch | string? | `200` / `429` / `404` from enterprise crawl |

**Do not** treat `kind=ads_channel` (TikTok 15,912 / Facebook 5,648) as analytics peers. They are review-physics controls.

### listings.jsonl
Listing copy snapshot (Wave A; small).

### problems.jsonl
Wave A `p1`–`p15` + enterprise `p16`–`p45` + PR #5 `P-001`–`P-016` (distinct IDs).

| field | type | notes |
| --- | --- | --- |
| id | string | `p*` or `P-*` |
| rank | int | lower = higher public WTP / decision weight |
| name | string | job-shaped pain |
| wtp | string | qualitative |
| review_proxy | string | who already prints reviews for this |
| mcfly | string | have / thin / refuse |
| tag | string | CURRENT_RELIGION \| RESEARCH_OPTION \| OUT_OF_SCOPE |
| urls | list | evidence |

### review_quotes.jsonl
Visible written reviews / Community sentences we actually saw. PR #5 CSV folded in (includes some **reprints** — `grade=reprint`). Vendor-selected Kleio site quotes are tagged in `notes`.

| field | type | notes |
| --- | --- | --- |
| app_id | string | |
| date | string? | |
| stars | int? | |
| store | string? | reviewer |
| country | string? | |
| tenure | string? | |
| theme | string | |
| quote | string | verbatim or tight snippet |
| url | string | |
| grade | string? | primary_listing \| reprint \| vendor_doc |

### sources.jsonl
URLs used. This wave adds `fetch_status`, `ok`, `excerpt`.

| field | type | notes |
| --- | --- | --- |
| url | string | primary key |
| type | string | listing\|official\|community\|reddit\|site\|docs\|market_report\|fetch\|… |
| fetched | date | |
| notes | string | |
| fetch_status | string? | HTTP code or error |
| ok | bool? | this-wave urllib success |
| excerpt | string? | first ~180 chars of stripped HTML |

### opportunities.jsonl
From `OPPORTUNITY_MAP.md` (Wave A).

### religion.jsonl
From `RELIGION_FLEX.md`.

### Wave D extras (JSONL only)
`objections.jsonl` · `positioning.jsonl` · `content_topics.jsonl` · `interviews.jsonl` (placeholders until founder runs scripts) · `first_customer_plays.jsonl`

### PR #5 CSV (kept)
`reviews.csv` · `problems.csv` · `themes.csv` · `stakeholder_conflicts.csv` — folded into JSONL; originals not deleted.

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

---

## SQLite

`competitive.sqlite` built by `build_db.py` from the JSONL files in `TABLES` (enterprise + harvest). Nested lists/dicts are stored as JSON text.

```bash
cd docs/research/competitive-2026-09/db
python3 assemble_enterprise.py
python3 build_db.py
sqlite3 competitive.sqlite "SELECT kind, COUNT(*) FROM competitors GROUP BY kind;"
sqlite3 competitive.sqlite "SELECT COUNT(*) FROM problems;"
sqlite3 competitive.sqlite "SELECT COUNT(*) FROM review_quotes;"
sqlite3 competitive.sqlite "SELECT COUNT(*) FROM sources;"
sqlite3 competitive.sqlite "SELECT COUNT(*) FROM harvest_listings;"
```

Human map of the niche: [`../ENTERPRISE_LANDSCAPE.md`](../ENTERPRISE_LANDSCAPE.md).  
URL proofs: [`../SOURCE_BIBLIOGRAPHY.md`](../SOURCE_BIBLIOGRAPHY.md).
