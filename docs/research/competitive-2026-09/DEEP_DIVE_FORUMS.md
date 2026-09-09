# DEEP_DIVE — Shopify Community + public forums

**Date:** 2026-09-09  
**Wave:** deeper (append; does not replace `MERCHANT_PROBLEMS.md` or `NICHE_MER.md`)  
**Rule:** cite URLs; **paraphrase**. No invented consensus. Star counts and view counts are page-stated at fetch time only.

Religion tags apply to *Mcfly’s possible response*, not to the poster.

---

## 0. What this wave adds

Session 1 already mined five Community threads and a Reddit snippet set. This file goes **deeper on the same aisle** and adds threads that were only titles before:

| Cluster | What people actually argue | Why Mcfly should care |
| --- | --- | --- |
| MER / blended vs platform ROAS | Admin has sales, not spend. Platforms over-claim. Sheets win by default. | `CURRENT_RELIGION` job is real; unpaid. |
| Triple Whale love/hate | Fighter-jet vs bicycle. Price + bloat. VAT. Support lottery. | Hate is **not** “pixels are theater.” Hate is **price / CS / tax / bloat**. |
| Profit apps | Total spend vs attributed spend. Historical COGS lock. Spreadsheet week-lag. | Review gravity sits here, not in MER poetry. |
| Ads vs till | Meta scaled the wrong campaigns. Shopify last-click ≠ Ads Manager. | Claims-vs-cash is the screenshot religion. |
| Returns / lookback | Attributed sales **move**. Returns ≠ refunds. Ads never retract. | Period matching is a trust bomb (see `DEEP_DIVE_RETURNS_LTV_SUBS.md`). |

---

## 1. Community: the MER / spend-next-to-sales problem (still unowned)

### 1.1 Multi-channel PPC reporting — still no consensus tool

**URL:** https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4  
**Fetched:** 2026-09-09 (session 1 + re-read this wave)

**Paraphrase:** A merchant (Ed) wants one ROAS view across Google / Facebook / Microsoft. Looker Studio connectors “add up.” Staff/community: Shopify “Sales attributed to marketing” exists; **Shopify does not ingest ad spend**. “You will need a third-party app.” Thread stays open. Page-stated ~111 views.

**`EVIDENCE`:** Admin will not do Mcfly’s headline job.  
**`CURRENT_RELIGION`:** paste-CSV cash desk.  
**`RESEARCH_OPTION`:** OAuth spend so the third-party app is not a weekly labor tax.  
**`RISK`:** TrueProfit already syncs spend on a 899-review listing.

### 1.2 Profit tracking as the *real* Community ask

**URL:** https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805  
**Page-stated:** 335 views / 18 likes / 11 users (session 1)

**Paraphrase (do not quote walls of text):**
- Native Profit-by-product works **if** Cost per item is filled.
- Still missing: ad spend, payment fees, shipping labels, app subscriptions.
- Consensus line (community builder): **revenue is native; true net profit has to be assembled.**
- Recipe: contribution margin first; layer **blended** ad spend at day/channel; **do not** pretend every order has a perfect CAC.
- Historical COGS, late carrier adjustments, refunds reopening orders, platform disagreement.
- Spreadsheets “always a week behind.”

**`EVIDENCE`:** The Community’s loved job is **assembled profit**, not “Total ROAS” as a brand name.  
**`RESEARCH_OPTION` (R12):** if App Store is the channel, profit-lite is the job; MER is the method.  
**`RISK`:** collide with TrueProfit / Lifetimely / BeProfit / Kleio.

### 1.3 Spreadsheet → profit-app switch, with Triple Whale as the overkill

**URL:** https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628  
**Also:** posts `/3` and `/9` on the same thread.

**Paraphrase:**
- OP is on Sheets **and** paying Triple Whale. Wants **net profit per order** without 30 minutes/day in Sheets. Store size cited ~$15–20k/month.
- Warning already in session 1: pull **TOTAL** ad spend, not attributed-only (understates cost).
- New this wave: replies treat TW as a **fighter jet for $50k+/mo ad spend + MTA**. At $15–20k/mo GMV they say you are paying for attribution you do not need.
- Accuracy checklist that keeps recurring (same thread + 361631 + 581032):
  1. Timestamp COGS at order time (supplier cost changes must not rewrite history).
  2. Use **total** period ad spend, not tracked-order spend.
  3. Profit by order **and** SKU, not only store-day.
  4. Export / sanity-check the math.

**`EVIDENCE`:** Community TW hate at this size is **overkill + price**, not “MTA is a lie.”  
**`CURRENT_RELIGION`:** anti-pixel sermon would miss the actual complaint.  
**`RESEARCH_OPTION`:** sell the bicycle (cash + total spend + COGS lock), not a lecture about pixels.  
**`RISK`:** ClearProfit / ProfitLossDash / Kleio already occupy “cheap bicycle.” Some of those posters look vendor-adjacent — treat product plugs as `VENDOR_CLAIM`.

