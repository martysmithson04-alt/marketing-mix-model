# Unit-economics scenarios (tables only)

**Date:** 2026-09-09  
**Mode:** RESEARCH ONLY. Every number is a **scenario** under **labeled assumptions**.  
**Forbidden:** “we will hit X MRR,” invented conversion rates presented as Mcfly’s, unpublished Partner Dashboard figures.

If a cell is not labeled `OFFICIAL`, `LIVE`, or `ARITHMETIC`, it is an `ASSUMPTION` or `MARKET_REPORT`. Changing an assumption changes the table — that is the point.

Companion: [`WAR_ROOM.md`](./WAR_ROOM.md) · [`COMPETITIVE_THREAT_BOARD.md`](./COMPETITIVE_THREAT_BOARD.md) · [`APP_STORE_MARKET.md`](./APP_STORE_MARKET.md) §10 (older 15%/20% math **without** 2.9%).

---

## A. Locked take-rate assumptions (do not silently change)

| ID | Assumption | Value | Tag | Source |
| --- | --- | --- | --- | --- |
| T1 | Revenue share, first $1,000,000 USD **lifetime** gross app revenue earned from 2025-01-01 | **0%** | `OFFICIAL` | https://shopify.dev/docs/apps/launch/distribution/revenue-share |
| T2 | Revenue share above that lifetime threshold | **15%** | `OFFICIAL` | same |
| T3 | Threshold reset | **Does not reset annually** | `OFFICIAL` | same + https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share |
| T4 | Share base | **Gross** sales; **refunds not deducted** | `OFFICIAL` | revenue-share page |
| T5 | Payment processing on **all** App Store billing | **2.9%** | `OFFICIAL` | same (“Fees and taxes are charged separately from revenue share”) |
| T6 | Sales tax / regulatory operating fees | **Not modeled** (merchant- or region-specific) | `ASSUMPTION` | same page flags them |
| T7 | High-volume exception ($20M+ prior-year app earnings or $100M+ company) | **Does not apply to Mcfly** | `ASSUMPTION` | official exception; Mcfly is a 2-day-old $39 app |
| T8 | How 15% and 2.9% stack | **Additive on gross**: keep `1 − share − 0.029` | `ASSUMPTION` (founder-specified “15% + 2.9%”) | official says “separately”; exact ledger order is Partner-payout `UNVERIFIED` |
| T9 | Alternate stack (sensitivity) | Processing first, then 15% of remainder: keep `0.971 × 0.85 = 0.82535` after threshold | `ASSUMPTION` | arithmetic |
| T10 | Mcfly list price | **$39.00 / store / month** | `LIVE` | https://apps.shopify.com/mcfly-analytics-public |
| T11 | Trial | 7 days; **$0** recognized during trial | `LIVE` + `ASSUMPTION` (no charge until subscription starts) | listing; https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials |
| T12 | Refunds / churn clawbacks | **0** in all tables unless a row says otherwise | `ASSUMPTION` | official: refunds do **not** reduce share base |
| T13 | Currency | USD | `LIVE` | listing |
| T14 | App Store registration | **$19 one-time** | `OFFICIAL` | revenue-share page |
| T15 | Course SKU | **$79 one-time** on site; **not** on the App Store card | `LIVE` | https://mcflyads.com/pricing |
| T16 | Partner account already on reduced-share plan | **Yes** | `ASSUMPTION` | confirm in Partner Dashboard (`UNANSWERED_QUESTIONS.md` Q8) |

**Keep-rate used in every later table unless noted:**

| Regime | Share | Processing | Keep (T8 additive) | Keep (T9 sequential) |
| --- | --- | --- | --- | --- |
| **R0** — lifetime gross ≤ $1M | 0% | 2.9% | **97.1%** | 97.1% (same) |
| **R15** — lifetime gross > $1M | 15% | 2.9% | **82.1%** | 82.535% |

Decision implication (arithmetic, not a forecast): a $39 app reaches $1M lifetime only at **very large N** (Table F). **R0 + 2.9% is the binding take** for any near-term Mcfly scenario. The 15% row is a **ceiling case**, not next quarter.

