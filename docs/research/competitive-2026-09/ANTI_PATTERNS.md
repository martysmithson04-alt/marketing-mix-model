# Anti-patterns — what killed apps / started 1-star storms

**Date:** 2026-09-09 (Wave B)  
**Mode:** RESEARCH ONLY.  
**Rule:** Every pattern cites a **public** corpse, a **visible 1-star cluster**, or an **official platform kill**. No composite fictional merchant. Mcfly has **0 reviews** — it has not earned a storm yet. It has **loaded the charges**.

---

## 0. How apps actually die (four deaths)

| Death | What it looks like | Examples | Mcfly exposure |
| --- | --- | --- | --- |
| **A. Platform ate the job** | Delist / sunset because Shopify (or the acquirer) shipped native or lost interest | Oberlo (Shopify-acquired, delisted 2022-05-12, shut 2022-06-15); Geolocation (uninstalled storewide 2025-03-24 — Markets redirection); Linkpop (retired 2025-07-07); Stocky (delisted 2026-02-02, shut 2026-08-31); Shopify Scripts (stop executing 2026-06-30) | Core job (spend next to sales) is **still missing** in Admin (Community 134251). Tail-risk if ShopifyQL `marketing_engagements` grows up. |
| **B. Acquisition / PE** | Price + support invert; old 5-stars become misleading | Lifetimely → AMP (Chef Preserve $30→$600; “AMP buys fair-priced apps”); BeProfit → Viably (billing + bot CS); Analyzify lifetime plans re-sold as add-ons (NVMOS 2026-01-20) | Not now. Lesson: named-human love is the first casualty. |
| **C. 1-star storm / rating death** | At low N, one billing or definition week permanently scars search | TW **16% 1★** on 91 (Wave A); BeProfit **~6%** on ~202; Mcfly at **5 reviews / one 1-star** ≈ dead listing (Shopify rating is **not** a simple average — [manage-app-reviews](https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews)) | **Highest near-term kill.** 7-day + paste + billing cliff. |
| **D. Silence** | 0 reviews, wrong rail, no reopen | Mcfly live: 0.0 / 0, launched 2026-09-07, filed next to **Free** pixels | **Current death.** Cheaper than a storm. Same result: no distribution. |

Oberlo / Stocky / Geolocation are **not** analytics peers. They are the reminder that “we have merchants” is not a strategy if the platform or the parent company changes its mind. Cite them as **platform-risk**, not as profit-app autopsies.

---

## 1. 1-star storms in *this* aisle (the ones that can happen to Mcfly)

### AP1 — Attributed spend pretending to be total spend

**Corpse-in-life:** BeProfit. A Farley Country Attire (UK, 2026-01-07, Taranker + listing 1★): connected Google Ads; imported **~15%** of actual spend; live chat said this is **by design** (UTM / converted traffic only). Reviewer: *“A profit tool must always show total ad spend.”* Useless for PMax.

**Also:** Community 588628 — pull **TOTAL** ad spend, not attributed-only.

**Why it storms:** the number looks like cash and **is theater**. It is Mcfly’s enemy thesis implemented as a bug.

