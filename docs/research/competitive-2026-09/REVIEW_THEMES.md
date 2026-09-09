# Review themes — public App Store pages only

**Fetched:** 2026-09-09  
**Honesty rule:** Shopify listings show a **star histogram (percentages)** and typically the **first 3 written reviews**. We do **not** pretend we read all 899 TrueProfit reviews. Counts below are:

- `N_total` = listing “Reviews (N)” 
- `N_visible` = written reviews on the first paint (usually 3)
- Star splits = Shopify’s rounded percentages (they will not sum to exact integers)
- Shopify Magic summaries appear only when **≥100 reviews and ≥4.0** (https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews)

Mcfly: **N_total = 0**. No themes. That is the entire distribution story.

---

## Snapshot table (LIVE 2026-09-09)

| App | URL | N | Rating | 5★% | 1★% | Visible written (date) |
| --- | --- | --- | --- | --- | --- | --- |
| Mcfly | /mcfly-analytics-public | 0 | 0.0 | — | — | none |
| Triple Whale | /triplewhale-1 | 91 | 4.1 | 79 | **16** | 3 (2026-07-20, 2026-07-06, 2026-06-04) |
| Polar | /polar-analytics | 116 | 4.9 | 97 | 3 | 3 + Magic summary |
| Lifetimely | /lifetimely-lifetime-value-and-profit-analytics | 535 | 4.9 | 96 | 2 | 3 |
| TrueProfit | /trueprofit | 899 | 5.0 | 98 | 1 | 3 |
| Analyzify | /analyzify | 313 | 4.7 | 94 | 4 | 3 |
| BeProfit | /beprofit-profit-tracker | 202 | 4.5 | 93 | 6 | 3 |
| Metorik | /metorik | 48 | 5.0 | 100 | 0 | 3 |
| Better Reports | /betterreports | 1,199 | 5.0 | 96 | 0 | 3 |
| Clarity | /microsoft-clarity | 2,125 | 4.6 | 83 | 6 | 3 |
| WeTracked | /wetracked-io-connect | 125 | 4.8 | 94 | 4 | 3 |
| Parkour | /parkour-pixel | 191 | 4.9 | 98 | 2 | 3 |
| Elevar | /gtm-datalayer-by-elevar | 168 | 4.7 | 89 | 7 | 3 |
| SyncWith | /syncwith | 10 | 4.5 | 90 | 10 | 3 |

**Read the 1-star column.** Triple Whale is the outlier (16%). Elevar 7%, BeProfit 6%, Clarity 6% are the next “real product, real pain” cluster. Polar/Lifetimely/TrueProfit/Parkour/Better Reports are reputation machines.

---

## Theme A — Support humans are the product

**Visible evidence (not a census):**

| App | Visible praise named | Source |
| --- | --- | --- |
| Triple Whale | “Juan” (two of three visible reviews) | Cocaine Coffee 2026-07-20; Marielle Stokkelaar 2026-06-04 |
| TrueProfit | Vani, Durra | PrimalCat 2026-08-29; GowiLab 2026-05-26 |
| Lifetimely | “Cristian D.”; “sat on multiple calls” | Nikura 2026-07-30; CS2 2026-08-21 |
| Polar | “team … responsive and proactive” | Magic summary + Naturtint 2026-08-10; Valabasas 2026-04-28 |
| Elevar | Sourabh, Raphael, Darshak — **named onboarders** | APM Monaco 2026-09-04; LÜME 2026-08-28; Old Bones 2026-06-23 |
| Analyzify | Görkem; “team behind the product” | illuminated mirrors 2026-05-26; iSTYLE.bg 2026-08-11 |
| Metorik | Founder-voice replies signed “Bryce” | all three visible |
| Better Reports | “created a custom report that was exactly what I needed” | Becky's Boutique 2026-07-01 |
| Parkour | “excellent support. Very responsive” | Endu 2026-08-01 |

**Inverse:**
- TW 1★ Kove Footwear: “Almost impossible to reach customer service.”
- BeProfit 1★ Adrienne Landau: paid $720/year unused; “will not respond … will not cancel.”
- WeTracked 1★ elife: “Misleading claims” + support could not evidence “more accurate than native.”