### 1.4 P&L app shopping list (crowded bicycle aisle)

**URL:** https://community.shopify.com/t/app-for-p-l-analyse/361631/7

**Paraphrase:** Lifetimely = LTV/cohorts. BeProfit = custom reports. TrueProfit = real-time P&L. ClearProfit self-plug as free unlimited. Webgility / Cin7 if you need tax filings + QB. Recurring caution: **historical COGS lock** and **total vs attributed spend**.

**URL:** https://community.shopify.com/t/tracking-app/581032/14

**Paraphrase:** BeProfit, TrueProfit, AutoDS, Mantle, Bloom, ProfitLossDash, Lifetimely, ClearProfit all named. Same three-item accuracy test. ProfitLossDash pitch: **flat rate, historical COGS lock, daily P&L**.

**`EVIDENCE`:** The Community does not ask for “cash MER.” It asks for a **daily pocket number**. Mcfly’s listing language is one abstraction above the ask.

### 1.5 Metrics-in-isolation → suite recommendation

**URL:** https://community.shopify.com/t/i-stopped-looking-at-shopify-metrics-one-by-one/653041/5

**Paraphrase:** Someone recommends Triple Whale, Lifetimely, or GoProfit to connect metrics. Another poster warns that more apps add complexity. No consensus.

**`EVIDENCE`:** Community staff/power-users still **name TW first** when the problem is “too many Shopify metrics.” Mcfly is not in that consideration set.

---

## 2. Community: ads vs till, lookback, returns

### 2.1 Attributed marketing numbers **move**

**URL:** https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915  
(session 1)

**Paraphrase:** Q3 numbers changed when re-pulled in Q4. Community: **30-day attribution lookback**.

**`EVIDENCE`:** Any Mcfly “claims-vs-cash” card that pastes Shopify *attributed* sales will **drift**. Till must be a **stable sales definition** (total / net after returns), not Admin’s marketing report.

### 2.2 Returns metric ≠ physical returns

**URL:** https://community.shopify.com/t/returns-metric-in-analytics-is-misleading-should-reflect-actual-returns-not-all-refund-events/637409

**Paraphrase:** Merchant says Shopify “Returns” counts every refund event, including pre-shipment size swaps. Reported return rate ~25% vs stated physical ~3%. `sales_reversals` looks like a rename, not a split. No queryable Returns table in ShopifyQL (poster claim). Seven-day example: $0 physical returns, Shopify showed −$572 from pre-fulfillment removals.

**`EVIDENCE`:** “Shopify Total Sales after returns” on the SAMPLE desk is **underspecified**. Finance will ask: refund events, physical returns, or cash refunded?  
**`RESEARCH_OPTION`:** publish the sales definition (see `DEEP_DIVE_RETURNS_LTV_SUBS.md`).  
**`RISK`:** support tickets forever; wrong default = TW-class 1-star.

### 2.3 Return-in-progress vs completed refund (API / analytics)

**URL:** https://community.shopify.com/t/need-help-with-shopify-returns-api-and-analytics/587957/2

**Paraphrase:** Marking “return in progress” used to hit analytics; now only a **completed refund/return** does. $0-refund workaround died when Shopify required a real balance change. One reply: pipe webhooks to your own DB because native reports keep moving.

**`EVIDENCE`:** Lag between customer intent and cash is a **first-class product problem**, not an edge case.

### 2.4 New returns system vs daily sales / tax

**URL:** https://community.shopify.com/t/anyone-else-notice-that-the-new-returns-system-breaks-all-of-shopify-sales-data/301853/54

**Paraphrase:** Creating a return (even for an exchange) deducted daily sales before cash moved. One merchant: this hits **revenues before cashflow** and numbers reported to **tax authorities**. Linked vs unlinked Loop-class portals produce different Shopify tax/sales stories.

**URL:** https://community.shopify.com/t/how-to-handle-orders-returned-to-sender/306065/1

**Paraphrase:** RTS / unclaimed parcels: merchant used to restock + reship on a 100% discount duplicate. After a platform change, creating a return deducts sales and flags “refund owed” even when ~90% are **reshipped, not refunded**.

### 2.5 Ads do not take the conversion back

**URL:** https://community.shopify.com/t/retract-or-modify-conversion-for-google-ads-facebook-when-customer-returns-order/199943

**Paraphrase:** Community advice: Google “negative conversions” / conversion upload. Meta/Google will **not** automatically un-count a purchase when Shopify refunds. You must engineer the reversal.

