# Review mining — real people problems

**Lane:** public reviews of Shopify profit / ROAS / ads-analytics apps.  
**Mined:** 2026-09-09.  
**Rule:** paraphrase + cite. Short verbatim only when the sentence was captured. Never invent reviewer voice.  
**Index:** [SOURCES.md](./SOURCES.md) · mapped bank [PROBLEM_BANK_FROM_REVIEWS.md](./PROBLEM_BANK_FROM_REVIEWS.md) · rows [db/](./db/).

Shopify profit apps sit at **4.8–5.0**. That is not “no pain.” It is a marketplace where 1-star is rare and therefore **high-signal**. Triple Whale is the exception: **~16% 1-star** on a smaller n.

---

## 1. What people hired these apps to do (from 5-star jobs, not marketing)

The praise cluster is almost identical across TrueProfit / BeProfit / Lifetimely / Kleio. Operators are not buying “attribution science.” They are buying **relief from a broken Monday ritual**.

| Job they describe | Typical voice (paraphrase) | Who | Evidence |
| --- | --- | --- | --- |
| Stop rebuilding P&L in Sheets | Excel was time-consuming and not accurate enough; the app made the business “finally make sense.” | Merchant / ops | Omni Wave, BeProfit, 2025-06-28 — https://taranker.com/shopify-beprofit-profit-tracker-app-customer-reviews |
| See earnings after ads + shipping + fees in one desk | Wanted a clear picture after all costs; multi-shop view is the unlock. | Multi-store merchant | Ecolino.ro, BeProfit, 2025-12-01 — same |
| Auto-pull Meta spend + COGS so nobody updates a sheet daily | Facebook spend and COGS used to be a daily spreadsheet chore. | Merchant | Rooted Threads, BeProfit, 2025-05-20 — same |
| Get LTV / CAC math that analysts failed to build | Spent an “ungodly amount” on data analysts who could not get LTV logic right; the app does it by default. | Growth + finance | organifi, Lifetimely, 2026-07-13 — https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics |
| One source of truth, not bloated | Tried many others; keeps coming back because it is simple, fast, not bloated. | Operator | Nikura, Lifetimely, 2026-07-30 — same listing |
| Replace a suite they already resent | Kleio made it easy to say goodbye to Triple Whale; $29/mo is the reason. | Merchant | Trek Light, Kleio, 2026-08-12 — https://apps.shopify.com/kleio |
| Make ad-platform tracking “electricity” | Conversion tracking is like water/electricity; bad signals waste spend. Hired Analyzify after Google↔Meta **over-attribution**. | Media / agency-adjacent | Sacred Rituel Beauty, Analyzify, 2025-07-29 — https://taranker.com/shopify-analyzify-app-customer-reviews |
| Centralize channels so daily decisions are possible | TW praised for one place + attribution (this is the **suite job**, not the profit job). | Media buyer | Maisie F., G2 — https://www.g2.com/it/products/triple-whale/reviews?qs=pros-and-cons |

**Implication:** two product religions live in the same aisle.

1. **Cash / P&L religion** — TrueProfit, BeProfit, Lifetimely, Kleio, GoProfit. Job = “what did we keep.”
2. **Path / pixel religion** — Triple Whale, Polar, Analyzify, Northbeam (off-store). Job = “what drove it” or “feed the algorithms.”

Mcfly’s current religion sits in (1). Review pain in (2) is still useful: it is how merchants get **hurt** when they buy the wrong job.

---

## 2. App teardowns

### 2.1 TrueProfit — https://apps.shopify.com/trueprofit

**Surface:** 5.0, ~880–899 reviews. Accounting-category profit desk. Order-tier pricing + **per-extra-order surcharge** (listing showed $0.07/extra order, cap mentioned around $1.00 in one scrape — verify before quoting prices externally).

**What 5-stars hire it for:** net profit without doing the math; shipping-cost honesty; mobile check; support named as people (Durra, Vani, Lilly).

**1-star cluster (small n, sharp):**

