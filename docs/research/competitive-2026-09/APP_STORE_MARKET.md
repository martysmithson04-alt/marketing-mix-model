# Shopify App Store as a market (2026-09)

**Purpose:** How discovery, listing conversion, reviews, pricing psychology, unpaid trials, and churn actually work — from **official Shopify docs** plus **live listings** plus clearly marked MARKET_REPORT practitioner blogs.

Mcfly is a **2-day-old, 0-review, $39, 7-day-trial** app in a category where loved peers have 200–2,000 reviews. This file is the market physics that will eat it.

---

## 1. What the App Store is (official)

Source: https://shopify.dev/docs/apps/launch/app-store-review

- The **public listing** is the single object used for:
  - App Store browse / search
  - In-admin recommendations
  - **Sidekick** answers
- Shopify bills merchants (App Pricing / Billing API). Off-platform billing is disallowed for public apps (requirements 1.2).
- Partner economics (same page): default app revenue share **20%**, reduced plan **15%**, **0% on first $1,000,000 USD** for eligible developers.
- Quality promotion path = **Built for Shopify** and intermediate achievements.

`CURRENT_RELIGION` implication: a beautiful mcflyads.com does **not** get you Sidekick or admin “Picked for you.” The listing does.

---

## 2. Discovery surfaces (official + observed)

| Surface | Official? | What we know |
| --- | --- | --- |
| Search | Yes | BFS apps get a **search ranking boost** and a BFS filter. https://shopify.dev/docs/apps/launch/built-for-shopify |
| Category pages | Yes | Mcfly categories on listing: **Marketing and sales · Visuals and reports** — same pair as TW, Polar, Lifetimely, TrueProfit, Clarity. |
| “More apps like this” | Observed | Collaborative-filtering style. Mcfly rail = **Clarity / WeTracked / Parkour** (pixels & heatmaps). Polar rail = pixel/CAPI apps. TrueProfit rail = reports + profit. |
| Homepage collections / story pages | Yes | Eligibility needs min installs, reviews, rating (thresholds **unpublished**). |
| Admin “Picked for you” / Sidekick | Yes | Fed from listing fields + quality signals. |
| App Store **ads** | Yes | Search ads above organic. BFS unlocks **plan-based targeting**. |
| External (site, Twitter, partners) | Practical | Still lands on the listing to install. |

**Brutal Mcfly read:** Shopify’s similarity graph already decided Mcfly is a **tracking utility**. The listing hero talks billboards; the graph heard “ad / ROAS / pixel-adjacent.” Until reviews exist, this rail is the only discovery. Those neighbors are **Free**.

`RESEARCH_OPTION`: rewrite listing first 50 words and screenshots so the graph has a chance to cluster with TrueProfit / Lifetimely (“profit / spend / P&L”) rather than Parkour. Evidence: TrueProfit’s rail is the commercially correct aisle. Risk: we don’t control the algorithm.

---

## 3. Listing conversion (official constraints + MARKET_REPORT rates)

### Official constraints that affect conversion

Requirements: https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements

- Pricing must be **accurate and complete** (plans, trial, charge details).
- **No reviews/testimonials in listing copy or images** (4.3.6 / 4.3.7). Social proof can only come from the **review module Shopify owns**.
- Mcfly therefore **cannot** paste founder quotes or “used by Harbor Home Co” as testimonials on the listing. SAMPLE desk on the marketing site is fine; on the App Store it is a policy risk if it reads as a customer result.

### MARKET_REPORT conversion bands (not Shopify-official)

https://taylorsicard.com/blog/shopify-app-listing-conversion (2026):

| Review cohort | Claimed view→install |
| --- | --- |
| <25 reviews | ~1–2% |
| 25–200 | ~2–5% (tool page) |
| 200+ | ~5–8% |
| “Well-positioned” blended | ~3–8% |

**Do not publish these as Mcfly metrics.** Use them as a planning stress test:

If Mcfly has **0 reviews**, TSC’s own framework says it lives in the **1–2%** bucket. To get 50 installs at 1% you need **~5,000 listing visits**. Those visits will mostly come from ads or outbound — the organic graph is feeding people who wanted a **free pixel**.

