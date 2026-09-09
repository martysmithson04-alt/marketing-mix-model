# Enterprise landscape — the whole niche

**Date:** 2026-09-09  
**Mode:** RESEARCH ONLY. Does not amend `docs/MASTER_PLAN.md`.  
**How to use:** every section is a decision object. If a paragraph would not change what you do next week, it is not here.  
**Evidence:** live URLs in [`SOURCE_BIBLIOGRAPHY.md`](./SOURCE_BIBLIOGRAPHY.md) + IDs in [`db/`](./db/). Prior waves: PRs [#5](https://github.com/martysmithson04-alt/marketing-mix-model/pull/5)–[#13](https://github.com/martysmithson04-alt/marketing-mix-model/pull/13).  
**Rule:** no invented installs, MRR, GMV, or “X% of merchants.” Ratings/prices are **listing snapshots** from 2026-09-09 unless a row says `UNVERIFIED` or `FETCH_FAILED`.

Religion is **FLEXIBLE**. Tags: `CURRENT_RELIGION` · `RESEARCH_OPTION` · `EVIDENCE` · `RISK`.

---

## 0. The niche in one screen

This is **not** “the attribution market.” It is the stack of paid and unpaid tools Shopify operators use to answer four different Monday questions:

| # | Monday question | Who asks | What they buy today | What they refuse |
| --- | --- | --- | --- | --- |
| Q1 | Did the **algorithm** get the conversion? | Media buyer (P2) | Free/paid **pixel + CAPI** (Parkour, WeTracked, Elevar) | Another dashboard they must paste into |
| Q2 | Did we **keep cash** after COGS/fees/ads? | Founder (P1) | **Profit desk** (TrueProfit, Lifetimely, Kleio, BeProfit) | Philosophy without a P&L |
| Q3 | Which **path** deserves credit? | Growth/CMO (P5) | **Suite / MTA** (TW, Polar, Northbeam, Attribuly) | A $39 CSV box |
| Q4 | Does the **bank / books** match Admin? | Finance (P4) | **A2X / Synder / Finaloop** | A marketing tile that includes VAT |

Mcfly’s live listing answers a **fifth** question that operators already solve with a Sheet:

> Admin has sales. Ads Manager has spend (and a lying ROAS). Put them on one desk. Total ROAS = sales ÷ spend. No pixels.

That job is **real** ([Community 134251](https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4); [r/PPC 1u81q7r](https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/)). It is **not** an empty category. Kleio ships the easy version at **$29 / 14-day / 5.0 (20)** ([apps.shopify.com/kleio](https://apps.shopify.com/kleio)). TrueProfit ships the loved version at **$35+ / 5.0 (900 this-wave listing)** ([trueprofit](https://apps.shopify.com/trueprofit)). Shopify files Mcfly next to **Clarity / Parkour / WeTracked** — free pixels — not next to Polar or TrueProfit ([mcfly-analytics-public](https://apps.shopify.com/mcfly-analytics-public)).

**Decision this section forces:** stop describing Mcfly as “the empty chair.” Decide which Monday question you will win, knowing Kleio already sits in Q2+Q1-spend at $10 less.

---

## 1. Segment map (the whole aisle)

```
                    ┌─────────────────────────────────────────────┐
                    │  NATIVE / DIY (default, $0)                 │
                    │  Shopify Admin · Ads Manager · Sheets       │
                    └───────────────┬─────────────────────────────┘
                                    │ “this is messy”
          ┌─────────────────────────┼──────────────────────────┐
          ▼                         ▼                          ▼
   PIXEL / CAPI              PROFIT / P&L DESK           REPORTS / PIPES
   Parkour Free              TrueProfit $35+             Report Pundit Free
   WeTracked                 Lifetimely Free→$49         Better Reports $19.90
   Elevar $225               Kleio $29 flat              SyncWith $4.99
   Analyzify $145            Juicy / GoProfit / Bloom    Mipler / Toaster
   Clarity / Lucky Orange    BeProfit $49                Coupler / Coefficient
          │                         │                          │
          └────────────┬────────────┴───────────┬──────────────┘
                       ▼                        ▼
              ATTRIBUTION OS              FINANCE RECON
              TW Free→$219→$749           A2X $29
              Polar from $750             Synder $65
              Attribuly $450              Finaloop $245/$995
              Daasity $1,899              Link My Books $21
              Northbeam (no listing)      (QB / Xero / NS)
              Rockerbox / Lebesgue
                       │
                       ▼
              INCREMENTALITY / MMM (sales-led, often no listing)
              Measured · Haus · Recast · Mutinex · Polar Causal Lift
```

**How money actually moves between segments**

| From | To | Trigger | Evidence |
| --- | --- | --- | --- |
| Sheets | Profit desk | “I just want net profit without 30 min/day” | [Community 588628](https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628) |
| Profit desk | Suite | Scale + “one place” + CS | Polar Naturtint 5★; Kleio Trek Light **left TW** for $29 |
| Suite | Profit desk / Kleio | Price + VAT + AI credits | TW Kove 1★ VAT; Kleio EMME “better than TW, $29” |
| Suite | Finance recon | Board pack ≠ books | [Community 577364](https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364); A2X 5.0/359 |
| Pixel | Stay in Ads Manager | “I don’t need another dashboard” | WeTracked isella 5★ |
| Any paid app | Uninstall + 1★ | Billing after cancel; VAT; meter surprise | BeProfit $720 zombie; TrueProfit trial charge |

`CURRENT_RELIGION`: Mcfly is a cash desk, not a pixel, not a GL, not an OS.  
`RESEARCH_OPTION`: the **paid review gravity** is the profit desk. The **volume review gravity** is free pixels + free reports. Mcfly currently has neither.

---

## 2. Buyer map (who signs, who vetoes, who reviews)

Full personas: [`PERSONAS.md`](./PERSONAS.md). Decision rights: [`DEEP_DIVE_BUYERS.md`](./DEEP_DIVE_BUYERS.md). JTBD canvas: [`NICHE_CANVAS.md`](./NICHE_CANVAS.md).

| ID | Buyer | Badge | Pays from | Reviews on App Store? | Mcfly today |
| --- | --- | --- | --- | --- | --- |
| **P1** Founder-operator | Signs $29–$149 | Yes | Own card | **Yes — this is review velocity** | Same wallet as TrueProfit $35 / Kleio $29; thinner job |
| **P2** Media buyer | Recommends; sometimes card | Rarely alone | Founder’s card | Sometimes, if TTV is daily | Useless as daily tool (CSV) |
| **P3** Agency | Recommends; client pays | Client | Client store | **Rare** (client owns the review) | Paste-first is *their* native; no portfolio SKU |
| **P4** Finance / fractional CFO | Veto / second seat | Sometimes | OpEx | Rare | No tax mode, no export, no books |
| **P5** CMO / Plus pod | Signs Polar/NB | Yes | Marketing budget | Almost never | $39 reads as not-serious |
| **P6** Omni / Amazon+Shopify | Signs add-ons | Yes | Ops | Rare | Lifetimely Amazon +$75 owns this |

**The App Store listing only recruits P1.** Outbound recruits P3/P4/P5. Doing a hostile store *and* no outbound is how a listing dies of silence (`RELIGION_FLEX.md` R11).

**Stakeholder conflict that creates the category:**

| Conflict | Who wins today | Who loses | Product that harvests it |
| --- | --- | --- | --- |
| Ads Manager ROAS ≠ Shopify till | Pixel vendor (feed the algorithm) | Founder (scaled the wrong campaign) | Suites + Kleio spend sync; Mcfly *could* own the **gap card** |
| VAT in / out of revenue | Suite default (often tax-in) | EU finance | TW 1★ Kove; Kleio tax toggle |
| Attributed spend vs **total** spend | Media buyer / vendor | Founder P&L | BeProfit 1★ “only UTM spend”; Mcfly/Margn religion |
| Order meter vs flat | Vendor finance | Scaling founder | TrueProfit surcharge + BeProfit zombies |
| Pixel install vs “platforms lie” | Free CAPI apps | Mcfly brand | Shopify already filed Mcfly on that rail |

---

## 3. Money flows (who takes what)

Official Shopify take-rate ([revenue-share](https://shopify.dev/docs/apps/launch/distribution/revenue-share)):

| Rail | Rule (2026 public text) |
| --- | --- |
| Partner registration | $19 one-time |
| Processing | **2.9%** on all App Store billing |
| Revenue share | **0%** on first **$1,000,000** lifetime gross from 2025-01-01; **15%** after |
| Gross | Sales, not net. Refunds do **not** reduce the share base |
| Public billing | Must use Shopify App Pricing unless Shopify wrote an exception (Polar discloses external charges) |
| Trial | Configurable; **180-day** anti-reinstall window |
| Uninstall | Cancels *future* recurring; current cycle + **external** charges may continue ([uninstalling-apps](https://help.shopify.com/en/manual/apps/uninstalling-apps)) |

**Mcfly list-price math (not a forecast):** $39 × (1 − 0.029) = **$37.87** net per paying store while under the $1M cap. After the cap: 15% + 2.9% on gross. One Polar Core listing floor ($750) ≈ **19** Mcfly stores. Kleio at $29 is **$10/mo cheaper** with a bigger desk.

### 3.1 Price-shape map (observed menus, not ARR)

| Shape | Who uses it | What it does to money | What it does to love |
| --- | --- | --- | --- |
| **Flat, no expansion** | Mcfly $39 · Kleio $29 | ARPU ceiling = list price. NRR cannot exceed 100% from expansion | Honest. Kleio proved 5★ are possible |
| **Order ladder + overage** | TrueProfit $35+$0.30 · Profitario | Expansion forced. Surprise invoices | 1★ factory when notice is late (bamtoo / Brooklyn — see `ANTI_PATTERNS.md`) |
| **Order ladder, same product** | Lifetimely Free≤50 / $49 / $149 / $299 | Free on-ramp **is** the review engine (535) | Love high at free; paid is the same desk |
| **GMV slider** | TW Foundation $219 → Automate $749+ · Polar from $750 | High ARPU, sales motion | TW 16% 1★ hangover |
| **Shopify-plan priced** | Better Reports $19.90 / $39.90 / $149.90 / $299.90 | Grows with store plan | 1,199 reviews; they *build* the report |
| **Free + external** | WeTracked, Rockerbox, Klar, Facebook/TikTok channels | App Store is a pipe; money off-store | Review velocity of “Free to install” |
| **Sales-led, no listing** | Northbeam · Hyros · Wicked · Measured · Haus · Recast | High ARPU, human cycle | Zero App Store love |

`CURRENT_RELIGION`: stay flat; never GMV-tax ([mcflyads.com/pricing](https://mcflyads.com/pricing)).  
`RESEARCH_OPTION`: flat is a **moral**, not a moat. Kleio already has the moral **and** the P&L. Agency SKU is the only expansion that does not break the moral.  
`RISK`: $39 vs Kleio $29 with less product is a donation.

### 3.2 Where review-gravity money sits (listing snapshots 2026-09-09)

| Cluster | Review mass (sum of listed counts) | Typical entry $ | Job they are paid for |
| --- | --- | --- | --- |
| Free heatmaps / pixels | Clarity 2,125 + Lucky Orange 878 + Parkour 191 + WeTracked 125 + … | $0 | Tracking / replays |
| Custom reports | Report Pundit 2,026 + Data Export 2,009 + Better Reports 1,199 + Mipler 633 | Free–$20 | “They built my report” |
| Official ad channels | TikTok 15,912 + Facebook 5,648 | $0 install | Ads, not analytics |
| Profit / P&L | TrueProfit **900** (this-wave listing) + Lifetimely ~535 + BeProfit 202 + Juicy 76 + GoProfit 90 + Kleio 20 | $29–$49 | Net profit after costs |
| Suites | Polar 116 + TW 91 + Attribuly 168 + Lebesgue 132 + Daasity 51 | $219–$1,899 | One-place OS / MTA |
| Finance recon | A2X 359 + Synder 217 + Finaloop 73 | $29–$245 | Payouts → books |
| Mcfly | **0** | $39 | Paste-first Total ROAS |

**Do not add these into a TAM.** They prove **which jobs print public love**, not how many dollars are available.

---

## 4. Incumbent map (system of record)

Full matrix: [`COMPETITIVE_MATRIX.md`](./COMPETITIVE_MATRIX.md) (65 App Store rows). Cards: [`COMPETITOR_CARDS.md`](./COMPETITOR_CARDS.md). Sales-led extras in `db/competitors.jsonl` (target ≥80). Query: `SELECT id, kind, price_scan, rating, review_count FROM competitors ORDER BY kind, review_count DESC`.

### 4.1 Structural peers (same commercial shape as Mcfly)

| id | Why they matter | Listing (2026-09-09) | Decision |
| --- | --- | --- | --- |
| **kleio** | Flat $29, 14-day, OAuth spend, CM1–CM3, tax toggle, MCP, **refuses MTA** | 5.0 / 20 · [kleio](https://apps.shopify.com/kleio) | **Primary peer.** S1 without claims-vs-cash is a late Kleio (`KLEIO_GAP_ANALYSIS.md`) |
| **margn** | “Total spend, never attributed-only”; BE ROAS; $19/$39/$79; 7-day; launched 2026-08-18 | 0.0 / 0 · [margn-1](https://apps.shopify.com/margn-1) | Mirror, not a moat. Price+newness≠wedge |
| **profit_calc** | Same **$39** list | 5.0 / 67 | Shelf is not empty |
| **bloom** | $20 unlimited + MCP + MTA claim | 5.0 / 39 | Cheap AI/MCP gravity |
| **juicy / go_profit** | Profit + ads in the $12–$29 band | 4.9/76 · 4.8/90 | Already have review mass Mcfly does not |
| **trackprofit / profitiq / marginlens / profit_panel** | 0-review clones | 0 / 0 | Crowding. Do not join this pile |

### 4.2 Wallet competitors (P1’s $35–$149)

TrueProfit · Lifetimely · BeProfit · Metorik · Profitario · Setpilot · CashDash · ClearProfit · ProfitMetrics.  
Loved job = **assembled net profit + auto spend**. VAT and cancel-path are the 1★ mines.

### 4.3 Distribution enemies (Shopify’s “more like this”)

Clarity · Parkour · WeTracked · Lucky Orange · Analyzify · Elevar · Littledata · Hotjar.  
These print reviews because TTV is **minutes** and the job is **feed the algorithm / watch the session**. Mcfly’s anti-pixel sermon does not move them. Partner (S5b); do not rebuild (S5).

### 4.4 Suites (do not replace; maybe overlay)

TW · Polar · Northbeam (no listing) · Attribuly · Lebesgue · Daasity · Rockerbox · Klar · Segmetrics · Hyros / Wicked (sales-led).  
MER is a **tile**. CS + pixel + GMV tax are the product.

### 4.5 Complements (do not clone)

A2X / Synder / Finaloop / Link My Books = books.  
Report Pundit / Better Reports / Mipler = custom reports as a **service**.  
SyncWith / Coupler / Coefficient / Supermetrics / Windsor / Funnel = pipes.  
Measured / Haus / Recast / Mutinex = incrementality/MMM, sales-led.

### 4.6 Autopsies (what death looks like)

[`FAILURE_AUTOPSIES.md`](./FAILURE_AUTOPSIES.md): Stocky official sunset 2026-08-31 · Metrilo 5.0/**2** after Brevo · Glew acquired 2026-03, store handle unverified · BeProfit 1★ after Viably · Klar/Segmetrics store-dead · dozen 0-review profit clones.

**Lesson:** a live listing ≠ a living product. 5.0 without a denominator is noise.

---

## 5. White space (real empties vs dead empties)

[`WHITE_SPACE.md`](./WHITE_SPACE.md) · [`CATEGORY_TOPOLOGY.md`](./CATEGORY_TOPOLOGY.md).

Shopify Analytics aisle = **1,546 apps**, merchandised as free pixels/heatmaps ([category page](https://apps.shopify.com/categories/store-management-operations-analytics/all)). Mcfly chips (“Marketing and sales · Visuals and reports”) are **feature tags inside Analytics**, not the Marketing navbar.

| Empty type | Example | Trap | Mcfly implication |
| --- | --- | --- | --- |
| **Taxonomy empty** | NFTs (12 apps, Applora) | Dead demand | Ignore |
| **Keyword crowded** | “true profit”, “ROAS” | Word saturated, job still unsolved | Do not SEO-fight TrueProfit on their noun |
| **Job underserved** | Admin will not ingest Meta/Google/billboard spend | Suites *tile* it; Sheets *do* it | This is the only durable native refusal |
| **Job underserved + occupied** | Assembled net profit | Kleio/TP already ship it | Enter only with a wedge they structurally refuse |
| **Identity thin** | Claims-vs-cash as a **product**, not a FAQ | Kleio **refuses** the card (anti-MTA FAQ) | **Only visible unique wedge** (`KLEIO_GAP_ANALYSIS.md` row 6) |

**Structural refusals that can be wedges (only these):**

1. **Shopify Admin** will not ingest Meta/Google/billboard spend (Community 134251).  
2. **TrueProfit** meters orders; does not treat billboards as religion.  
3. **Kleio** refuses a claims-vs-cash card (platforms are the right *bidder*).  
4. **TW/Polar** will not be a $29–$39 flat honest desk.

`CURRENT_RELIGION` offline/billboard ledger is a wedge **if** those operators exist and pay. Wave A already called the SEO tiny.  
`RESEARCH_OPTION`: the wedge to *build* is **Ads Manager claim vs Shopify till**, paste-first if Meta §10.d blocks the API (`COMPLIANCE_LANDMINES.md`).  
`RISK`: if merchants will not paste a claim **and** API is blocked **and** we will not sell spend-only vs Kleio $29 → S1 is dead (`STRATEGY_KILL_CRITERIA.md` S1-K4).

---

## 6. Mcfly position today (2026-09-09)

Live control: [apps.shopify.com/mcfly-analytics-public](https://apps.shopify.com/mcfly-analytics-public) · [mcflyads.com](https://mcflyads.com)

| Field | Live | Repo / religion | Collision |
| --- | --- | --- | --- |
| Price | **$39/mo**, 7-day | Drafts still say free DP → ~$79 | Commercial suicide to raise at 0 reviews |
| Reviews | **0.0 / 0** | — | Two days old at first fetch; still a brochure |
| Launched | Sept 7, 2026 | — | Margn launched Aug 18 — same table |
| Metric name | **Total ROAS** | Cash MER in repo | Two public names |
| Mechanism | Paste / CSV; **“No ad-account OAuth”** on site | MASTER_PLAN Phase 2 = OAuth | Religion already inconsistent |
| Refused | No pixels. No path credit | Same | Correct; not a differentiator vs Kleio |
| Claims | LTV / Goals as paid extras | Repo v1 did not ship them | Listing integrity risk (requirement 4.3.7 + honesty) |
| Adjacent apps | Clarity, WeTracked, Parkour | Polar / TrueProfit in founder’s head | Distribution failure |
| Course | $79 one-time on site | Consulting discarded as core | Side door only |

**Four-score (research judgment, not a KPI):**

| Score | Live Mcfly | Why |
| --- | --- | --- |
| Money | **Weak** | $39 flat, 0 reviews, no freemium, no agency SKU, no expansion. $37.87 net |
| Love | **Unproven / structurally hard** | Adjacent apps win on 2-minute dopamine. Paste-CSV does not |
| Ease | **Mixed** | Easier for the *developer* than OAuth. Harder for the *merchant* than TrueProfit/Kleio |
| Real problem | **Partial** | Spend-next-to-sales is real. Net profit after costs is **more** real and owned |

**Brutal line (unchanged, still true):** priced like TrueProfit, scoped like a spreadsheet, merchandised like Parkour, reviewed like an app that does not exist. Post-Kleio addendum: **also $10 more than a founder-built P&L that already has 20 fives.**

---

## 7. Ranked opportunities (what would change a decision)

Scored H/M/L on money · love · ease · real problem. Full catalog: [`OPPORTUNITY_MAP.md`](./OPPORTUNITY_MAP.md). Strategic menu: [`SYNTHESIS.md`](./SYNTHESIS.md). Post-Kleio scores: [`S1_PRD_LITE.md`](./S1_PRD_LITE.md) · [`VNEXT_OPTION_SCORECARD.md`](./VNEXT_OPTION_SCORECARD.md).

| Rank | Opportunity | Tag | Four-score | Why it ranks here | Kill |
| --- | --- | --- | --- | --- | --- |
| **1** | **Claims-vs-cash card** (paste or API) | `STRETCH` / S1 wedge | H H M H | Only capability Kleio structurally refuses **and** r/PPC already screams | Merchants won’t paste **and** Meta §10.d blocks API |
| **2** | **OAuth spend-only** (Meta/Google; TikTok later) | `RELIGION_BEND` R3 | H H H H | Removes CSV tax; MASTER_PLAN Phase 2 already wanted it | App Review refused / silent; recon >5% 14 days |
| **3** | **14-day trial + listing integrity** | `STRETCH` | M M H M | Category default; 7-day + blank store = TTV mismatch | — (do even if product does not move) |
| **4** | **Tax / shipping / returns definition sheet** | `STRETCH` | M H M H | Prevents TW-VAT 1★; Kleio already shipped it | Support forever if unlabeled |
| **5** | **Monday Close email/Slack/PDF** | `STRETCH` | M H H M | Better Reports 1,199; Kleio outsourced this to MCP | DPs won’t open it |
| **6** | **Agency portfolio SKU** | `STRETCH` S3 | H M M H | Paste-first is native for agencies; App Store love stays low | 5 agencies won’t pay more than SyncWith $4.99 |
| **7** | **Pixel partner (Parkour/Elevar), do not own** | `RELIGION_BEND` S5b | M H H H | Cheap hedge; listing already on that rail | Partner 1★ (WeTracked evidence failure) |
| **8** | **Assembled contribution + cost-incomplete flag** | `RELIGION_BEND` S2 | H H M H | Review corpus *is* this job | Cannot name a wedge vs TP **and** Kleio |
| **9** | **Forever-free ≤50 orders** | `RELIGION_BEND` S7 | M H H M | Lifetimely’s review engine | Only if 30 days paid still = 0 reviews |
| **10** | Stay paste-only + course | `CURRENT_RELIGION` S6 | L L L M | Cheapest. Likely dies of silence | Already the default failure mode |

**Do not rank:** heatmaps, custom report builders, GL posting, creative studios, Moby clones, GMV tax, first-party pixel. Those are `ADJACENT_NO` or `RELIGION_BREAK`.

---

## 8. Strategic options after Kleio (menu, not a ship order)

| Option | One line | Wave B sum | Wave E revision | When it is the answer |
| --- | --- | --- | --- | --- |
| **S1 Governor** | Auto spend + claim card + definitions + Monday artifact | 19 | **14–16** | App Store is the channel **and** claim card will be used |
| **S2 Profit-lite** | Assemble COGS/fees/shipping + auto spend; offline+flat+claim as wedge | 16 | 16 (feasibility 2) | Loved number must be net profit **and** you can name the wedge |
| **S3 Agency** | N stores, Sheets in, PDF out, portfolio price | 16 | 16 | App Store abandoned as acquisition; outbound is the company |
| **S4 Overlay** | Number finance signs after TW/NB | 13 | 13 | One DP finance lead will put you in the board pack |
| **S5 Pixel rebuild** | Become CAPI | 14 | 14 | Never (brand suicide + Free competitors) |
| **S5b Partner pixel** | Works-with Parkour/Elevar | modifier | keep | Cheap with S1 |
| **S6 Narrow + course** | Stay | 9 | 9 | Only if you accept brochure status |
| **S7 Freemium** | Free desk → $39 | 17 bolt-on | keep as bolt-on | After paid path still has 0 reviews |

**Post-Kleio default if App Store is the channel:** S1 **narrowed** to spend + claim card + tax-sane till + Monday artifact. Not a P&L. Not eight ad networks.  
**If the loved number is net profit:** S2, knowing Kleio is $29 with a published waterfall.  
**If religion will not OAuth:** S3 outbound. Do not fight the store with a CSV.

Full kills: [`DECISION_BRIEF.md`](./DECISION_BRIEF.md) · [`STRATEGY_KILL_CRITERIA.md`](./STRATEGY_KILL_CRITERIA.md).

---

## 9. Category physics Mcfly does not get to vote on

| Law | Official / live source | Decision |
| --- | --- | --- |
| Reviews need installs; Magic summary needs **100 written + 4.0** | [manage-app-reviews](https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews) | You cannot review-farm. You can only ship TTV |
| No testimonials on the listing | Requirements 4.3.7 | Site social proof ≠ listing |
| BFS floor: **50 net paid-plan installs + 5 reviews** | [BFS requirements](https://shopify.dev/docs/apps/launch/built-for-shopify/requirements) | Do not chase BFS this quarter |
| 7-day trial + blank store until CSV | Live listing vs [offer-free-trials](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials) | 14-day is the aisle default |
| Analytics aisle merchandises **free pixels** | [1,546-app aisle](https://apps.shopify.com/categories/store-management-operations-analytics/all) | Copy must fight the rail or leave the store |
| ShopifyQL marketing schema is **Shop Campaigns**, not Meta/Google | [shop_campaign_insights](https://shopify.dev/docs/api/shopifyql/latest/schemas/marketing/shop_campaign_insights) | Native will not grow your denominator |
| Meta user tokens (Kleio docs): **60 days, no auto-refresh** | [Kleio ad integrations](https://www.getkleio.com/docs/integrations/ad-integrations) | OAuth is a product, not a checkbox |

---

## 10. How to see the niche in the DB

```bash
cd docs/research/competitive-2026-09/db
python3 build_db.py
sqlite3 competitive.sqlite
```

```sql
-- Who is in which aisle
SELECT kind, COUNT(*) FROM competitors GROUP BY kind;

-- Review gravity (listing snapshots only)
SELECT id, name, rating, review_count, price_scan
FROM competitors
WHERE review_count IS NOT NULL
ORDER BY CAST(review_count AS INT) DESC
LIMIT 25;

-- Problems with evidence
SELECT id, name, wtp, mcfly FROM problems ORDER BY CAST(rank AS INT);

-- Quotes by theme
SELECT app_id, stars, theme, quote FROM review_quotes;

-- Sources that actually fetched
SELECT type, COUNT(*) FROM sources GROUP BY type;
```

Schema: [`db/SCHEMA.md`](./db/SCHEMA.md). Index of every file: [`MASTER_INDEX.md`](./MASTER_INDEX.md). What to do: [`DECISION_BRIEF.md`](./DECISION_BRIEF.md).
