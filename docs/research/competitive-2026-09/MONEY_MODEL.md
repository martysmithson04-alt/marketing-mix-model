# Money model — ARPU, expansion, churn drivers (public signals only)

**Date:** 2026-09-09 (Wave B)  
**Mode:** RESEARCH ONLY.  
**Honesty rule:** This file contains **no Mcfly ARPU, no Mcfly churn %, no install forecast, no “we will hit $X MRR.”** Partner Dashboard is the only place those numbers can live. What follows is (a) official Shopify take-rate math on **list prices**, (b) **observed** competitor price *shapes*, (c) public 1-star / forum drivers of churn and expansion. TSC / StoreLeads / Shno figures are `MARKET_REPORT`, not Mcfly metrics.

---

## 0. Brutal Mcfly read (today)

Live list price: **$39 / store / month**, 7-day trial, **one plan**, no annual, no seats, no order meter, no GMV slider, no Amazon add-on, no agency SKU ([listing](https://apps.shopify.com/mcfly-analytics-public), [mcflyads.com/pricing](https://mcflyads.com/pricing)). Course: **$79 one-time** (side door). Repo drafts that still say free DP → ~$79 are stale (`MASTER_PLAN.md` §8, `site/pricing.html` still mentions ~$79).

Implications that do **not** require invented volume:

1. **ARPU ceiling = $39** (plus maybe a $79 course once). There is no public upgrade path. TSC’s own pricing essay (MARKET_REPORT): *if pricing is a flat fee with no usage ceiling and no upgrade path, ARPU cannot rise* ([shopify-app-economics-one-chart](https://taylorsicard.com/blog/shopify-app-economics-one-chart)).
2. **NRR cannot exceed 100% from expansion** because expansion is structurally zero. Accounts can only stay or leave.
3. **Net to Mcfly on $39** (official Shopify, not a forecast):
   - Processing **2.9%** on all billing ([revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share)).
   - Revenue share: **0%** on the first **$1,000,000 USD lifetime** gross app revenue earned from **2025-01-01**; **15%** after. Refunds do **not** reduce the gross used for share. High-volume exception ($20M+/yr App Store or $100M+ company) pays 15% on all — irrelevant to Mcfly.
   - So **per paying store, while under the $1M lifetime cap:** $39 × (1 − 0.029) = **$37.87** before tax/regulatory fees. After the cap: $39 × (1 − 0.15 − 0.029) = **$32.01** if you naively stack (Shopify documents them as **separate** charges; do not treat 17.9% as an official blended rate — compute from Partner invoices).
4. **One Polar Core seat at the listing floor ($750)** equals **~19 Mcfly stores** at $39 list, before anyone’s costs. Polar also has CS. Mcfly at $37.87 net cannot buy Polar’s onboarding.
5. **TrueProfit Basic is $35** + $0.30/extra order, surcharge cap **$300** on Basic ([trueprofit.io/pricing](https://trueprofit.io/pricing), listing). Same wallet, **expansion built in**. Mcfly is priced like the entry of the profit cluster and scoped like a Sheet.

The live site’s anti-GMV-tax copy is a **moral**. It is also a **revenue-model refusal**. That is allowed. It is not free. Volume or an agency SKU must do the work the meter would have done — and Mcfly has neither reviews nor a portfolio SKU.

---

## 1. Official money rails (Shopify)

Source: https://shopify.dev/docs/apps/launch/distribution/revenue-share · Help Center Partner earnings · changelog 2025-04-24.

| Rail | Rule |
| --- | --- |
| App Store registration | **$19** one-time per Partner account |
| First $1M lifetime gross (from 2025-01-01) | Developer keeps **100%** (still pays **2.9%** processing + tax) |
| After $1M | Shopify **15%** share on gross; processing still 2.9% |
| Gross definition | **Gross sales, not net.** Refunds do not come off the share base. All apps + Associated Developer Accounts aggregate. |
| Billing | Must go through Shopify App Pricing for public apps. Off-platform billing is a compliance / 1-star factory (BeProfit off-Shopify trial — PR #5). |
| Trials | Configurable days; **180-day** anti-reinstall window; trial attaches to **new** subscriptions only ([offer-free-trials](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials)). |
| Uninstall | Cancels **future** recurring charges. Current cycle may still bill. External charges are **not** cancelled by uninstall ([help.shopify.com uninstalling-apps](https://help.shopify.com/en/manual/apps/uninstalling-apps)). |
| Reviews after churn | Merchant can review within **45 days of uninstall**. Churn is a listing event. |

Wave A `APP_STORE_MARKET.md` still mentioned a 20% default in one sentence. **Correct to official 2026 text:** 0% then 15% + 2.9%, not 20%. Do not publish the old 20% as current law.

---

## 2. Observed ARPU *shapes* (not competitor ARR)

We do **not** know TrueProfit’s ARPU. We know their **menu**. Treat every dollar below as a **list price**, 2026-09-09 unless noted.

### Shape 1 — Flat, no expansion (Mcfly, Kleio)

| App | List | Trial | What you get | Expansion |
| --- | --- | --- | --- | --- |
| Mcfly | **$39** | 7-day | Spend-vs-sales desk (paste) | **None** |
| Kleio | **$29** | 14-day | P&L, LTV, ad connect, MCP, unlimited users, 1M orders in DB | **None** (founder pitch: “$29/month. Period.” — [getkleio.com](https://getkleio.com/)) |

Kleio is the existence proof that **flat + profit + auto ads** can print 5.0/20 and **TW defections** without a meter. It is also the existence proof that Mcfly’s $39 flat is **not a unique moral**. Kleio is $10 cheaper, 14 days longer, and ships the job reviewers name.

`RESEARCH_OPTION`: if we stay flat, we are choosing Kleio’s money model with **less product**. That is not a strategy. That is a donation to Kleio.

### Shape 2 — Order ladder + overage (TrueProfit)

[trueprofit.io/pricing](https://trueprofit.io/pricing) + listing (re-fetch: 5.0 / **880** visible on one scrape, Wave A had 899 — do not freeze N):

| Plan | Base | Orders | Extra | Surcharge cap |
| --- | --- | --- | --- | --- |
| Basic | $35 | 300 | $0.30 | $300 |
| Advanced | $60 | 600 | $0.20 | $500 |
| Ultimate | $100 | 1,500 | $0.10 | $700 |
| Enterprise | $200 | 3,500 | $0.07 | $1,000 |

**List-price math (not ARPU):** a store at 800 orders/mo on Basic pays $35 + 500 × $0.30 = **$185** unless they upgrade to Advanced $60 (600 included + 200 × $0.20 = **$100**). The meter **forces** the conversation. MerchantFlow (2026-06, MARKET_REPORT) attacks this as surprise invoices up to **$1,000/mo** on Enterprise cap.

**Public pain:** bamtoo (Taranker 1★, 2024-12-21): two-month sales lift → billed **quadruple**, no notification. Brooklyn Singapore (2026-01-20): **400%** hike on a founder-legacy plan, 1-week notice. This is expansion **and** a 1-star factory. See `ANTI_PATTERNS.md`.

TrueProfit FAQ: no yearly plan; **5+ stores** can get a “special discount.” Multi-store is a **sales** expansion, not a listing SKU.

### Shape 3 — Order ladder, same product every tier (Lifetimely / AMP)

Live listing 2026-09-09 (drift vs Wave A $49 S):

| Plan | List (listing) | Orders |
| --- | --- | --- |
| Free | $0 | ≤50 |
| S | **$79** | ≤500 |
| M | $149 | ≤3,000 |
| L | $299 | ≤7,000 |
| Amazon | **+$75** | add-on |

AMP canonical `useamp.com/pricing.md` (updated 2026-07-30) continues the ladder: XL $499 / 15k · XXL $749 / 25k · Unlimited $999. Price Geek July 2026 omitted S $79 — **conflict flagged**, listing + AMP markdown win for S.

**Expansion mechanic:** the store grows → they pay more for **the same features**. 5-stars call it source of truth. 1-stars call it a rip-off after AMP: Chef Preserve **$600/mo** vs **$30** under founder Karri (Taranker, 2025-07-09). Twitter Bikes: free ≤50 “cannot do anything without starting to pay.”

This is the **highest public ARPU ceiling** in the profit aisle that still looks like a self-serve app. It is also the clearest **success-tax** churn story.

### Shape 4 — Orders + shops (BeProfit)

Listing: $49 / $99 / $149 / $249 (Plus = unlimited shops). Free plan **removed** (Daily Ritual Boutique 1★). ~6% 1-star — highest among profit desks. Viably acquisition. Expansion = shops + orders. Churn story = **zombie annual** (Adrienne Landau $720/yr unused; Clear Cosmetics “It’s like Netflix”).

### Shape 5 — Shopify-plan priced + scheduled-run overage (Better Reports)

$19.90 / $39.90 / $149.90 / $299.90 tied to **Shopify plan**. Extra scheduled runs $0.03–$0.04. Expansion rides the merchant’s **already-accepted** Shopify invoice mental bucket. 5.0 / ~1,198. This is the cleanest “grow with the merchant” shape that is not a GMV tax.

### Shape 6 — GMV / package floors + external (TW, Polar)

- TW listing: Free / Foundation **$219** or $2,190/yr / Automate **$749** or $7,490/yr; **external charges may apply**. Site: GMV slider; listing numbers are **floors**.
- Polar listing: Core **from $750**, “based on online GMV.” Own vs-page ~$400 **conflicts** — do not publish a Polar ARPU.

Expansion here is **enormous** and **hated**. TW 16% 1-star. Polar Trustpilot (Maja, 2025-11-07): listed price ≠ sales quote after install. Kleio’s entire brand is “save $2,280–$60,840/year” vs TW/Lifetimely (vendor arithmetic on getkleio.com — **VENDOR_CLAIM**, do not repeat as fact).

### Shape 7 — Impulse pipe (SyncWith)

Shopify listing **$4.99** Premium. 4.5 / 10. This is the **DIY MER** tax. Agencies already pay it. Mcfly $39 must beat “$4.99 + my tab,” not beat Polar.

### Shape 8 — Finance recon (A2X)

Mini $29 / Basic $45 / Pro $79 / Advanced $115; 30-day trial; 5.0 / 359. Different buyer. Channel-scaled in third-party writeups (Eightx). Not Mcfly’s ARPU — a reminder that **finance will pay** for definitions + bank match, not for Total ROAS poetry.

---

## 3. Worked **list-price** comparisons (not forecasts)

Same store, three public menus. **Do not** turn this into Mcfly revenue.

| Store shape | Mcfly list | Kleio list | TrueProfit list (cheapest legal plan) | Lifetimely list (listing) |
| --- | --- | --- | --- | --- |
| 40 orders/mo | $39 | $29 | $35 | **$0** |
| 280 orders/mo | $39 | $29 | $35 | $79 |
| 800 orders/mo | $39 | $29 | ~$100 on Advanced (see §2) or $185 if they stay Basic | $149 |
| 4,000 orders/mo | $39 | $29 | Enterprise $200 + overage toward $1,000 cap | $299 |
| 2 shops, 280 orders each | **$78** | ? (listing is per install; not stated) | 2× plan + maybe 5-store discount | 2× ladder |
| + Amazon | $39 (Shopify only) | Shopify-shaped | Works-with Amazon on listing | **+$75** |

**Read:** Mcfly is the **expensive toy** at 40 orders (Lifetimely is free) and the **cheap desk** at 4,000 orders (everyone else has expanded). The stores most likely to *review a profit app* are the middle — and in the middle Mcfly is **same or higher price, thinner job** than Kleio/TrueProfit.

No statement is made about how many stores sit in each row. That would be fake TAM.

---

## 4. Expansion drivers actually observed

What made a merchant pay **more next month** in this aisle:

| Driver | Who uses it | Public proof it expands | Public proof it 1-stars |
| --- | --- | --- | --- |
| Order volume | TP, Lifetimely, BeProfit, Elevar $/order | Menus exist; Enterprise SKUs exist | bamtoo; Chef Preserve; BeProfit free-plan deletion |
| Extra shops | BeProfit Plus $249; Metorik 5 stores @ $75; TP “5+ stores discount” | Listing SKUs | Bioenex: ops costs not spread |
| Amazon / extra channel | Lifetimely +$75 | Listing add-on | carnivoro: add-on ≈ full price, still buggy |
| GMV / spend | TW, Polar, Northbeam (MARKET_REPORT floors) | Sliders, $750 floor | TW hangover; Polar quote-after-install |
| Shopify plan | Better Reports | 1,198 reviews | Low 1-star % |
| AI / credits | TW Moby | Listing hero | Cocaine Coffee 5★ *and* Kove 1★ |
| CS / Slack tier | Lifetimely XL; Polar; Elevar | Reviews name humans | Cloudflops: highest plan, bot chat |
| Scheduled-run overage | Better Reports | Docs + pricing | Not a visible 1-star theme this fetch |
| Implementation hours | Analyzify $145–$375 + paid setup | Recurring SKU | Duckfeet / Raregen / Tameson 1-stars |

**Mcfly expansion options that do not require becoming TW:**

| Option | Tag | Money | Love | Risk |
| --- | --- | --- | --- | --- |
| Agency / N-store SKU | `STRETCH` | H if 10 agencies | M (agencies don’t leave 899 reviews) | Support N× |
| 14-day + keep $39 | `STRETCH` | Conversion, not ARPU | M | Official 180-day |
| Forever-free ≤50 orders (Lifetimely) | `RELIGION_BEND` | Volume / reviews | H | MASTER_PLAN freeloader; TSC uninstall-ranking gossip |
| $99 finance overlay | `STRETCH` | H per account, L volume | M | $39 already signals “toy” to P5 |
| Order meter | `RELIGION_BREAK` vs live anti-tax copy | H | L | BeProfit/TP 1-stars |
| GMV tax | `RELIGION_BREAK` | H | L | Brand suicide |
| Course $79 | `FIT_NOW` | L | M | Consulting-energy |

TSC (MARKET_REPORT): expansion is “the cheapest growth there is.” Mcfly’s religion currently **forbids** the cheap growth. That is a founder choice. Score it honestly in `VNEXT_OPTION_SCORECARD.md`.

---

## 5. Churn drivers observed (not Mcfly %)

We have **zero** Mcfly churn observations. Category drivers, with citations:

### 5.1 Never activated / never used (silent)

- TSC: median Shopify app **15–20%** trial→paid; **60–70%** of installs never reach first value; after 7 days unactivated, recovery unlikely ([onboarding-benchmarks](https://taylorsicard.com/blog/shopify-app-onboarding-benchmarks)).
- TSC: “Didn’t use it enough” on an exit survey usually means **never activated**.
- BeProfit Adrienne Landau: **$720/year, never used**.
- Official uninstall reasons include “Not using app now” (Oxify playbook paraphrases Shopify’s dropdown — treat as secondary).

This is Mcfly’s **default future**. Paste-first + 7-day + no push = non-use. MASTER_PLAN §11 is this driver with a weekly costume.

### 5.2 Billing / zombie / trial cliff

- Official: uninstall cancels future, **not always the current cycle**. Merchants who do not understand 30-day cycles write 1-stars (Boxi explainer; VocaSpark vs TrueProfit).
- TrueProfit VocaSpark (2026-07-04): charged after trial despite uninstall; vendor refunded.
- BeProfit Clear Cosmetics (2026-03-04, later deleted on Shopify 2026-07-18): months of charges; “It’s like Netflix.”
- Polar / TW: **external** charges survive uninstall (official Help Center warning).

### 5.3 Success tax / plan mismatch

- TSC root cause #4: plan/feature misalignment.
- Lifetimely Chef Preserve; TrueProfit Brooklyn Singapore 400%; Daily Ritual Boutique locked out when free vanished and entry became $49.

Mcfly cannot hit this **until** it meters. Flat $39 avoids this 1-star class. It also avoids expansion.

### 5.4 Definition / accuracy break

- TW VAT-in-revenue (Kove).
- TrueProfit VAT excluded from net (vendor reply) + “doesn’t track VAT collection.”
- BeProfit A Farley: **~15% of Google spend** imported by design (UTM-attributed only).
- WeTracked elife: could not evidence “more accurate than native.”
- Community 588628: pull **TOTAL** spend, not attributed.

One wrong definition → finance 1-star → rating death at low N. Mcfly at 5 reviews cannot survive one Kove.

### 5.5 ICP mismatch / wrong aisle

- TSC: highest-retention installs are **search + agency referral**, not broad curiosity.
- Mcfly’s “more like this” is **free pixels**. Those merchants wanted Parkour. They are the wrong ICP for a $39 cash desk. High curiosity-install + 7-day blank desk = TSC’s free-trial ICP problem **without** even a free plan.

### 5.6 Seasonality

- TSC root cause #3. BFCM order meters explode (TP overage). Flat $39 is **season-safe** for the merchant and **season-blind** for Mcfly revenue. Elevar $0.50/order is the opposite.

### 5.7 Acquisition / PE decay

- Lifetimely → AMP; BeProfit → Viably. 1-stars cluster on **support + price** after the deal. Not Mcfly’s problem until someone buys Mcfly. Lesson: **named-human love is the first thing PE kills.**

### 5.8 Platform ate the job

- Oberlo delisted 2022; Geolocation sunset 2025; Linkpop 2025; Stocky delist Feb 2026 / shut Aug 31, 2026; Shopify Scripts die Jun 30, 2026. If Shopify ever puts **ad spend next to sales** in native Analytics, Mcfly’s core job evaporates. Community 134251 says they have **not**. Shop Campaigns have native spend+ROAS **only for Shop Campaigns**. This is a **tail-risk**, not a 2026-09 fact.

---

## 6. What we can say about Mcfly unit economics without lying

Allowed statements:

- List price is $39. Net ≈ **$37.87**/mo/store before the lifetime cap, ignoring tax, refunds, and support cost.
- Support cost is **not** $0. Wave A: loved apps staff humans. At $37.87, **one 30-minute onboarding call per store per month** already destroys contribution if the founder’s time is valued at a normal contractor rate. Do not invent the rate. Just do not pretend $39 is high-margin without a **zero-touch** loop.
- Course $79 is **not** recurring. Do not annualize it.
- 20% Shopify share is **obsolete** as of the 2025 lifetime-cap regime.
- “We need N stores to replace a job” is only valid as **list-price ratios** (Polar $750 / $39 ≈ 19). It is not a sales target.

Forbidden statements (do not add later):

- Mcfly MRR, ARR, ARPU, churn, LTV, CAC, payback.
- “X% of Shopify stores will pay.”
- TSC 15–20% trial-to-paid applied to Mcfly as if measured.

---

## 7. Religion vs money (the actual fight)

| Money fact | CURRENT_RELIGION | What it costs |
| --- | --- | --- |
| Flat $39, anti-GMV | Keep | No expansion; Kleio is $29 with more product |
| No forever-free | Keep | Lifetimely prints reviews on ≤50 orders; Mcfly pays $39 against $0 |
| 7-day trial | “Not bait” | Category paid cluster is **14**; TTV is not instant |
| No OAuth | Live site | TrueProfit/Kleio/Lifetimely expand **because** spend syncs; Mcfly cannot |
| No pixel | Keep (research agrees) | Lose the free-review rail; keep brand |
| Prefer serious stores | Keep | TSC: broad trials = ICP churn; also: 0 reviews |

The money-max path in this aisle, evidenced by **menus + review volume**, is **order-ladder profit desk + 14-day + auto spend** (TrueProfit/Lifetimely) or **flat cheap profit desk + MCP** (Kleio) or **GMV suite** (TW/Polar). Mcfly’s current model matches **none** of those three. It matches **SyncWith + a sermon**, at 8× SyncWith’s price.

`RESEARCH_OPTION` that raises money **without** a meter: agency SKU + 14-day + OAuth spend (ARPU from N stores, not from punishing growth). That is S1/S3 in `VNEXT_OPTION_SCORECARD.md`.

---

## Sources (Wave B)

- Shopify revenue share (LIVE): https://shopify.dev/docs/apps/launch/distribution/revenue-share
- Shopify trials / uninstall / reviews: linked above
- Live listings 2026-09-09: Mcfly, Kleio, TrueProfit, Lifetimely, Better Reports
- trueprofit.io/pricing · useamp.com/pricing.md (2026-07-30)
- TSC economics / churn / onboarding (MARKET_REPORT)
- PR #5 review mining (TrueProfit/Lifetimely/BeProfit 1-stars) — cite, do not duplicate
- Help: https://help.shopify.com/en/manual/apps/uninstalling-apps