TSC’s other claim: first **50 reviews** are the early-life investment, “even if you give the app away.” That **directly contradicts** MASTER_PLAN “no forever-free / prefer few serious stores.” This is a live religion fight.

| | Give it away for reviews | Stay paid $39 / 7-day |
| --- | --- | --- |
| Tag | `RESEARCH_OPTION` | `CURRENT_RELIGION` |
| Evidence | TSC; Lifetimely Free ≤50 orders; TW Free; Clarity | MASTER_PLAN §8; live $39 |
| Risk | Freeloaders, uninstall rate (TSC says ranking cares about uninstalls) | 0-review death spiral |

---

## 4. Reviews — the actual ranking object

Official: https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews

| Rule | Detail |
| --- | --- |
| Who can review | Installed merchants, or within **45 days of uninstall** |
| Rating math | **Not a simple average.** Weighted for recent / useful / trustworthy |
| Search impact | “positive reviews make your app appear higher in … search results and category pages” |
| AI Magic summary | ≥**100 reviews with body text** and ≥**4.0**; up to 14 days to appear |
| Ask rules | Neutral language only. **No “leave a positive review.”** No incentives. No install-time nag. No unsolicited review email. |
| Deep link | `https://apps.shopify.com/mcfly-analytics-public#modal-show=WriteReviewModal` |
| Reply | Partner permission “Manage public listings”; merchant notified; they can edit stars |
| Fake / incentivized | Removal; possible **ranking demotion** or unpublish |

**Mcfly cannot buy reviews.** The legal path to 100 Magic-summary reviews is **time-to-value so strong that people write unprompted**, plus a **neutral in-app ask after a successful Monday close** (App Bridge Reviews API — mentioned on the same official page).

`RESEARCH_OPTION`: trigger a review modal after the first period where spend>0 and Total ROAS renders — **not** at install. Evidence: official “don’t ask at onboarding.” Risk: still 0 if they never add spend.

### What 1-star physics looks like in this category

See `REVIEW_THEMES.md`. TW 16% 1★ on 91 reviews is a **visible** scar (4.1). Polar 4.9 on 116 looks “enterprise.” Review volume without rating quality is Clarity (4.6 / 2,125 / 6% 1★) — acceptable because Free.

Mcfly at 5 reviews with one billing 1-star = **4.0-ish and dead**. Billing/trial design is a ranking feature.

---

## 5. Built for Shopify — the promotion paywall

https://shopify.dev/docs/apps/launch/built-for-shopify

Benefits that matter for a 0-review app (once eligible):

- Badge on **every card** (search, category)
- Search filter + **ranking boost**
- Homepage / category / admin / Sidekick eligibility
- App Store ads **plan targeting**
- Priority review of future apps

Criteria include **proven usefulness**: installs, reviews, rating on a rolling window — **numeric gates not published**. Repo `APP_STORE_LISTING.md` “~50 paid-plan installs + 5 reviews” is a **founder heuristic**, not a Shopify number.

Other automatic highlights Mcfly might already be close to:

- “Use directly in the Shopify admin” if the app is embedded (repo says it is).

`CURRENT_RELIGION` “don’t chase BFS” is rational at 0 installs. `RESEARCH_OPTION`: treat BFS criteria as a **checklist** now (embedded, clean uninstall, listing completeness, performance) so the day reviews exist, apply immediately. Evidence: ranking boost is one of the few official levers. Risk: failing BFS three times suspends application 3 months (official).

---

## 6. Pricing psychology (live category, not vibes)

### What is on the shelf next to Mcfly’s jobs