---

## B. Per-store take-home at live list prices

`ARITHMETIC` from T8 / T10. Competitor prices `LIVE` 2026-09-09.

| App | List $/mo | Source | Net @ R0 (×0.971) | Net @ R15 (×0.821) |
| --- | --- | --- | --- | --- |
| Margn Starter | 19.00 | https://apps.shopify.com/margn-1 | 18.45 | 15.60 |
| Kleio Everything | 29.00 | https://apps.shopify.com/kleio | 28.16 | 23.81 |
| TrueProfit Basic (no overage) | 35.00 | https://apps.shopify.com/trueprofit | 33.99 | 28.74 |
| **Mcfly** | **39.00** | https://apps.shopify.com/mcfly-analytics-public | **37.87** | **32.02** |
| Margn Growth | 39.00 | margn-1 | 37.87 | 32.02 |
| Lifetimely S | 49.00 | https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics | 47.58 | 40.23 |
| SyncWith Premium | 4.99 | https://apps.shopify.com/syncwith | 4.85 | 4.10 |
| TW Foundation (listing floor) | 219.00 | https://apps.shopify.com/triplewhale-1 | 212.65 | 179.80 |
| Polar Core (listing floor) | 750.00 | https://apps.shopify.com/polar-analytics | 728.25 | 615.75 |
| Margn Pro | 79.00 | margn-1 | 76.71 | 64.86 |
| TrueProfit Enterprise (no overage) | 200.00 | trueprofit | 194.20 | 164.20 |

**R15 sensitivity (T9 vs T8) on Mcfly $39:** T8 net $32.02 · T9 net $32.19 · delta **$0.17/store/mo**. Stacking rule does not change any decision at Mcfly’s likely N.

---

## C. TrueProfit overage vs Mcfly flat (same merchant)

