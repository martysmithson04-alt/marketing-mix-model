# DEEP_DIVE — First 50 reviews (honest) + App Store Ads economics

**Date:** 2026-09-09  
**Wave:** deeper. Extends `APP_STORE_MARKET.md` §§3–5. Official Shopify docs first. Practitioner blogs = `MARKET_REPORT`. **No invented CPCs, install rates, or Mcfly forecasts.**

---

## 1. What “first 50 reviews” actually is

Not a Shopify-published gate. It is **industry gossip** that happens to match observed physics:

| Claim | Source | Tag |
| --- | --- | --- |
| First 50 reviews = early-life investment; even give the app away | https://taylorsicard.com/blog/shopify-app-listing-conversion | MARKET_REPORT |
| &lt;25 reviews → ~1–2% view-to-install; 200+ → ~5–8% | same | MARKET_REPORT — **do not publish as Mcfly** |
| Magic summary at **100 written + ≥4.0** | https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews | **OFFICIAL** |
| BFS needs min installs/reviews/rating (numbers **unpublished**) | https://shopify.dev/docs/apps/launch/built-for-shopify | OFFICIAL |
| Repo “~50 paid + 5 reviews” before BFS | `docs/APP_STORE_LISTING.md` | Founder heuristic |

So “50” is a **practitioner milestone** between “invisible” and “Magic summary.” Mcfly is at **0**. Report Pundit is at **2,026**. Kleio is at **20** after ~18 months. Klar is at **0** after ~21 months **on purpose** (outbound).

---

## 2. Official rules — the only honest path

**Primary:** https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews  
**Requirements 1.3 update:** https://shopify.dev/changelog/updated-app-store-requirements-13-always-use-honest-and-transparent-review-practices (2026-07-06)  
**Reviews API:** https://shopify.dev/docs/api/app-home/apis/user-interface-and-interactions/reviews-api

### 2.1 Who can review

- Installed merchants, or within **45 days of uninstall**.
- Reviews unpublished until they meet **trust/quality** standards; may appear later.
- Unpublished reviews **do not count**.
- Rating is **not** a simple average (recent / useful / trustworthy).

### 2.2 What you may say

Official acceptable shape (paraphrase): we value feedback; tell us how we’re doing.  
**Forbidden:** “positive review,” incentives (discount, free month, feature unlock), install-time nag, unsolicited review email, fake reviews, forcing edits of 1-stars (you may ask them to **consider updating** after you fix a bug — no incentive).

July 2026 changelog: incentivizing can mean **portion of reviews removed, demotion, delist, Partner termination**. Trust logic tightened.

### 2.3 Reviews API constraints (official)

A modal **only shows** if Shopify allows it:

- Not if installed **&lt; 24 hours** (`recently-installed`)
- Not if already reviewed
- Not on mobile app
- Not if merchant ineligible
- **Once per 60 days**; **3 times per 365 days**
- Do **not** bind the prompt to a click that looks broken when rate-limited
- Ask at the **end of a successful workflow**, not onboarding

Deep link still exists: `https://apps.shopify.com/mcfly-analytics-public#modal-show=WriteReviewModal`

### 2.4 Honest playbook (legal; still hard)

This is the **only** first-50 path that does not bet the Partner account:

1. **Time-to-value before ask.** Official: do not ask at install. Mcfly’s blank store until CSV means the legal ask **cannot fire in week 1** unless SAMPLE → real is instant.  
2. **Trigger = first computed week with spend>0 and a rendered ratio.** Neutral copy. Opt-out forever.  
3. **Support-close ask.** Official best practice. Kleio/Report Pundit/Better Reports 5★ are **named humans**.  
4. **Founder replies on every review** (Kleio pattern).  
5. **14-day trial** so they have a week of data **and** time left to review (category default).  
6. **Free or cheap cap only if** you accept freeloaders (Lifetimely ≤50 orders; Report Pundit ≤1,000 lifetime). `RESEARCH_OPTION` / contradicts MASTER_PLAN.  
7. **Design partners in public shops** (not dev stores). Reviews from junk stores get archived (practitioner claim, thesaashub MARKET_REPORT).  
8. **Never pay for stars.** July 2026 enforcement is explicit.

