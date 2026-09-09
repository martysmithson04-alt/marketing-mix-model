# DEEP_DIVE — Returns / refunds / lag, LTV, subscription overlap

**Date:** 2026-09-09  
**Wave:** deeper. Complements `NICHE_MER.md` § definitions and `DEEP_DIVE_FIVE_APPS.md` (Loop, Recharge).

Mcfly live listing: “store sales,” SAMPLE on site says “Shopify Total Sales after returns,” listing also claims **LTV / order-history**. Repo `APP_FEATURES.md` still treats LTV as later. This file is the **trust physics** behind those three words.

---

## 1. Three clocks that refuse to be one formula

| Clock | What moves | Public home | Why MER breaks |
| --- | --- | --- | --- |
| **Ad conversion** | Pixel / CAPI / Ads Manager | Community 199943 | Platforms rarely auto-retract on refund |
| **Shopify analytics** | Refund events, returns, exchanges, order edits | 637409, 587957, 301853, 306065, 180915 | “Returns” ≠ physical returns; lookback moves attributed sales |
| **Cash / GL** | Payouts, store credit, Loop exchanges, Recharge retries | Community 577364; A2X; Loop; Recharge | Credit ≠ cash; failed payment ≠ lost subscriber instantly |

`CURRENT_RELIGION`: `sales ÷ spend` for the **same calendar days**.  
`EVIDENCE`: those three clocks are not the same days.  
`RESEARCH_OPTION`: show **gross / refunds / net** and optionally a **lag window** (7/14/30) rather than one heroic ratio.  
`RISK`: “one formula” marketing dies. Honesty rises.

Northbeam Apex docs already expose `Accounting mode: Accrual` (session 4). Polar/Klar sell “order time lags” as a **feature** (Klar pricing page lists Order Time Lags). The category knows this. Mcfly’s SAMPLE does not.

---

## 2. Returns vs refunds vs exchanges (Admin is not a cash desk)

### 2.1 Refund events inflate “return rate”

**URL:** https://community.shopify.com/t/returns-metric-in-analytics-is-misleading-should-reflect-actual-returns-not-all-refund-events/637409

**Paraphrase:** Pre-shipment size swaps and cancellations counted as returns. Poster: ~25% Shopify return rate vs ~3% physical. `sales_reversals` felt like a rename. ShopifyQL has no clean Returns table (poster).

**Implication for Mcfly:** if you pull “returns” from Analytics, apparel brands will call you a liar. If you pull **cash refunded**, you will **miss** Loop exchanges that kept revenue but swapped SKUs (margin change, not cash out).

### 2.2 Status ≠ money

**URL:** https://community.shopify.com/t/need-help-with-shopify-returns-api-and-analytics/587957/2

**Paraphrase:** “Return in progress” no longer deducts sales; completed refund does. $0-refund hack died.

**Implication:** a daily MER that updates on **intent** will fight finance; a daily MER that updates only on **cash** will fight the operator who already paused the SKU.

### 2.3 Exchanges deduct sales before cash (or without cash)

**URL:** https://community.shopify.com/t/anyone-else-notice-that-the-new-returns-system-breaks-all-of-shopify-sales-data/301853/54  
**URL:** https://community.shopify.com/t/how-to-handle-orders-returned-to-sender/306065/1

**Paraphrase:** Creating a return for an exchange or RTS reship marked “refund owed” and moved daily sales / tax reporting. One merchant: **tax-authority** numbers moved before cashflow.

### 2.4 Ads stay optimistic

**URL:** https://community.shopify.com/t/retract-or-modify-conversion-for-google-ads-facebook-when-customer-returns-order/199943

**Paraphrase:** Google negative conversions / upload. Not automatic. Meta similar.

**`EVIDENCE`:** platform ROAS is **gross-of-returns** unless someone engineers reversals. Blended **net** sales ÷ spend will look “worse” than Ads Manager **and that is correct**.  
**`RESEARCH_OPTION`:** claims-vs-cash should include a **returns haircut** line: “their conversions still include refunded orders.”  
**`RISK`:** need refund timestamps + original conversion time.