| Theme | Paraphrase + snippet | Who / when | Cite |
| --- | --- | --- | --- |
| Trial/uninstall still billed | Installed twice; charged after trial even though they uninstalled day one of the period. | VocaSpark, PT, 2026-07-04 | listing 1★ |
| Variant costs go stale after reinstall | Reinstall left variants outdated; **no self-serve refresh** — must ticket. | same | listing 1★ |
| VAT / tax not in “true” profit | Reviewer: does not track VAT collection. Vendor reply: **Shopify VAT is excluded from Net Profit.** | same + vendor 2026-07-08 | listing 1★ |
| Hidden order overage | Sales uplift for two months → billed **quadruple** subscription + fee; **no notification** that orders now cost extra. | bamtoo, DE, 2024-12-21 | https://taranker.com/shopify-trueprofit-app-customer-reviews?filter-by=1 |
| Legacy bait-and-switch | 3-year user given **1-week notice** to accept a **400%** hike on a founder-legacy plan or be banned. | The Brooklyn Singapore, 2026-01-20 | same |
| Charged after uninstall | Support told them uninstall to stop billing; charged again while **not installed**; 3 messages, 2 weeks silence. | BrickHelmets, 2026-01-11 | same |
| Wrong ad spend + returns | Login broken for days; “wrongly counts ad spend, returns etc.” | BeShaped, PL, 2025-09-18 | same |
| Trial then charge after promised extension | Analytics inaccurate; 12 days to “fix”; promised trial extension; charged a full month; refund fight. | Sunnys UAE, 2025-06-27 | same |
| Google Ads connect is folklore | Tried connect 5×; support said **delete all browser data**. Other customers had the same bug, unfixed. | myvial, 2024-09-18 | same |
| Transaction fees are a formula, not Shopify actuals | Fees calculated by formula though Shopify has the real fee; reviewer names **BeProfit as able to pull Shopify fees**. | WASABI Knives, DE, 2021-05-10 | listing 1★ |
| Config vs “IT will fix it” | Data all wrong; CS said IT would fix; then blamed **merchant configuration**. | Wine Not HKG, 2024-07-22 | listing 1★ |

**Deep read:** TrueProfit wins the *job* (net profit desk) and loses on **pricing honesty + cost-basis mutability**. The VAT reply is a finance landmine: EU merchants who think “net profit” means after tax collected/remitted will not match their books. The WASABI review (old, still on the 1★ filter) is the same class of problem as BeProfit’s attributed-spend lie: **the app invents a cost the ledger already knows**.

---

### 2.2 Lifetimely (now AMP) — https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics

**Surface:** 4.9, ~460–535 reviews. P&L + cohort LTV. **Order-volume ladder** (Eightx 2026: free ≤50 · $79 · $149 · $299 · $499 · $749 · $999; Amazon +$75). Every paid tier is the same product — you pay for **volume + support intensity**.

**What 5-stars hire it for:** source of truth; LTV by customer/tag/product; analysts who could not reproduce the math; “not bloated.”

**1-star / 2-star cluster:**

| Theme | Paraphrase + snippet | Who / when | Cite |
| --- | --- | --- | --- |
| Volume tax as rip-off | Paying **$600/month** on volume pricing; used to pay **$30** under founder Karri. Price is not even the main issue — support is. | Chef Preserve, US, 2025-07-09 | https://taranker.com/shopify-lifetimely-lifetime-value-and-profit-analytics-app-customer-reviews?filter-by=1 |
| Acquisition killed the product | AMP buys fair-priced apps and charges “an arm and a leg.” Discount all pre-AMP 5-stars. Inaccurate **Google Ads + Amazon ad spend**. 30 chats + 10 emails; 20 days unresolved; “hundreds of screenshots.” | same | same |
| Free plan is a teaser | “FREE up to 50 orders, but you cannot do anything without starting to pay.” | Twitter Bikes, US, 2025-07-08 | same + listing |
| Paid plan extortionate / free pathetic | One-line 2026 review. | Brat, UK, 2026-06-26 | listing 1★ |
| €150/mo without live support | Prices do not load; support takes hours; switched before they answered. | Sellsbydanchic, DE, 2025-05-23 | listing 1★ |
| Post-purchase upsell breaks the books | Numbers “not relevant at all” with a post-purchase upsell. Support answers fast **to close tickets**, not to fix; 10 days wasted. | Koss Design, IE, 2024-11-28 | listing 1★ |
| Amazon add-on = second full price, still buggy | Amazon plugin as expensive as Shopify plugin; months of tickets; promised fix after cancel; still buggy. Wants **one place** for Shopify + Amazon. | carnivoro, DE, 2025-09-02 | listing 1★ |
| Trial downgrade still billed top tier | Downgraded in trial; charged the most expensive plan. Also: **weighted LTV inaccurate**. | Armor Class, DK, 2024-05-15 | listing 1★ |
| AMP focus = upsells, not merchant value | Post-AMP: slower, benchmarks broken, prices “extremely high” vs old. | Papasplatz, DE, edited 2025-09-14 | listing 1★ |

