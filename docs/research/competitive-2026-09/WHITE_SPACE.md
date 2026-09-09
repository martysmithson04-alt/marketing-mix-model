# Shopify App Store white space — 2026-09

**Lane:** PARALLEL ENTERPRISE research (underserved store problems + wedge vs platform).  
**Companions:** [`MARKET_STRUCTURE.md`](./MARKET_STRUCTURE.md), [`MONETIZATION_PATTERNS.md`](./MONETIZATION_PATTERNS.md).  
**Does not amend** [`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) or [`docs/COMPETITORS.md`](../../COMPETITORS.md).

**Tag legend:** **CURRENT_RELIGION** = locked Mcfly wedge. **RESEARCH_OPTION** = observed gap, not a roadmap item. **No invented TAM, lift %, or install counts.**

---

## 1. How to read “white space” on this store

Three different empties get confused:

| Empty | What it means | Trap |
| --- | --- | --- |
| **Taxonomy empty** | Few apps in a Shopify tag (Applora “least crowded”) | Often **dead demand** (NFTs, leftover “- Other” buckets) |
| **Keyword crowded** | Many apps bidding the same search phrase | “True profit,” “ROAS,” “page builder” — **word** is saturated |
| **Job underserved** | Merchants still assemble the answer in Sheets / three tabs | The job can be crowded **and** unsolved |

Mcfly’s locked job sits in the third column: **money out vs Shopify in, break-even, allocate** — a job the suites **tile** and the profit apps **approximate**, but do not own as religion.

---

## 2. Where the directory is crowded (crawl, labeled)

[Applora](https://applora.ai/appstore), week ending **2026-09-06** (independent public crawl, not Shopify):

**Most crowded tags they published on the snapshot page** (their list started at rank 2 in the scrape; rank 1 was not visible in the fetched HTML):

| Tag (Applora) | Apps (their count) |
| --- | --- |
| Inventory sync | 614 |
| Inventory optimization | 603 |
| Delivery and pickup | 591 |
| Workflow automation | 547 |
| Cart customization | 528 |
| Shipping rates | 523 |
| Custom product apps | 496 |
| Content apps | 496 |

**Least crowded tags they published:**

| Tag (Applora) | Apps |
| --- | --- |
| NFTs and tokengating | 12 |
| Returns and warranty - Other | 38 |
| Internationalization - Other | 41 |
| Digital goods and services - Other | 42 |
| Selling in person - Other | 47 |
| Gift cards | 54 |
| Gift wrap and messages | 55 |
| Giveaways and contests | 63 |

**Keyword competition** on the same snapshot: several queries hit their **10,000** cap (page builder, free shipping progress bar, landing pages, collection pages, free shipping bar, cart page, FAQ page, page speed). Those are **storefront** wars, not cash-desk wars.

**RESEARCH_OPTION:** Do not enter a least-crowded tag to “find white space.” Gift wrap is empty because it is a **feature**, not a company. Inventory sync is crowded because the **job is real** and still painful.

**CURRENT_RELIGION:** Mcfly does not become an inventory, shipping, or page-builder app.

---

## 3. Jobs merchants still say are unsolved

### 3.1 “What did we actually keep?” (contribution / net profit)

Shopify’s native profit reports need **Cost per item** and still stop at **gross** profit. They do not automatically fold **ad spend, app subscriptions, shipping variance, processor fees, refunds** into one net view. Shopify staff and merchants say this in public:

- Shopify Community thread [Understanding profit tracking for Shopify stores](https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805) (2026): merchants ask for an app that combines COGS, shipping, transaction fees, ads, returns; Shopify’s reply is that **Cost per item** powers product profit, but **other expenses remain outside** the native picture.
- [Shopify Help / reporting docs](https://help.shopify.com/en/manual/reports-and-analytics) (structure): profit reports are COGS-based; ad platforms are not a native join. (Do not invent a “30–50% gap” — that figure appears in **vendor blogs**, e.g. [Godmode, 2026](https://www.trygodmode.com/blog/shopify-real-profit-2026-dashboard-lies), and is **not** used here as fact.)

App Store **search** for “true profit” (fetched 2026-09-09) returns a **long** list: True Profit (899 reviews), BeProfit (202), Lebesgue, Profitario, Margeny, Meyoo, etc. The **keyword** is crowded. The **religion** is not:

| Player | Public job | Still missing vs Mcfly religion |
| --- | --- | --- |
| True Profit / BeProfit / Profitario | Net profit after COGS/fees/ads | Attribution add-ons; P&L surface area; not **break-even MER + allocate** |
| Lifetimely | P&L + LTV + cohorts; order-volume price | Vendor page now includes “Attribution — ad spend, ROAS, CPC” ([pricing](https://www.lifetimely.io/pricing)) — **path-adjacent**, not cash-only |
| Polar / TW | MER as **one tile** among MTA/MMM/AI | [`docs/COMPETITORS.md`](../../COMPETITORS.md): MER inverted or buried |

**CURRENT_RELIGION:** Own **cash MER = Shopify sales ÷ ad spend** and **break-even from contribution margin**. That is narrower than “true net profit P&L” and **intentionally so**.

**RESEARCH_OPTION (do not pull into v1):** A later **cost layer** (Shopify Cost per item, shipping, fees) would move Mcfly toward contribution-margin **truth** without becoming MTA. MASTER_PLAN already uses margin % as an **input**, not an imported COGS engine. Expanding to auto-COGS is a **Phase 6+ pull**, and it steps toward Lifetimely/True Profit clutter.

### 3.2 “The dashboard is sales. The bank is something else.”

Same community thread + [Report Pundit on COGS reports](https://www.reportpundit.com/post/shopify-cogs-report-profit-margins): native reports are a **gross-profit foundation**, not an all-cost model. Operators still export to Sheets.

**CURRENT_RELIGION:** Mcfly’s Sheets companion (Phase 5) is the **honest** answer for people who want the ledger in a workbook — **after** the app brain exists. Do not become SyncWith ([`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) §2).