### 2.5 Loop as the industrial version of the same problem

See `DEEP_DIVE_FIVE_APPS.md` §5. Loop 4.6/442, $155/$340. Instant exchange / bonus credit **retains GMV** that ads already counted. Works with NetSuite + Global-E.

Kleio listing already surfaces **return rates** in product analytics. Profit apps that ignore return rates will lose apparel.

---

## 3. Lookback lag is a cousin of refund lag

**URL:** https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915

30-day Admin lookback: last month’s attributed sales **are not a closed book**.

Shopify App Store Ads official FAQ has the same shape for **developers**: revenue attributed to **impression date**, metrics keep growing; refunds **not** in their revenue number; wait ~60 days.  
**URL:** https://shopify.dev/docs/apps/launch/marketing/advertising/faq

**Irony:** Shopify tells **app developers** that SaaS ROAS charts must be read with lag — then merchants use Shopify marketing reports as if they were cash.

**`RESEARCH_OPTION`:** Mcfly Monday Close stamped **“books closed for this window: net sales as of {as_of}; refunds after as_of will move next week.”**  
`CURRENT_RELIGION` “one formula” without an as-of is how you get Community 180915 energy aimed at *you*.

---

## 4. LTV — three products pretending to be one word

| Product | What “LTV” means | Live proof | Price signal |
| --- | --- | --- | --- |
| **Order-history depth** | Sum of a customer’s orders so far | Mcfly listing claim; Lifetimely name | Listing extra / Lifetimely $49+ |
| **Cohort LTV** | Revenue by acquire-week over 3/6/12 mo | Lifetimely 4.9/535; Repeat Customer Insights 5.0/14 from $59 | Real WTP |
| **Predicted / subscription LTV** | Remaining tenure × margin | Recharge analytics; Stay AI MARKET_REPORT | Inside take-rate tools |

### 4.1 Repeat Customer Insights (supporting card, not one of the five)

- **URL:** https://apps.shopify.com/repeat-customer-insights
- **Live:** 5.0 / **14** · $59 / $99 / $249 · 14-day · Little Stream Software · launched 2016 (third-party; listing “From $59”)
- **Job:** RFM, cohorts (12 mo on Entrepreneur), product → LTV, channel quality, Klaviyo tags
- **Visible review (Pacas, 2023):** cohorts + LTV, easy export

**`EVIDENCE`:** a 10-year-old **paid** LTV app has **14 reviews**. LTV does **not** print App Store velocity the way profit or pixels do. Lifetimely’s 535 is **profit + free tier + LTV**, not LTV alone.

### 4.2 Lifetimely still owns the word

Already carded. This wave only adds: Mcfly claiming “Paid extras: LTV” next to 0 reviews and a 2-day-old app is a **listing-integrity risk** (already in SYNTHESIS §5). Forums do not ask Mcfly for LTV. They ask Lifetimely.

### 4.3 CAC:LTV without refunds is fanfic

If LTV uses **gross** orders and CAC uses **platform** spend, apparel + EU VAT + Loop credit will produce a beautiful ratio that finance will torch.

**`RESEARCH_OPTION`:** LTV:CAC only after (a) net sales definition, (b) total spend, (c) cohort window labeled.  
**`CURRENT_RELIGION`:** do not ship a vanity LTV tile to decorate the listing.

---

## 5. Subscription apps overlap with analytics spend

### 5.1 Recharge is the default graph

Live: https://apps.shopify.com/subscription-payments — 4.8 / **3,118** · $25 / $99+1.49% / $499+1.34% · 60-day trial · Works with **Triple Whale** + Avalara.

Visible 2026 review (Munchkin): reporting has a learning curve; **no reporting automation**.

MARKET_REPORT (D2C Times 2026): Recharge cohort LTV **does not join ad-platform spend**. That join is the only Mcfly-shaped hole.

