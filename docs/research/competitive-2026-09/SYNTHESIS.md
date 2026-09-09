# Synthesis — vNext strategic options (research only)

**Date:** 2026-09-09  
**This is not a ship order.** It is a menu. MASTER_PLAN stays locked until the founder amends it.

**Wave B scores this menu:** [`VNEXT_OPTION_SCORECARD.md`](./VNEXT_OPTION_SCORECARD.md) (money / love / ease / feasibility / religion-flex). Love, money, onboarding, and 1-star physics: [`LOVE_LOOPS.md`](./LOVE_LOOPS.md) · [`MONEY_MODEL.md`](./MONEY_MODEL.md) · [`ONBOARDING_BATTLE.md`](./ONBOARDING_BATTLE.md) · [`ANTI_PATTERNS.md`](./ANTI_PATTERNS.md).

Four scores everywhere: **money · love · ease · real problems**. Religion is a hypothesis. Evidence is public URLs. No invented install or revenue forecasts.

---

## 0. What is actually true on 2026-09-09

1. Mcfly **is live**: https://apps.shopify.com/mcfly-analytics-public — $39/mo, 7-day trial, launched Sept 7, **0 reviews**.
2. Shopify already files it next to **free pixels/heatmaps**, not next to Polar or TrueProfit.
3. The paid cluster that prints reviews is **net profit + autopilot spend** (TrueProfit 5.0/899 from $35; Lifetimely 4.9/535; BeProfit 4.5/202).
4. The love cluster that prints reviews is **free tracking** (Clarity 2,125; Parkour 191; WeTracked 125).
5. The job Mcfly names — *Admin has sales, not spend* — is **real** (https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4).
6. Operators already solve that job with a **weekly Sheet** (r/shopify 1rpjuk0; r/PPC 1qgb8mg) or by buying a suite and ignoring half of it.
7. Finance’s real job is **assemble net profit and reconcile the bank** (Community 657805, 577364; A2X 5.0/359).
8. Repo religion (no OAuth, ~$79, cash MER, refuse pixels) **already disagrees** with live site (no OAuth, $39, Total ROAS) and with MASTER_PLAN Phase 2 (OAuth planned). Flexibility is not hypothetical; it is **inconsistent**.
9. Allocation without channel sales assumes sales ∝ spend (`packages/mer-core/src/allocation.ts`). Media buyers will not love that.
10. There is no public evidence that “anti-attribution” is a **review-winning** phrase. Reviewers praise profit they trust, support with a first name, and tracking that matches Events Manager.

**Ruthless line:** Mcfly is priced like TrueProfit, scoped like a spreadsheet, merchandised like Parkour, and reviewed like an app that does not exist.

---

## 1. Constraints that do not care about religion

- Shopify rating is not a simple average; reviews need installs; Magic summary needs **100 written + 4.0** (https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews).
- You cannot put testimonials on the listing (requirements 4.3.7).
- 7-day trial + blank store until CSV is a **TTV mismatch** vs the 14-day profit cluster.
- 20% (or 15%) Shopify share on $39 ≈ **$31–$33** net. Polar’s listing floor is $750. Volume or agency seats must do the work.
- TSC MARKET_REPORT: 0–25 reviews → ~1–2% view-to-install. Treat as gossip, but the direction matches 0-review reality.

---

## 2. Strategic options (mutually exclusive enough to choose)

Each option: thesis, who, what to build *if* chosen later, religion tag, four-score, evidence, risk, kill criterion.

---

### Option S1 — “Cash governor” (recommended default if money+love+ease matter)

**Thesis:** Stay anti-path. Add **OAuth spend sync** + **claims-vs-cash** + **finance definitions** + **Monday email**. Do not build a pixel. Do not become a P&L suite.

**Persona:** P2 media buyer (daily ease) + P4 finance (definitions) + P1 founder (one number).

**vNext surface (research):**
- Connect Meta/Google/TikTok spend **or** paste. Same formula.
- Card: Ads Manager claimed revenue vs Shopify sales (their claim / our till).
- Tax/shipping/returns toggle.
- Slack/email Monday Close.
- 14-day trial. Works-with logos. Review modal after first computed week.
- Keep $39 flat. Add agency seat later.

**Religion:** `RELIGION_BEND` — MASTER_PLAN Phase 2 already wanted OAuth; live site currently forbids it.

**Scores:** Money **H** · Love **H** · Ease **H** · Real **H** (problems 3+4+15)

**Evidence:** Community 134251; r/PPC 1u81q7r + 1pqv5kh; TrueProfit already syncs spend; Better Reports proves push artifacts; TW VAT 1★.

**Risk:** App Review calendar. Connector support. Still thinner than TrueProfit on costs.

**Kill if:** 30 design partners still won’t open the email; spend sync drifts >5% (already a MASTER_PLAN kill).

**Why this maximizes without becoming TW:** you remain the **governor**, not the OS. Pixel partners (Parkour/Elevar) stay complementary.

---

### Option S2 — “Profit-lite desk” (highest collision, highest review gravity)

