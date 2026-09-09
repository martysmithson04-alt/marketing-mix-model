# Primary source harvest — Mcfly niche (2026-09-09)

**Mode:** RESEARCH ONLY. Append-only under `docs/research/competitive-2026-09/`.  
**Coordinates with:** ENTERPRISE_LANDSCAPE lane — this file does **not** replace, rename, or rewrite landscape / synthesis / competitor-card docs.  
**Fetcher:** [`db/harvest_primary.py`](./db/harvest_primary.py)  
**Machine rows:** [`db/harvest_listings.jsonl`](./db/harvest_listings.jsonl) · [`db/harvest_threads.jsonl`](./db/harvest_threads.jsonl) · [`db/harvest_docs.jsonl`](./db/harvest_docs.jsonl) · [`db/harvest_sources.jsonl`](./db/harvest_sources.jsonl)

Every card, thread, and claim below is tied to a live URL fetched this run. No surface summary without a URL. Numbers that are not on the page at fetch time are omitted (`null`), never invented.

---

## Method

1. **App Store listings.** Seed handles from prior corpus + English sitemap keyword filter (`profit|roas|ltv|analytics|attribution|report|cohort|margin|…`). Live GET `https://apps.shopify.com/{handle}`. Parse JSON-LD `SoftwareApplication` (name, rating, review count), visible price / trial / launched, og:description as positioning one-liner. Snowball “more like this” handles. Keep niche-matching 200s. Target **80+ cards**.
2. **Threads.** Live GET named Shopify Community + Reddit URLs; Reddit `.json` search for MER/ROAS/Triple Whale/profit trackers. **Paraphrase + URL only** (no verbatim comment dumps).
3. **Competitor docs.** Live GET Kleio, TrueProfit helpdesk, Polar Intercom/marketing, Triple Whale KB/readme. Extract spend-import / tax / attribution stance excerpts.

Sitemap used to discover handles (not as a substitute for listing fetches): https://apps.shopify.com/sitemap_apps_en.xml

---

## Status

Harvest running. Tables below are filled from `db/harvest_*.jsonl` after the live pass. If a section is empty, the fetch has not landed yet — do not cite empty cells.

---

## 1. Shopify App Store cards

| handle | price | trial_days | rating | reviews | launched | positioning | url |
| --- | --- | --- | --- | --- | --- | --- | --- |
| _pending live fetch_ | | | | | | | |

---

## 2. Shopify Community + Reddit (paraphrase + URL)

| kind | paraphrase | url |
| --- | --- | --- |
| _pending live fetch_ | | |

---

## 3. Competitor public docs — spend / tax / attribution

| vendor | theme | excerpt (paraphrase/short) | url |
| --- | --- | --- | --- |
| _pending live fetch_ | | | |

---

*Owner: ENTERPRISE primary-source harvest lane. Do not merge this file into ENTERPRISE_LANDSCAPE.md — link it.*