### 5.2 What subscription does to MER

| Event | Ads Manager | Naive sales÷spend | Cash |
| --- | --- | --- | --- |
| First prepaid month | Conversion | Sale | Cash in |
| Month 2–N recurring | Often **not** a new purchase conversion | Sale if you count Shopify orders | Cash in |
| Failed payment + dunning | Nothing | Missing sale | No cash |
| Cancel mid-cycle + refund | Original conversion remains | Refund lag | Cash out |
| Swap / skip | Nothing | Noise | Usually keep cash |

**`EVIDENCE`:** blended MER on a subscription brand **without** splitting first-order vs recurring will **overstate** media efficiency (recurring is not ad-caused in the same week). Polar/TW already sell new-vs-returning. Northbeam Apex North Star includes first-time / returning / blended.

**`CURRENT_RELIGION`:** ads-only spend vs total sales — **wrong** for Recharge brands if total sales include replenishment the ads did not buy this week.  
**`RESEARCH_OPTION`:** optional split: new-customer sales vs returning/subscription sales in the numerator (still no MTA). Evidence: Apex first-time North Star; r/PPC new/returning daily table (1qgb8mg).  
**`RISK`:** Shopify customer.new vs Recharge subscriber identity will disagree.

### 5.3 Stay / Skio (not deep-carded; pointer)

Ecommerce Fastlane MARKET_REPORT 2026: Stay AI wins AI retention / LTV optimization; Skio wins subscriber UX. Recharge wins infrastructure + Klaviyo.  
**URL:** https://ecommercefastlane.com/recharge-subscriptions-review/

Do not quote their dollar tables without a live listing fetch. Mention only as **wallet competition**: retention spend crowds out “another analytics app.”

### 5.4 Analytics apps already in the subscription graph

- TW listing Works-with: Recharge (wave 1).
- Elevar: “Offline & Subscriptions.”
- Lifetimely / TrueProfit: LTV tiles.
- Kleio: LTV by product.

Mcfly is late to a **solved-enough** noun.

---

## 6. Worked example (illustrative arithmetic, not a merchant)

Suppose week 1: $10,000 spend, $40,000 Shopify total sales, $8,000 of those later refunded in week 3, $6,000 of week-1 sales were Recharge recurrences, Ads Manager claimed $52,000.

| Definition | Ratio | Who likes it |
| --- | --- | --- |
| Ads Manager ROAS | 5.2× | Media buyer |
| Mcfly-style total sales ÷ spend (week 1, no as-of) | 4.0× | Founder Monday |
| Net after week-3 refunds ÷ spend | 3.2× | Finance |
| New-customer sales only ÷ spend | 3.4× before refunds / 2.6× after | Honest CAC |
| Recurring included as if ads did it | 4.0× | Ego |

**Do not publish this table as a case study.** It is a **definition menu**. The product fight is **which row is default**.

---

## 7. Religion

| ID | Topic | CURRENT | OPTION | EVIDENCE | RISK | Call |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | One ratio | Sales÷spend | Gross / refunds / net + as-of | 637409, 180915 | Copy complexity | **OPTION** |
| T2 | Returns | “After returns” | Refund vs exchange vs credit | Loop; 301853 | Scope | Definitions |
| T3 | LTV | Listing extra | Ship net cohort **or** remove claim | Lifetimely 535; RCI 14 | Integrity | Align |
| T4 | Subs | Ignore | New vs returning numerator | Recharge; Apex first-time | Identity mess | Split later |
| T5 | Ad retract | Ignore | Show “platforms still count refunds” | 199943 | Need timestamps | Claims card |

The bends that raise four scores: **T1, T3, T5**.  
T4 is real for a subset (subscription CPG) and can wait.  
T2 is mandatory the moment an EU/apparel design partner exists.

---

*Community URLs fetched/re-used 2026-09-09. No invented refund rates.*