**CFO-adjacent (secondary, Eightx, not a store review):** data refreshes every few hours — **unusable for intraday MER**. Amazon daily. Shopify-only. Sweet spot they claim: $50k–$300k monthly revenue. Below ~$30k/mo a spreadsheet wins.  
https://eightx.co/blog/compare/reviews/lifetimely-for-ecommerce-review

**Deep read:** Lifetimely is the **closest cousin to a cash desk that then taxes success**. The Chef Preserve review is the single richest pain document in the profit-app aisle: volume pricing + support bureaucracy + ad-spend distrust after an acquisition. AMP is a **stakeholder conflict in one company**: merchant value vs portfolio upsell.

---

### 2.3 BeProfit — https://apps.shopify.com/beprofit-profit-tracker

**Surface:** 4.4–4.5, ~173–202 reviews. **Highest 1-star rate among profit desks (~6%)**. Acquired by Viably (vendor replies, 2025-02). Plans ~$49–$249; free plan **removed**.

**What 5-stars hire it for:** multi-shop / Shopify+Amazon rollup; “live CPA and BCAC”; markets; API into BI; spreadsheet retirement.

**1-star cluster (this is the gold vein):**

| Theme | Paraphrase + snippet | Who / when | Cite |
| --- | --- | --- | --- |
| **Attributed spend ≠ total spend** | Connected Google Ads; imported **~15%** of actual spend. Live chat: **by design** — only counts spend attributable via UTMs / converted traffic. Inflates profit. “A profit tool must always show total ad spend.” Useless for PMax. Wasted half a day. | A Farley Country Attire, UK, 2026-01-07 | https://taranker.com/shopify-beprofit-profit-tracker-app-customer-reviews |
| Zombie annual billing | Someone installed in 2023; company paid **$720/year**, never used; will not cancel/refund even after pre-charge cancel request. | Adrienne Landau, US, 2026-04-22 | listing 1★ |
| Cancel still takes the year | Timely cancel; still debited **full annual**. Support “stalls.” | STADIUMDREAMS, 2026-01-29 | Taranker |
| Profit calc prefs broken | “Not calculating the profit correctly. Especially Calculation Preferences.” | Celluweg, 2026-01-17 | Taranker |
| Cannot leave | One-day user; chat refused deactivation; left on read. | Girl Stitch, US, 2025-07-30 | listing 1★ |
| Off-Shopify 45-day trial auto-charge | Side-channel trial; not told it would auto-bill. | Dibsies, US, 2025-02-10 | listing 1★ |
| Refund “policy” not in T&Cs | Same-day renewal refund refused; reviewer could not find the no-refund clause. | Toxic Envy Boutique, US, 2025-02-03 | listing 1★ |
| Products missing → cannot enter COGS → all data skewed | Escalated; week and a half, then still unfixed weeks later. | PuppyPad, US, edited 2024-04-02 | listing 1★ |
| Highest plan, no human | App good historically; now **bot chats**, email dead, 2 weeks wait; **highest plan**, no AM. “Sign the app is dying.” | Cloudflops Sverige, SE, 2024-07-31 | listing 1★ |
| $30M / 3-brand: marketing costs will not pull | “Does not pull marketing costs correctly”; agent Anthony; then ghosted. | Moon Magic, SG, edited 2026-03-04 | listing 1★ |
| Free plan deleted, reports locked | Was on paid &lt;$30, dropped to free; free vanished; entry **$49**; locked out of own expense history. | Daily Ritual Boutique, US, 2024-04-17 | listing 1★ |