| Price shape | Live examples | Psychology |
| --- | --- | --- |
| **Free forever** | Clarity; Parkour | Install-now, review-now. Mcfly’s rail. |
| **Free to install + external** | WeTracked; TW; Polar | Listing looks cheap; invoice surprises. TW/Polar disclose “External charges may be billed… separately.” |
| **Free tier then paid** | TW Free; Lifetimely ≤50 orders | Review engine + upgrade. MASTER_PLAN hates this. |
| **Flat mid** | Mcfly **$39** | Honest. Also: no upgrade path, no GMV upside, no “I grew so I pay more” but also no “this is serious.” |
| **Order-metered** | TrueProfit $35+$0.30/extra; Lifetimely $49/149/299; BeProfit $49–249; Elevar $225+$0.50/order | Familiar SaaS. Punishes growth — the thing Mcfly attacks. |
| **Shopify-plan-priced** | Better Reports $19.90–$299.90 | Aligns with merchant’s **existing** mental bucket. |
| **GMV / spend tax** | Polar from $750; TW $219/$749 floors + slider | Enterprise signal. 1-star fuel. |
| **$4.99 impulse** | SyncWith Premium | Pipe, not desk. |

GapQuery MARKET_REPORT (https://www.gapquery.com/blog/shopify-app-pricing-by-category): median paid app entry **$9.99**. Analytics/profit **live listings we fetched do not live there**. Mcfly $39 is **inside** the profit cluster ($25–$49 entry), not expensive, not cheap.

### $39 vs $79 (repo vs live)

| | $39 live | $79 repo draft |
| --- | --- | --- |
| vs TrueProfit Basic $35 | Same wallet, thinner product | 2.3× TrueProfit for thinner product |
| vs Lifetimely S $49 | Slightly cheaper | 1.6× |
| vs TW Foundation $219 | 5.6× cheaper (entry band only) | 2.8× cheaper |
| Signal | “utility” | “serious desk” or “overpriced CSV” |

`RESEARCH_OPTION`: **$39 is correct only if** auto-spend or profit-lite ships. Otherwise it is priced like TrueProfit and scoped like a sheet. Raising to $79 without reviews is suicide. Lowering to Free without a time-to-value loop prints junk installs.

### Annual

Better Reports / BeProfit show ~20% annual. TW listing shows 17% ($219→$2,190). GapQuery MARKET_REPORT: don’t add annual until ~50 paying and you know churn. Mcfly listing: monthly only.

---

## 7. Unpaid trials (official + live)

Official: https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials

- Trial delays billing N days.
- **180-day window** prevents reinstall-to-reset.
- Trials attach to **new** subscriptions only.
- Dev stores: $0 private test plan (new billing system).
- Merchant who installs mid-trial sees charges on the **next Shopify invoice** after trial — this is how TrueProfit 1★ VocaSpark happens.

### Live trial lengths in this research

| App | Trial on listing |
| --- | --- |
| Mcfly | **7-day** |
| TrueProfit / Lifetimely / BeProfit / Better Reports / SyncWith | **14-day** |
| Elevar | **15-day** |
| Metorik | **30-day** |
| Clarity / Parkour | n/a (free) |
| Polar / TW paid | not shown as Shopify trial on the cards we saw (TW has a Free plan instead) |

Shopivibe MARKET_REPORT: 7-day only if time-to-value is **immediate**; 14 default; 30 if value is slow.

**Mcfly time-to-value is not immediate.** Live site: “Real store starts blank until you add spend.” A 7-day clock + a founder who must export 3 Ads Managers is how you get **uninstall before review eligibility even matters**.

`RESEARCH_OPTION`: 14-day + sample-to-real wizard + review ask on first computed Monday.  
`CURRENT_RELIGION`: 7-day “we’re not bait.” Honesty that **hurts conversion**.

---

## 8. Churn physics (what we can say without private data)

We do **not** have Mcfly or competitor churn %. Public proxies:

| Proxy | Source | Meaning |
| --- | --- | --- |
| Uninstall review window 45 days | Official reviews doc | Uninstallers **can still 1-star you** |
| Ranking weights uninstall rate | TSC MARKET_REPORT (algorithm not public) | Junk free installs can **hurt search** |
| Zombie billing 1-stars | BeProfit Adrienne $720/yr; TrueProfit VocaSpark | Churn that feels like theft becomes a listing wound |
| “Never used” | BeProfit 1★ | Apps that don’t email a weekly artifact get forgotten **and still billed** |
| MASTER_PLAN kill | `docs/MASTER_PLAN.md` §11 | Partners won’t open weekly after 30 days of accurate MER |

**Retention product for this category (observed):**
- TrueProfit / Lifetimely: daily profit habit (open to see if you made money).
- Better Reports: the report **arrives**.
- TW: Slack/Moby (and credit meters).
- Mcfly: a desk you must remember to paste.

`RESEARCH_OPTION`: **push** the Monday Close. If the artifact visits them, churn should resemble Better Reports more than a blank embedded app.

---

## 9. Listing craft vs Mcfly live listing

See `LISTING_TEARDOWNS.md` for line-by-line. Market-level gaps:

| Element | Winners do | Mcfly live |
| --- | --- | --- |
| Price scan | Free or “from $X” with tiers | Single $39 |
| Social proof | 100–2,000 reviews + Magic | 0 |
| Time-to-value in first 50 words | “2 minutes,” “real-time,” “autopilot” | “Add spend by day or CSV” |
| Works with | Meta, Google, Klaviyo logos | none on fetch |
| Languages | Polar 3; Clarity 14; TrueProfit 3 | English |
| Featured in | Guides / BFCM (TrueProfit, TW, Elevar) | none |
| Developer gravity | Microsoft; 2017–2021 launch dates | Sept 7, 2026, West Jordan mailbox |

---

## 10. Money math you *can* do without inventing installs

Shopify take: assume reduced 15% after eligibility, else 20%. On $39:

- Gross to Mcfly @20% = **$31.20**/mo/store
- @15% = **$33.15**
- First $1M revenue @0% (if eligible) = full $39

To match **one** Polar $750 seat (listing floor, before GMV) you need **~19–24** Mcfly stores depending on share. Polar also has CS costs Mcfly cannot staff at $31 net.

TrueProfit at $35 + overage likely **out-earns** Mcfly per successful merchant because meters scale. Mcfly’s brand promise is to **refuse** that. Fine — then volume or agency seats have to do the work.

**No install forecast is included.** Partner Dashboard is the only honest source.

---

## 11. Religion vs market physics

| Physics | CURRENT_RELIGION | RESEARCH_OPTION |
| --- | --- | --- |
| Reviews are the listing | Prefer serious stores, no bait | Design-partner **and** a legal review loop; maybe a limited free SKU |
| 7-day trial | Honest, not bait | 14-day because TTV is paste-slow |
| $39 flat | Anti-GMV moral high ground | Keep flat; add agency seat; don’t order-meter |
| No testimonials on listing | (already) | Invest 100% of proof in **product screenshots + formula** |
| Adjacent to free pixels | “We’re not them” | Steal their **ease**, not their pixel |
| BFS later | Repo heuristic | Prep now, apply when gates are actually met |

The App Store will not grant Mcfly a moral exemption because the formula is cleaner. It will grant distribution to **apps people review**.

---

## 12. Wave 2 — ads + first 50 (pointer)

Full official auction / billing / review-API / illegal-vs-legal ask: **`DEEP_DIVE_DISTRIBUTION.md`**.

Headline facts fetched 2026-09-09:

- App Store Ads = **CPC, first-price** (you pay your bid). Min budget **$5/day**. Search + category + homepage slots. Ads **only** open the listing.
- Relevance can beat a higher bid. Mcfly’s organic rail is **free pixels** — bidding `pixel`/`capi` is how you pay to lose.
- Reviews API: no ask &lt;24h; 1×/60d; 3×/365d; not mobile; not onboarding.
- Policy 1.3 (2026-07-06 changelog): incentivized reviews → removal, demotion, delist, Partner death.
- Report Pundit shows the **honest volume** path (free ≤1000 lifetime + human close → 2,026). Kleio shows the **honest lean** path ($29 + founder replies → 20). Klar shows the **skip the store** path (0 Shopify reviews, OMR in DE).

`RESEARCH_OPTION`: do not buy ads yet. Do the Kleio-path legal ask after a real close. `CURRENT_RELIGION` 7-day + paste makes even the legal ask fail.
