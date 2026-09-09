# Shopify App Store market structure — 2026-09

**Lane:** PARALLEL ENTERPRISE research (Shopify App Store + category strategy).  
**Repo stance this file does not amend:** [`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) §1–§4 and [`docs/COMPETITORS.md`](../../COMPETITORS.md).  
**Method:** public Shopify docs, live App Store listings, and named third-party crawls. **No invented numbers.** Third-party floors are labeled as such.

**Tag legend**

| Tag | Meaning |
| --- | --- |
| **CURRENT_RELIGION** | Locked Mcfly directive. Research must not treat this as optional. |
| **RESEARCH_OPTION** | Observed market pattern or packaging choice. Not a product decision. Do not ship from this tag. |

---

## 1. What the App Store actually is

The Shopify App Store is a **permissioned, billed, categorized directory**, not an open marketplace. Public distribution requires Partner registration, App Store review, and Shopify-hosted billing. Shopify states this directly:

- Public multi-merchant distribution goes through the App Store. Registration is a **one-time $19 USD** Partner fee ([Revenue share for App Store developers](https://shopify.dev/docs/apps/launch/distribution/revenue-share)).
- Listed apps that charge must use **Shopify App Pricing** or the legacy Billing API. Off-platform billing is prohibited unless Shopify has notified the developer otherwise ([App Store requirement 1.2](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements)).
- New public apps default to **Shopify App Pricing**, configured in the Partner Dashboard, not in app code ([Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing); [changelog, 2026-05](https://shopify.dev/changelog/shopify-app-pricing-charge-for-usage-recurring-subscriptions-or-both)).

**CURRENT_RELIGION:** Mcfly’s public listing, when submitted, bills through Shopify. [`docs/SHOPIFY_LAUNCH.md`](../../SHOPIFY_LAUNCH.md) already locks this. Do not invent a Stripe checkout for a listed app.

**RESEARCH_OPTION:** Polar’s listing discloses that *some* charges may be billed outside the Shopify invoice ([Polar App Store listing](https://apps.shopify.com/polar-analytics), pricing card, fetched 2026-09-09). That is a documented exception path, not a template Mcfly can copy without Shopify’s written exception.

---

## 2. Official taxonomy (where Mcfly sits)

Shopify publishes **seven** listing categories. Reviewers assign the primary tag; partners do not get to invent a eighth bucket ([App listing categories](https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories)).

| Category | Shopify’s job-to-be-done |
| --- | --- |
| Sales channels | Sell on other platforms |
| Finding products | Source inventory |
| Selling products | Payments, subscriptions, pricing, digital, custom products |
| Orders and shipping | Fulfill, ship, inventory, returns |
| Store design | Theme, SEO, media, pop-ups, i18n |
| **Marketing and conversion** | Ads, email/SMS, checkout, promotions, reviews, loyalty |
| **Store management** | Operations, **analytics**, security, finances, support |

**Analytics is not a top-level category.** Shopify’s taxonomy puts the **Analytics** tag under **Store management → Operations**: “Apps that analyze and generate insights or recommendations for a store.” Marketing analytics features also appear as structured features under Marketing and conversion.

Live storefronts confirm the split:

- [Marketing and conversion](https://apps.shopify.com/categories/marketing-and-conversion) (fetched 2026-09-09) is dominated by reviews, pop-ups, bundles, email, ads — **cash-now** storefront apps.
- [Store management](https://apps.shopify.com/categories/store-management) (fetched 2026-09-09) is ops, support, security, and a secondary **Analytics** rail (pixels, heatmaps, surveys, profit tiles).

**CURRENT_RELIGION:** Mcfly is a **cash desk** (spend vs Shopify sales → break-even → allocate), not a storefront conversion widget and not an attribution OS. Listing drafts in [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md) currently say “Marketing → Marketing analytics / Advertising.” That is a *draft*, not a locked taxonomy choice.

**RESEARCH_OPTION:** Primary tag **Store management / Analytics** is the official home for “insights or recommendations for a store.” Secondary tag only if a real marketing-automation surface ships (it must not, under religion). Do not keyword-stuff both tags; Shopify’s own guidance is: primary = main function, secondary only if the second function is real ([App listing categories](https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories)).

---

## 3. Scale of the directory (third-party crawl — labeled)

Shopify does not publish official app-count or review-count totals. The independent crawl **Applora** (week ending **2026-09-06**) reports a public snapshot. Treat as **one crawler’s count**, not Shopify’s:

| Snapshot field (Applora, week ending 2026-09-06) | Reported figure |
| --- | --- |
| Currently listed apps | 27,808 |
| Apps ever tracked | 28,173 (27,808 listed + 365 delisted) |
| Public reviews indexed | 1,114,121 |
| Reviewing stores (from public reviews) | 605,091 |
| Developers | 15,701 |
| Built for Shopify apps | 1,577 |
| BFS share of listed | 5.7% |
| Reviews per listed app (derived by Applora) | 40.1 |

Source: [Applora — Shopify App Store Statistics 2026](https://applora.ai/appstore), snapshot dated 2026-09-06.

**Implication (structure, not a Mcfly KPI):** the directory is large; **BFS is scarce**; most listed apps are not “loved” at Judge.me scale. Discovery is a ranking + review-compounding problem, not a “build it and they come” problem.

**CURRENT_RELIGION:** [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md) and [`docs/SHIP_NOW.md`](../../SHIP_NOW.md) already refuse chasing Built for Shopify until ~50 paid-plan installs + 5 reviews. That matches Shopify’s own BFS floor ([Built for Shopify requirements](https://shopify.dev/docs/apps/launch/built-for-shopify/requirements) §1.2.1–1.2.2: **50 net installs from active shops on paid plans** and **five reviews**).

---

## 4. Two economies inside one store

The App Store is not one market. It is at least **two economies** that share a search box.

### 4.1 Storefront cash desks (Marketing and conversion)

These apps change what a buyer sees. Value is visible in minutes: a review widget, a bundle, a popup, a subscription widget.

Live category page (fetched 2026-09-09) recommended / featured examples:

| App (listing) | Public rating / reviews (that fetch) | Pricing signal on listing |
| --- | --- | --- |
| [Judge.me Product Reviews](https://apps.shopify.com/judgeme) | 5.0 / 46,634 (search card); listing also showed 40,209 on a parallel fetch — **use the listing you submit against, not a cached number** | Forever Free + Awesome **$15/month** |
| [Loox](https://apps.shopify.com/loox) | 4.9 / 8,818 (listing) | Free + **$49.99/mo** (300 orders + overage) + **$299.99/mo** |
| [Pop Convert](https://apps.shopify.com/categories/marketing-and-conversion) (category card) | 4.9 / 8,788 | Free plan available |
| [Klaviyo](https://apps.shopify.com/categories/marketing-and-conversion) (category card) | 4.7 / 3,282 | Free to install |
| [Recharge](https://apps.shopify.com/subscription-payments) | 4.8 / 2,965 | From **$25/month**; usage % on higher plans |

**Pattern:** the apps that “print money” in this economy combine (a) a **free or cheap visible widget**, (b) **huge review volume**, (c) a paid upgrade that is a small fraction of the GMV they claim to protect. Judge.me’s paid SKU is a **flat $15/month**, not a GMV tax ([Judge.me listing](https://apps.shopify.com/judgeme)).

### 4.2 Operator OS / analytics (Store management + off-store sales)

These apps change what an operator believes on Monday. Value is a number, not a widget. Review volume is **one to two orders of magnitude smaller** than reviews/popups.

Live search / listing snapshots (fetched 2026-09-09):

| App | Public rating / reviews | Pricing signal |
| --- | --- | --- |
| Triple Whale (App Store search card, “By Triple Whale”) | 4.1 / 91 · Free plan available | Official site: **GMV × package** (Free / Foundation / Automate / Enterprise); **unlimited users**; paid packages are **12-month** ([triplewhale.com/pricing](https://triplewhale.com/pricing)) |
| [Polar: AI-Analytics Platform](https://apps.shopify.com/polar-analytics) | 4.9 / 116 | Listing: **Core from $750/month**, “pricing based on online GMV”; **unlimited users / history / connectors** |
| TP: True Profit Analytics (search card) | 5.0 / 899 · Free trial | Profit / LTV tracker — review volume closer to a **cash-desk wedge** than to Polar |
| Lifetimely (vendor pricing page, 2026-09-09) | (listing URL not resolved this pass) | **Order-volume ladder**, not seats: Free ≤50 orders; S $49; M $149; L $299; XL $499; XXL $749; Unlimited $999 ([lifetimely.io/pricing](https://www.lifetimely.io/pricing)) |

**CURRENT_RELIGION:** Mcfly competes in the **operator** economy as a **single-wedge cash desk**, not as a Triple Whale / Polar multi-problem OS ([`docs/COMPETITORS.md`](../../COMPETITORS.md)).

**RESEARCH_OPTION:** True Profit’s **899** public reviews vs Polar’s **116** and Triple Whale’s **91** (same-day App Store fetch) is a structural signal: **narrow profit language + trial** can accumulate listing proof faster than a $750 GMV suite. That is distribution physics, not a request to clone True Profit’s P&L stack.

---

## 5. How category leaders package price

Shopify’s platform supports three **legal** shapes ([Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing)):

1. **Recurring** — free / monthly / yearly / monthly-with-yearly-discount  
2. **Usage** — fixed, graduated, or volume meters via App Events API  
3. **Combined** — recurring + usage  

Shopify’s own billing guidance: keep plans few; offer trials; bill in the merchant’s local currency when supported ([About billing](https://shopify.dev/docs/apps/launch/billing)). Plan caps on Shopify App Pricing: **up to eight public plans** and **15 private plans**; **at most one free public plan without usage charges** ([Migrate to Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/migrating-to-shopify-app-pricing)).

What leaders *actually* sell (public pages, 2026-09):

| Archetype | Who uses it (public) | Meter | When it wins |
| --- | --- | --- | --- |
| **Flat recurring** | Judge.me Awesome **$15/mo**; Mcfly target **~$79/store/mo** | Time | One job, easy listing compare, low support about “why did my bill jump” |
| **Order / volume ladder** | Lifetimely (orders/mo); Loox mid-tier (300 orders + **$50 per extra 300**) | Activity | Feels “fair” as the store grows; still predictable vs GMV |
| **Profile / ticket / send usage** | Klaviyo (profiles + email/SMS usage on [klaviyo.com/pricing](https://www.klaviyo.com/pricing)); Gorgias (tickets, **not seats** — [gorgias.com/pricing](https://www.gorgias.com/pricing)) | Consumption | Cost tracks the work the app does |
| **GMV / revenue tax** | Triple Whale (explicit FAQ: “combination of your brand’s **annual GMV** and the package”); Polar listing “**based on online GMV**” from **$750/mo** | Store size | Captures upside; punished by operators who outgrow the tool |
| **Take-rate + base** | Recharge: **$25/mo** (first 50 subscribers, no txn fee) → **$99/mo + 1.49% + 19¢** → **$499/mo + 1.34% + 19¢** ([Recharge listing](https://apps.shopify.com/subscription-payments)) | GMV of *the job* (subscription GMV), not whole-store GMV | Wins when the app *is* the cash register for that motion |
| **Seat tax** | Rare among Shopify-native leaders in this pass. Gorgias markets **“never priced per agent”** and lists **3 seats on Starter, 500 on higher plans** ([gorgias.com/pricing](https://www.gorgias.com/pricing)). Triple Whale and Polar both advertise **unlimited users**. | Headcount | Wins for horizontal SaaS; **loses** in Shopify admin where one owner installs for the shop |

**CURRENT_RELIGION:** Mcfly is **flat mid-two-digits to low-three-digits**, launch free for design partners, target **~$79/store/mo**, **not** GMV-scaled suite tax ([`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) §8; [`docs/COMPETITORS.md`](../../COMPETITORS.md)).