**Deep read:** BeProfit is the clearest **anti-Mcfly** (and anti-cash) failure mode in the aisle: a “profit” number that **hides unattributed spend**. That is path-religion smuggled into a P&L. It is also the clearest **billing-as-product** failure (zombie subscriptions, annual traps). Viably acquisition reviews read like Lifetimely/AMP: support quality is the first thing PE kills.

---

### 2.4 Analyzify — https://apps.shopify.com/analyzify

**Surface:** 4.7, ~271–313 reviews. **Not a profit desk.** Server-side GA4 / Meta / TikTok / Google Ads tracking + paid implementation.

**What 5-stars hire it for:** “tracking as electricity”; white-glove GTM they dare not touch; server-side so platform numbers “align”; agency implementing across many stores.

**1-star cluster (implementation as a product is a product risk):**

| Theme | Paraphrase + snippet | Who / when | Cite |
| --- | --- | --- | --- |
| Recurring outage → sales drop | Worked, then died; paid support to fix (not their fault); died again; **significant sales drop**; left after years. | MakeMyGift, CA, 2026-05-08 | https://appnavigator.io/app/analyzify/reviews/?rating=1 |
| Premium support expires while tickets open | Premium plan; first ticket 2025-08-07; **zero critical issues resolved**; support window expired 2025-09-16 because of *their* delay. Google Ads **cart data** still wrong. | The Watch Factory, IN, 2025-09-24 | same |
| $295 “professional implementation” no-show | Listed 1–2 business days; two days later nothing; self-installed from docs. | Raregen Hair, HK, 2025-09-11 | same |
| “Destroys tracking” | Made Shopify + GA4 tracking worse. | British Supplements, UK, 2025-09-09 | same |
| Quadruplicate GA4 + Google Ads disapprovals | Multiple GA4 properties at once (reviewer: **≥4** on one store). App Embed **and** Customer Events firing the same events. Google Ads disapprovals, “significant revenue loss.” Support certified “validation complete” while UI still showed the mess. Advice: stay near **native Shopify**. | Duckfeet Australia, 2025-04-13 | same |
| Paid setup, then pay again for any change | “Expensive setup then a very limited time after which they charge you again.” | Tech Instrumentation, US, 2024-07-01 | listing 1★ |
| Fiverr is cheaper than their support | Huge store; support treats urgency lightly; “$50–100 on Fiverr… 8 times over.” | 5minskin, US, 2024-05-16 | listing 1★ |
| Six stores, one GTM, months late | Paid licenses for **six identical-codebase stores**; first prod beta after **five months**; then a critical bug (order name reference not tracked) with **a month of silence**. | Tameson.com, NL, edited 2024-06-06 | AppNavigator 1★ |
| Help-center bounce + upsell to humans | Pay $$$, get article links; pay more for a human to fix. | Good Health Co, US, 2025-06-17 | listing 1★ |
| Lifetime plan, features re-sold as add-ons | Bought “One Time / lifetime”; later add-ons charge for things “included in our original legacy plan.” | NVMOS, 2026-01-20 | https://taranker.com/shopify-analyzify-app-customer-reviews |
| Agency work that nuked audiences | (Updated Italian review) Admin access to GA4/Ads; **90% traffic drop in two days, 95% revenue in 10 days**; no error admitted. | Ennebiservice, 2023-09-04 update | AppNavigator 1★ |

**Deep read:** Analyzify is the **agency/media-buyer job** colliding with **merchant cash**. Sacred Rituel Beauty hired them because Google and Meta were **over-claiming the same sale** — the exact Mcfly thesis — then paid a tracking vendor to *feed the platforms better*. Duckfeet is the failure mode: the “fix” corrupts the measurement layer and **Google pauses spend**. This is RESEARCH_OPTION territory (pixels/CAPI), not current religion — but the **pain** (platforms lie; merchants pay priests) is on-religion.