**Mcfly load:** `CURRENT_RELIGION` is the fix. Risk is the **inverse**: allocation that assumes sales ∝ spend, or a future “smarter” connector that drops unmatched PMax. `NON_GOAL` (PR #5 P-001).

### AP2 — Unlabeled VAT / revenue definition

**Storms:**  
- Triple Whale, Kove Footwear (NL, 2026-07-06): VAT **included** in revenue; “I wonder how many people don't even realize this.”  
- TrueProfit, VocaSpark (PT, 2026-07-04): doesn’t track VAT collection. Vendor 2026-07-08: **“Shopify VAT is excluded from Net Profit.”** Same war, opposite default.

**Why it storms:** EU/UK finance. One review teaches the category to distrust you.

**Mcfly load:** Live SAMPLE says “Shopify Total Sales after returns.” Listing says “store sales.” `mer-core` does not encode tax policy. First NL/DE/UK paying store can write Kove’s review. At 0–10 reviews that is fatal.

### AP3 — Trial / uninstall / zombie billing

**Storms:**  
- TrueProfit VocaSpark: charged after trial + uninstall; refund after the 1-star.  
- TrueProfit BrickHelmets (2026-01-11, Taranker): support said uninstall to stop billing; charged while **not installed**.  
- BeProfit Adrienne Landau (2026-04-22): **$720/year unused**; will not cancel.  
- BeProfit STADIUMDREAMS (2026-01-29): cancelled in time, still took the year.  
- BeProfit Clear Cosmetics (2026-03-04; later **deleted** on Shopify 2026-07-18): months of charges; support: *“It’s like Netflix.”*  
- BeProfit Dibsies: **off-Shopify** 45-day trial auto-charge.  
- Polar/TW: **external charges** survive Admin uninstall (official Help Center).

Official physics ([uninstalling-apps](https://help.shopify.com/en/manual/apps/uninstalling-apps)): uninstall cancels **future** recurring; **current cycle may still bill**; external ≠ Shopify bill.

**Mcfly load:** 7-day trial + paste means a high fraction never activate (TSC MARKET_REPORT) and then hit day 8. First invoice + unused app = Adrienne’s plot at $39. Refund-and-reply (TrueProfit) is the only documented damage control. “It’s like Netflix” is how you get a deletion **and** a Taranker ghost.

**Also official:** merchant can 1-star for **45 days after uninstall**. Churn writes the listing.

### AP4 — Success tax / legacy bait-and-switch

**Storms:**  
- TrueProfit Brooklyn Singapore (2026-01-20): **400%** hike, **1-week** notice, or be banned.  
- TrueProfit bamtoo (2024-12-21): overage, **no notification**, bill ~4×.  
- Lifetimely Chef Preserve (2025-07-09): **$600/mo** vs **$30** under Karri; AMP “arm and a leg”; Google/Amazon spend still wrong after 30 chats.  
- Lifetimely Twitter Bikes: free ≤50 is a teaser.  
- BeProfit Daily Ritual Boutique: free plan **deleted**; entry $49; **locked out of own expense history**.  
- Analyzify NVMOS (2026-01-20): bought lifetime; features re-sold as add-ons.

**Mcfly load:** live anti-GMV copy makes this **brand-breaking** if we later meter. Flat $39 avoids AP4 **until** someone “$79 after launch”’s existing merchants the way `MASTER_PLAN.md` still daydreams. Raising list price on a 0-review app is not a storm; it is **suicide**. Raising on a 50-review app without a grandfather is Brooklyn Singapore.

### AP5 — Metered AI after the sale

**Storm:** TW Foundation. Cocaine Coffee **5★** (2026-07-20): warn about AI limits. Kove **1★**: AI help needs **credits**. Same product, two textures, one lesson: **credits are a listing wound even when the rest is “world class.”**

Lifetimely/AMP pricing FAQ (2026): *“Not today. In the future, usage above a monthly allowance will be billed by tokens. We’ll give notice.”* They are loading the gun in public.

**Mcfly load:** no AI is currently a **shield**. `RESEARCH_OPTION` “explain this number” must stay **unmetered** or we buy TW’s scar on a 0-review base.

### AP6 — Accuracy claim you cannot evidence

**Storm:** WeTracked elife 1★ — Events Manager errors, incorrect purchase value, support **could not provide methodology**. Inverse: WeTracked Suppstore 5★ “ROAS got up 30%” (reviewer claim). Shopify listing rules: no unsubstantiated claims; **no testimonials in listing copy** ([app-store-requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements)).

**Mcfly load:** “No pixels. No path credit.” is safe. “Total ROAS” as a **name** is unsafe — it sounds like Ads Manager ROAS, the thing we call a lie (`RELIGION_FLEX.md` R6). Claiming LTV:CAC on the listing without the engine is AP6 in **slow motion**.

### AP7 — Pixel that gets the ad account banned / tracking destroyed

**Storms:**  
- TW Diluu (UK, 2024-10-23): *“My Google ads account got banned because of installing this pixel.”*  
- Analyzify Duckfeet Australia (2025-04-13): ≥4 GA4 properties; App Embed **and** Customer Events; Google Ads **disapprovals**; “significant revenue loss”; vendor certified “validation complete.”  
- Analyzify British Supplements: made Shopify + GA4 **worse**.  
- Analyzify Ennebiservice (update 2023-09-04): 90% traffic drop in two days after agency work.

**Mcfly load:** religion correctly **refuses** this class. Partnering with a bad pixel (WeTracked 1★) imports it. S5 “become a pixel company” is how a cash desk inherits Diluu.

### AP8 — Data lock-in as the only retention

**Storm texture:** BioPower Pet on TW — would leave but **historical data invested**. That is not love. That is a hostage review waiting to happen.

**Mcfly load:** today Mcfly holds **nothing** worth hostage (no COGS history, no years of P&L). Good for ethics. Bad for NRR. Do not “fix” this by trapping CSV exports. A2X/Better Reports retain because the **artifact is in the merchant’s inbox/GL**, which is the opposite of lock-in and **still** retains.

### AP9 — Support lottery / highest plan, no human

**Storms:** TW Kove “almost impossible to reach”; BeProfit Cloudflops (2024-07-31) highest plan, **bot chats**, “sign the app is dying”; Moon Magic $30M/3-brand, marketing costs won’t pull, then ghosted; Analyzify Watch Factory: premium support **window expired** while tickets were open because of *vendor* delay.

**Mcfly load:** one founder inbox can be a **5-star machine** at n=20 (Kleio / Mathias; Metorik / Bryce). It becomes AP9 the week the founder is tired. Do not publish SLAs you cannot keep (Analyzify 1–2 business days).

### AP10 — Demo-gated / cannot even try

**Storm:** Polar’s three visible 1-stars — all **pre-value** (sales call, email, no personal Gmail). Trustpilot Maja (2025-11-07): **listed price ≠ quote after install**.

**Mcfly load:** self-serve $39 is the opposite. Do not add a calendar wall to look enterprise. $39 + sales call is a joke.

### AP11 — Listing / theme leftovers / “impossible to uninstall”

Category-adjacent (subscriptions, reviews widgets) more than analytics, but the **merchant memory** is real: SimpleSubscription 2026 guides tell buyers to read 1-stars for “impossible to uninstall,” orphaned contracts, surprise fees. Official: theme code often **stays**. Analytics apps that inject pixels inherit this rage.

**Mcfly load:** embedded Admin + no storefront pixel is **structurally clean**. Keep it. A future Mcfly pixel is how we buy uninstall-checklist 1-stars.

### AP12 — Review policy violations (the storm Shopify throws *for* you)

Official: asking for **positive** reviews, incentives, install-time nags, paid reviews → removal, **ranking demotion**, or unpublish. Magic summary needs **100 written + ≥4.0**.

**Mcfly load:** desperation at 0 reviews is the moment founders break this. TSC “first 50 even if you give the app away” is **not** permission to buy stars. Legal path: time-to-value + **neutral** App Bridge modal **after** first computed week.

---

## 2. What killed *distribution* without a spectacular crash

These are quieter than 1-stars and more relevant to Mcfly.

| Pattern | Evidence | Mcfly today |
| --- | --- | --- |
| **Wrong “more like this” rail** | Mcfly = Clarity / WeTracked / Parkour **Free**. Kleio has the **same rail** and still gets TW-defection 5-stars because the **product** is a profit desk | Packaging + TTV, not a blog post, moves the graph — and we do not control the graph |
| **7-day trial on a slow job** | Shopivibe + every profit listing at 14 | Loaded |
| **Name split** | MER in app / Total ROAS on listing / cash MER in MASTER_PLAN | Loaded |
| **Claimed unshipped features** | LTV, Goals, CSV | Loaded (AP6) |
| **Homework as the product** | SyncWith $4.99 already is the pipe; Sheets are $0 | Loaded |
| **Capital death by suite** | MASTER_PLAN: $250 founder vs TW OS | Still true. AP7/S5 is how you go bankrupt **and** get banned |
| **Consulting as core** | MASTER_PLAN discarded $750 diagnostics | Course $79 is a side door; Elevar-shaped onboarding at $39 is consulting in denial |

---

## 3. Mcfly-specific charges already in the magazine

Not hypothetical. Present on 2026-09-09.

1. **Blank first screen** (`ONBOARDING_BATTLE.md`) — TSC’s exact abandonment story.  
2. **7-day × paste** — AP3 waiting for one invoice.  
3. **Definition underspecified** — AP2 waiting for one VAT store.  
4. **Listing integrity** — CSV / LTV / Goals / mailto / “Paid plan adds” on a single plan.  
5. **OAuth stub vs “no OAuth” site vs Phase 2 plan** — merchant who clicks Connect feels AP6.  
6. **Allocation heuristic** — media-buyer ridicule; not a storm until someone follows it with real money.  
7. **$39 vs Kleio $29 / TrueProfit $35** — same wallet, less job. Churn reason “too expensive” will mean “no value” (TSC).  
8. **Anti-GMV sermon + possible future $79** — AP4 if executed on existing accounts.  
9. **Pixel rail ICP** — TSC mismatch. Those uninstalls may never review (silence death) or may 1-star “doesn’t track my Facebook pixel.”  
10. **0 named humans** — AP9 the first weekend the inbox is slow.

Any **two** of {3, 4, 1} in the first ten reviews and the listing is a 4.0 scar before Magic is mathematically possible.

---

## 4. Patterns that look like growth and are graves

| Temptation | Why it looks smart | Grave | Cite |
| --- | --- | --- | --- |
| Forever-free to buy reviews | TSC first 50; Lifetimely 535 | Uninstall ranking gossip; Twitter Bikes teaser 1-star; MASTER_PLAN freeloaders | TSC; Lifetimely 1★ |
| GMV / order meter to “grow ARPU” | TP/Lifetimely menus | bamtoo, Chef Preserve, Brooklyn Singapore | Taranker |
| Build a pixel because the rail said so | Clarity 2,125 | Diluu ban; Duckfeet; WeTracked evidence fail; brand hypocrisy | listings |
| Moby / credits | TW listing energy | Kove + Cocaine Coffee | TW listing |
| Sales-gated enterprise | Polar 4.9 | 6-minute 1-stars; quote ≠ list | Polar 1★; Trustpilot |
| Off-Shopify billing | Control, annual | Dibsies; official uninstall won’t cancel it | Help Center |
| “It’s like Netflix” | Honest SaaS | Clear Cosmetics | AppNavigator / deleted listing |
| Lock data in | NRR | BioPower hostage | TW listing |
| White-glove SLA | Elevar 5-stars | Analyzify missed 1–2 day SLA | AppNavigator |

---

## 5. Religion-flex: which anti-patterns are *ours* if we stay pure

Staying paste-only + anti-pixel **avoids** AP1 (if we never “attribute” spend), AP7, AP11.

Staying paste-only **causes** silence death, AP3 (unused trial), AP9 (every merchant needs a human to finish the CSV), and listing integrity stress (we claim autopilot-shaped features to look like the aisle).

Purity is not safety. Purity is **choosing death D (silence)** to avoid deaths B/C. A 1-star storm at n=8 is still worse than silence — silence can be reversed with a real TTV; a 4.0 scar at n=8 is a year.

The adult move is **avoid AP1–AP7 mechanisms** while **fixing the silence** (OAuth spend, 14-day, push artifact, definitions). That is S1 in the scorecard. Cloning TrueProfit’s meter or TW’s pixel is how we **import** a known storm.

---

## Sources

- Live listings + Wave A `REVIEW_THEMES.md` + PR #5 `REVIEW_MINING.md` (Taranker, AppNavigator, listing 1★)
- https://help.shopify.com/en/manual/apps/uninstalling-apps
- https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews
- https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements
- Oberlo: https://www.digismoothie.com/blog/oberlo-shutdown
- Geolocation: https://www.digismoothie.com/cs/blog/geolocation-app-replacement
- Linkpop: https://coywolf.com/news/ecommerce/shopify-is-shutting-down-linkpop/
- Stocky: https://getalertr.com/blog/stocky-shutdown-shopify-merchants
- Scripts: https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026
- Clear Cosmetics / BeProfit: https://appnavigator.io/app/beprofit-profit-tracker/reviews/2105768
- BeProfit billing pattern: https://www.thepricegeek.com/profit-analytics/beprofit-review/