**Thesis:** The market already told you the loved paid job is **net profit after COGS/fees/shipping/ads**. Add that on top of Total ROAS. Keep offline channels and flat price as the wedge TrueProfit structurally refuses (order surcharge; no billboard religion).

**Persona:** P1 founder (TrueProfit buyer) + P4.

**vNext:** Shopify Cost per item + fees + shipping + custom expenses + auto spend + “cost incomplete” flag + product-level contribution with **disclosed** blended allocation.

**Religion:** `RELIGION_BEND` — still no MTA. Break-even becomes computed, not typed.

**Scores:** Money **H** · Love **H** · Ease **M** · Real **H** (problem 1)

**Evidence:** TrueProfit 899; Lifetimely 535; Community 657805 recipe; BeProfit 202.

**Risk:** Feature race with a 5.0/899 incumbent. Historical COGS hell. VAT 1-stars. You become “another profit tracker” on a crowded rail (TrackProfit / Margn / MarginLens already surround BeProfit).

**Kill if:** cannot beat TrueProfit on **one** structural wedge (offline + flat + claims-vs-cash) within two review-quarters.

**Do not do S2 without a wedge.** Cloning TP at $39 is suicide.

---

### Option S3 — “Agency scoreboard” (best fit for CURRENT paste-first)

**Thesis:** Paste-first is not a bug for agencies — they already live in Sheets. Sell **N stores, one close pack, client-safe slides**, $X per portfolio.

**Persona:** P3.

**vNext:** multi-store, CSV/Sheets in, PDF/Slack out, white-label numbers, no “your pixel is theater” on the client slide.

**Religion:** `CURRENT_RELIGION` kept.

**Scores:** Money **H** (if 10+ agencies) · Love **M–H** · Ease **M** · Real **H** for that persona · **App Store love L** (agencies don’t leave 899 reviews)

**Evidence:** SyncWith affiliate-sheet review; r/PPC agency Sheets; Metorik/BeProfit multi-store SKUs; Polar unlimited users.

**Risk:** Outbound-heavy. App Store stays empty. Support N×. Becomes a services company.

**Kill if:** 5 agencies won’t pay more than SyncWith $4.99 + their own tab.

---

### Option S4 — “Suite overlay” (enterprise-adjacent, small N, high ARPU)

**Thesis:** Do not replace TW/Polar/NB. Sell the **number finance signs** after the suite. $39–$99 on top. Dual clock. Tax-sane. Export for A2X/bookkeeper.

**Persona:** P5 + P4.

**vNext:** claims-vs-cash, definition sheet, accrual vs delivery, CSV/API out. Maybe MCP read-only.

**Religion:** `CURRENT_RELIGION` (no pixel) + `STRETCH`.

**Scores:** Money **M–H** per account · Love **M** · Ease **M** · Real **H** · Volume **L**

**Evidence:** Polar already lists MER; r/PPC already uses MER as North Star *while keeping* a suite; TW 4.1/16% 1★ hangover; A2X 359.

**Risk:** Suites add a “finance MER” tile and erase you. Sales cycle is human. $39 may read as not-serious (RESEARCH_OPTION: $99 overlay price).

**Kill if:** cannot get one design-partner finance lead to put Mcfly in the board pack next to TW/NB.

---

### Option S5 — “Pixel company” (max review velocity, max brand risk)

**Thesis:** The App Store rail already thinks you are Parkour. Become a CAPI + cash desk. Freemium pixel, paid desk.

**Persona:** P2, then upsell P1.

**vNext:** Mcfly pixel or tight Parkour/WeTracked partnership + passback of *new-customer revenue* (Apex-shaped, cash North Star).

**Religion:** `RELIGION_BREAK`.

**Scores:** Money **H** if it works · Love **H** · Ease **H** · Real **disputed** · Brand **L**

**Evidence:** Parkour 191 Free; WeTracked “I don’t need another dashboard”; Elevar $225; entire TW/Polar industry; WeTracked 1★ when accuracy cannot be evidenced.

**Risk:** Compete with Free. EMQ support hell. 16% 1-star TW fate. Founder voice (“platforms are lying”) becomes hypocrisy. MASTER_PLAN kill-on-contact.

**Only consider S5 as a *partnership* (S5b), not a rebuild.** S5b = list “works with Parkour/Elevar,” do not own the pixel.

---

### Option S6 — “Stay narrow + course” (cheapest, likely dies)

**Thesis:** Keep paste-only, $39, $79 course, anti-pixel sermons. Fix listing typos. Wait for serious stores.

**Persona:** none proven.

**Religion:** `CURRENT_RELIGION` purity.

**Scores:** Money **L** · Love **L** · Ease **L** · Real **M**

**Evidence:** 0 reviews after launch; TSC 1–2% conversion gossip; SyncWith already is the $4.99 version of this job.

**Risk:** App Store irrelevance. Course is consulting-energy (MASTER_PLAN discarded consulting as core).

**Kill if:** 30 days post-launch still 0 reviews and Partner Dashboard views don’t convert. (Founder has the dashboard; this agent does not.)

---

### Option S7 — “Free desk, paid depth” (distribution physics)

