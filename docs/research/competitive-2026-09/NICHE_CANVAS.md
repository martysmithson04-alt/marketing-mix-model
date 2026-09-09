# Niche canvas — JTBD for operator, agency, CFO

**Date:** 2026-09-09  
**Mode:** RESEARCH ONLY. Inferred from public listings, reviews, Community, Reddit. **No private interviews in this corpus** until you fill `db/interviews.jsonl` (`INTERVIEW_SCRIPTS.md`).  
**IDs** point into the DB: `P-` / `p*` problems · `R-` / `Q-` quotes · `C-` competitors · `S-` sources. Query `db/competitive.sqlite`.

Four scores on every job: **money · love · ease · real problem**.

---

## How to read a canvas

Each job is one **progress** a buyer hires a product to make. Forces are Christensen-style: push (pain of current) · pull (better life) · habit (anxiety of switch) · anxiety (of the new). Mcfly **today** vs **RESEARCH_OPTION** are separate so religion cannot hide.

---

## Canvas 1 — Operator (P1 founder + P2 media buyer)

Two humans share a Slack and do **not** share a job. Split where it matters.

### 1A. Founder-operator (P1) — “Did we keep money?”

| | |
| --- | --- |
| **Job (functional)** | Know weekly **net cash after ads and costs** without a 30-minute Sheet |
| **Job (emotional)** | Sleep. Stop guessing. Stop being lied to by Ads Manager |
| **Job (social)** | Tell a partner / spouse / investor a number that will not be walked back |
| **Current hire** | Shopify Analytics + Meta/Google + a Sheet + maybe TrueProfit/Lifetimely/Kleio/BeProfit |
| **Push** | Sheet is “always a week behind”; Admin has sales, not spend; platforms over-claim |
| **Pull** | Open one desk → black or red. Kleio reviewers: daily P&L pulse. TrueProfit: “must need to see how much you're actually making” |
| **Habit** | Already in Ads Manager and Admin every morning |
| **Anxiety of new** | Another $39 that still needs CSV; VAT wrong; billed after uninstall |
| **WTP signal** | They already pay **$29–$149** for profit desks. They install **free** pixels at huge volume. They bounce off TW as “pretty expensive” |
| **Love when** | Number appears in minutes; named human; “source of truth” (Lifetimely Nikura) |
| **Hate when** | Meter surprise, VAT-in-revenue, cancel hell, attributed-only spend |

**Evidence IDs**

