# DEEP_DIVE — five apps not fully carded in wave 1

**Date:** 2026-09-09  
**Rule:** live listing facts first. Vendor sites = `VENDOR_CLAIM`. Third-party writeups = `MARKET_REPORT`. Visible reviews only (usually first 3).

Wave 1 stubbed Klar and Report Pundit. Kleio / Recharge / Loop were absent. Cards are expanded in `COMPETITOR_CARDS.md`; this file is the teardown.

The five:

| # | App | Why this wave |
| --- | --- | --- |
| 1 | **Klar Analytics** | EU Polar-class; 0 Shopify reviews; GMV-like net-revenue tax; GDPR |
| 2 | **Report Pundit** | 5.0 / **2,026**; human-builds-the-report; first-50-reviews physics |
| 3 | **Kleio Analytics** | $29 flat; 5.0 / 20; literal TW defections |
| 4 | **Recharge** | Subscription LTV wallet Mcfly listing claims but does not own |
| 5 | **Loop Returns** | Returns/refunds machine that **breaks** marketing ROAS |

---

## 1. Klar Analytics

### Live listing (2026-09-09)

- **URL:** https://apps.shopify.com/klar-analytics
- **Developer:** Klar Insights GmbH · Markstr. 18, Munich, 80802, DE
- **Launched:** December 24, 2023
- **Price on listing:** **Free to install. Additional charges may apply.** Points to https://www.getklar.com/pricing (listing text). Live site is https://getklar.com/pricing.
- **Reviews:** **0.0 / 0** — same empty state as Mcfly, 21 months later.
- **Languages:** English (listing). Site is DE-first in reviews elsewhere.
- **Works with:** Facebook, Google Ads, GA, Klaviyo, Meta, TikTok
- **Job on listing:** marketing + margins + retention in one place; “next-gen Marketing Attribution”; Tracking & Attribution **plus** Business Controlling; onboarded in minutes; **GDPR, data hosted in the EU**
- **Bullets:** MTA + MMM; creative; profitability; retention/cohorts; influencer
- **Data access:** customers (name/email/address), device/geo/IP, staff, products, **orders + returns**, discounts, marketing, **edit store analytics / web pixels**, Shopify Payments, Online Store
- **Rail:** Clarity 4.6/2125 Free · WeTracked 4.8/125 · Parkour 4.9/191 — **identical pixel rail as Mcfly**

### Official site price (LIVE, 2026-09-09)

**URL:** https://getklar.com/pricing

| Plan | Floor | Basis |
| --- | --- | --- |
| Core | **€200**/mo | Last 12 months **net revenue** (after returns and taxes); adjusted every **3 months** (monthly) or 12 months (annual) |
| Core + Attribution | **€400**/mo | Adds 1st-party pixel, MTA, data-driven models, MMM, journey viz, A/B |
| Trial | 14 days **after account is completely set up** | Not a Shopify Billing trial on the card |
| Contract | Monthly cancel **or** annual lock | No setup fee (stated) |
| Users | Unlimited | Stated |
| Hosting | EU, GDPR, **ISO 27001** claimed | `VENDOR_CLAIM` |

Folio3 MARKET_REPORT said “starts at $129/mo” — **stale / do not publish**. LetsMetrix said “usage-based / fully free” because they scraped the Shopify **Free to install** card — **wrong**. External-charge pattern = TW/Polar.

### Off-store review geography (MARKET_REPORT)

https://ecom-tools.de/en/klar-review/ (2026): OMR Reviews 4.8 / 129 (DE); **G2 / Capterra / Trustpilot / Shopify = 0**. Author rating 4.2; notes data delays; Core from €200, Attribution from €400; scales after ~€1.8M annual (MARKET_REPORT band — re-verify).

**`EVIDENCE`:** Klar **chose not to fight the Shopify review game**. They sell outbound / DACH / controlling. 0 App Store reviews after ~21 months is a **strategy**, not a failure like Mcfly’s day-2 empty state — **unless** they wanted store distribution.

### Four-score vs Mcfly

| Score | Klar | Mcfly |
| --- | --- | --- |
| Money | €200–400+ GMV-like | $39 flat |
| Love | Strong on OMR (DE); 0 on Shopify | 0 |
| Ease | CS onboarding; trial after setup | Paste |
| Real | Profit + retention + optional MTA | Spend vs sales only |

**Religion:** suite + pixel on the paid attribution SKU. MER/profit is Core.  
**Mcfly kill shot that is fair:** flat price, no GMV, English App Store honesty.  
**Mcfly kill shot that is cope:** “we replace Klar.” EU brands buying ISO + controlling will not.