**RESEARCH_OPTION (do not adopt without rewriting religion):** an **order-volume** ladder (Lifetimely shape) is a middle path — not GMV theater, still scales. A **usage meter** on spend-sync events is now a first-class Shopify App Pricing primitive. Both are *options*, not the plan.

**RESEARCH_OPTION:** Seat pricing is the **wrong** default for an embedded single-store cash desk. Category leaders in analytics/helpdesk are abandoning or capping seats and charging the **store** or the **work**.

---

## 6. Multi-problem platforms vs single-wedge cash desks

### 6.1 Platform pattern (Triple Whale, Polar, expanding Klaviyo)

Public packaging:

- **Triple Whale** — Free pixel/first-last-click → Foundation (MTA + BI + Moby) → Automate (actions) → Enterprise (Compass MMM/incrementality). Add-ons: Retention, Conversion, Compass, warehouse sync, concierge ([triplewhale.com/pricing](https://triplewhale.com/pricing)). Claim on that page: “Trusted by **65,000+** top brands” / FAQ “more than **60,000** brands” (vendor claim; not an App Store install count).
- **Polar** — one Core stack (Snowflake + semantic layer + pixel + activations + MCP) from **$750/mo** GMV; Custom unbundles incrementality / CAPI / MCP ([polaranalytics.com/pricing](https://www.polaranalytics.com/pricing); [listing](https://apps.shopify.com/polar-analytics)). Vendor claim: “**4,000+** ecommerce brands and agencies.”
- **Klaviyo** — email/SMS core expanding into **Service / Helpdesk** and Composer on the same pricing page ([klaviyo.com/pricing](https://www.klaviyo.com/pricing)). Gorgias claims it “power[s] customer conversations for **40% of Shopify brands**” ([gorgias.com/pricing](https://www.gorgias.com/pricing)) — vendor claim.

**When platforms win (observed, not invented):**

- Buyer is a **team** (media + retention + ops) that wants one login.
- Budget is already a **line item** (hundreds to thousands per month).
- Switching cost is **pixel + UTMs + CSM ritual** (Northbeam / Polar onboarding reviews on Polar’s listing mention dedicated onboarding).
- Shopify relationship / habit: “everyone already has it” ([`docs/COMPETITORS.md`](../../COMPETITORS.md)).

**When platforms lose:**

- GMV slider makes the bill a **tax on success**.
- Surface area creates **number conflict** (Meta vs Moby vs Compass vs finance).
- App Store review volume stays **thin** relative to cash-desk apps (TW 91, Polar 116 vs Judge.me tens of thousands — same-day fetch). Platforms grow **off-store** (sales, content, Shopify Plus networks), not primarily via listing conversion.

### 6.2 Single-wedge cash desks (Judge.me, Loox paid SKU, Lifetimely, True Profit)

**When wedges win:**

- One sentence job: “collect reviews,” “see profit after costs,” “run subscriptions.”
- **Time-to-visible-result** measured in minutes (widget on PDP; first profit row).
- Price is a **rounding error** vs the job (Judge.me $15; Lifetimely free ≤50 orders).
- Listing conversion compounds because merchants can **install three competitors the same afternoon** and keep the one that showed a result (practitioner pattern: [Kompassify onboarding guide, 2026](https://kompassify.com/blog/shopify-app-onboarding-guide)).

**CURRENT_RELIGION:** Mcfly is the wedge: **cash MER + break-even + one allocation call.** “Beat them all” ≠ rebuild the OS ([`docs/COMPETITORS.md`](../../COMPETITORS.md)).

**RESEARCH_OPTION:** Wedges that later grow a **second** paid SKU (Loox AI / unlimited; Lifetimely Amazon **+$75/mo**; Gorgias Voice/SMS add-ons) do it **after** the first job is habitual. Mcfly’s locked later surfaces (Sheets, live spend pipes) are companions to the same religion, not a new category.

---

## 7. Built for Shopify as a category gate, not a launch trophy

BFS is a **quality badge** with a published floor and category-specific rules ([Built for Shopify requirements](https://shopify.dev/docs/apps/launch/built-for-shopify/requirements)):

| Gate | Published rule |
| --- | --- |
| Installs | ≥ **50** net installs from **active shops on paid plans** |
| Reviews | ≥ **5** reviews + a minimum recent rating |
| Embed | Latest App Bridge; primary workflows in admin; seamless signup on Shopify credentials |
| Homepage | Simplified monitoring/reporting **on the app home** |
| Onboarding | Concise; not collapsed; no “install another app” as a required step; dismiss onboarding UI after completion |
| Analytics category | If the app gathers **storefront behavioral** data, it must use **Web Pixel extensions**, not script tags. Community thread: reporting-only apps that only use Admin GraphQL may be exempt from the pixel rule ([Shopify developer community, 2025](https://community.shopify.dev/t/bfs-analytics-app-30-active-installs-have-connected-pixels/19356)) |

**CURRENT_RELIGION:** Do not chase BFS before the floor. Mcfly v1 is **Admin API sales + spend**, not a storefront pixel — religion already forbids the pixel. If reviewers ever mis-tag Mcfly as a behavioral analytics app, the correct reply is: **reporting on Admin data, no storefront event collection.**

**RESEARCH_OPTION:** Design the **homepage as a cash dashboard on day one** (sales, spend, MER, break-even). That is both religion and a BFS homepage rule (§3.1.4 / §4.2.3). It is not scope creep.

---

## 8. Listing conversion is a separate market from product quality

Shopify’s official listing rules constrain what “prints money” copy can even say ([App Store requirements §4](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements); [best practices](https://shopify.dev/docs/apps/launch/shopify-app-store/best-practices)):

- Introduction: Shopify best-practices page specifies a **100-character** introduction that names benefits; avoid keyword stuffing and data claims.
- Screenshots: **1600×900**, **3–6** desktop, unique, real UI, **no browser chrome**, **no pricing / reviews / outcome guarantees** in images. Uniqueness enforced from **2026-03-26** ([changelog](https://shopify.dev/changelog/clearer-standards-for-app-listing-images)).
- **No statistics or unsubstantiated claims** in listing copy or images (§4.3.3, §4.3.4) — including “verifiable” stats.
- Pricing **only** in Pricing details — not in the icon, screenshots, or body (§4.2).
- Feature media: Shopify recommends a **2–3 minute promotional** video, screencasts ≤25% of the video — or a single-focal-point static.

A former Partner-Program operator’s **2026** practitioner benchmarks (not Shopify official; do not treat as Mcfly KPIs): view-to-install **~3–8%** for a strong listing; **~1–2%** under 25 reviews; **~5–8%** at 200+ reviews; first **50** reviews as the early investment ([Taylor Sicard, June 2026](https://taylorsicard.com/blog/shopify-app-listing-conversion)). The same essay’s funnel planning ranges (search CTR, install→active, active→paid) are **his planning anchors**, not platform statistics.

**CURRENT_RELIGION:** Listing copy in [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md) must stay factual (formula, refusals, who it’s for). Shopify §4.3.3 means **do not** put “3–8% install rate” or invented lift claims on the listing.

**RESEARCH_OPTION:** The apps that compound (Judge.me-scale) win the **review flywheel** first, often with a **Forever Free** SKU that is a real product, not a demo. Mcfly’s locked launch is **free for design partners**, not “forever free.” That is the correct religion for signal quality; it is a **slower** App Store compounding curve. See [`MONETIZATION_PATTERNS.md`](./MONETIZATION_PATTERNS.md).

---

## 9. Category strategy implications for Mcfly

| Question | Evidence | Tag |
| --- | --- | --- |
| Which category? | Official Analytics tag = Store management → Operations | **RESEARCH_OPTION** to set primary tag there; listing draft currently says Marketing |
| Who is the incumbent OS? | TW (GMV + free TOFU), Polar ($750 GMV floor), Northbeam (off-store, spend-gated) | **CURRENT_RELIGION:** do not parity |
| Who is the cash-desk peer set? | Lifetimely (order ladder), True Profit (high review volume, trial), BeProfit / Profitario / Lebesgue (search clutter) | **RESEARCH_OPTION:** watch listing language (“true profit,” “net profit”) — crowded **words**, not crowded **cash MER religion** |
| What prints listing money? | Free visible widget + review count (Judge.me, Loox, popups) | **RESEARCH_OPTION** for *tactics*; Mcfly cannot become a widget without leaving the product |
| What prints operator money? | GMV tax at the top; order/usage ladders in the middle; flat at the bottom | **CURRENT_RELIGION:** stay flat ~$79 |
| Platform vs wedge? | Platforms win teams + habit; wedges win first 10 minutes + price honesty | **CURRENT_RELIGION:** wedge |

White-space detail (underserved store problems, not just analytics competitors) lives in [`WHITE_SPACE.md`](./WHITE_SPACE.md).

---

## 10. Sources

### Official Shopify

- [App listing categories](https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories)
- [App Store requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements) (§1.2 billing, §4 listing)
- [App Store best practices](https://shopify.dev/docs/apps/launch/shopify-app-store/best-practices)
- [About billing](https://shopify.dev/docs/apps/launch/billing)
- [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing)
- [Migrate to Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/migrating-to-shopify-app-pricing)
- [Shopify App Pricing changelog](https://shopify.dev/changelog/shopify-app-pricing-charge-for-usage-recurring-subscriptions-or-both)
- [Revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share)
- [Built for Shopify requirements](https://shopify.dev/docs/apps/launch/built-for-shopify/requirements)
- [Onboarding UX](https://shopify.dev/docs/apps/design/user-experience/onboarding)
- [Setup guide composition](https://shopify.dev/docs/api/app-home/latest/patterns/compositions/setup-guide)
- [Listing image uniqueness changelog (2026-03-12, enforced 2026-03-26)](https://shopify.dev/changelog/clearer-standards-for-app-listing-images)
- [BFS analytics pixel community thread](https://community.shopify.dev/t/bfs-analytics-app-30-active-installs-have-connected-pixels/19356)

### Live App Store / vendor pricing (fetched 2026-09-09 unless noted)

- [Marketing and conversion category](https://apps.shopify.com/categories/marketing-and-conversion)
- [Store management category](https://apps.shopify.com/categories/store-management)
- [Judge.me listing](https://apps.shopify.com/judgeme)
- [Loox listing](https://apps.shopify.com/loox) · [loox.app/pricing](https://loox.app/pricing)
- [Recharge listing](https://apps.shopify.com/subscription-payments)
- [Polar listing](https://apps.shopify.com/polar-analytics) · [polaranalytics.com/pricing](https://www.polaranalytics.com/pricing)
- [triplewhale.com/pricing](https://triplewhale.com/pricing)
- [klaviyo.com/pricing](https://www.klaviyo.com/pricing)
- [gorgias.com/pricing](https://www.gorgias.com/pricing)
- [lifetimely.io/pricing](https://www.lifetimely.io/pricing) (vendor: last updated 2026-09-09)

### Third-party (labeled)

- [Applora App Store statistics, week ending 2026-09-06](https://applora.ai/appstore)
- [Taylor Sicard — listing conversion, June 2026](https://taylorsicard.com/blog/shopify-app-listing-conversion)
- [Kompassify — Shopify app onboarding, Aug 2026](https://kompassify.com/blog/shopify-app-onboarding-guide)

### In-repo religion (not market evidence)

- [`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md)
- [`docs/COMPETITORS.md`](../../COMPETITORS.md)
- [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md)

**Confidence:** High on official taxonomy, billing rules, revenue share, BFS floors, and same-day listing prices cited above. **Medium** on Triple Whale dollar floors (official page is a GMV slider; third-party blogs disagree — see [`MONETIZATION_PATTERNS.md`](./MONETIZATION_PATTERNS.md)). **Low** on any unpublished install counts.

**Do not** paste competitor dollar amounts onto mcflyads.com without re-fetching the live page.