---

### 2.5 Triple Whale — on Shopify store — https://apps.shopify.com/triplewhale-1

**Surface:** 4.0–4.1, **85–92 reviews**, **16–17% 1-star**. This is the only suite in the set whose App Store rating looks like a real product, not a review-harvested 4.9.

G2 is the opposite theater: **~4.5 / 480+** — sales-assisted, seat-wide, happier sample.

**What 5-stars hire it for:** scale from starter → enterprise package; “would not have grown without it”; one Juan who actually answers. Also: **AI credit surprise** even in a 5-star (Cocaine Coffee, 2026-07-20: warn about Foundation AI limits).

**1-star / 2-star cluster:**

| Theme | Paraphrase + snippet | Who / when | Cite |
| --- | --- | --- | --- |
| **VAT left in revenue** | “casually … includes VAT in your revenue (revenue should never be including VAT). I wonder how many people don't even realize this.” Also: CS unreachable; AI help needs **credits**; UI unchanged for years. | Kove Footwear, NL, 2026-07-06 | https://appnavigator.io/app/triplewhale-1/reviews/2272366 |
| Small shop, enterprise UI, data lock-in | Full of bugs; UI terrible; menus a “cluster.” Geared to **large enterprises with many users**; for a small op it is overload. Would leave if not so much **historical data invested**. | BioPower Pet, US, 2026-04-02 | listing (also 2★-adjacent in scrapes) |
| Onboarding theater, CSM void | Polished sales onboarding; once contracted, CSM unsure, “I’ll ask someone else,” no actionable answers. | Zamage, US, 2025-12-12 | listing 1★ |
| Bugs they caused take days | Critical issues, often on TW’s side; days even after follow-ups; hits **business performance**. | Pangama Jewelry, US, 2025-07-11 | listing 1★ |
| Monthly billed = monthly **contract**; 60-day guarantee dead | Fine print; support silent. | Tooltekt, UK, 2024-11-18 | listing 1★ |
| Pixel → Google Ads ban | “My Google ads account got banned because of installing this pixel.” | Diluu, UK, 2024-10-23 | listing 1★ |
| Account collision / no disconnect | Friend logged in on their laptop; new install **attached store to friend’s account**; no self-serve detach. | Saabuni, UK, 2024-09-12 | listing 1★ |
| Impossible cancel / no refund | “They'll never issue a refund… nearly impossible to cancel.” | ETHNIK LIVING, US, 2024-11-06 | listing 1★ |
| Cannot start: error + no human | 2★: cannot even launch; setup error; “absolutely no customer service.” | Noirblanc, DE, 2025-01-19 | listing 2★ |
| G2: $600/mo, 3 months, no support | Concept good; **over $600/month**; waiting three months; only “we’re working on it.” | G2 cons cluster | https://www.g2.com/it/products/triple-whale/reviews?qs=pros-and-cons |
| G2: attribution “constantly faulty” | CS worst in years; attribution unreliable; “more harm than benefit.” | same | same |
| G2 agency: 50% mis-sourced | Agency partner, performance pricing: tech **fails to attribute to the original source ~50% of the time**; “failing constantly now after the AI era.” | Ash O., G2, 2.5/5 | same |

**Vendor-owned admission (not a review, but explains the fights):** order edits / Loop returns can make **day-level Shopify ≠ TW**. TW parks edited values on the **original order date**.  
https://triplewhale.readme.io/docs/why-do-my-order-based-sales-metrics-not-match-between-shopify-and-triple-whale

**Secondary operator (Eightx):** treat as decision-support, **not books**. Pixel only sees post-install. Wait one journey length before trusting.  
https://eightx.co/blog/compare/reviews/triple-whale-for-ecommerce-review

**Deep read:** Triple Whale’s App Store 1-star rate is the **honest suite score**. Themes: (a) finance definition (VAT), (b) lock-in via history, (c) sales ≠ success, (d) pixel risk, (e) AI metered after the sale. Kleio’s 5-stars are literally “we left TW for $29.” That is a **price + religion** defection, not a feature defection.