**`RESEARCH_OPTION`:** if Mcfly ever wants EU, **Klar is the packaging lesson** (net revenue after returns **and taxes** as the price basis — they at least *say* tax-sane).  
**`RISK`:** copying GMV/net-revenue tax = site hypocrisy.

---

## 2. Report Pundit: Custom Reports

### Live listing (2026-09-09)

- **URL:** https://apps.shopify.com/report-pundit
- **Developer:** Estore Automate · Libby, MT, US
- **Launched:** August 13, 2019
- **Price:** Free ≤ **1,000 lifetime orders**; Basic **$9** (Basic Shopify plan); Grow **$19** (Shopify plan); Advanced **$35** (Advanced). 14-day trial on paid. Priced to **Shopify plan** (same psychology as Better Reports).
- **Reviews:** **5.0 / 2,026** · 98% 5★ · ~1% 1★ (UI %)
- **Job:** 150+ pre-built (sales, **tax**, payout, profit, fulfillment, customer, Markets, POS, inventory); custom columns; metafields; **multi-store and currency**; schedule to Excel/CSV/PDF/Slack/Sheets; **live human builds the report**
- **Works with:** Checkout, cash tracking, GA4, GAds, Meta Ads, POS, ship cost
- **Rail:** TrueProfit 5.0/899 · unnamed profit+ROAS 4.9/76 · SyncWith reports 4.7/32
- **Featured in:** Shopify guides (service businesses; scale)

### Visible reviews (first 3, paraphrase)

| Date | Store | Theme |
| --- | --- | --- |
| 2026-09-03 | Woodshed (US, ~1 yr) | Tried ≥3 reporting apps; only RP could customize ordering metrics; team communicative |
| 2026-09-02 | Sundance Ski (CA, ~2 mo) | Economical; Admin reports could not do restock; chat added fields |
| 2026-08-28 | Cambridge University Press Bookshop (UK, ~2 yr) | Asked for a specific addition; support + reports first rate |

Older visible in search snippets: POS reporting; inventory lag as the rare limitation.

### Why 2,026 reviews (distribution lesson)

This is **Better Reports physics** with a cheaper ladder and a **real free plan**:

1. Free ≤1,000 lifetime orders → review engine (Lifetimely-class, even lower).
2. Human chat **builds the artifact** → dopamine + 5★.
3. Recurring scheduled email/Sheets → they do not have to remember the app.
4. Shopify-plan pricing → bill feels like “part of Shopify.”
5. Tax / payout / Markets / POS — **finance-adjacent jobs Admin cannot do**.

**`CURRENT_RELIGION`:** Mcfly is a desk you open.  
**`RESEARCH_OPTION`:** Mcfly is a **Monday artifact someone else (or a scheduler) delivers**. Evidence: RP + Better Reports (1,199).  
**`RISK`:** become a custom-report shop (labor). RP’s moat **is** that labor.

**Four-score:** Money M (low ARPU, huge volume) · Love H · Ease H (they do it for you) · Real H (Admin holes).

Mcfly should **not** clone Report Pundit. Mcfly should steal **one** mechanic: **human or scheduled close**, not 150 report types.

---

## 3. Kleio Analytics

### Live listing (2026-09-09)

- **URL:** https://apps.shopify.com/kleio
- **Site:** https://getkleio.com/
- **Developer:** Kleio · Klosterport 9, 4., Aarhus C, 8000, DK
- **Launched:** February 19, 2025
- **Price:** **$29/mo** · 14-day trial · “Everything” · unlimited users · **1,000,000 orders in database**
- **Reviews:** **5.0 / 20** · 100% 5★
- **Founder-named listing** (“Hey, Mathias here”)
- **Works with:** AppLovin, GoAffPro, Google Ads, Meta Ads, ShipHero
- **Job:** dashboard; ad-channel acquisition; P&L; LTV by product/variant; product analytics (margins, **return rates**, AOV, discount)
- **Rail:** **same Clarity / WeTracked / Parkour cluster as Mcfly and Klar**

### Visible reviews (paraphrase; do not paste walls)

| Date | Store | Theme |
| --- | --- | --- |
| 2026-08-12 | Trek Light (US, 5 mo) | MCP + Claude; support; **“Kleio made it easy to say goodbye to TripleWhale.”** |
| 2026-08-11 | EMME (US, 8 mo) | “Better than triplewhale, cheaper than triplewhale, It’s literally $29/month.” Founder + support |
| 2026-04-23 | Hummii Snacks (US, ~2 mo) | Daily P&L pulse; MCP into a scheduled daily Claude report |