**`CURRENT_RELIGION`:** prefer serious stores; no bait.  
**`EVIDENCE`:** that religion plus 7-day + paste = 0 reviews. Klar shows 0 reviews is survivable **with outbound**. Mcfly’s live site points **at** the listing.  
**`RISK` of giving it away:** TSC also claims ranking cares about **uninstall rate** (algorithm not public). Junk free installs can **hurt**.

### 2.5 How the five new apps actually got reviews (observed, not confessed)

| App | Reviews | Honest mechanism `INFERRED` from public facts |
| --- | --- | --- |
| Report Pundit | 2,026 | Free cap + **they build the report in chat** + 7 years |
| Recharge | 3,118 | Category-defining since 2014 + 60-day trial + customer-facing product |
| Loop | 442 | Customer-facing ops; Magic summary; CS names |
| Kleio | 20 | $29 + 14-day + founder replies + TW-defection story + MCP dopamine |
| Klar | 0 on Shopify | **Did not try**; OMR in DACH instead |

Mcfly’s closest **honest analog is Kleio**, not Report Pundit (no labor army) and not Recharge (not a checkout product).

---

## 3. App Store Ads — official economics only

**Hub:** https://shopify.dev/docs/apps/launch/marketing/advertising  
**Create / bidding:** https://shopify.dev/docs/apps/launch/marketing/advertising/create-ads  
**Billing:** https://shopify.dev/docs/apps/launch/marketing/advertising/ad-billing  
**FAQ:** https://shopify.dev/docs/apps/launch/marketing/advertising/faq

### 3.1 Surfaces and slots

| Type | Desktop slots | Mobile slots |
| --- | --- | --- |
| Search | 4 | 3 |
| Category / subcategory | 4 | 2 |
| Homepage | 4 | 4 |

Ads are badged; homepage/category use a **Sponsored apps** block.  
**Only published App Store apps.** Shopify does not advertise its own apps. One ad = one app. Ads **always land on the listing**, not mcflyads.com.

### 3.2 Auction (the expensive sentence)

- **CPC. First-price.** You pay **exactly your bid**, not one cent above the next bidder.  
- Search: bid **and relevance**. High relevance can win at a **lower** bid (official example: position 1 at $0.50 because relevance; highest bid can miss the slots).  
- If you are the only bidder, you still pay your bid and sit #1.  
- Bid changes **immediately** move rank.  
- Homepage/category: bid for the placement; auction on page load.  
- Minimum bid: **exists, amount not published**.  
- **Minimum daily budget: $5.00.**  
- Installed merchants **do not see your ad**; uninstallers can.  
- Incompatible shops (install requirements) do not see the ad.  
- VPN / traffic anomalies can hide ads.  
- Non-English keywords allowed (accents stripped).  
- BFS unlocks **plan-based targeting** (wave 1 BFS doc).

### 3.3 Billing (official)

- Charge per click = bid.  
- Invoiced every **30 days** or when balance **>$100**, USD.  
- Visa / MC / Amex; **no prepaid**.  
- Ad credits (promos) apply first; card after credits exhaust.  
- Credits apply across running **search** ads (FAQ).

### 3.4 What Shopify will tell you about ROAS on *your* ads (meta)

FAQ: customer + revenue attributed to **impression date**, not charge date. Metrics **grow for months**. Refunds **not** in revenue. Shopify revenue share **not** deducted in the number. Churned customers **not** removed from customer count. Max delay install→paid: **up to 64 days + trial**. Look at numbers **~60 days after impression**.

**`EVIDENCE`:** Shopify’s own ad analytics have the **same lag/trust problem** this corpus keeps finding on the merchant side. Do not steer Mcfly paid acquisition on day-7 “ad ROAS” in Partner Dashboard.

### 3.5 What official docs will **not** tell you

- Average CPC for “analytics,” “ROAS,” “profit,” “pixel.”  
- Suggested bid ranges (shown in Partner Dashboard per keyword; default **$1** if no data — AdsX MARKET_REPORT).  
- Conversion rates.

**Do not invent them.**

---

## 4. MARKET_REPORT math (stress test only)

https://www.adsx.com/blog/shopify-app-store-ads-guide (AdsX):

