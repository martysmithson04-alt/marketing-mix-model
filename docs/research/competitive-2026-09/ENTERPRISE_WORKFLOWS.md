# Enterprise / mid-market workflows — public patterns only

**Date:** 2026-09-09  
**Honesty:** This is **not** a leak of any brand’s private stack. It is a synthesis of (a) vendor-documented product anatomy, (b) App Store listing jobs, (c) Shopify Community + Reddit operator writeups, (d) official Shopify Analytics behavior as documented. Where a pattern is inferred, it is labeled `INFERRED`.

Mcfly `CURRENT_RELIGION` is a **Monday cash ritual**. Mid-market teams run **weekly finance + daily media + monthly board**. Those clocks do not match.

---

## Clock speeds (operator language, public)

| Clock | Question | Public source |
| --- | --- | --- |
| **Intraday** | Is the pixel firing? Did Meta spend cap? | Elevar “monitoring and alerts” listing; Parkour EMQ comments |
| **Daily** | What do I scale/kill in Ads Manager? | r/PPC 1r2pvgy; TW Moby/Automate listing |
| **Weekly** | Did blended MER / profit hold? | r/shopify 1rpjuk0 “weekly” sheet; Mcfly site 10-minute ritual |
| **Monthly / close** | Can finance reconcile payouts, ads, refunds, tax? | Community 577364; A2X positioning |
| **Quarterly / board** | Incrementality, MMM, plan vs actual | Polar Causal Lift reviews; Northbeam MMM+ homepage; Community 180915 30-day lookback warning |

Mcfly today only pretends to own **weekly**. It has no daily feed and no close pack.

---

## Pattern 1 — “Sheets is the OS” (most common public DIY)

**Who describes it:** Community 134251 (Looker Studio + connector cost); r/PPC 1qgb8mg (agency $200k+/mo: Sheets blended ROAS); r/shopify 1p1fogj (UTMs + Sheets); SyncWith listing.