**RESEARCH_OPTION:** Position against “DIY MER in Sheets” (SyncWith / Supermetrics) rather than against Judge.me. The underserved buyer is the operator **already doing the ritual badly**.

### 3.3 Purchasing / Stocky-shaped inventory (real gap, wrong company)

[Plenisher](https://plenisher.ai/) (public marketing, fetched 2026-09-09) states the job Shopify does not do: **suppliers, POs, multi-supplier costs, reorder**. They market a **Stocky migration** and “Everything Stocky does stays free” up to 10,000 products; Pro **$49/mo**. Treat Stocky sunset **dates** as something to **re-verify on Shopify’s own changelog** before citing in customer copy — this memo only records that **multiple vendors are selling the hole**.

Applora’s **inventory sync / optimization** counts (600+ apps) say the category is **crowded**. Plenisher’s pitch says the **purchasing half** is still missing. Both can be true (sync ≠ buying).

**CURRENT_RELIGION:** Out of scope. Note only so agents do not “helpfully” add PO features.

### 3.4 App-stack tax / conflicting numbers

[oContis Studio — app bloat](https://ocontis.studio/blog/post/the-hidden-cost-of-running-a-shopify-store-when-12-apps-quietly-eat-your-margins/) describes 8–15 paid apps and weekly reconciliation. Their **£400–£1,800** stack range is **that author’s estimate**, not a census.

**RESEARCH_OPTION:** Mcfly’s anti-OS stance is a **stack-tax** sales argument: one Monday number instead of a fourth analytics login. Do not invent a “saves $X/mo” claim (Shopify listing **forbids stats** anyway).

**CURRENT_RELIGION:** Do not grow Mcfly into the thing that **causes** the bloat.

### 3.5 Returns, B2B, fraud, consent — served, not owned by Mcfly

Live category pages (2026-09-09) show **active** incumbents: Exchange It (returns, featured on Store management), Blockify (fraud), Complianz-class consent (Applora rank movers), Wholesale Pricing Discount B2B (Applora +32 spots). These are **other companies’** wedges.

**CURRENT_RELIGION:** Do not open these.

---

## 4. Analytics white space that is **not** “build a better pixel”

Search clutter (same-day App Store search) for Triple Whale / Polar / “true profit” is full of **pixel + ROAS + AI CMO** clones. That is the opposite of white space.

What remains **thin as a product identity** (not as a keyword):

| Gap | Evidence it is thin | Evidence it is wanted | Tag |
| --- | --- | --- | --- |
| **Cash MER as the product** (sales÷spend, period-matched, auditable) | Suites treat MER as a tile; some invert it ([`docs/COMPETITORS.md`](../../COMPETITORS.md)) | Operator Monday question in MASTER_PLAN; community profit threads still start from “ads + Shopify don’t match” | **CURRENT_RELIGION** |
| **Break-even MER from margin** | Lifetimely/True Profit sell P&L; few listings scream **1/margin** as the decision line | Finance-literate operators; Mcfly already ships the input | **CURRENT_RELIGION** |
| **Allocation from cash, not paths** | TW Automate / Apex / Polar CAPI optimize **models** | MASTER_PLAN kill criterion: product must not collapse to a blended ROAS tile | **CURRENT_RELIGION** |
| **Price honesty vs GMV** | Polar **$750** card; TW GMV slider | Merchant resentment is the suites’ own comparison pages (Polar attacks TW’s GMV climb) | **CURRENT_RELIGION** |
| **Admin-only reporting (no pixel)** | BFS analytics rules push pixels; community exception for GraphQL-only reporting | Matches religion **and** a possible BFS exemption path | **CURRENT_RELIGION** + **RESEARCH_OPTION** (document for reviewers) |
| **Agency / multi-store cash desk at flat-ish price** | Polar/TW sell unlimited stores **inside a GMV tax** | MASTER_PLAN: agency later; Phase 6 multi-brand **revenue-pulled** | **RESEARCH_OPTION** |
| **Recon / freshness as trust** | Suites hide pipeline health behind CSM | MASTER_PLAN kill: spend must stay within ~5% of Ads Manager | **CURRENT_RELIGION** (Phase 2), not a new category |

**Not white space (do not “fill”):**

- Another MTA model, Triple Pixel clone, Compass, Causal Lift, Moby chat  
- SyncWith connector zoo  
- Creative studio / landing-page AI (TW Automate)  
- Helpdesk / email (Klaviyo + Gorgias are expanding **into each other**)

---

## 5. When a multi-problem platform wins the white space (and when it must not)

Platforms **absorb** adjacent jobs after they own distribution:

- TW: measurement → creative → landing pages → retail/wholesale (Enterprise FAQ on [pricing](https://triplewhale.com/pricing)).  
- Polar: warehouse → CAPI → Klaviyo audiences → MCP.  
- Klaviyo: email → SMS → Service helpdesk on one bill ([pricing](https://www.klaviyo.com/pricing)).  
- Gorgias: tickets → AI Agent → Voice/SMS add-ons.

**They win that expansion when:**

1. The first job is **habitual** (email is sending; tickets are flowing; pixel is live).  
2. The second job **uses the same graph**.  
3. The buyer already accepted a **large, scaling bill**.

**They lose — and a wedge wins — when:**

1. The adjacent job has a **loved specialist** (Judge.me vs “reviews inside the OS”).  
2. The platform’s **religion** poisons the new job (attribution theater poisoning cash MER).  
3. The merchant is still in the **first 10 minutes** of the first job.

**CURRENT_RELIGION:** Mcfly does not become a platform by collecting underserved jobs. White space is **permission to stay narrow**, not a backlog.

**RESEARCH_OPTION:** The only adjacent jobs that **rhyme** with the cash desk (if revenue ever pulls): live spend pipes (already Phase 2), Sheets (Phase 5), multi-store portfolio, break-even **alerts**. Each is the **same number**, more often. None is a new category tag.

---

## 6. White-space map for Mcfly (decision table)

| Opportunity | Crowding | Fit to religion | Verdict |
| --- | --- | --- | --- |
| Cash MER + break-even + allocate | Low **as identity**; high as “analytics” search | Perfect | **CURRENT_RELIGION — this is the company** |
| Full SKU P&L / auto-COGS / Amazon | High (“true profit”) | Partial (margin yes; P&L zoo no) | **RESEARCH_OPTION — later, pulled** |
| Pixel / MTA / incrementality | High + capital-intensive | Forbidden | Refuse |
| Reviews / loyalty / popups | Extreme + loved incumbents | Wrong job | Refuse |
| Inventory purchasing (Stocky hole) | High sync / thin purchasing | Wrong job | Refuse (note only) |
| Returns / helpdesk / email | Owned by platforms + specialists | Wrong job | Refuse |
| Connector marketplace | SyncWith / Coupler / Coefficient | Explicitly discarded | Refuse |
| Flat ~$79 cash desk vs GMV OS | Pricing white space | Locked | **CURRENT_RELIGION** |
| Forever-free listing flywheel | Proven by Judge.me | Tensions §8 | **RESEARCH_OPTION** only |
| Store management / Analytics primary tag | Taxonomy home | Neutral | **RESEARCH_OPTION** for listing form |

---

## 7. Listing / category white space (practical)

Shopify merchants browsing **Marketing and conversion** are shopping for **widgets that make money today**. A cash desk in that aisle is easy to misread as “another ads app.”

Merchants browsing **Store management → Analytics** are closer to the Monday ritual — but they sit next to heatmaps and pixels.

**RESEARCH_OPTION:** Primary tag **Analytics** (Store management). Card subtitle in **merchant cash language** (“Spend vs Shopify sales — cash MER and break-even”), not “AI attribution.” Secondary tag only if Shopify’s form forces a marketing feature Mcfly actually has (it should not).

**CURRENT_RELIGION:** Copy remains anti-theater. [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md) already. Shopify §4.3.3: **no** “the only cash MER app” superlatives.

---

## 8. What would falsify this white-space read

Update this file if public evidence flips:

- A **loved**, **flat-priced**, **anti-attribution** cash-desk app accumulates Judge.me-scale reviews — then the identity gap is gone; compete on craft/reliability only.  
- Shopify ships **native spend-vs-sales MER + break-even** in Admin — then the wedge is a feature, not a product (watch Shopify Analytics / Sidekick, not rumor).  
- Design partners will not open weekly after accurate MER ([`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) §11) — then the job was never the job.

Until then, the underserved problem is not “more analytics.” It is **a cash definition operators can defend without a GMV invoice or a pixel liturgy**.

---

## 9. Sources

### Official / community

- [App listing categories](https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories)
- [App Store requirements §4.3](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements)
- [Shopify Community — profit tracking](https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805)
- [BFS analytics pixel thread](https://community.shopify.dev/t/bfs-analytics-app-30-active-installs-have-connected-pixels/19356)

### Live App Store / vendors (2026-09-09)

- [Store management category](https://apps.shopify.com/categories/store-management)
- [Marketing and conversion category](https://apps.shopify.com/categories/marketing-and-conversion)
- App Store search: “true profit”, “triple whale”, “polar analytics”
- [lifetimely.io/pricing](https://www.lifetimely.io/pricing)
- [triplewhale.com/pricing](https://triplewhale.com/pricing)
- [klaviyo.com/pricing](https://www.klaviyo.com/pricing)
- [polaranalytics.com/pricing](https://www.polaranalytics.com/pricing)
- [plenisher.ai](https://plenisher.ai/)

### Third-party (labeled)

- [Applora snapshot week ending 2026-09-06](https://applora.ai/appstore)
- [Report Pundit — COGS / native profit limits](https://www.reportpundit.com/post/shopify-cogs-report-profit-margins)
- [oContis — app bloat](https://ocontis.studio/blog/post/the-hidden-cost-of-running-a-shopify-store-when-12-apps-quietly-eat-your-margins/)
- [Godmode — “dashboard lies”](https://www.trygodmode.com/blog/shopify-real-profit-2026-dashboard-lies) (vendor; **do not** reuse its 30–50% claim)

### In-repo

- [`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md)
- [`docs/COMPETITORS.md`](../../COMPETITORS.md)
- [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md)

**Confidence:** High that cash-MER-as-product is still an identity gap. **High** that “true profit” as a **search term** is crowded. **Medium** on inventory-purchasing as a durable hole (vendor-led narrative). **None** of this is a license to expand Mcfly scope.
