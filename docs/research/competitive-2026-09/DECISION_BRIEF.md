# Decision brief — what to do (and what to kill)

**Date:** 2026-09-09  
**Audience:** founder only.  
**Mode:** RESEARCH ONLY. No agent ships product from this file. MASTER_PLAN stays locked until **you** amend it.  
**Inputs:** PRs #5–#13 + [`ENTERPRISE_LANDSCAPE.md`](./ENTERPRISE_LANDSCAPE.md) + [`KLEIO_GAP_ANALYSIS.md`](./KLEIO_GAP_ANALYSIS.md) + [`STRATEGY_KILL_CRITERIA.md`](./STRATEGY_KILL_CRITERIA.md).  
**Rule:** a kill is binary and observable. “Iterate” is not a kill. “Twitter wants a pixel” is not a kill.

---

## 0. The choice you actually have

Three facts that survive every wave:

1. Mcfly is live: **$39 / 7-day / 0 reviews / paste-first / “no OAuth”** on the site ([listing](https://apps.shopify.com/mcfly-analytics-public), [product](https://mcflyads.com/product)).
2. Kleio is live: **$29 / 14-day / 5.0 (20) / OAuth spend / CM1–CM3 / tax toggle / MCP / refuses MTA** ([kleio](https://apps.shopify.com/kleio), [getkleio.com](https://getkleio.com/)).
3. The App Store job that prints paid 5-stars is **assembled net profit + auto spend**. The job that prints volume 5-stars is **free pixel / free report**. Mcfly has neither.

You do **not** get to pick “be the empty chair.” You pick one of:

| Path | What it means this quarter | Religion |
| --- | --- | --- |
| **A. Fight the store** | Narrow S1: spend sync + claims-vs-cash + tax-sane till + Monday artifact. Fix the listing. 14-day. | Bend R3 / R4-B. Still no pixel, no P&L engine |
| **B. Become the P&L** | S2 vs Kleio $29 and TrueProfit $35. Only if you can name **one** wedge they structurally refuse | Rewrite “we are not a profit tracker” |
| **C. Leave the store as a brochure** | S3/S4 outbound: agencies and/or finance overlays. Paste-first is a feature | Keep religion. Accept 0 reviews |

**Do not pick A and C at once.** A hostile store with no outbound is S6 (score 9). That is how the listing dies of silence.

**Do not pick B without a wedge.** Cloning TrueProfit at $39 is suicide. Cloning Kleio at $39 is a $10 donation.

---

## 1. Recommended default (post-Kleio)

**If App Store is the primary acquisition channel → Path A (S1 revised).**

Wave B scored S1 at 19/25. Wave E cut it to **14–16** because Kleio already is “OAuth + tax-sane + daily desk” at $29. S1 is still the least-incoherent store path **only if** the **claims-vs-cash card** is real and used. Without that card, S1 is a late, thinner, more expensive Kleio.

**S1 Ring 1 (this is the product, nothing else):**

1. Meta + Google **spend** OAuth **or** paste. Same formula. TikTok later, not now.  
2. **Claim vs till** card: Ads Manager reported revenue (paste first; API only if counsel says Meta §10.d allows).  
3. Named sales definition: tax-in / tax-out, shipping, returns. One sentence a bookkeeper can recite.  
4. Monday Close email (or Slack).  
5. 14-day trial. Works-with: Admin, CSV, Sheets. Remove unshipped LTV/Goals from the listing.  
6. Keep **$39 flat**. Do not raise. Do not meter.

**Explicitly out of S1:** pixel, CAPI, MTA, assembled COGS engine, eight ad networks, MCP write, agency billing, dual-clock as a company, allocation that assumes sales ∝ spend without a warning.

**If the loved number users ask for is net profit, repeatedly → Path B (S2),** and you must write the wedge on a card before you write code: **offline + flat + claims-vs-cash**. If you cannot, do not start S2.

**If you will not OAuth and will not become a P&L → Path C.** Stop treating the App Store as the company.

---

## 2. Next week (calendar, not roadmap)

These are **founder / listing / evidence** moves. Not feature shipping.

| # | Do | Why this week | Done when |
| --- | --- | --- | --- |
| 1 | **Pick A, B, or C in writing.** Amend MASTER_PLAN §1–§4 if A or B. Or write “store = brochure.” | Agents must not ship fanfic. Live site and MASTER_PLAN already disagree on OAuth | A commit **you** make, not an agent |
| 2 | **Listing integrity** (even if product does not move): remove “mailto”; remove “Paid plan adds…” unless a free plan exists; pick **one** public name (formula first: “sales ÷ spend”); add Works-with Admin/CSV/Sheets; 5+ **SAMPLE**-labeled screenshots of a filled desk | Shopify files you next to Parkour. Typos + unshipped LTV/Goals are 1★ seeds | Live listing matches shipped reality |
| 3 | **Trial → 14 days** if billing lets you | Aisle default (TP/Lifetimely/Kleio/BR). 7-day + CSV = TTV death | Partner Dashboard shows 14 |
| 4 | **Run the interview scripts** on 5 humans you already know (`INTERVIEW_SCRIPTS.md`). One P1, one P2, one P3 if you have an agency, one P4 if you have a bookkeeper | We have **zero** first-party interviews. Public reviews are not your customers | 5 note rows in `db/interviews.jsonl` with real names you trust |
| 5 | **Open Partner Dashboard.** Write down views, installs, uninstalls, trial starts. Do not invent them in this repo | 0 reviews is not a kill in week one. **0 views** vs **views that bounce** is a different decision | A private note. Not a public metric |
| 6 | **Do not** start Meta/Google App Review until you have chosen Path A **and** read `COMPLIANCE_LANDMINES.md` | Review calendar is the S1 feasibility tax. Starting it on a maybe is how you waste the quarter | — |

**Kill this week’s plan if:** you will not pick A/B/C. Everything else is motion.

---

## 3. Next quarter (if Path A)

Observable outcomes. No conversion-rate fanfic.

| Gate | Pass | Fail → |
| --- | --- | --- |
| Spend | One design-partner store has Meta **and** Google spend green 14 days; recon ≤5% vs Ads Manager (MASTER_PLAN §11) | S1-K1 / S1-K2. Remainder is CSV = S6, or switch to C |
| Till | Shopify sales match Admin Total sales ±1% in the published tax mode | Do not ship the claim card on a lying numerator |
| Claim card | Used at least once (paste or API) | You shipped Kleio-minus-CM3. Pivot to B or C |
| Ritual | That human opens Monday Close three weeks running | S1-K3. Love loop is dead |
| Listing | LTV/Goals claims gone unless shipped; 14-day live | Integrity kill — you are lying on the store |
| Reviews | Do **not** set a public review target. If a DP leaves a review, it is a gift | 0 reviews after a quarter of **real DPs using the desk** → Path C or S7-lite, not “more features” |

**Do not this quarter:** BFS chase (needs 50 paid installs + 5 reviews), GMV tax, $79 list price, MCP write, TikTok+Snap+Pinterest zoo, pixel build, course-as-company.

**Money this quarter:** stay $39. The only allowed expansion *design* is an agency SKU **spec**, not a ship, unless you chose Path C.

---

## 4. If religion flexes (the honest menu)

| Flex | Call | Do | Do not |
| --- | --- | --- | --- |
| **R3 OAuth spend** | **Yes** if Path A | Spend-only. Meta + Google. CSV for billboards | Conversion API, CAPI, “true ROAS” models |
| **R4 Trial / free** | **14-day now.** Forever-free only if paid path still = 0 reviews after you had real DPs | Match Kleio/TP | 7-day + homework |
| **R5 Price** | **Keep $39 flat** | Agency seat later | GMV slider, order meter, $79 at 0 reviews |
| **R6 Name** | **One name.** Formula in sentence one | “Sales ÷ spend (blended), we call it X” | MER **and** Total ROAS in parallel |
| **R7 Costs** | **S2 only.** Typed % stays for S1 with a “this is not net profit” label | Cost-incomplete flag if you assemble | Silent averages |
| **R8 Allocate** | **Show the assumption or hide the card** | Pause-test protocol as a checklist | `sales ∝ spend` as advice |
| **R1 Pixel** | **Partner only** | Works-with Parkour/Elevar | Build a Mcfly pixel |
| **R2 MTA** | **Keep refuse** | Claims-vs-cash | 4–7 models |
| **R12 Profit** | **If Path B, rewrite MASTER_PLAN.** If Path A, MER is the method, profit is the *job you are not taking yet* | Honesty on the listing | Pretending Total ROAS is net profit |
| **R11 Channel** | Pick store **or** outbound | — | Neither |

The bends that raise four scores: **R3, R4-B, R8, listing integrity**.  
The breaks that look like money and usually kill the company: **R1-A, R2, R5-GMV, R10-A (Moby credits)**.

---

## 5. Kill criteria (copy these onto a card)

From Wave E, tightened. Fire **any one** and stop the strategy, not the sprint.

### Path A / S1 — stop building the governor

| ID | Kill | Why it’s fatal |
| --- | --- | --- |
| **S1-K1** | Meta **or** Google production access refused, or no decision in a time you will actually wait, **and** you will not run CSV-only | Ease was the App Review. Remainder is S6 |
| **S1-K2** | Spend recon >5% vs Ads Manager for **14 days** after a TZ/currency fix | A lying denominator is TW-VAT |
| **S1-K3** | The design partners you **actually have** will not open the weekly artifact | Dead loop = dead S1. Do not invent N=30 |
| **S1-K4** | API claim card blocked by Meta §10.d **and** merchants will not paste **and** you refuse to sell spend-only at $39 vs Kleio $29 | Wedge gone, price lost |
| **S1-K5** | You will not amend MASTER_PLAN / live “no OAuth” sentence | S1 remains fanfic. Agents must not ship it |
| **S1-K6** | First loved number users ask for is **net profit**, repeatedly, and they leave for Kleio/TrueProfit | S1 was a delay. Go to Path B or stop |

**Do not kill S1 because:** Kleio has 20 reviews (narrow, don’t freeze) · Polar lists MER · the allocator is embarrassing (hide it).

### Path B / S2 — stop the P&L

| ID | Kill |
| --- | --- |
| **S2-K1** | You cannot state the wedge vs Kleio **and** TrueProfit in one sentence a merchant repeats |
| **S2-K2** | Cost-incomplete flag is not shipped **before** a profit number is shown (Community 657805) |
| **S2-K3** | You start matching TrueProfit’s order surcharge or Kleio’s eight ad networks |

### Path C / S3–S4 — stop outbound

| ID | Kill |
| --- | --- |
| **S3-K1** | Five agencies will not pay more than SyncWith $4.99 + their own tab |
| **S4-K1** | You cannot get **one** finance lead to put Mcfly in a board pack next to TW/NB |

### Always-on integrity kills

| ID | Kill |
| --- | --- |
| **I-1** | Listing claims LTV/Goals/OAuth/free plan the app does not do |
| **I-2** | You publish an invented review count, install count, or MRR |
| **I-3** | You start a pixel to “get reviews” |

---

## 6. What not to do (even if a chat suggests it)

- Ship pixels, MTA, or a connector zoo from research.  
- Raise to $79 or add a GMV slider at 0 reviews.  
- Treat “anti-attribution” as a review-winning phrase. Reviewers praise **profit they trust**, **named support**, and **tracking that matches Events Manager**.  
- Chase Built for Shopify this quarter.  
- Amend MASTER_PLAN in an agent commit. **You** amend it.  
- Fly-deploy or feature-ship from this branch. Research only.

---

## 7. One paragraph

Kleio closed the “cheap flat cash desk” hole. TrueProfit closed the “loved paid profit” hole. Shopify closed the “we’ll ingest ad spend” hole — it won’t. Mcfly’s remaining honest products are (A) the **governor that shows the lie** next to auto spend, (B) a **wedged** profit-lite desk, or (C) an **agency/finance** company that treats the App Store as a brochure. Paste-only $39 with a 7-day trial and a sermon is not a fourth option. It is how Margn looks at 0 reviews. Pick A, B, or C this week. Kill with the table, not with vibes.