---

### 2.6 Polar Analytics — on Shopify store — https://apps.shopify.com/polar-analytics

**Surface:** 4.9, ~103–116 reviews, **three 1-stars**, all **pre-value** (could not even try).

| Theme | Paraphrase | Who / when | Cite |
| --- | --- | --- | --- |
| Sales-call gate | “before you can try — it requires a sales call.” (6 minutes on the app) | dryoasisplants, US, 2024-10-01 | https://appnavigator.io/app/polar-analytics/reviews/1550354 |
| Email verify never arrives | Uninstalled in 6 minutes. | Skechers.dk, 2023-05-12 | listing 1★ |
| No personal Gmail | Gmail button then “private emails not allowed” — cannot use. | Minseart, DE, 2025-04-25 | listing 1★ |

**Off-store, named operator (Trustpilot, 2025-11-07, Maja):** Shopify-listed price **≠ sales quote after install** (sales much higher). Paid anyway. Missing **YoY revenue line chart**. Inventory **×6** because 6 Shopify stores share one warehouse — 1.5 months, still told “unusual setup.” Status = merchant chases; vendor says fixed, it is not.

https://www.trustpilot.com/reviews/690da52c91938d8e1b9286b7

**5-stars hire Polar for:** one place for ecom + marketing data; MTA + incrementality as a *partner* (Chicory, 2025-09-24); dedicated AM onboarding. That is a **data-team / agency** job, not a Monday cash desk.

**Deep read:** Polar’s App Store page is a **demo-gated warehouse**. Pain is procurement + GMV tax + multi-store inventory identity — finance/ops, not ROAS. The three 1-stars are a **self-serve allergy**.

---

### 2.7 GoProfit + Kleio (undercutters — why they exist)

These are not “top” by review volume. They exist **because of the pains above**.

- **GoProfit** https://apps.shopify.com/go-profit — 4.8 / 85. Marketing site (competitor-authored, treat as such) weaponizes TrueProfit **order overage**. Listing still shows **$0.2 per extra order** on some tiers — so the category has not escaped the tax; it has rebranded it.
- **Kleio** https://apps.shopify.com/kleio — 5.0 / 20, **flat $29**, all features, high order ceiling. Reviews explicitly **replace Triple Whale**. Digismoothie (secondary): Kleio **omits ad attribution** on purpose — contribution margin over path credit. That is Mcfly-adjacent religion at a dumpster price.

---

### 2.8 Northbeam — not on Shopify store (context only)

No App Store 1-star corpus this pass. Public pattern from vendor docs + directories:

- Entry **~$1k/mo**, overkill under ~$20–50k ad spend.
- Vendor docs: platform vs Northbeam discrepancies are **expected** (different models). Missing Northbeam UTMs = spend and revenue on **different line items**.
  https://docs.northbeam.io/docs/setting-up-google-ads-for-northbeam
- SalesHive vendor page (secondary): some users want **blended / MER-style** views instead of heavy modeled performance.

This is the **finance-vs-court-of-appeal** product. Pain is ceremony + price + UTM priesthood — not “I cannot see profit.”

---

## 3. Recurring themes (frequency × depth)

Scored from **distinct review events** in this pass (not star %). A theme with 8 events across 4 apps is more real than 80 5-stars saying “great support.”

