# Mcfly Analytics — Competitive research corpus (2026-09)

**Status:** RESEARCH ONLY. No production feature shipping.  
**Branch:** `research/competitive-2026-09`  
**Anchor listing:** [apps.shopify.com/mcfly-analytics-public](https://apps.shopify.com/mcfly-analytics-public)  
**Marketing site:** [mcflyads.com](https://mcflyads.com)  
**Research date window:** 2026-09-09 (live fetches). Re-verify prices and review counts before publishing any number on mcflyads.com.

---

## What this folder is

A founder-facing, evidence-tagged competitive deep-dive. It is **not** a shipping roadmap and **not** a rewrite of `docs/MASTER_PLAN.md`.

Religion is **FLEXIBLE here**. Every alternative (pixels, MTA, OAuth, freemium, GMV tax, profit P&L, etc.) is tagged:

| Tag | Meaning |
| --- | --- |
| `CURRENT_RELIGION` | What Mcfly currently ships / lists / refuses |
| `RESEARCH_OPTION` | A viable alternative that may make more money, be more loved, be easier, or solve a more real merchant problem |
| `EVIDENCE` | Live URL + observed fact (no invented metrics) |
| `RISK` | What breaks if we take the option |

---

## How to read this

Start with [`SYNTHESIS.md`](./SYNTHESIS.md) if you want the decision menu. Everything else is evidence.

| File | What |
| --- | --- |
| [`RESEARCH_LOG.md`](./RESEARCH_LOG.md) | Dated fetches, contradictions, open questions |
| [`APP_STORE_MARKET.md`](./APP_STORE_MARKET.md) | Discovery, reviews, trials, pricing psychology, churn physics |
| [`PERSONAS.md`](./PERSONAS.md) | Founder, operator, agency, finance, enterprise pod, omni |
| [`PROBLEM_BANK.md`](./PROBLEM_BANK.md) | 15 problems ranked by public WTP signals |
| [`MERCHANT_PROBLEMS.md`](./MERCHANT_PROBLEMS.md) | Voice index — their sentences + URLs |
| [`NICHE_MER.md`](./NICHE_MER.md) | MER / blended ROAS / till vs Ads Manager |
| [`REVIEW_THEMES.md`](./REVIEW_THEMES.md) | Visible review sample + star histograms |
| [`ENTERPRISE_WORKFLOWS.md`](./ENTERPRISE_WORKFLOWS.md) | Sheets / TW / Polar / NB / Elevar / A2X / Admin patterns |
| [`OPPORTUNITY_MAP.md`](./OPPORTUNITY_MAP.md) | vNext opportunities scored + clustered |
| [`COMPETITOR_CARDS.md`](./COMPETITOR_CARDS.md) | Live cards (20+) |
| [`LISTING_PATTERN_BANK.md`](./LISTING_PATTERN_BANK.md) | 25 listing patterns |
| [`LISTING_TEARDOWNS.md`](./LISTING_TEARDOWNS.md) | vs live Mcfly listing |
| [`MCFY_GAP_MATRIX.md`](./MCFY_GAP_MATRIX.md) | Capability × four scores |
| [`RELIGION_FLEX.md`](./RELIGION_FLEX.md) | CURRENT vs OPTION + call |
| [`SYNTHESIS.md`](./SYNTHESIS.md) | S1–S7 strategic options |
| [`S1_PRD_LITE.md`](./S1_PRD_LITE.md) | WAVE E — S1 cash-governor PRD-lite (`RESEARCH_OPTION`, not a ship order) |
| [`KLEIO_GAP_ANALYSIS.md`](./KLEIO_GAP_ANALYSIS.md) | WAVE E — Kleio public product vs `MCFY_GAP_MATRIX` line-by-line |
| [`INTEGRATION_MAP.md`](./INTEGRATION_MAP.md) | WAVE E — Meta/Google Ads vs Shopify Finance vs CSV |
| [`COMPLIANCE_LANDMINES.md`](./COMPLIANCE_LANDMINES.md) | WAVE E — PCD / GDPR / ads policy per RESEARCH_OPTION |
| [`STRATEGY_KILL_CRITERIA.md`](./STRATEGY_KILL_CRITERIA.md) | WAVE E — S1 stress-test + S2/S3/S5 kill criteria |
| [`db/`](./db/) | JSONL + `competitive.sqlite` |

Pricing / workflows / category map live inside APP_STORE_MARKET, ENTERPRISE_WORKFLOWS, LISTING_TEARDOWNS rather than duplicate files.

---

## Method (non-negotiable)

- Cite **live** App Store / public URLs. If a number is not on a live page at fetch time, it is marked `UNVERIFIED` or `MARKET_REPORT`.
- Do not invent review counts, GMV, ARR, conversion rates, or “X% of merchants.”
- Shopify “More apps like this” is treated as **category adjacency signal**, not truth about product quality.
- Internal repo docs (`MASTER_PLAN.md`, `APP_STORE_LISTING.md`, `COMPETITORS.md`) are **CURRENT_RELIGION / stale-draft** sources. Live listing + live site win when they conflict.
- Maximize four scores in every recommendation: **money, love, ease, real merchant problems**. Religion is a hypothesis, not a virtue.

---

## Live Mcfly snapshot (2026-09-09)

Fetched from [https://apps.shopify.com/mcfly-analytics-public](https://apps.shopify.com/mcfly-analytics-public):

| Field | Live value | Repo draft (stale) |
| --- | --- | --- |
| App name | Mcfly Analytics | Mcfly Analytics |
| Price | **$39/month**, 7-day free trial | Free design-partner → ~$79 later (`APP_STORE_LISTING.md`, `MASTER_PLAN.md`) |
| Rating / reviews | **0.0 (0 reviews)** | n/a |
| Launched | **September 7, 2026** | “after Fly health + first install” |
| Tagline (title) | “Ad spend next to store sales — Total ROAS +…” | “Cash MER for Shopify — spend vs sales, not attribution theater” |
| Hero | “See ad spend next to store sales — including billboards. Total ROAS = sales ÷ spend you added.” | Cash MER / anti-theater |
| Primary metric name | **Total ROAS** (sales ÷ spend) | Cash MER in repo; Total ROAS on live site |
| Refused | “No pixels. No path credit.” | Same |
| Paid extras claimed | LTV / order-history depth + Goals | Repo v1 did not list LTV/Goals as shipped |
| Categories | Marketing and sales · Visuals and reports | Marketing analytics / Advertising |
| Data access | Customers, orders, device/activity, store owner | `read_orders` in launch docs |
| Developer address | 7533 S Center View Ct STE N, West Jordan, UT, 94084, US | — |
| Adjacent apps (Shopify “more like this”) | Microsoft Clarity (4.6 / 2125 / Free), WeTracked (4.8 / 125 / Free to install), Parkour Pixel (4.9 / 191 / Free) | — |

**Brutal read:** Shopify is already classifying Mcfly next to **free pixel / heatmap / CAPI apps**, not next to Polar ($750, 4.9/116) or Lifetimely (4.9/535) or TrueProfit (5.0/899). That is a distribution and packaging failure, not a compliment.

---

## Four-score scorecard (research judgment, not a metric)

| Score | Live Mcfly | Why |
| --- | --- | --- |
| **Money** | Weak | $39 flat, 0 reviews, 2 days old, no freemium funnel, no agency SKU, no GMV upside. Course at $79 one-time on site is a side door. |
| **Love** | Unproven / structurally hard | 0 reviews. Adjacent apps have hundreds–thousands of reviews because they **install a pixel or heatmap in 2 minutes**. A paste-CSV cash desk does not create that dopamine. |
| **Ease** | Mixed | Paste-first is easier than Meta OAuth *for the developer*. For the merchant it is **more work** than TrueProfit’s “auto-track ad spend” or Clarity’s one-click install. |
| **Real problem** | Partial | “Shopify Analytics has sales, not spend” is real. “I don’t know if I made cash this month after COGS/shipping/fees” is **more** real and already owned by TrueProfit / Lifetimely / BeProfit / Metorik. |

---

## Corpus status (this run)

Delivered: 16 markdown files + `db/` (7 JSONL, sqlite, builder), then **WAVE E** architecture pack (5 files).  
DB counts: 21 competitors · 15 problems · 22 visible review quotes · 50 sources · 22 opportunities · 12 religion rows.  
Kleio is **not** in the Wave A DB; treat `KLEIO_GAP_ANALYSIS.md` as the live card until the DB is rebuilt.

Recommended read order after this README: `SYNTHESIS.md` → `STRATEGY_KILL_CRITERIA.md` → `S1_PRD_LITE.md` → `KLEIO_GAP_ANALYSIS.md`.

---

## Explicit non-goals

- Do not ship pixels / OAuth / billing changes from this research.
- Do not silently amend `MASTER_PLAN.md`.
- Do not invent social proof, review volume, or “we will hit X installs.”
- Do not treat “anti-attribution” as automatically the money-max path.

---

*Owner: research agent on Cursor Cloud. Founder decides. Religion can lose to evidence.*
