# Shopify App Store monetization patterns — 2026-09

**Lane:** PARALLEL ENTERPRISE research (monetization + listing conversion + first 10 minutes).  
**Companion:** [`MARKET_STRUCTURE.md`](./MARKET_STRUCTURE.md) (taxonomy and platform-vs-wedge).  
**Does not amend** [`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) §8 pricing or [`docs/COMPETITORS.md`](../../COMPETITORS.md).

**Tag legend:** **CURRENT_RELIGION** = locked Mcfly directive. **RESEARCH_OPTION** = observed pattern, not a ship decision. **No invented numbers.** Vendor sliders and third-party floors are labeled.

---

## 1. The take Shopify already takes

Before designing a price, model the **platform tax**. Official ([Revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share)):

| Item | Published rule |
| --- | --- |
| App Store registration | **$19 USD** one-time per Partner account |
| Revenue share (standard) | **0%** on first **$1,000,000 USD** lifetime gross app revenue earned from **January 1, 2025**; **15%** above that |
| Large-developer override | If prior-year App Store earnings ≥ **$20,000,000** **or** company revenue ≥ **$100,000,000**, pay **15% from dollar one** (no $1M exemption) |
| Processing | **2.9%** on all billing, **plus** applicable sales tax — charged **separately** from revenue share |
| Basis | **Gross** sales, not net. **Refunds are not deducted.** Multiple apps and Associated Developer Accounts **sum** to the $1M threshold |
| Theme / referral income | **Not** in App Store revenue-share math |

Help Center wording matches the 100% / 85% split ([How Partners earn](https://help.shopify.com/en/partners/partner-program/how-to-earn) — page returned 403 to this agent; the same table is quoted on Shopify’s partner-earnings docs and restated on the revenue-share developer page above).

**CURRENT_RELIGION:** Mcfly is pre-revenue. The **$1M lifetime 0% band** is runway, not a destination. Do not build pricing to “optimize the Shopify take.”

**RESEARCH_OPTION:** Once (if) Mcfly clears $1M **lifetime** partner revenue, the **steady-state** App Store cost is **15% + 2.9% processing + tax**, not the 2021-era “resets every January” story. Third-party explainers (e.g. [Taylor Sicard on the lifetime cap](https://taylorsicard.com/blog/shopify-app-revenue-share-lifetime-cap)) describe the 2025 wording change; **cite Shopify’s page** for any founder model.

---

## 2. What Shopify will let you charge

### 2.1 Legal rails

- Listed apps: **Shopify App Pricing** (default for new public apps) or legacy **Billing API** ([About billing](https://shopify.dev/docs/apps/launch/billing); [requirement 1.2](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements)).
- Shopify App Pricing models ([docs](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing)):
  - Recurring: free, monthly, yearly, monthly-with-yearly-discount
  - Usage: **fixed / graduated / volume** meters via **App Events API**
  - Combined: recurring + usage
- Shopify **hosts** the plan-selection page: `https://admin.shopify.com/store/:store_handle/charges/:app_handle/pricing_plans`
- Caps: **≤8 public plans**, **≤15 private**, **≤1 free public plan without usage** ([migration guide](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/migrating-to-shopify-app-pricing)).
- Merchants must **upgrade/downgrade without support or reinstall** ([requirement 1.2.3](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements)).
- One-time app purchases: **not** supported on Shopify App Pricing — use Manual Pricing / Billing API.
- Shopify’s billing best-practice table ([About billing](https://shopify.dev/docs/apps/launch/billing)): simple plans; few plans; **free trials**; local currency. Shopify’s own trial hint: “Align with Shopify’s free trial or **$1 plan**.”

**CURRENT_RELIGION:** When billing ships, it is Shopify Billing / App Pricing, trial announced before charge, **not** “forever free” ([`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) §8).

**RESEARCH_OPTION:** Configure plans in the Partner Dashboard (Shopify App Pricing) rather than hand-rolling `appSubscriptionCreate`, unless a one-time SKU appears (it should not). Use **welcome links per plan** so paid vs design-partner private plans land on different first screens ([Shopify App Pricing — redirection URL](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing)).

### 2.2 What the listing is allowed to say about money

Official ([requirement 4.2](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements); [best practices §5.C](https://shopify.dev/docs/apps/launch/shopify-app-store/best-practices)):

- Complete pricing: all tiers, trial length, what triggers a charge.
- **No prices in images or the icon.**
- **No prices in the body / logo.** Pricing lives in **Pricing details** only.
- Plans display **lowest → highest** automatically.
- Shopify recommends a **14-day** trial when paid.
- Enterprise / extra charges: put them in **Description of additional charges** and, if billed off Shopify, a **link** (Polar and Recharge listings both show “External charges may be billed… separately”).

**CURRENT_RELIGION:** Listing must match reality. [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md) already: free design-partner launch → ~$79 later. Do not promise live Meta sync or paid billing that is not live ([`docs/SHOPIFY_LAUNCH.md`](../../SHOPIFY_LAUNCH.md) rejection #5).

---

## 3. Six pricing archetypes that actually print (with public receipts)

### A. Forever-free wedge + cheap flat upsell

**Example:** [Judge.me](https://apps.shopify.com/judgeme) (fetched 2026-09-09)

| Plan | Public price | What the listing says is included |
| --- | --- | --- |
| Forever Free | $0 | Unlimited product/store reviews, visual reviews, widget, carousels, rich snippets, importer |
| Awesome | **$15 / month** + 15-day trial | AI replies/summary/translations, 130+ integrations, extra widgets, coupons, Google Shopping, design/CSS |

**Why it prints:** the free SKU is a **complete job** (reviews on the storefront). Paid is automation + integrations + AI — not “unlock the widget.” Review volume (listing/search cards this day: **40k–46k**) is the distribution engine.

**RESEARCH_OPTION:** A Mcfly “forever free” MER with paid allocation would **copy this shape**. Religion currently prefers **time-boxed design-partner free**, then flat paid — to avoid a freeloader flood ([`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) §8). Do not silently flip to forever-free.

### B. Free starter + order-overage mid + unlimited top

**Example:** [Loox](https://apps.shopify.com/loox) (fetched 2026-09-09)

| Plan | Public price |
| --- | --- |
| Beginner | Free — request emails, widgets, SEO, Shop syndication |
| Mid | **$49.99 / month** — “300 orders included + **$50 per additional 300 orders**” + AI + video + referrals + syndication |
| Top | **$299.99 / month** — unlimited request emails + unlimited referrals |

Vendor site ([loox.app/pricing](https://loox.app/pricing)): billed on Shopify’s 30-day cycle; cancel anytime.

**Why it prints:** free gets the widget live; growth **auto-upgrades** the bill with order volume; unlimited is a **relief SKU** for high-order stores.

**RESEARCH_OPTION:** Order-overage is Shopify-native **usage** (Archetype C) dressed as “plans.” Mcfly could theoretically meter **orders** or **spend-sync days**. Religion says **flat**. Flag only.

### C. Official usage meters (profiles, tickets, events)

**Klaviyo** ([klaviyo.com/pricing](https://www.klaviyo.com/pricing), fetched 2026-09-09): **Free** = up to **250 profiles**, **500 emails/month**, **$5** mobile messages, **$5** Composer. Paid marketing is built as a **plan configurator** (the page showed a platform total of **$45 USD** for a configured bundle — that is **one configurator state**, not a list price). Historical third-party writeups (e.g. older Klaviyo ladders) **lag**; do not republish them.

**Gorgias** ([gorgias.com/pricing](https://www.gorgias.com/pricing), fetched 2026-09-09) — **tickets, not seats**:

| Plan | Monthly list (monthly billing) | Included tickets | Overage | Seats |
| --- | --- | --- | --- | --- |
| Starter | **$40/mo** (helpdesk $10 + AI Agent $30) | 50 | $0.40 / ticket | 3 |
| Basic | **$90/mo** list / **$77/mo** annual | 300 | $0.40 / ticket | 500 |
| Pro | **$550** / **$471** annual | 2,000 | $0.36 / ticket | 500 |
| Advanced | **$1,430** / **$1,227** annual | 5,000 | $0.36 / ticket | 500 |

AI Agent: then **$1.50** per automated interaction past the included bucket (plan table also lists per-interaction rates **$1.00–$0.85** depending on tier — **use the live page** if quoting). Onboarding: Starter/Basic **self-serve**; Pro **1:1**; Advanced **white-glove**.

**Why it prints:** price tracks **work the app does**. Shopify App Pricing’s graduated/volume meters exist specifically for this.

**CURRENT_RELIGION:** Mcfly’s job is a **Monday ritual**, not a send/ticket factory. Usage-metering MER **does not match** the job unless the meter is something honest (e.g. connected stores). Default remains flat.

### D. GMV × package (operator OS)

**Triple Whale** official FAQ ([triplewhale.com/pricing](https://triplewhale.com/pricing), fetched 2026-09-09):

- Prices = **annual GMV × package** (Foundation / Automate / Enterprise). Slider on the page; **this fetch did not capture dollar outputs** (client-side slider).
- Paid packages: **12-month** subscriptions; monthly billing **or** annual prepaid (**two months free**); annual prepaid **locks the GMV tier for the year**.
- **Unlimited users**; “as many stores as needed.”
- Free plan: Triple Pixel, first/last click, Moby intro — no commitment.
- Sonar included on new paid packages (vendor FAQ).

Third-party **floors** (do not treat as official; they disagree with each other):

| Source | Claimed TW floor |
| --- | --- |
| [wetracked.io, 2026](https://www.wetracked.io/post/triple-whale-pricing) | Paid from **$219/month** monthly; Automate from **$749/month** |
| [Fairview, 2026](https://getfairview.com/blog/lifetimely-vs-triple-whale) | Starter ~**$1,490/year**; Advanced ~**$2,190/year**; Enterprise custom >$20M GMV |
| [Polar’s comparison page](https://www.polaranalytics.com/alternatives/triple-whale) | “around **$429/month** for a $1M GMV brand” |

**Polar** listing ([apps.shopify.com/polar-analytics](https://apps.shopify.com/polar-analytics)): **Core from $750/month**, “pricing based on online GMV,” annual discounts, unlimited users/history/connectors. Polar’s own marketing site prices from a **GMV slider** and does not print a single public dollar on the static page beyond the App Store floor.

**Why it prints for them:** bill grows with the account’s ability to pay; sales-assisted; free/cheap TOFU (TW) or high floor + CSM (Polar).

**CURRENT_RELIGION:** This is the **enemy shape**. Mcfly copy already: “not GMV-scaled suite tax.”

### E. Take-rate on the job’s GMV (subscriptions)

**Recharge** listing ([apps.shopify.com/subscription-payments](https://apps.shopify.com/subscription-payments), fetched 2026-09-09):

| Plan | Public price |
| --- | --- |
| Starter | **$25 / month** — no transaction fees for first **50 subscribers**; 60-day trial |
| Mid | **$99 / month** + **1.49% + 19¢** per transaction |
| High | **$499 / month** + **1.34% + 19¢** (listing: “scalable transaction rates”) |

Listing discloses **external charges may be billed separately** from the Shopify invoice.

**Why it prints:** the app **touches the money**. A take-rate is aligned. Mcfly does **not** touch checkout.

**RESEARCH_OPTION:** Never apply a take-rate to **ad spend** or **Shopify GMV** for a reporting app. That is Polar/TW’s sin in operator clothing.

### F. Order-volume ladder (profit analytics peer)

**Lifetimely** vendor canonical page ([lifetimely.io/pricing](https://www.lifetimely.io/pricing), “Last updated: 2026-09-09”):

| Plan | Monthly Shopify orders | Price |
| --- | --- | --- |
| Free | ≤50 | $0 |
| S | ≤500 | **$49/mo** |
| M | ≤3,000 | **$149/mo** |
| L | ≤7,000 | **$299/mo** |
| XL | ≤15,000 | **$499/mo** |
| XXL | ≤25,000 | **$749/mo** |
| Unlimited | 25,000+ | **$999/mo** |

14-day trial on paid; Amazon add-on **+$75/mo**; **unlimited users** on paid; if over limit **two consecutive months**, they contact you (vendor FAQ). Some 2026 comparison blogs **omit S / XXL / Unlimited** — those blogs are stale relative to this page.

**Why it prints:** feels fairer than GMV (a high-AOV store is not punished); still captures growth. **Closer to Mcfly’s peer set** than TW.

**RESEARCH_OPTION:** If religion is ever rewritten, an **order ladder** is the least-ugly scale meter. **Not recommended** while §8 is locked at ~$79 flat.

---

## 4. Listing conversion patterns that print money

### 4.1 Official constraints (the rails)

Shopify ([best practices — App listing](https://shopify.dev/docs/apps/launch/shopify-app-store/best-practices); [requirements §4](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements)):

| Element | Official rule / guidance |
| --- | --- |
| Name | ≤30 characters; **brand first**; distinctive; same recognizable name in TOML + listing |
| Icon | 1200×1200; no text, screenshots, or Shopify marks |
| Card subtitle | “Write effective app card subtitles” (requirement 4.4.1) — this is the search-result line |
| Introduction | **100 characters**; benefits; **no data claims** |
| Feature media | 1600×900; one focal point; or 2–3 min promotional video (screencast ≤25%) |
| Screenshots | 1600×900; **3–6** unique; ≥1 of real app UI; no chrome, PII, **pricing, reviews, guarantees** |
| Demo store | Link to the page that **shows the job** |
| Features / integrations | Structured features (up to **25** per category field) + integrations list |
| Claims | **No stats** in copy or images, even “verifiable” ones; no “first / best / only”; no testimonials in listing body |

**CURRENT_RELIGION:** [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md) tagline (“Cash MER… not attribution theater”) and refusal list are on-religion. Re-check character counts against the live form before submit. **Do not** put “~3–8% convert” or lift percentages on the listing.

### 4.2 Practitioner conversion physics (labeled, not official)

[Taylor Sicard, June 2026](https://taylorsicard.com/blog/shopify-app-listing-conversion) (ex-Shopify Partner Program; **his** 2026 planning table, not Shopify analytics):

| His claimed lever | His claimed band |
| --- | --- |
| Strong listing view→install | **~3–8%** |
| <25 reviews | **~1–2%** |
| 200+ reviews | **~5–8%** |
| First milestone | **50 reviews** |
| Demo video | **30–60 sec** (his conversion advice; Shopify feature-media guidance is **2–3 min** promotional — these are **different artifacts**: listing video vs feature media) |
| Test window | **7–14 days**, one variable |

Same essay’s **planning** funnel (explicitly “rough numbers I plan against,” not laws): search→listing **2–6%**; listing→install **3–8%**; install→active first session **40–70%**; active→paid **3–15%**.

**RESEARCH_OPTION:** Treat review count as the **listing** bottleneck; treat onboarding as the **paid** bottleneck. Mcfly’s design-partner path can manufacture the first reviews **off** public discovery (custom installs) — that matches religion (“serious stores over tire-kickers”) and Sicard’s “first 50 even if you give it away.”

### 4.3 What loved listings do (observed 2026-09-09)

| Pattern | Who | What the listing actually does |
| --- | --- | --- |
| Outcome in the **card subtitle** | Judge.me: “Collect unlimited product reviews…”; Polar: “Analytics that unify your data, track LTV, and grow revenue”; True Profit: “TrueProfit tracks accurate Net Profit…” | One job, merchant vocabulary |
| **Free plan available** badge | Judge.me, Loox, TW search card, Klaviyo | Lowers install friction; Shopify search UI surfaces this |
| Price **on the card** when high | Polar: **$750/month** on the search card | Qualifies buyers; also **scares** cash-desk shoppers — intentional |
| Built for Shopify + awards | Judge.me: BFS + “2025 Build Award Winner” | Trust badge next to stars |
| Integrations as social proof | Judge.me lists Klaviyo, Gorgias, Flow, Shop App | “Fits the stack I already pay for” |
| Merchant-think AI summary | Polar listing (Shopify Magic, shown at **100+ reviews** and ≥4.0) | Extra conversion block Mcfly will **not** have at launch |

**RESEARCH_OPTION:** Polar’s **$750** card price is a **filter**. Mcfly’s ~$79 (when billed) should be **visible in Pricing details**, not hidden behind “Contact sales,” so the cash-desk buyer does not bounce to a GMV suite.

---

## 5. What “loved” apps do in the first 10 minutes

### 5.1 Official Shopify onboarding religion

Shopify ([Onboarding](https://shopify.dev/docs/apps/design/user-experience/onboarding); [Setup guide](https://shopify.dev/docs/api/app-home/latest/patterns/compositions/setup-guide); [Homepage pattern](https://shopify.dev/docs/api/app-home/patterns/homepage); BFS §4.2.2–4.2.3):

- Brief, direct, **≤5 steps**. Extra steps → drop-off.
- Request information **only if necessary**.
- Non-essential onboarding is **dismissible**.
- Discrete steps **auto-complete**; show a **progress** indicator.
- After completion, **remove** onboarding UI.
- Do **not** require installing another app as a setup step.
- Homepage must show the app is **working** and, if possible, **how well** — not a static welcome.
- Primary workflows stay **in Admin** (BFS §3.1.2); no second signup if self-serve (BFS §3.1.3).
- Welcome links after plan approval can deep-link into `/welcome` ([Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing)).

### 5.2 Practitioner first-session pattern (labeled)

[Kompassify, Aug 2026](https://kompassify.com/blog/shopify-app-onboarding-guide):

- Merchants **trial several apps the same afternoon**; keep whoever shows a result first.
- First screen: one sentence of **what happens next**, a **3–5 step** checklist with **install already ticked**, **real store data** (not demo rows).
- **Do not** open on settings, plan chooser, feature tour, review-ask, or “how did you hear about us.”
- Ship a **working default**; configuration is part of the product, not a gate.
- Design the **empty-store** path (zero orders) as onboarding, not an error.
- Instrument **first seven days** (uninstalls, activation, trial convert).

Gorgias publishes the **motion** in public pricing: self-serve on cheap tiers, **1:1 onboarding** on Pro, **white-glove** on Advanced. Polar listing reviews (fetched 2026-09-09) praise **“easy setup”** and **CSM/onboarding team** — a **human** first 10 minutes at $750+, not a wizard.

### 5.3 Mapping to Mcfly’s existing surfaces

Mcfly already has the **minimum cash-desk loop** in-repo ([`docs/APP_FEATURES.md`](../../APP_FEATURES.md)): Settings (margin) → Spend → Dashboard MER → Allocation.

| Minute | Loved-app pattern | Mcfly-shaped version (research, not a build ticket) | Tag |
| --- | --- | --- | --- |
| 0:00 | OAuth, no second login | Already locked (embedded, no shop-domain form) | **CURRENT_RELIGION** |
| 0:30 | Real **sales** number on home | Pull Shopify sales for MTD immediately; empty state if zero orders | **RESEARCH_OPTION** |
| 2:00 | One required input | Contribution margin % (already Settings) — **ask it on home**, not buried | **RESEARCH_OPTION** |
| 4:00 | First “I did something” | Add **one** spend row (Meta) with yesterday’s number | **CURRENT_RELIGION** (manual spend is v1) |
| 6:00 | Visible result | MER + break-even on **this store’s** sales | **CURRENT_RELIGION** |
| 8:00 | One action | Allocation card if spend > 0 (already shipped) | **CURRENT_RELIGION** |
| 10:00 | Do **not** ask for a review | Wait until a Monday ritual exists | **CURRENT_RELIGION** + Shopify “no review-gating” spirit |

**CURRENT_RELIGION:** Do not insert pixel setup, UTM school, or a 2–4 week Northbeam-style calibration into the first session.

**RESEARCH_OPTION:** A Polaris **setup guide** (3 steps: margin, spend, see MER) with step 0 = installed is exactly Shopify’s composition. That is craft, not a new product.

---

## 6. When platforms print vs when wedges print

| Condition | Platform (TW / Polar / Klaviyo+) wins | Wedge (Judge.me / Lifetimely / Mcfly-shaped) wins |
| --- | --- | --- |
| Buyer | Team with a tool budget | Founder / one operator |
| Job | “Replace four tools” | “Answer one Monday question” |
| Proof | CSM, warehouse, pixel, 12-month contract | Number on screen in 10 minutes |
| Price | GMV or fat usage | Flat or small ladder |
| Distribution | Sales + habit + Shopify relationship | App Store reviews + free SKU |
| Failure mode | Bill shock + number conflict | Too thin → uninstall when they want an OS |

**CURRENT_RELIGION:** Mcfly wins the **right-hand column** or it does not win. Expanding left is how a $250-budget founder dies of scope ([`docs/COMPETITORS.md`](../../COMPETITORS.md)).

**RESEARCH_OPTION:** Some wedges **later** add a second meter (Loox overage, Lifetimely Amazon, Gorgias Voice). Do that only when **revenue pulls** ([`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) Phase 6+).

---

## 7. Mcfly monetization board (religion vs options)

| Move | Tag | Why |
| --- | --- | --- |
| Free design partners → announce ~$79 → Shopify App Pricing flat | **CURRENT_RELIGION** | MASTER_PLAN §8; ENTERPRISE_READY price honesty |
| 14-day trial when paid goes live | **RESEARCH_OPTION** that **fits** Shopify’s written recommendation | Does not contradict religion |
| Yearly (2 months free) as a Shopify-hosted option | **RESEARCH_OPTION** | TW uses this; Shopify App Pricing supports it |
| Forever-free MER tier | **RESEARCH_OPTION** that **tensions** religion | Faster reviews; freeloader risk |
| Order-volume ladder | **RESEARCH_OPTION** | Lifetimely shape; not GMV; still not ~$79 flat |
| GMV slider | **CURRENT_RELIGION: refuse** | Suite tax |
| Seat tax | **RESEARCH_OPTION: refuse unless enterprise SSO era** | Leaders moved off seats |
| Usage meter on “allocation runs” or “syncs” | **RESEARCH_OPTION** | Platform-native; easy to feel like SyncWith’s refresh tax — religion already hates that |
| Private $0 plan for design partners | **RESEARCH_OPTION** that **fits** | Shopify App Pricing private plans + welcome links |
| Off-platform invoice | **CURRENT_RELIGION: refuse** for a listed app | Requirement 1.2 |

---

## 8. Sources

### Official Shopify

- [Revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share)
- [About billing](https://shopify.dev/docs/apps/launch/billing)
- [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing)
- [Migrate to Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/migrating-to-shopify-app-pricing)
- [App Store requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements) (1.2, 4.2, 4.3, 4.4)
- [App Store best practices](https://shopify.dev/docs/apps/launch/shopify-app-store/best-practices)
- [Onboarding](https://shopify.dev/docs/apps/design/user-experience/onboarding)
- [Setup guide](https://shopify.dev/docs/api/app-home/latest/patterns/compositions/setup-guide)
- [BFS requirements](https://shopify.dev/docs/apps/launch/built-for-shopify/requirements) §4.2.2–4.2.3

### Live listings / vendor pricing (2026-09-09)

- [Judge.me](https://apps.shopify.com/judgeme)
- [Loox](https://apps.shopify.com/loox) · [loox.app/pricing](https://loox.app/pricing)
- [Recharge](https://apps.shopify.com/subscription-payments)
- [Polar](https://apps.shopify.com/polar-analytics)
- [triplewhale.com/pricing](https://triplewhale.com/pricing)
- [klaviyo.com/pricing](https://www.klaviyo.com/pricing)
- [gorgias.com/pricing](https://www.gorgias.com/pricing)
- [lifetimely.io/pricing](https://www.lifetimely.io/pricing)

### Third-party (labeled)

- [Taylor Sicard — listing conversion](https://taylorsicard.com/blog/shopify-app-listing-conversion)
- [Taylor Sicard — revenue share lifetime cap](https://taylorsicard.com/blog/shopify-app-revenue-share-lifetime-cap)
- [Kompassify — onboarding](https://kompassify.com/blog/shopify-app-onboarding-guide)
- [wetracked.io — TW pricing](https://www.wetracked.io/post/triple-whale-pricing)
- [Fairview — Lifetimely vs TW](https://getfairview.com/blog/lifetimely-vs-triple-whale)
- [Polar vs TW marketing](https://www.polaranalytics.com/alternatives/triple-whale)

**Confidence:** High on Shopify rails and same-day listing prices. **Medium** on TW dollar floors (slider + conflicting blogs). **Do not** publish competitor prices on mcflyads.com without a fresh fetch.