**Ingredients (public):**
1. Shopify orders/sales → Sheets (SyncWith $4.99 — https://apps.shopify.com/syncwith; Better Reports scheduled Sheets — https://apps.shopify.com/betterreports; native export).
2. Meta/Google/TikTok spend → Sheets (platform CSV, Supermetrics, Coupler — named on Mcfly product page as **customer-paid** pipes).
3. Formula: `blended ROAS or MER = Shopify revenue / total ad spend` (r/shopify 1rpjuk0).
4. Optional: incrementality by **pausing a channel 2 weeks** (r/PPC 1qgb8mg). Commenter’s 40–60% overlap claim is **not** a study.

**Failure modes they write down:**
- Connector cost “adds up” (Community 134251).
- Sheet is “always a week behind” (Community 657805).
- Attributed-only spend **understates** cost (Community 588628).
- No one else trusts the tab.

**Mcfly relationship:**
- `CURRENT_RELIGION` is this pattern **productized**.
- Live product page already says: template → Sheets → CSV → paste; SyncWith optional.
- Gap: they still do the work in Sheets, then **re-enter** into Mcfly. That is a **tax on the workflow they already have**.

`RESEARCH_OPTION`: ingest the same template automatically (Apps Script / Sheets add-on Phase 5 in MASTER_PLAN) **or** pull spend via API so the sheet is optional. Evidence: Better Reports “complimentary report service” + scheduled email is what earned 1,199 reviews. Risk: become SyncWith.

---

## Pattern 2 — Triple Whale as daily operator OS

**Public anatomy:** https://apps.shopify.com/triplewhale-1  
Free: pixel, first/last click, 12-month lookback, 10 users, post-purchase survey.  
Foundation $219: MTA, Sonar, cohorts, SQL, Moby.  
Automate $749: Moby automations/specialists, creative gen.  
External charges may apply. GMV slider on https://www.triplewhale.com/pricing (LIVE) — listing prices are **floors**.

**Workflow `INFERRED` from listing + reviews + TW blog:**
1. Install Triple Pixel (storefront + identity).
2. Connect Meta/Google/TikTok/Klaviyo/Amazon (Works with list).
3. Daily: Moby / dashboards for creative + spend.
4. Weekly: cohorts / subscription (Foundation).
5. Activation: Sonar Send (retention) + Optimize (CAPI passback).

**Public pain:**
- 16% 1★ on 91 reviews.
- AI credit meter (visible 1★ and 5★).
- VAT-in-revenue (visible 1★).
- CS lottery (Juan 5★ vs “impossible to reach” 1★).
- GMV tax (Venon MARKET_REPORT bands; TW site confirms GMV+package pricing).

**Mcfly wedge that is real:** be the **cash/tax-sane overlay** the CFO looks at after TW.  
**Mcfly delusion:** replace TW for a $219-already-paying team.

---

## Pattern 3 — Polar as warehouse + CS

**Public anatomy:** https://apps.shopify.com/polar-analytics  
Core from $750/mo, GMV-based, unlimited users/history/connectors, Polar MCP, Advertising Signals, Klaviyo Audiences. Languages EN/FR/DE. Paris developer.

**Workflow `INFERRED`:**
1. CS-led onboarding (reviews: “onboarding process,” “three months”).
2. 45+ connectors into governed metrics (listing).
3. Pixel for “attribution accuracy.”
4. Optional incrementality (Chicory review).
5. Activation back into Klaviyo + ads.

**Talk Shop 2026** (MARKET_REPORT): Polar = own/customize; TW = act. https://www.letstalkshop.com/blog/triple-whale-vs-polar-analytics

**Mcfly wedge:** $39 vs $750 for the **one** question Polar buries in “acquisition (ad spend, blended CAC, ROAS, MER…)”.  
**Mcfly delusion:** a data team that bought Snowflake-class Polar will uninstall it for a CSV desk.

---

## Pattern 4 — Northbeam as court of appeal + Apex loop

**Public anatomy:** https://www.northbeam.io/ — MTA + incrementality + MMM.  
Apex: https://docs.northbeam.io/docs/northbeam-apex — send Northbeam signal into Meta Custom Attribution; order-level CAPI; North Star = first-time / returning / blended; windows 1/3/7; models clicks-only / C+DV / last / linear / first.

**Pricing:** no official dollar card on homepage. Third parties describe ~$1,500 Starter floor, spend-scaled, no free trial (mbuzz, Botapolis). **Do not quote as fact.**

**Workflow `INFERRED`:**
1. Heavy UTM / pixel calibration (classic NB sales motion; treat as category lore, not measured here).
2. Weekly model as the number that overrules Meta.
3. Apex closes the loop so Meta **optimizes to Northbeam**.

**Mcfly religion clash:** Apex is the opposite of “don’t train Meta on theater.”  
`RESEARCH_OPTION`: if money-max is the goal, **passback of cash MER / new-customer revenue** (not path credit) is a middle path. Evidence: Apex already lets you pick “First-Time” revenue as North Star. Risk: Meta partnership + becoming NB-lite.

---

## Pattern 5 — Split stack: profit app + pixel app (cost-conscious mid)

**Public existence proof:** merchants install both categories at scale.
- Profit: TrueProfit 899, Lifetimely 535, BeProfit 202.
- Pixel: Parkour 191, WeTracked 125, Analyzify 313, Elevar 168.

TrueProfit listing already includes “Real-time sync ad spends” **and** “Marketing Attribution” on Enterprise $200. The split collapses as they grow.

**Workflow:**
1. Parkour/WeTracked/Elevar feeds Meta so campaigns spend.
2. TrueProfit/Lifetimely shows net profit / LTV.
3. Founder uses (2) to cap (1).

**Mcfly hole:** it is neither (1) nor a complete (2).

`RESEARCH_OPTION`: occupy the **governor** slot explicitly: “pixel optional, profit-lite + Total ROAS required.” Partner listing with a pixel app rather than building one.

---

## Pattern 6 — Elevar (or Analyzify / Littledata) as tracking infrastructure

**Elevar listing:** https://apps.shopify.com/gtm-datalayer-by-elevar — $225 / $650 / $1,250 + $/order. Server-side, session enrichment, up to N destinations, “Offline & Subscriptions.”

**Visible workflow:** multi-week punch lists (Old Bones: “cleaning up redundant tags, validating enhanced conversions, confirming subscription tracking, and fixing deduplication across Meta, Google Ads, GA4, and Reddit”).

This is **enterprise even when the brand is not**. Mcfly will never win this RFP. Mcfly can **consume** clean order timestamps from Shopify regardless of who pixels.

---

## Pattern 7 — Finance close: A2X / Taxomate / Finaloop → QB / Xero / NetSuite

**Public:**
- Community 577364 recon pain.
- A2X NetSuite: https://support.a2xaccounting.com/en/articles/7211660-connecting-a2x-to-netsuite
- r/shopify 1h27sj3: Finaloop + Taxomate → QB/Xero as TrueProfit alternative.

**Workflow:**
1. Shopify payout lands in bank.
2. Connector explodes payout into sales / refunds / fees / tax / gift cards.
3. Bookkeeper journals into GL.
4. Ad invoices (Meta/Google) enter as **bills**, often a week late — **cash MER by bank-date ≠ MER by Ads Manager date**.

**Mcfly gap (critical, under-discussed in CURRENT_RELIGION):**
- Period matching “sales ÷ spend for the same days” is **not** how finance books ads (accrual vs cash, prepaid, agency invoices, credit).
- Northbeam Apex docs even expose `Accounting mode: Accrual`.
- A Monday Total ROAS that uses Ads Manager day-spend and Shopify day-sales will **disagree with the P&L** and lose the CFO.

`RESEARCH_OPTION`: dual clocks — **delivery date** (operator) vs **invoice/accrual date** (finance). Evidence: Apex accounting mode; Community recon. Risk: complexity vs “one formula.”

---

## Pattern 8 — Shopify-native marketing reports as the silent competitor

**Official (Help Center snippet + Community 180915 + ShopifyQL):**
- Sales attributed to marketing ≠ total sales. Only UTM / admin marketing.
- Default model last non-direct click; others available.
- 30-day lookback → **historical numbers move**.
- Shop Campaigns have native spend + ROAS — **only for Shop Campaigns**.
- Cost per item → Profit by product; still no ad spend (Community 657805).

**Workflow many teams already run:** dump Admin marketing report into the board deck, argue with Meta, stop.

**Mcfly must beat Shopify-native on one sentence:** “Admin will not add the dollars you paid Meta, Google, TikTok, or the billboard.” That sentence is **true** (Community 134251). It is also **insufficient** if TrueProfit already adds those dollars **and** COGS.

---

## Pattern 9 — Domo / Looker / BigQuery “holistic view”

**Public:**
- Community 134251 started from Looker Studio.
- LinkedIn/analyst posts (e.g. BigQuery GA4+GAds+Meta) discuss blended ROAS SQL and immediately get the overlap question: you cannot sum platform revenues.
- Polar/TW both sell warehouse export stories (TW blog: export to BigQuery/Snowflake/S3; Polar: dedicated Snowflake).

**Workflow:**
1. ELT (Fivetran/Stitch/Supermetrics/Airbyte) → warehouse.
2. Semantic layer (Polar’s pitch; DIY dbt).
3. BI (Looker, Domo, Omni, Hex).
4. A data person on retainer.

**Mcfly:** not a competitor. Could be a **metrics definition** they copy (Total ROAS, BE). That is influence, not revenue — unless Mcfly sells an API (`packages/api-contract` already exists in-repo as a stub).

`RESEARCH_OPTION`: read-only metrics API / MCP (Polar and TrueProfit already advertise MCP). Evidence: those listings. Risk: AI wrapper without a loved desk.

---

## Pattern 10 — Agency Monday pack

**Public ingredients:** SyncWith affiliate sheet (review); Better Reports scheduled email; Polar unlimited users; r/PPC agency Sheets.

**Workflow:**
1. Pull all clients Friday.
2. Slide: spend, sales, blended, vs last week, vs target.
3. Monday standup.
4. Invoice retainer.

**Mcfly `CURRENT_RELIGION` actually fits** if:
- multi-store
- PDF/Slack
- client-safe (no “your pixel is theater” on the slide)

Without those, the agency stays in Sheets.

---

## What mid-market teams will **not** do (publicly visible)

1. **Replace** a $750 Polar with a $39 CSV app. They add, they do not swap.
2. Trust a blended number that **excludes VAT policy**.
3. Wait for a 7-day trial if first screen is blank.
4. Let a rules engine that assumes sales ∝ spend (`allocation.ts`) move six figures.
5. Standardize on Ads Manager ROAS after they’ve been burned (r/PPC 1u81q7r).

---

## Workflow Mcfly should imagine (research, not ship)

A vNext that respects real clocks:

| Clock | Artifact | Data | Religion note |
| --- | --- | --- | --- |
| Daily | Spend vs sales sparkline, no advice | Shopify sales + **synced** spend | `RESEARCH_OPTION` OAuth |
| Weekly | Monday Close: Total ROAS vs BE vs goal; claims-vs-cash | Same + optional platform-claimed revenue **as a claim** | `CURRENT_RELIGION` + gap card |
| Monthly | Contribution: sales − COGS − fees − shipping − ads | Profit-lite | `RESEARCH_OPTION` |
| Close | Export: definitions + source docs for the bookkeeper | CSV/journal lines | not A2X |
| Quarterly | Allocation test window 7/14/28 + optional pause protocol | Heuristic + human | do not pretend MTA |

This is how you **solve many real problems** without becoming Triple Whale.