| Kind | ID | Points at |
| --- | --- | --- |
| Problem | `p1_net_profit` / `P-001` / `P-006` | Net profit; Sheet incumbent |
| Problem | `p3_spend_next_to_sales` | Admin will not ingest spend |
| Problem | `p4_platform_vs_till` | Meta ≠ Shopify |
| Quote | TrueProfit GowiLab 5★ | “must need to see… profit” · `review_quotes` / [trueprofit](https://apps.shopify.com/trueprofit) |
| Quote | Lifetimely Nikura 5★ | “source of truth… not bloated” |
| Quote | Community 588628 OP | “real net profit per order without 30 minutes a day” · `R-COM-001` |
| Source | `S-community-657805` | [657805](https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805) |
| Source | `S-reddit-1pzy8iv` | [r/shopify profit/month](https://www.reddit.com/r/shopify/comments/1pzy8iv/app_or_plugin_to_calculate_profit_each_month/) |
| Competitor | `C-trueprofit` `C-lifetimely` `C-kleio` `C-beprofit` | Wallet peers |

**Mcfly today (`CURRENT_RELIGION`):** answers sales÷spend **if they paste**. Does not assemble costs. $39 vs Kleio $29 / TP $35.

**RESEARCH_OPTION:** Path A = show the **lie** (claim vs till) + auto spend. Path B = assemble contribution with a cost-incomplete flag.  
**RISK:** Path A without a used claim card is a late Kleio. Path B without a wedge is a late TrueProfit.

### 1B. Media buyer (P2) — “What do I scale today?”

| | |
| --- | --- |
| **Job (functional)** | Change bids this morning without lying to the founder about cash |
| **Job (emotional)** | Not get blamed when Meta ROAS ≠ Shopify |
| **Job (social)** | Win the meeting against finance without a theology fight |
| **Current hire** | Ads Manager + CAPI (Parkour/WeTracked/Elevar) + maybe TW Free/Foundation + a daily Sheet (r/PPC 1qgb8mg) |
| **Push** | Platforms overlap; iOS; PMax; “my Shopify and Meta numbers have never matched” |
| **Pull** | Stay **inside** Ads Manager with better events **or** one daily table (channel, campaign, spend, sessions, orders, revenue, new/returning) |
| **Habit** | Live in ads UIs. Will not open a third desk for a sermon |
| **Anxiety** | Tracking change nukes the account (Analyzify 1★ themes) |
| **WTP signal** | Hundreds–thousands when the tool **writes back** (Elevar $225; NB Apex). **$0** for a CSV desk |
| **Love when** | “I do not have to use another dashboard” (WeTracked isella) |
| **Hate when** | Unproven accuracy (WeTracked 1★ elife); AI credits (TW Kove) |

**Evidence IDs**

| Kind | ID | Points at |
| --- | --- | --- |
| Problem | `p2_pixel_capi` / `P-009` | Pixel/CAPI; tracking can nuke ads |
| Problem | `p4_platform_vs_till` / `P-015` | Four scoreboards; till should win |
| Problem | `p7_passback` | Feed the algorithm |
| Quote | WeTracked isella 5★ | Stay in Ads Manager |
| Quote | WeTracked elife 1★ | No methodology / evidence |
| Quote | r/PPC 1u81q7r | Numbers never matched |
| Source | `S-reddit-1qgb8mg` `S-reddit-1pqv5kh` `S-reddit-1r2pvgy` | Holistic view / attribution / D2C |
| Competitor | `C-parkour` `C-wetracked` `C-elevar` `C-analyzify` `C-triple_whale` | Daily stack |

**Mcfly today:** useful only if the **founder mandates** the cash number. Useless as the buyer’s daily tool.

**RESEARCH_OPTION:** OAuth spend + claim-vs-till **screenshot they can Slack**. Partner a pixel (S5b). Do not become the pixel.  
**RISK:** P2 will never leave you a Parkour-shaped review.

---

## Canvas 2 — Agency (P3)

| | |
| --- | --- |
| **Job (functional)** | One close pack across N client stores: spend vs sales, client-safe, on Monday |
| **Job (emotional)** | Not get fired for a number the client’s Ads Manager contradicts |
| **Job (social)** | Look like the adult in the room vs the client’s in-house buyer |
| **Current hire** | Sheets + SyncWith/Supermetrics/Coupler + screenshots + maybe Metorik/BeProfit multi-store + Polar if the client is big |
| **Push** | N logins; refresh tax; each client wants a different religion (ROAS vs MER vs profit) |
| **Pull** | Portfolio SKU, white-label numbers, PDF/Slack out, **no “your pixel is theater” on the client slide** |
| **Habit** | Already live in Sheets. Paste-first is **native**, not a bug |
| **Anxiety** | Client owns the App Store review; agency switching cost is a tab, not a contract |
| **WTP signal** | Metorik 5 stores @ $75; BeProfit Plus $249 unlimited shops; Polar unlimited users @ $750; SyncWith $4.99 is the **substitute** |
| **Love when** | Multi-store ops costs can be spread (BeProfit Bioenex 4★ *wants* this) |
| **Hate when** | Per-shop GMV stack; work-email / sales-call gate (Polar) |

**Evidence IDs**

| Kind | ID | Points at |
| --- | --- | --- |
| Problem | `p12_multistore` / `P-010` / `P-016` | Multi-store / agency rollup |
| Problem | `p5_custom_reports` | Scheduled pack |
| Problem | `p15_monday_ritual` | Monday artifact |
| Quote | BeProfit Bioenex 4★ | Spread ops costs across stores |
| Quote | SyncWith listing / agency Sheets | Pipe without religion |
| Source | `S-listing-syncwith` `S-listing-metorik` `S-listing-polar` | Portfolio menus |
| Competitor | `C-syncwith` `C-metorik` `C-beprofit` `C-polar` `C-agencyanalytics` | Current hires |

**Mcfly today (`CURRENT_RELIGION` kept):** paste-first fits. **No** N-store SKU, no white-label, no outbound motion.

**RESEARCH_OPTION (S3):** sell **N stores, one close pack**. Price above SyncWith or die.  
**RISK:** agencies do not leave 899 reviews. Path C accepts that. Path A does not get App Store love from this canvas.  
**Kill:** S3-K1 — five agencies will not pay more than SyncWith + a tab.

---

## Canvas 3 — CFO / controller / fractional finance (P4)

| | |
| --- | --- |
| **Job (functional)** | Assemble **contribution / net profit** and **reconcile the bank**. Exportable definitions. VAT-sane |
| **Job (emotional)** | Not sign a board pack that includes tax in revenue or drops PMax spend |
| **Job (social)** | Win vs marketing’s four scoreboards with a definition sheet, not a vibe |
| **Current hire** | Shopify payouts + A2X/Synder/Link My Books + a cost Sheet + maybe Finaloop + Kleio Finance Summary if they found it |
| **Push** | “Revenue is native; true net profit has to be assembled” (Community 657805). Reconciliation thread 577364 |
| **Pull** | Tax toggle; dual clock (delivery vs invoice); cost-incomplete flag; CSV/API out to the bookkeeper |
| **Habit** | Month-end in QB/Xero/NS. Will not replace A2X |
| **Anxiety** | Marketing app posts to the GL; silent averages; no audit trail |
| **WTP signal** | A2X 5.0/359 from $29; Synder $65; Finaloop $245/$995 **service**. Polar $750 when they want a warehouse |
| **Love when** | “HOURS of journal entries → match → done” (A2X Sōl Collective) |
| **Hate when** | VAT in revenue (TW Kove 1★); TrueProfit “doesn’t track VAT collection” (VocaSpark 1★) |

**Evidence IDs**

| Kind | ID | Points at |
| --- | --- | --- |
| Problem | `p1_net_profit` `p9_gl_recon` `P-002` `P-004` `P-005` `P-012` | Profit, VAT, COGS rot, edits/returns, fees |
| Quote | A2X Sōl Collective 5★ | Journal time |
| Quote | TW Kove 1★ | VAT in revenue; AI credits |
| Quote | TrueProfit VocaSpark 1★ | VAT collection; trial bill |
| Source | `S-community-577364` `S-community-657805` | Recon + profit recipe |
| Source | Kleio metrics doc | CM1–CM3 + tax-in/out — the definition sheet Mcfly does not have |
| Competitor | `C-a2x` `C-synder` `C-finaloop` `C-kleio` `C-linkmybooks` | Finance stack |

**Mcfly today:** no tax mode, no dual clock, no GL (correct), no export ritual. Typed margin is a **toy** next to Kleio’s waterfall.

**RESEARCH_OPTION:**  
- Path A: **definition sheet + tax toggle + export**. Still not A2X.  
- Path B: assembled CM with missing-cost flag.  
- Path D/S4: overlay — the number finance **signs** after TW. $99 may read more serious than $39 (`RESEARCH_OPTION`).  
**RISK:** suites add a “finance MER” tile and erase you. Dual clock is Kleio/A2X territory; S1 Wave E left it out of Ring 1 on purpose.  
**Kill:** S4-K1 — no finance lead will put you in the pack.

---

## Cross-canvas: who Mcfly can satisfy at once

| If you optimize for… | Primary canvas | Secondary | You will lose | Path |
| --- | --- | --- | --- | --- |
| App Store reviews | 1A Founder | 1B only if spend auto | Agency love-at-scale; CFO books | A or B |
| Cash without becoming TP | 1A + claim card | 1B screenshot | P&L depth | **A** |
| Net profit 5-stars | 1A + 3 | — | Feasibility; Kleio/TP collision | **B** |
| Portfolio revenue | 2 Agency | 1A as the number inside the pack | App Store velocity | **C / S3** |
| Board-pack ARPU | 3 CFO | 1B as the lie card | Volume | **C / S4** |

**One-product lie:** a single $39 listing cannot be the founder’s P&L, the buyer’s bidder, the agency’s scoreboard, and the CFO’s books. Pick the primary canvas this week (`DECISION_BRIEF.md` §0).

---

## Force diagram (all three)

```
PUSH (current pain)              PULL (better life)
Sheet lag / Meta≠Shopify    →    One number, black or red
VAT / four scoreboards      →    Definition sheet finance will sign
N client logins             →    One close pack

HABIT (stay)                     ANXIETY (don't switch)
Ads Manager / Admin / QB    →    CSV homework, meter, cancel hell
Free pixel already works    →    Tracking change nukes ads
SyncWith tab already works  →    Another login the client won't open
```

Mcfly **increases anxiety** today (paste, 7-day, 0 reviews, unshipped LTV/Goals) while **under-delivering pull** vs Kleio/TrueProfit. That is why ease and love are structurally hard. Path A reduces anxiety (OAuth, 14-day, honest listing) and increases pull (claim card). Path B increases pull (profit) and anxiety (cost engine). Path C leaves the store and sells to habit (Sheets/board pack).

---

## Empty cells (do not fake)

| Cell | Status |
| --- | --- |
| First-party interview quotes | **None.** Scripts ready: `INTERVIEW_SCRIPTS.md`. Playbook: `FIRST_CUSTOMERS_PLAYBOOK.md` |
| Mcfly install/view/churn | **Partner Dashboard only.** Not in this repo |
| “X% of operators want MER” | **Do not invent** |
| Northbeam / Hyros official price | **No public card** this corpus (`FETCH_FAILED` / sales-led) |