### Site packaging (`VENDOR_CLAIM`)

https://getkleio.com/ — “Stop overpaying.” Comparison table vs TW $219–$5,099 and Lifetimely $999–$1,999 (those Lifetimely figures **conflict** with the live Shopify $49/$149/$299 card — **do not republish Kleio’s competitor prices as fact**). Deliberately **skips ad attribution** (Digismoothie MARKET_REPORT; Kleio docs).

### Why this card matters more than its N=20

Kleio is the **closest living cousin** to a religion-flexible Mcfly:

| Dimension | Kleio | Mcfly live |
| --- | --- | --- |
| Price | $29 flat | $39 flat |
| Trial | 14-day | 7-day |
| Reviews | 20 × 5★ in ~18 months | 0 in 2 days |
| Spend | Ad integrations (Meta/Google/…) | Paste |
| Job | P&L + LTV + inventory | Total ROAS + BE |
| Attribution | Explicitly refused (MARKET_REPORT) | Explicitly refused |
| AI | MCP, no credit meter in reviews | None |
| Founder voice | On the listing | None |

**`EVIDENCE`:** you can refuse MTA **and** get 5★ if you ship **profit + auto ads + founder replies + $29**.  
**`CURRENT_RELIGION`:** anti-pixel is not the differentiator vs Kleio — **thin job + paste + $39** is.  
**`RISK`:** Kleio is already cheaper, deeper, and collecting the exact TW-defection reviews Mcfly wants.

**Research call:** treat Kleio as the **primary $29–$39 competitor**, not Polar. Polar is a different buyer.

---

## 4. Recharge Subscriptions

### Live listing (2026-09-09)

- **URL:** https://apps.shopify.com/subscription-payments
- **Developer:** 1507 20th St, Santa Monica, CA, US
- **Launched:** October 14, 2014
- **Price:** **$25/mo** (first 50 subscribers, no txn fee on that SKU) · Starter **$99/mo + 1.49% + 19¢** · Plus **$499/mo + 1.34% + 19¢** (scalable) · **60-day** trial on $25 and Starter · **External charges may apply**
- **Reviews:** **4.8 / 3,118** · 89% 5★ · **5% 1★**
- **Works with:** Checkout, customer accounts, POS, Flow, Attentive, **Avalara**, Gorgias, Klaviyo, Stripe, **Triple Whale**
- **Job:** portal, churn prevention, dunning, bundles, loyalty, **retention analytics / cohort benchmarks**
- **Featured in:** retention guides; Flakon stack

### Visible reviews (paraphrase)

| Date | Store | Theme |
| --- | --- | --- |
| 2026-08-11 | Pikko (AU, >1 yr) | Complex platform change; support |
| 2026-08-07 | Munchkin (US, 8 mo) | **Reporting learning curve; no reporting automation** (reviewer); core works; support good |
| 2026-07-15 | Equine America VET (UK, 2 mo) | Essentials + notification support |

### Overlap with analytics spend (why Mcfly should not shrug)