**Implication for Mcfly:** 0 reviews means 0 named humans. The apps that **feel enterprise** on the App Store are the ones that staff onboarding. Polar $750 and Elevar $225 are not bought as UI; they are bought as **a person**. `CURRENT_RELIGION` “desk not OS” still needs a human inbox that answers. Live site says “Support: a human inbox.” That is table stakes, not a moat.

`RESEARCH_OPTION`: concierge onboarding for first 20 paid stores (paste their first CSV with them). Evidence: Elevar/Polar/Better Reports review language. Risk: does not scale; becomes consulting (MASTER_PLAN discarded $750 diagnostics).

---

## Theme B — “Source of truth” / accuracy / I can finally see profit

Visible:
- Lifetimely Nikura (UK, ~4 years, 2026-07-30): “It acts as our **source of truth**.” “simple and fast and not bloated.”
- BeProfit NomaDesk (2026-08-24): “can trust that my numbers are accurate … down to a tee.”
- TrueProfit PrimalCat: shipping-cost tracking → “more accurate view of my actual profit.”
- TrueProfit GowiLab: “must need to see how much you're actually making in profit.”
- Metorik Sadhev (2025-02-15): “We trust Metorik more than the panel data available on Meta and Google.”
- Community 657805 (not a review): “Revenue is native, true net profit has to be assembled.”

**Mcfly fit:** This is the love language of the cash desk — **if** the number includes the costs they mentally include. “Total ROAS” without COGS will not earn “source of truth” from Nikura-type reviewers.

---

## Theme C — Billing / trial / uninstall trauma

Visible:
- TrueProfit 1★ VocaSpark (PT, 27 days, 2026-07-04): charged after trial despite uninstall; variants outdated on reinstall; **VAT not tracked**. Vendor replied: full refund processed; “Shopify VAT is excluded from Net Profit.”
- BeProfit 1★ Adrienne Landau: zombie $720/year subscription.
- Shopify official: trials tracked across **180 days** to stop reinstall farming — https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials

**Mcfly risk:** 7-day trial + paste-first = high chance they **never reach value** and then either (a) churn silently or (b) get billed and 1-star. TrueProfit’s refund-and-reply pattern is the damage-control playbook.

`RESEARCH_OPTION`: 14-day trial (category norm on Lifetimely/TrueProfit/BeProfit/Better Reports; Elevar 15; Metorik 30). Evidence: those listings. Risk: longer unpaid use. `CURRENT_RELIGION` 7-day assumes immediate value Mcfly does not deliver without a CSV.

---

## Theme D — Metric definitions will 1-star you (VAT, revenue, “accuracy”)

Visible:
- TW 1★ Kove Footwear: “Triple Whale just casually leaves **includes VAT in your revenue** (revenue should never be including VAT).”
- TrueProfit 1★ VocaSpark: “doesn't track VAT collection.”
- WeTracked 1★ elife: Events Manager errors; “incorrect purchase value”; could not prove superiority vs native Meta app.

**Mcfly implication:** Publish **exact** sales definition (gross / total / net; tax in or out; shipping in or out; gift cards; returns timing). Live SAMPLE says “Shopify Total Sales after returns.” Make that a settings toggle or finance will copy Kove’s review.

`RESEARCH_OPTION`: tax-region presets. Evidence: two independent 1-stars in this fetch. Risk: accounting complexity.

---

## Theme E — AI is a listing magnet and a review landmine

Visible TW:
- 5★ Cocaine Coffee: “triple whale should give more warning about **AI usage limitations**, especially for the foundation plan.”
- 1★ Kove: “For the AI help section you need to **buy credits**.”

Listing heroes: TW “Moby 2”; Polar “AI‑Analytics”; Lifetimely “AI Profit Agent”; TrueProfit MCP; Clarity “Brand Agents.”

**Mcfly:** no AI on listing. That is **differentiation** (honest desk) and **discovery penalty** (Sidekick + search copy loves “AI”).

`RESEARCH_OPTION`: non-metered “explain this number” so you never sell credits. Evidence: TW credit 1-stars. Risk: still a toy next to Moby.

---

## Theme F — Time-to-value and “2 minutes”