**`EVIDENCE`:** Ads Manager ROAS is structurally **optimistic on returned goods**. Till-vs-ads is not just iOS; it is **refund lag**.  
**`CURRENT_RELIGION`:** blended sales÷spend (if sales are net of refunds) is the honest weekly check.  
**`RESEARCH_OPTION`:** show **gross sales, refunds, net** as three lines so the lag is visible.

---

## 3. Triple Whale — love, hate, and what the hate is *not*

### 3.1 On the App Store (already in `REVIEW_THEMES.md`; restated)

**URL:** https://apps.shopify.com/triplewhale-1  
**Live this corpus:** 4.1 / 91 · 79% 5★ · **16% 1★**

Visible 1★ themes (paraphrase): AI credits not warned; CS unreachable; **VAT included in revenue** (Kove Footwear, NL).  
Visible 5★: named CS (Juan); “world class.”

### 3.2 Official TW VAT contradiction (new this wave)

**URL:** https://kb.triplewhale.com/en/articles/10201911-is-vat-international-sales-tax-included-in-the-sales-metric  
**Fetched:** 2026-09-09. Article dated on page **2026-07-26**.

**Paraphrase:** Help Center: “VAT is **not** included in our Sales metric at this time.” Workaround: add VAT as a **custom variable expense**.

**URL:** https://triplewhale.readme.io/docs/total-sales  
**URL:** https://triplewhale.readme.io/docs/order-revenue  

**Paraphrase:** Public docs define **Order Revenue** as Gross + Shipping + Taxes − Discounts (before refunds). **Total Sales** adds refunded sales/shipping/tax deductions — and **includes Taxes** in the addends.

**`EVIDENCE`:** Even the vendor’s public corpus disagrees with itself (KB “VAT not in Sales” vs docs that **add taxes** into Order Revenue / Total Sales vs a NL 1★ that says VAT is in revenue). This is the **trust-kill pattern**: merchants cannot tell which “Sales” they are looking at.  
**`RESEARCH_OPTION`:** one labeled definition, market-default (ex-VAT in EU/UK/AU, tax-in as a toggle).  
**`RISK`:** get the default wrong for US merchants who think “Total Sales” = Shopify Total Sales (usually tax-in).

### 3.3 Community TW = overkill bicycle problem

Covered in 588628 above. Not “pixels bad.” **Price + MTA they do not use.**

### 3.4 Reddit TW alternatives (PUBLIC_SNIPPET; some threads thin)

**URL:** https://www.reddit.com/r/PPC/comments/1ohxwk6/best_triple_whale_alternative/  
**Paraphrase:** Switchers name Venon (cheaper, better support — commenter), Northbeam (MTA, complex mix), Polar (Shopify-native, “lighter”), TrueProfit (support replies, Meta/Google). Bloated dashboard complaint.

**URL:** https://www.reddit.com/r/FacebookAds/comments/1c6am9l/any_good_alternatives_to_triple_whale/  
**Paraphrase:** Two years on TW; bugs; expensive for value. TrueProfit named as cheaper. Vendor replies (ThoughtMetric, Aimerce, Admetrics) — treat as `VENDOR_CLAIM`.

**URL:** https://www.reddit.com/r/triplewhale/comments/1qs7n0s/attribution_app_alternatives/  
**Paraphrase:** “Crazy expensive.” B2B+DTC on one store; B2B tagged; paid ads hit both; wants D2C-only ROAS. **0 comments** at fetch snippet — the pain is real, the thread is not a study.

**URL:** https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/  
(session 1) Operator scaled the wrong campaigns for months.

**URL:** https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/  
(session 1) Agency at $200k+/mo: **ignore platform attribution**; Sheets blended ROAS; 2-week Meta pause tests. Overlap 40–60% is a **commenter claim**.

### 3.5 Practitioner / vendor-adjacent 2026 writeups (MARKET_REPORT)

These are **not** Community. Use as packaging lore, not census.

| Source | Claim (paraphrase) | Tag |
| --- | --- | --- |
| https://eightx.co/blog/compare/reviews/triple-whale-for-ecommerce-review | TW is a marketing-performance layer. Keep Shopify + accounting as books. Pixel is decision-support, not audit. GMV climb; one dated operator $329→$549 mid-contract. | MARKET_REPORT |
| https://d2c-times.com/triple-whales-attribution-os-the-honest-2026-scorecard/ | Blank: blended MER is the number Maxx pointed at. Survey layer vs Meta ROAS anecdote (Caraway / Barrientos — vendor-adjacent quote). | VENDOR_ADJACENT |
| https://www.newmotionit.com/blog/shopify/setup-triple-whale-shopify-dtc-profit-tracking-attribution | MER = revenue ÷ total ad spend; set target from gross margin (55% → 1.8×, 35% → 2.9×). TW Summary as daily MER. | MARKET_REPORT / agency SOP |
| https://d2c-times.com/polar-analytics-vs-triplewhale-in-2026-which-dtc-intelligence-layer-wins/ | Agency quote (Kelp / Teel): “TW is where your media buyer lives. Polar is where your CFO and CMO finally agree.” Some clients run **both**. | MARKET_REPORT |