| ID | Theme | Apps | Events in this pass | Depth |
| --- | --- | --- | --- | --- |
| T-SPEND | Profit number **drops unattributed ad spend** | BeProfit (smoking gun), community checklist, Moon Magic | 3+ named + 1 community rule | **Critical** — opposite of cash MER |
| T-TAX | Tax/VAT definition wrong or unexplained | TW (VAT **in** revenue), TrueProfit (VAT **out** of net, no collection view) | 2 named + vendor replies | **Critical** for EU/UK finance |
| T-COGS | Cost basis stale / missing / rewrite | TrueProfit variants, BeProfit missing products, community “timestamp COGS,” Lifetimely upsell | 5+ | **Critical** |
| T-OVERAGE | Volume / order / GMV tax + surprise bill | TrueProfit bamtoo + 400% legacy, Lifetimely $600, Polar Trustpilot, TW GMV, BeProfit free-plan kill | 8+ | **Critical** |
| T-CANCEL | Cannot leave; zombie charges; annual trap | BeProfit ×4, TW ×2, TrueProfit uninstall charge | 7+ | High |
| T-SUPPORT | Sale/onboarding ≠ ongoing support | TW Zamage + G2 $600, BeProfit post-Viably, Analyzify premium expiry, Lifetimely AMP | 10+ | High |
| T-LOCKIN | History / multi-year data as prison | BioPower Pet TW; Analyzify lifetime rebill; TrueProfit legacy ban | 3 | High |
| T-PIXEL | Tracking “fix” breaks ads or accounts | Diluu TW pixel ban; Duckfeet GA4 quad; Ennebiservice 95% revenue; British Supplements | 4 | High (media) |
| T-SHEETS | Spreadsheet is the status quo and it lies | Shopify Community OP; Omni Wave; Rooted Threads | 3+ | The default JTBD |
| T-MULTI | Multi-store / Amazon / warehouse identity | Polar inventory ×6; BeProfit multi-shop praise; Lifetimely Amazon add-on; Tameson 6 licenses | 4 | Agency + multi-brand |
| T-GATE | Cannot try without sales / work email | Polar ×3 1-stars | 3 | Mid (enterprise motion) |
| T-AI | Metered AI after the sale | TW Kove + Cocaine Coffee | 2 | Mid |
| T-FEES | Payment fees modeled, not pulled | TrueProfit WASABI vs Shopify actuals | 1 (old) but structurally important | Mid |
| T-MATCH | Shopify day sales ≠ suite day sales | TW vendor doc; community MER vs P&L | vendor + operators | **The finance fight** |

---

## 4. Agency vs merchant vs finance — conflicts the reviews already contain

These are not personas we invented. They are **disagreements inside the same threads**.

### 4.1 What each stakeholder is optimizing

| Stakeholder | Winning number | Losing number | What they punish vendors for |
| --- | --- | --- | --- |
| **Merchant / founder** | Net cash after *all* spend; predictable SaaS bill | Platform ROAS; surprise overage | Hidden order tax, cannot cancel, numbers they cannot explain to a partner |
| **Media buyer / growth** | Channel ROAS, pixel health, CAPI, “what to scale today” | Blended MER that “hides” their channel | Tracking outages, Google disapprovals, 50% mis-attribution (Ash O.) |
| **Agency** | Multi-account, client-ready export, performance pricing, white-glove | Per-store license × N, sales-gated tools, CSM who cannot answer | Tameson 6× license for one GTM; Polar demo wall; TW agency 50% miss |
| **Finance / CFO / bookkeeper** | VAT-ex revenue, Shopify payout, timestamped COGS, QuickBooks | Modeled revenue, tax-gross sales, rewritten history | Kove VAT; TrueProfit VAT exclusion without a collection view; Polar inventory × locations; Eightx “not books” |

### 4.2 Conflict set (review-grounded)

**C1 — Total spend vs attributed spend (merchant+finance vs media+vendor)**  
A Farley Country Attire vs BeProfit live chat. Community echo: “make sure it pulls TOTAL ad spend… Some tools only count spend they can match… which massively understates your real ad costs.”  
https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628  

If Mcfly ever “improves” MER by dropping unmatched spend, we become BeProfit.

**C2 — VAT-gross marketing revenue vs VAT-ex books (media vs finance)**  
Kove Footwear: TW leaves VAT in revenue; “how many people don't even realize.” TrueProfit’s opposite sin: exclude VAT from net and do not show collection. Same war, two wrong defaults.

**C3 — Intraday MER vs daily/weekly P&L (buyer vs CFO)**  
Eightx: Lifetimely lag makes **intraday MER** impossible; TW is the “better” (theater) answer. Community $15–20k/mo merchant: TW is a **fighter jet**; they want net profit per order, not MTA.