`LIVE` surcharge: Basic $35 + **$0.30/extra order**, cap $300 (https://apps.shopify.com/trueprofit).  
`ASSUMPTION`: orders above the 300 included; Mcfly stays $39 with no meter.

| IF orders / mo | TP list $ | TP net @ R0 | Mcfly list $ | Mcfly net @ R0 | TP − Mcfly (list) |
| --- | --- | --- | --- | --- | --- |
| 300 (no extra) | 35.00 | 33.99 | 39.00 | 37.87 | −4.00 |
| 400 | 65.00 | 63.12 | 39.00 | 37.87 | +26.00 |
| 500 | 95.00 | 92.25 | 39.00 | 37.87 | +56.00 |
| 800 | 185.00 | 179.64 | 39.00 | 37.87 | +146.00 |
| 1,300 (hits $300 cap) | 335.00 | 325.29 | 39.00 | 37.87 | +296.00 |
| 3,000 (still capped) | 335.00 | 325.29 | 39.00 | 37.87 | +296.00 |

TP **out-earns** Mcfly per successful growing merchant once extras start. Mcfly’s brand promise is to **refuse** that (`mcflyads.com/pricing` anti-GMV). Then **N or agency seats** must do the work — not a hope, a structural requirement.

---

## D. Volume ladders — IF N paying stores at $39

`ASSUMPTION`: all N are paying (post-trial), $39, no annual discount, no refunds, no agency SKU, no course.  
**Not a forecast.** N is an input you plug in after Partner Dashboard exists.

| IF paying stores N | Gross MRR $ | Net MRR @ R0 $ | Net MRR @ R15 $ | Gross ARR $ | Net ARR @ R0 $ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 39 | 37.87 | 32.02 | 468 | 454.43 |
| 3 | 117 | 113.61 | 96.06 | 1,404 | 1,363.28 |
| 5 | 195 | 189.35 | 160.10 | 2,340 | 2,272.14 |
| 10 | 390 | 378.69 | 320.19 | 4,680 | 4,544.28 |
| 20 | 780 | 757.38 | 640.38 | 9,360 | 9,088.56 |
| 50 | 1,950 | 1,893.45 | 1,600.95 | 23,400 | 22,721.40 |
| 100 | 3,900 | 3,786.90 | 3,201.90 | 46,800 | 45,442.80 |
| 215 | 8,385 | 8,141.84 | 6,884.09 | 100,620 | 97,702.02 |
| 500 | 19,500 | 18,934.50 | 16,009.50 | 234,000 | 227,214.00 |
| 1,000 | 39,000 | 37,869.00 | 32,019.00 | 468,000 | 454,428.00 |
| 2,137 | 83,343 | 80,926.05 | 68,424.60 | 1,000,116 | 971,112.64 |

Polar listing floor $750 vs Mcfly $39: **IF** one Polar-priced seat ≈ **19.2** Mcfly seats at list (`ARITHMETIC` 750/39). CS cost of Polar is not Mcfly’s (`APP_STORE_MARKET.md` §10).

---

## E. Months of $39 revenue to cross $1M lifetime (when 15% starts)

`ARITHMETIC`: months = `1,000,000 / (39 × N)` at constant N. No growth, no churn, no other SKUs.

| IF constant paying N | Gross $/mo | Months to $1M | Years to $1M |
| ---: | ---: | ---: | ---: |
| 10 | 390 | 2,564.1 | 213.7 |
| 50 | 1,950 | 512.8 | 42.7 |
| 100 | 3,900 | 256.4 | 21.4 |
| 215 | 8,385 | 119.3 | 9.9 |
| 500 | 19,500 | 51.3 | 4.3 |
| 1,000 | 39,000 | 25.6 | 2.1 |
| 2,137 | 83,343 | 12.0 | 1.0 |

**Read:** R15 is not a 2026 planning constraint unless N is in the **hundreds-to-thousands** or another SKU explodes lifetime gross. Do not use “15% Shopify tax” as a reason to raise price at 0 reviews.

---

## F. Trial / listing funnel — IF views and IF rates

Official: reviews need installs; listing is the discovery object.  
`MARKET_REPORT` view→install (TSC 2026): <25 reviews ~**1–2%**; 200+ ~**5–8%** — https://taylorsicard.com/blog/shopify-app-listing-conversion. **Not Mcfly’s rate.**  
`ASSUMPTION` trial→paid bands below are **stress tests**, not forecasts. Mcfly trial-to-paid is `UNVERIFIED` (Partner Dashboard).

| IF listing views / 30d | IF view→install | IF installs | IF trial→paid | IF paying adds | IF new gross MRR $ | IF new net MRR @ R0 $ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 100 | 1% | 1 | 10% | 0.1 | 3.90 | 3.79 |
| 100 | 1% | 1 | 30% | 0.3 | 11.70 | 11.36 |
| 500 | 1% | 5 | 20% | 1 | 39.00 | 37.87 |
| 1,000 | 1% | 10 | 20% | 2 | 78.00 | 75.74 |
| 5,000 | 1% | 50 | 20% | 10 | 390.00 | 378.69 |
| 5,000 | 2% | 100 | 20% | 20 | 780.00 | 757.38 |
| 5,000 | 5% | 250 | 20% | 50 | 1,950.00 | 1,893.45 |
| 10,000 | 2% | 200 | 30% | 60 | 2,340.00 | 2,272.14 |

TSC’s own frame: **~5,000 views** to get ~50 installs at 1% (`APP_STORE_MARKET.md` §3). Those views, on Mcfly’s current rail, are people who wanted **Clarity/Parkour**.

**Blank cells you must fill from Partner Dashboard before using this table:** actual views, installs, trial starts, paid, uninstalls.

---

## G. Cost stack — IF operating costs

`ASSUMPTION` entire section. MASTER_PLAN §3 capital ~$250. No production P&L is in this repo.

| Cost | IF monthly $ | Tag | Note |
| --- | --- | --- | --- |
| Fly / host / DB | **5 / 20 / 50** (three rows in G2) | `ASSUMPTION` | Prefer the band; do not invent a bill |
| Sentry / email / extras | **0** | `ASSUMPTION` | Add if you pay it |
| App Store ads | **0** | `ASSUMPTION` | `WAR_ROOM.md`: no ads until views exist |
| Shopify registration | 19 **once** | `OFFICIAL` | ignore in monthly after month 0 |
| Support labor | **hours × wage** (Table G3) | `ASSUMPTION` | Binding for a solo founder |
| OAuth / API vendor fees | **0** | `ASSUMPTION` | Meta/Google may add review time, not a listed $ |

### G2. Paying stores to cover hosting only (no labor)

Net/store @ R0 = **$37.87**.

| IF host $/mo | IF stores to cover host (ceil) |
| ---: | ---: |
| 5 | 1 |
| 20 | 1 |
| 50 | 2 |

Hosting is **not** the constraint. Labor is.

### G3. Support intensity vs $39 net

`ASSUMPTION` wage bands. Founder sweat = $0 cash, **not** $0 cost.

| IF support h / store / mo | IF wage $/h | Labor $/store | Cash net @ R0 after labor $ | Sign |
| ---: | ---: | ---: | ---: | --- |
| 0.0 | 50 | 0 | 37.87 | + |
| 0.25 | 50 | 12.50 | 25.37 | + |
| 0.50 | 50 | 25.00 | 12.87 | + |
| 0.75 | 50 | 37.50 | 0.37 | ≈0 |
| 1.00 | 50 | 50.00 | −12.13 | − |
| 0.50 | 0 (sweat) | 0 | 37.87 | + cash, − time |
| 0.50 | 100 | 50.00 | −12.13 | − |
| 2.00 (sit-with-them onboarding) | 50 | 100.00 | −62.13 | − |

Kleio reviews praise **two-hour founder calls**. That is G3’s 2.00 row. Love is **labor-negative** at $39 unless those hours are treated as acquisition, not ongoing support.

| IF ongoing support stays at | Break-even wage @ $37.87 net |
| --- | --- |
| 0.50 h/store/mo | **$75.74 / h** |
| 1.00 h/store/mo | **$37.87 / h** |

### G4. Contribution after host $20 + support 0.50 h @ $50

`ASSUMPTION`.

| IF N paying | Net @ R0 $ | Host $ | Labor $ | Contribution $ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 37.87 | 20 | 25 | −7.13 |
| 3 | 113.61 | 20 | 75 | 18.61 |
| 5 | 189.35 | 20 | 125 | 44.35 |
| 10 | 378.69 | 20 | 250 | 108.69 |
| 20 | 757.38 | 20 | 500 | 237.38 |

**IF** those costs: contribution turns positive between **1 and 3** paying stores. That is arithmetic on assumptions, not a plan to “hit 3 MRR.”

---

## H. Price experiments (do not ship from this table)

`ASSUMPTION`: same R0 keep 97.1%; same N. Live listing is $39.

| IF list $/mo | Net/store @ R0 $ | Why someone would try it | Why it may fail |
| ---: | ---: | --- | --- |
| 0 (forever free) | 0 | Review engine (Lifetimely Free ≤50; TW Free; TSC first-50-reviews) | MASTER_PLAN rejects bait; uninstall ranking `MARKET_REPORT` |
| 19 (Margn Starter) | 18.45 | Comparison vs Margn | Labor row G3 goes red faster |
| 29 (Kleio) | 28.16 | Same-religion price match | Still thinner product; Kleio has 20 reviews |
| **39 (live)** | **37.87** | Anti-meter moral; TP-adjacent | Same wallet, thinner job |
| 49 (Lifetimely S) | 47.58 | “Serious desk” | 0 reviews + paste TTV |
| 79 (repo draft) | 76.71 | MASTER_PLAN target | `RELIGION_FLEX.md` R5: suicide at 0 reviews |
| 99 (S4 overlay) | 96.13 | Finance overlay on TW | Needs a P5 buyer; volume L |

Annual **IF −17%** (TW / Margn listing pattern): $39 × 12 × 0.83 = **$388.44 / yr** list · net @ R0 **$377.18 / yr** · vs monthly $468 / $454.43. GapQuery/TSC: don’t add annual until ~50 paying — `MARKET_REPORT`, not a rule.

---

## I. Agency / portfolio SKU — IF packaged

`ASSUMPTION` prices. Evidence of the *shape*: Metorik multi-store from $75; BeProfit Plus $249; Polar unlimited users (`OPPORTUNITY_MAP.md` C4).

| IF SKU | List $/mo | Net @ R0 $ | vs 3 × $39 list | Note |
| --- | ---: | ---: | ---: | --- |
| 1 store (live) | 39 | 37.87 | — | control |
| 3 stores @ $39 each | 117 | 113.61 | 117 | support ×3 (G3) |
| IF agency 3-pack $99 | 99 | 96.13 | −18 list | cheaper than 3 singles; still + vs 1 |
| IF agency 10-pack $249 | 249 | 241.78 | vs 390 | BeProfit-shaped; support ×10 |

Kill from `SYNTHESIS.md` S3: 5 agencies won’t pay more than SyncWith $4.99 + their tab.

---

## J. Course $79 — IF billed off App Store

`LIVE` price: https://mcflyads.com/pricing “MDS Made Easy $79 one-time.”  
`ASSUMPTION` J1: billed via **Stripe** (not Shopify Billing) at **2.9% + $0.30**.  
`ASSUMPTION` J2: alternate — billed via Shopify at R0 2.9% only.

| Path | List $ | Fees $ | Net $ | Tag |
| --- | ---: | ---: | ---: | --- |
| Stripe 2.9%+$0.30 | 79.00 | 2.59 | 76.41 | `ASSUMPTION` J1 |
| Shopify R0 (2.9% only) | 79.00 | 2.29 | 76.71 | `ASSUMPTION` J2 |
| Shopify R15 additive | 79.00 | 14.14 | 64.86 | T8 |

Course does **not** create App Store reviews (reviews require install). MASTER_PLAN discarded consulting as core. Treat as a **side door**, not a unit-econ engine.

| IF course sales / mo | IF J1 net $ |
| ---: | ---: |
| 0 | 0 |
| 1 | 76.41 |
| 4 | 305.64 |

---

## K. Kleio / Margn / Mcfly wallet — same N, different list

`ARITHMETIC` @ R0. **IF** the merchant picks one.

| IF N paying | Kleio $29 net $ | Mcfly $39 net $ | Margn $19 net $ | Margn $39 net $ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 28.16 | 37.87 | 18.45 | 37.87 |
| 10 | 281.59 | 378.69 | 184.49 | 378.69 |
| 50 | 1,407.95 | 1,893.45 | 922.45 | 1,893.45 |

Mcfly **keeps more per seat than Kleio** at the same N. Kleio **gets the seat** (20 reviews, 14-day, P&L, OAuth). Gross take-home is not the constraint; **win rate** is. This table is why “raise to $79 to make unit-econ work” is backwards.

---

## L. Polar / TW floors vs Mcfly N (illustration, not a target)

`LIVE` floors. External TW charges **not** included.

| Other product (listing floor) | List $ | Mcfly $39 seats to match **list** | Mcfly net @ R0 to match their **list** |
| --- | ---: | ---: | ---: |
| SyncWith Premium | 4.99 | 0.13 | — |
| Kleio | 29 | 0.74 | — |
| TrueProfit Basic | 35 | 0.90 | — |
| TW Foundation | 219 | 5.6 | 5.8 seats of Mcfly net |
| TW Automate | 749 | 19.2 | 19.8 |
| Polar Core | 750 | 19.2 | 19.8 |

Use only to remember: **one suite seat ≠ a Mcfly company.** Volume or a higher SKU (I) is the alternative to becoming a suite.

---

## M. What is *not* in these tables (on purpose)

| Missing | Why |
| --- | --- |
| Mcfly MRR / installs / views | Not in repo; Partner Dashboard only |
| Churn % | No public Mcfly or honest competitor churn |
| LTV of a Mcfly subscriber | Would be invented |
| CAC | $0 ads assumed; outbound hours sit in G3, not here |
| “We’ll hit $10k MRR” | Forbidden by this file’s header |

Fill Table F’s blank dashboard cells. Then re-run D and G4. That is the only honest loop.