Visible:
- Parkour hero: “Setup takes just **2 minutes**, no coding.” Review AROMATICA: EMQ “9.2 on purchase event” (reviewer claim).
- Parkour Kismet Glow (9 days): switched from native FB/IG; “used to get a lot of fake orders. now it's clean.”
- Elevar reviews are **onboarding success stories** in the first 11 days (APM Monaco).
- Better Reports Becky's Boutique: **~20 hours** using the app, already 5★ because support built the report.
- TW Cocaine Coffee: **2 days** using, 5★ — support + “world class” (or a fast dopamine pixel).
- Mcfly: first value = **after spend is added**. Real store “starts blank.” That is a review-killer.

---

## Theme G — Multi-store / ops cost allocation

Visible BeProfit Bioenex (2026-08-21): “could be bit better for users with many stores … operational costs could be spread across all stores.”

Polar Magic summary: “data centralization … multi-touch attribution and customizable reports.”

**Mcfly:** no multi-store. Agency love blocked.

---

## Theme H — Pixel/ROAS claims that cannot be evidenced

WeTracked 5★ Suppstore (2026-07-10): “My ROAS got up 30% and overal tracking to 90-100% On scale this app makes its self pay 30x.” **Reviewer claim.**  
WeTracked 1★ elife: support “could not provide any data, testing methodology, comparison date, or technical evidence.”

**Mcfly kill shot (keep):** never claim ROAS lift. Claim **reconciliation**.  
**Mcfly trap:** if a future pixel RESEARCH_OPTION ships, this 1-star is the template of death.

Shopify listing rules: no unsubstantiated claims; no testimonials in listing body — https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements

---

## Theme I — Free + Microsoft-scale distribution

Clarity 2,125 reviews, Free Forever, launched **2025-07-17** — ~14 months to 2,125 reviews. Visible complaints: “watch the recording all day” without explanation; sluggish; JP user wants PNG download fix. 6% 1★ is survivable at this volume.

**Mcfly cannot copy the free heatmap motion.** It can copy the lesson: **zero-price + instant value + a brand (Microsoft)** prints reviews. Mcfly has none of those three.

---

## Theme J — Shopify Magic summary (Polar only in this set)

Polar (≥100 reviews, 4.9) shows Magic:

> “Merchants recommend this app for its transformative data centralization from platforms like Shopify and Google Ads… multi-touch attribution and customizable reports… seamless integration and easy setup. Exceptional customer support…”

That summary **teaches the category** to the next buyer. Mcfly cannot get it until **100 written reviews and ≥4.0**. Official: https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews

`RESEARCH_OPTION`: design the first 100 reviews around a **single job** (“I pasted spend, saw Total ROAS vs break-even”) so Magic, if it ever generates, does not say “pixel/CAPI.”

---

## Theme K — Longevity as social proof

Visible tenure:
- Lifetimely Nikura: almost 4 years
- Polar Valabasas: about 2 years
- Elevar Old Bones: over 2 years
- Analyzify Mahone's: about 3 years
- TW Marielle: over 2 years
- BeProfit Adrienne: over 2 years (**negative** — zombie billing)
- Mcfly launched **2026-09-07** (2 days before this research)

---

## Approximate honest 1-star mass (do not over-precision)

Shopify gives percents, not counts. Rough **implied** 1-star volume = round(N × 1★%). This is **approximate** (rounding):

| App | N | 1★% | Implied ~1-star reviews |
| --- | --- | --- | --- |
| Triple Whale | 91 | 16 | ~15 |
| Polar | 116 | 3 | ~3 |
| Lifetimely | 535 | 2 | ~11 |
| TrueProfit | 899 | 1 | ~9 |
| BeProfit | 202 | 6 | ~12 |
| Elevar | 168 | 7 | ~12 |
| Clarity | 2,125 | 6 | ~128 |
| WeTracked | 125 | 4 | ~5 |
| Analyzify | 313 | 4 | ~13 |
| Better Reports | 1,199 | 0 | ~0 (UI rounded) |
| Mcfly | 0 | — | 0 |

TW’s **~15 ones on 91** is a branding crisis. Clarity’s ~128 ones are noise in 2,125.

---

## What reviewers never say (useful negative space)

In the visible sample, **nobody** asked for:
- “anti-attribution religion”
- “billboard CSV”
- “Total ROAS as a named product”
- “please don’t build a pixel”

They asked for: profit I trust, support that answers, tracking that matches Events Manager, VAT handled, billing that doesn’t zombie, AI that isn’t metered, multi-store costs.

`CURRENT_RELIGION` is absent from the review corpus. That does **not** make it wrong. It makes it **unproven as a love driver**.