**C4 — Historical lock-in vs switch (ops vs vendor)**  
BioPower Pet will not leave TW because of history. TrueProfit threatens a ban if they refuse a 400% hike. Analyzify resells “lifetime.” Switching cost is the moat; reviews call it a **trap**.

**C5 — Agency seat vs merchant license (agency vs vendor finance)**  
Tameson: six stores, one codebase, one GTM, six licenses. Polar Trustpilot: six stores, one warehouse, inventory ×6. Agencies need **one brain, many shops**. Vendors bill **N brains**.

**C6 — Onboarding theater vs production support (sales vs operator)**  
Zamage (TW), Analyzify premium window, BeProfit post-acquisition bots, Lifetimely AMP screenshot bureaucracy. The person who sold “world class” is not the person who fixes Friday’s spend.

**C7 — Pixel priesthood vs cash desk (agency vs founder)**  
Sacred Rituel Beauty paid Analyzify because Meta and Google **over-attributed**. Duckfeet paid them and got **disapproved campaigns**. Same category, opposite outcome. The founder still does not know if ads cleared the till.

**C8 — Success tax (finance vs vendor)**  
bamtoo (TrueProfit), Chef Preserve (Lifetimely), Polar GMV quote-after-install, TW GMV. The better the year, the higher the analytics bill — **while the number they bought is “are we profitable.”**

---

## 5. Community checklist (operators already know the kill tests)

From the Shopify Community thread (not an app review; operators teaching each other). Treat as **job spec**:

1. Gross sales − discounts − refunds − **COGS per variant** − **total** ad spend − transaction fees − recurring expenses = net profit.
2. **Timestamp COGS** on the order. Today’s supplier price must not rewrite last month.
3. Pull **total** Meta/Google spend, not attributed spend.
4. Prefer order-level + SKU profit, not only daily totals.
5. Price must make sense at **$15–20k/mo** — many $49–$149 apps fail this.
6. TW is overkill if you are not spending like a mid-market media team.

https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628

This is closer to Mcfly’s religion than any suite listing.

---

## 6. What we must not conclude

- **4.9 ≠ loved.** It means the unhappy leave or never review. BeProfit’s 6% 1-star and TW’s 16% are the honest ones.
- **Named support heroes** (Juan, Durra, Anthony, Oğulcan) are not a feature. They are **a bus-factor**. When they vanish (AMP, Viably), the 1-stars appear.
- **“Accurate” in a 5-star** often means “matches my vibes / my sheet,” not “reconciles to payout.” Finance will still pick a fight.
- Editorial “best profit app 2026” posts are **affiliate-shaped**. Used only as maps.

---

## 7. Mcfly-facing synthesis (research, not a build order)

**Confirmed by reviews, on current religion**

1. People want **one cash desk** that includes **all ad spend**, fees, refunds, shipping — not a model.
2. They hate **success taxes** (orders, GMV, seats).
3. They cannot leave suites because of **history + contracts**.
4. EU/UK finance will reject any revenue that is silently tax-gross.
5. Spreadsheet is the competitor to beat, not Triple Whale, for the $15–50k/mo band.

**RESEARCH_OPTION (pain is real; religion would flex)**

1. **Order-level / SKU contribution** (community + BeProfit praise). Current Mcfly is period MER.
2. **Timestamped COGS + variant cost refresh** (TrueProfit / BeProfit / community).
3. **LTV / CAC payback** (Lifetimely 5-stars; organifi). Not cash MER.
4. **Multi-store + Amazon + shared-warehouse identity** (Polar, BeProfit, carnivoro).
5. **QuickBooks / payout recon** (Lifetimely integration praise; Eightx books warning).
6. **VAT modes**: ex / inc / collection — a **toggle with a definition**, not a silent default.
7. **Agency rollup, one license** (Tameson, Ecolino).
8. **Tracking/CAPI** (Analyzify job) — refuse under current religion; the *pain* is still “platforms over-claim.”

Mapped rows: [PROBLEM_BANK_FROM_REVIEWS.md](./PROBLEM_BANK_FROM_REVIEWS.md).