- First-price warning: bid $4 vs next $1.50 → you pay $4 every click.  
- **Illustrative** funnel (their table, not ours): $2 CPC → 15% click-to-install → 10% install-to-paid → **$133** per paying merchant; $29 plan → ~4.6 months payback.

**Do not publish $2 / 15% / 10% as Mcfly.** Use only as a **pessimism check**:

On Mcfly **$39** @ 20% Shopify share ≈ **$31.20** net (wave 1).  
If paid CPA to a **paying** merchant were even **$80–$150** (illustrative band, `UNVERIFIED`), payback is **3–5 months** — **if they do not churn when the CSV gets old**. A 7-day trial + paste desk makes install-to-paid **worse** than AdsX’s 10% cartoon.

TSC: 0-review listings convert views at ~1–2%. Ads send **listing views**. You are buying the worst converting object in their table.

**`RESEARCH_OPTION`:** do not buy App Store Ads until (a) TTV is automatic or SAMPLE-to-real is &lt;10 minutes, and (b) ≥10 honest reviews, and (c) keywords are **profit / P&L / spend vs sales**, not **pixel / attribution** (those clicks want Parkour Free).  
**`CURRENT_RELIGION`:** listing is live; site points at it. Buying ads into a 0-review pixel rail is lighting money on fire.

### 4.1 Keyword relevance trap (official + observed rail)

Official: relevance lowers CPC and raises rank.  
Observed: Mcfly’s “More like this” = Clarity / WeTracked / Parkour.  
If you bid `facebook pixel`, `capi`, `attribution`, Shopify’s relevance graph may **charge you to lose** to Free apps.

If you bid `profit analytics`, `net profit`, `ad spend`, you fight TrueProfit (899) and Kleio (20) — still hard, but **correct aisle**.

---

## 5. Honest distribution menu (research)

| Path | Official? | Cost shape | Review yield | Fit |
| --- | --- | --- | --- | --- |
| Organic search | Yes | $0 | 0 at 0 reviews | Dead until reviews |
| Category / Sidekick / BFS | Yes | Quality gates | After gates | Later |
| App Store Ads | Yes | ≥$5/day, first-price CPC | Only if TTV + listing convert | **Not yet** |
| Reviews API + support ask | Yes | Labor | Slow, clean | **Now** (after TTV) |
| Free / low cap | Policy-ok if not incentivized | Support | Fast (RP, Lifetimely) | Religion fight |
| Outbound / agency | Yes | Sales time | Reviews still need installs | S3/S4 |
| Course $79 | Side door | One-time | **No** App Store review | Not distribution |
| Fake / paid / “screenshot for 20% off” | **Illegal** | Account death | Negative | Never |

---

## 6. Worked **policy** example (not a forecast)

Legal week-1 for a design partner:

1. They install on a **real** shop.  
2. They add spend (or OAuth — `RESEARCH_OPTION`).  
3. Monday Close renders.  
4. In-app: “We value feedback…” + Reviews API.  
5. Founder replies if they write.  
6. No discount, no “5 stars,” no email blast.

Illegal week-1:

1. “Leave a review, get a free month.”  
2. Install modal: “Enjoying Mcfly? 5 stars!”  
3. Employees review from dummy shops.  
4. Agency writes reviews on client stores in exchange for a seat.

July 2026 1.3 exists to catch 2–4.

---

## 7. Religion

| ID | Topic | CURRENT | OPTION | EVIDENCE | RISK | Call |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | First 50 | Serious paid, hope | Legal ask after first close + 14-day + named human | Official reviews doc; Kleio 20 | Letting 7-day expire empty | **Do the legal loop** |
| D2 | Free for reviews | Refuse | RP/Lifetimely-style cap | RP 2026; TSC 50 | Uninstall ranking gossip | Only if D1 fails 30 days |
| D3 | App Store Ads | Unspecified | Wait for TTV + aisle + ≥10 reviews | Official first-price; AdsX cartoon | Burn cash on pixel keywords | **Wait** |
| D4 | Outbound vs store | Both half-done | Pick (Klar path **or** Kleio path) | Klar 0 vs Kleio 20 | Neither | Don’t do neither (R11) |
| D5 | Listing URL ads | Site as hero | Ads can only hit listing | Official | Site polish unused | Listing integrity first |

---

*Public info only. Partner Dashboard CPCs are the only real numbers; they are not in this repo.*