**Brutal read for Mcfly:** the *loved* TW feature in 2026 writeups is often **the same blended MER Mcfly claims as identity**. TW just **wraps it in a daily OS**. Hate is GMV tax, AI meters, VAT ambiguity, CS — not the MER tile.

**`CURRENT_RELIGION` kill shot that is cope:** “we replace TW.”  
**`RESEARCH_OPTION` kill shot that is fair:** price honesty + tax definition + not an OS. Kleio’s 5★ “goodbye TripleWhale” at $29 is the live existence proof (`DEEP_DIVE_FIVE_APPS.md`).

---

## 4. Reddit: ads vs till (operator voice)

Already logged in `RESEARCH_LOG.md` session 3. This wave adds the **decision-rights** reading:

| Thread | Who talks | What they decide |
| --- | --- | --- |
| r/shopify 1rpjuk0 | Founder / operator | Meta ≠ Shopify “will never sync.” Weekly sheet of **total spend vs total Shopify revenue** = blended. |
| r/PPC 1r2pvgy | D2C founder | Scale on Shopify revenue; Meta directional. Arithmetic example (commenter): if Meta $200k / Shopify $150k, “true ROAS 25% lower.” |
| r/PPC 1pqv5kh | Media | Platforms for **optimization**; backend / blended MER as **reality check**. |
| r/PPC 1qgb8mg | Agency | Agency **owns the scoreboard** (Sheets). Brand **owns the pause-test** if spend is large. |
| r/shopify 1jpb8cy | Founder | TW / Kendall “pretty expensive.” |
| r/shopify 1pzy8iv | Founder | Profit = orders + COGS + ads + fees. TrueProfit ~$35 named. |
| r/dropshipping 1s3mx43 | EU operator | TrueProfit “doesn’t account for VAT properly”; Excel; commenter says VAT can be **activated** in TP if you ask CS. |

**Pattern:** the person who **buys** the suite is often the media buyer or founder-operator. The person who **kills** the suite is finance (VAT) or the founder who only wanted profit (Community 588628).

---

## 5. Profit-app forum physics (hate/love, paraphrased)

| Theme | Where | Implication |
| --- | --- | --- |
| Attributed-only spend inflates profit | Community 588628, 361631, 581032 | Mcfly must never “match” spend to tracked orders as the default MER. |
| Historical COGS rewrite | same | Typed margin % is actually *safer* than a bad COGS import — until assembled + locked. |
| Success tax / overage | r/dropshipping 1taxn7g (NeoProfit founder: TP “over $100/mo” on overage — `VENDOR_CLAIM`) | Flat $39 is a real wedge **if** the job is complete. |
| EU VAT | r/dropshipping 1s3mx43; TW 1★; TP 1★ in sibling PR #5 | International is not a locale pack; it is **trust**. |
| Spreadsheet week-lag | Community 657805 | Push artifact (email) beats another login. |

---

## 6. What the forums do **not** say (do not invent)

- No public thread found that says “I want a $39 anti-pixel Total ROAS desk.”
- No Community consensus that Triple Whale’s *formula* is inverted. The MER-as-spend÷revenue claim in `docs/COMPETITORS.md` remains **re-verify in a live TW UI** before attacking.
- ClearProfit / ProfitLossDash / NeoProfit plugs may be founders. Frequency ≠ adoption.
- View counts are not WTP.

---

## 7. Religion card from this file

| ID | Topic | CURRENT | OPTION | EVIDENCE | RISK | Call |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | Job name | Total ROAS / cash MER | “Did I make money after ads + costs” | 657805, 588628, 1pzy8iv | TP collision | **OPTION if App Store** |
| F2 | TW attack line | Pixels/MTA theater | Price + tax + bloat + CS | 588628; TW 16% 1★; Kleio 5★ | Brand becomes “cheap TW” | Attack **those**, not MTA |
| F3 | Spend | Paste | Total spend auto | Community accuracy checklists | Connector zoo | **Do total; OAuth** |
| F4 | Sales def | Underspecified | Gross / refunds / net + tax toggle | 637409; 180915; TW KB vs docs | Support | **Do definitions** |
| F5 | Forum GTM | Sermon | Bicycle for $15–50k/mo stores that already hate TW | 588628 | Small ARPU | **This is the review engine** |

---

*Sources dated 2026-09-09. Re-fetch before publishing any review count or price on mcflyads.com.*