**Thesis:** Lifetimely Free ≤50 orders and TW Free are why they have reviews. Ship a forever-free **Total ROAS for one channel / 50 orders** and charge $39 for multi-channel + Goals + LTV.

**Religion:** `RELIGION_BEND` vs “no forever-free bait.”

**Scores:** Money **M** (volume, take-rate) · Love **H** · Ease **H** · Real **M** · Support load **H**

**Evidence:** Lifetimely 535; TW 91 despite 16% 1★; Clarity 2125; official review rules (no paid-for-review). TSC: first 50 reviews are the investment.

**Risk:** MASTER_PLAN freeloader flood; uninstall rate may hurt ranking (TSC MARKET_REPORT); Shopify trial 180-day vs a real free plan is cleaner than trial-abuse.

**Pair with S1 or S2**, not alone.

---

## 3. Comparison matrix

| Option | Religion | App Store fit | Collision | Time-to-first-review (qualitative) | Four-score |
| --- | --- | --- | --- | --- | --- |
| S1 Governor | Bend (OAuth) | Profit/analytics aisle if copy changes | Medium (TP still deeper) | Medium | **Best balance** |
| S2 Profit-lite | Bend | Profit aisle | **High (TP)** | Medium-fast | High if wedged |
| S3 Agency | Keep | Weak | Low | Slow | High money, low love-at-scale |
| S4 Overlay | Keep | Weak | Low | Slow | Niche high-ARPU |
| S5 Pixel | Break | Current rail | High (free pixels) | Fast | High risk |
| S5b Partner pixel | Bend | Mixed | Low | Medium | Cheap hedge |
| S6 Narrow | Keep | Current rail, paid among frees | SyncWith | Slowest | Worst |
| S7 Freemium | Bend | Strong | Support | Fastest | Needs a paid core (S1/S2) |

**If the founder literally wants maximum chance of money + love + ease + real problems:**  
**S1 + S5b + S7-lite (or 14-day, not forever-free) + listing integrity.**  
Add **S2 wedge pieces** (fees, Cost per item) only if S1’s number is still not loved.

**If the founder wants religion purity:** S3 + S4 outbound, accept App Store as a brochure.

**Do not:** S5 rebuild, S6-as-strategy, GMV tax, metered AI credits, allocation advice that assumes sales ∝ spend without a warning.

---

## 4. Packaging recommendation *inside* whichever option

Keep **flat $39** as the public moral (live site already burned the GMV-tax story). Do not raise to $79 until reviews exist. Do not order-meter unless you want BeProfit’s zombie 1-stars.

Add later, not instead:
- Agency portfolio SKU (S3)
- Optional $99 “finance overlay” (S4) — only if S4 is chosen
- $79 course can stay a side door; do not let it become the company

Trial: **14 days** unless TTV becomes truly instant (OAuth + first number in <10 minutes).

---

## 5. Listing recommendation (all options except “ignore App Store”)

From `LISTING_TEARDOWNS.md`, do these even if product does not move (they are copy/integrity, still research until founder edits the listing):

1. Remove “mailto” and “Paid plan adds…” unless a free plan exists.  
2. Move “no pixels” out of the 5th bullet.  
3. Align LTV/Goals claims with shipped reality.  
4. Add Works-with: Shopify Admin, Google Sheets, CSV.  
5. Show 5+ screenshots of a **filled** SAMPLE desk labeled SAMPLE.  
6. Pick one public name: **Total ROAS** (live) or **cash MER** (repo), not both.

---

## 6. What we still must not invent

- Install counts, view-to-install for Mcfly, churn, contribution margin of the business.
- Northbeam official price.
- Polar $400 vs $750.
- “X% of merchants want MER.”
- TW 60,000 brands, NB 37% ROAS — `VENDOR_CLAIM` only.

---

## 7. Founder decision checklist

Answer in-repo later; do not make the agent ship:

- [ ] Is App Store the primary acquisition channel? (If no → S3/S4. If yes → S1/S2/S7.)
- [ ] May we OAuth spend without a pixel? (If no → S3/S6 and accept ease loss.)
- [ ] Must we show net profit, not just sales÷spend? (If yes → S2 wedge.)
- [ ] Is a limited free SKU allowed to buy the first 50 reviews? (S7)
- [ ] Who is the design-partner human who will be “Juan / Bryce / Nora”?
- [ ] Amend MASTER_PLAN §1–§4 if S1/S2/S7 is chosen — **do not let chat silently overwrite it.**

---

## 8. One paragraph

Mcfly’s religion is *intellectually* right: platforms over-claim, Admin has no spend, blended sales÷spend is the adult number. Public evidence says the *market* pays and reviews **profit autopilot** and **free pixels**. A paste-only $39 desk with a 7-day trial and zero reviews maximizes none of money, love, ease, or problem-coverage. The least-incoherent vNext is a **cash governor**: auto spend, claims-vs-cash, tax-sane definitions, Monday artifact, optional pixel partner, 14-day trial, flat price, agency later. That bends religion without becoming Triple Whale. Becoming Triple Whale is how a $250-budget founder dies of scope — that part of MASTER_PLAN is still true. Staying a sermon with a CSV box is how the listing dies of silence.