1. **LTV lives here for subscription brands.** Mcfly listing claims LTV/order-history. Recharge already sells cohort LTV, churn, MRR. Stay AI / Skio MARKET_REPORT: retention automation as the LTV lever (https://ecommercefastlane.com/recharge-subscriptions-review/).
2. **Wallet:** take-rate + $99–$499. A $39 MER desk is a rounding error — **or** a “why do I need another analytics login?”  
3. **Works with Triple Whale** — the suite already ingested the subscription graph. Polar/TW listings also list Recharge.
4. **D2C Times MARKET_REPORT** (https://d2c-times.com/retention-engine-or-overreach-reviewing-recharges-2026-playbook/): Recharge Analytics cohort LTV **does not close the loop to ad-platform spend**. That hole is Mcfly-shaped — **if** Mcfly can ingest Recharge MRR + ad spend.  
5. Visible review: reporting is **clunky / not automated**. Same Monday-artifact gap as Mcfly.

**`CURRENT_RELIGION`:** subscriptions are out of scope (single Shopify store, ads-only spend).  
**`RESEARCH_OPTION`:** one line on the desk — “subscription net vs one-time net” + spend — without becoming Recharge. Evidence: Elevar already sells “Offline & Subscriptions” tracking; TW Works-with Recharge.  
**`RISK`:** recurring billing edge cases (failed payment → refund → retry) will destroy a naive sales÷spend.

**Four-score if Mcfly chases Recharge:** Money L (they already pay a take-rate) · Love L · Ease L · Real M (CAC:LTV loop). **Do not become a subscription platform.**

---

## 5. Loop Returns & Exchanges

### Live listing (2026-09-09)

- **URL:** https://apps.shopify.com/loop-returns
- **Developer:** PO Box 16250, Columbus, OH, US (same city lore as TW — coincidence, not a claim)
- **Launched:** May 27, 2021
- **Price:** Checkout+ **Free** (labels US/CA, Return Bars, package protection — volume gates on Loop’s own site) · Essential **$155/mo** · Advanced **$340/mo**
- **Reviews:** **4.6 / 442** · 88% 5★ · **7% 1★** · **Magic summary ON** (≥100 written + ≥4.0)
- **Works with:** Checkout, accounts, POS, Flow, Admin, Attentive, Global-E, Gorgias, Klaviyo, **NetSuite**, ShipHero
- **Job:** automate returns/exchanges; bonus credit / instant exchange; fraud; tracking; “increase LTV”
- **Site:** https://www.loopreturns.com/pricing/ — same $155 / $340 floors; Checkout+ free software + labels

Botapolis MARKET_REPORT (2026-06-04): paid tiers often **annual**; exchange features that retain revenue sit on Advanced; order-tracking a separate ~$99 product. **Re-verify before publishing.**

### Visible reviews (paraphrase)

| Date | Store | Theme |
| --- | --- | --- |
| 2026-06-09 | United By Blue (US, >3 yr) | Login/password lockout; customers upset (1★-shaped pain; Loop replied) |
| 2026-09-04 | Schneiders (US, 7 mo) | Partner / setup / CS |
| 2026-08-21 | Wms&Co (US, ~1 mo) | Same password issue; support reset next day |

### Why Loop is an analytics competitor even though it is not

Loop does not sell ROAS. It **changes the cash that ROAS claims**:

- Exchanges and store credit **are not cash refunds** but often hit Shopify sales/returns metrics (Community 301853, 306065, 637409).
- Instant exchange / bonus credit **keeps GMV** that Ads Manager already counted as a sale.
- NetSuite + Klaviyo + Global-E: international + GL + retention — the **same objects** finance uses to reject a MER number.
- 7% 1★ (login, edge-case returns) is a reminder that **ops apps eat 1-stars** when they touch customers.

**`EVIDENCE`:** a cash desk that ignores Loop-class outcomes will **disagree with both Ads Manager and the GL**.  
**`RESEARCH_OPTION`:** ingest Shopify refund **and** return/exchange events as separate lines (cash vs credit vs exchange).  
**`RISK`:** Loop API surface; apparel-only complexity.

---

## 6. Head-to-head (Mcfly implications)

| App | Buyer | Wallet | Reviews | Mcfly relation |
| --- | --- | --- | --- | --- |
| Klar | EU CMO/CFO | Growth €200+ | 0 on Shopify | Packaging (tax-sane GMV) + proof that 0 reviews ≠ death **if outbound** |
| Report Pundit | Ops / finance-adjacent | Shopify-plan $0–$35 | 2,026 | Steal scheduled/human artifact; do not clone reports |
| Kleio | Founder-operator | Profit $29 | 20 | **Direct competitor.** They already ran the “anti-TW, flat, profit” play. |
| Recharge | Retention | Take-rate + $99–$499 | 3,118 | Adjacent LTV; do not clone; optional subscription split |
| Loop | CX / ops | $155–$340 | 442 | Refund/exchange definitions or lose trust |

---

## 7. Religion

| ID | Topic | CURRENT | OPTION | EVIDENCE | RISK | Call |
| --- | --- | --- | --- | --- | --- | --- |
| K1 | Competitor set | TW/Polar/NB | Add **Kleio** as peer | Kleio 5★ TW goodbye | Obsess | **Yes** |
| K2 | Review engine | Serious paid only | RP-style free cap **or** 14-day + human close | RP 2026; Lifetimely | Freeloaders | See R4 |
| K3 | LTV claim | Listing claims | Either ship order-history **or** partner Recharge/RCI | Recharge 3118; RCI 5.0/14 | Lie on listing | Align claim to code |
| K4 | Returns | “after returns” | Split refund / exchange / credit | Loop + Community 637409 | Scope | **Definitions first** |
| K5 | EU suite | Ignore | Do not clone Klar; steal tax-in-price language | getklar.com/pricing | GMV hypocrisy | Language only |

---

*Listing numbers fetched 2026-09-09. Re-fetch before site copy.*
