# Strategy kill criteria — S1 stress-test and S2 / S3 / S5 rivals

**Date:** 2026-09-09  
**Wave:** E  
**Mode:** RESEARCH ONLY. Not a ship order. Does not amend `MASTER_PLAN.md`.  
**Inherited scores (Wave B `VNEXT_OPTION_SCORECARD.md`):** S1 **19** · S2 **16** · S3 **16** · S5 rebuild **14** · S5b modifier · S4 **13** · S6 **9** · S7-lite bolt-on **17**.  
**This wave’s job:** write **observable kills** so a founder can stop, not “iterate.” Stress-test S1’s 19 against Kleio, pipes, and policy. Specify S2 / S3 / S5 as real alternatives, not leftovers.

Companions: `S1_PRD_LITE.md` · `KLEIO_GAP_ANALYSIS.md` · `INTEGRATION_MAP.md` · `COMPLIANCE_LANDMINES.md`.

---

## 0. How a kill works here

A kill criterion is **binary and public-or-dashboard-visible**. It is not “vibes got bad.”

| Kind | Example | Who can see it |
| --- | --- | --- |
| **Already in MASTER_PLAN §11** | Spend recon >5% for 14 days; DPs won’t open weekly in 30 days | Founder + logs |
| **Market object** | A named rival already shipped the desk cheaper with reviews | This folder |
| **Calendar** | App Review refused or silent 60 days | Partner / Meta / Google inboxes |
| **Policy** | Meta §10.d blocks the wedge card | Counsel / App Review essay |
| **Integrity** | Listing claims a thing the app does not do | Live listing vs repo |

**Anti-kills** (do not use these to stop):

- Triple Whale has more features.
- Someone on Twitter wants a pixel.
- A chat prompt prefers a shinier niche.
- Review count is 0 **in the first fortnight after a Sept 7 launch** — too early to kill S1; **not** too early to kill S6-as-strategy (Wave B already called S6 a 9).

Scores below are **research judgment**. Wave E **revises S1 to 14–16** (`S1_PRD_LITE.md` §1). Other Wave B sums stay unless a section says otherwise.

---

## 1. S1 — Cash governor (still the default **if** App Store is the channel)

**Thesis (unchanged):** anti-path; OAuth **spend**; claims-vs-cash; tax-sane till; Monday artifact; no pixel; no P&L engine.

**Wave E correction:** Kleio already is OAuth + tax-sane + daily desk at **$29** and **refuses** the claim card. S1 without that card is a late Kleio. S1 with an **API** claim card may be a Meta policy problem. The live product is **paste-a-claim + ShopifyQL till + Meta/Google spend**.

### 1.1 What “S1 is working” would look like (not a forecast)

Observable, no invented conversion rates:

1. A design-partner store has **green** Meta and Google spend for 14 days, recon ≤5% vs Ads Manager (MASTER_PLAN).
2. Till matches Admin Total sales ±1% in the published tax mode (`INTEGRATION_MAP.md`).
3. At least one human **opens Monday Close** three weeks running (MASTER_PLAN weekly-open).
4. The claim card is used (paste or API) at least once — otherwise we shipped Kleio-minus-CM3.
5. Listing no longer claims unshipped LTV/Goals.

If (1)–(3) happen and (4) does not, S1 succeeded as **ease** and failed as **wedge**. That is a **pivot to S2 or S3**, not a celebration.

### 1.2 Kill S1 (stop building the governor)

Kill **the strategy** if **any** of these fire:

| ID | Kill | Why it’s fatal |
| --- | --- | --- |
| **S1-K1** | Meta **or** Google production access refused, or no decision in a time the founder will actually wait, **and** we will not run CSV-only | S1’s Ease 4 was the App Review. Remainder is S6. |
| **S1-K2** | Spend recon >5% vs Ads Manager for **14 days** after a good-faith TZ/currency fix (MASTER_PLAN §11) | Reliability > charts. A lying denominator is TW-VAT. |
| **S1-K3** | Design partners we actually have (do **not** invent N=30) will not open the weekly artifact | The love loop was the email. Dead loop = dead S1. If N is tiny, use **all of them**, not a fantasy sample. |
| **S1-K4** | Combined API claim card is blocked by Meta §10.d **and** merchants will not paste a claim **and** we refuse to sell spend-only at $39 vs Kleio $29 | Wedge gone, price lost. |
| **S1-K5** | Founder will not amend MASTER_PLAN / live site OAuth sentence | S1 remains fanfic. Agents must not ship it. |
| **S1-K6** | First loved number users ask for is **net profit**, repeatedly, and they churn to Kleio/TrueProfit | S1 was a delay. Go to §2 or stop App Store. |

### 1.3 Do **not** kill S1 because

- Kleio has 20 reviews (that is a **reason to narrow**, not to freeze).
- Polar lists MER (they list everything).
- Allocation card is embarrassing (disarm it; don’t burn the desk).

### 1.4 S1 residual risk if it “wins”

$39 flat still does not expand (Money 2–3). Connector support never ends (60-day Meta). We remain thinner than TrueProfit. Wave B’s 19 treated Religion-flex as a virtue; Wave E treats it as **permission**, not a moat.

---

## 2. S2 — Profit-lite desk (highest collision)

**Thesis:** the paid job that prints 5-stars is **net profit after COGS / fees / shipping / ads** (`PROBLEM_BANK.md` #1). TrueProfit 5.0/~899 from $35 · Lifetimely 4.9/~535 · BeProfit 4.5/202 · **Kleio 5.0/20 at $29 with a published CM1–CM3 waterfall**. Keep **offline + flat + claims-vs-cash** as the only visible structural wedges.

**Religion:** `BEND` + rewrite MASTER_PLAN “we are not a profit tracker.” Break-even becomes **computed**. Still no MTA. Ads stay **total** spend (AP1).

**Wave B:** 16/25 (Money 4 · Love 4 · Ease 3 · Feasibility **2** · Religion-flex 3). Feasibility 2 is the honest cell.

### 2.1 What S2 actually is (so we can kill it)

Not “add a profit tile.” A minimum S2 that would not be laughed out of Kleio’s FAQ:

| Must have | Kleio already | TrueProfit already |
| --- | --- | --- |
| Shopify cost + **missing-cost flag** | Yes (Missing Data queue) | Yes (reviews mention variants) |
| Shopify Payments fees; other gateways typed | Yes | Yes |
| Shipping / fulfillment / returns as variable costs | Yes (rules + ShipHero) | Yes (shipping-cost 5-stars) |
| Auto spend (else the P&L is a CSV novel) | Yes (8 platforms) | Yes (listing) |
| Tax-out below revenue | Yes | Mixed (VAT 1-stars exist in-aisle) |
| Cost-incomplete banner | Implied | Community 657805 demanded it |

**Optional later (do not start here):** cohorts, LTV:CAC, MCP write, Amazon, inventory.

**Wedge required (Wave B + this wave):** at least **one** of {first-class offline ledger, claims-vs-cash exhibit, true flat-no-surcharge while TP surcharges per order}. Kleio already **is** flat. So vs Kleio the wedge **collapses to offline + claim card**. Vs TrueProfit, flat + offline + no order meter still matters.

### 2.2 Kill S2

| ID | Kill | Why |
| --- | --- | --- |
| **S2-K1** | Cannot name **one** wedge vs **both** TrueProfit **and** Kleio in a single listing sentence a stranger believes | Cloning TP at $39 is suicide (`SYNTHESIS.md`). Cloning Kleio at $39 is charity. |
| **S2-K2** | Historical COGS / variants / deleted SKUs make the number untrustworthy on the first design-partner store and we have no **cost-incomplete** honesty | Community 657805 is a graveyard of this. |
| **S2-K3** | VAT / tax-in profit ships and a EU/UK merchant 1-stars us the TW way | Review physics: 16% 1★ is a suite-sized hole. We are not a suite. |
| **S2-K4** | We start SKU-level “this product loses money after ads” by **silently** allocating blended spend | That is MTA-by-shame. Religion-flex 3 becomes 1. |
| **S2-K5** | Capital/time: cost engine still wrong after we have already burned the Meta/Google calendar **and** a warehouse | Feasibility 2 was a warning. One-founder S2 is how MASTER_PLAN’s $250 constraint dies. |
| **S2-K6** | MCP / AI write-scope pulled in to “keep up with Kleio” before the waterfall is trusted | PCD + blast radius (`COMPLIANCE_LANDMINES.md` §4). |

**Two-review-quarter kill (Wave B):** if after two public review-quarters we are still “another profit tracker” on the BeProfit rail (TrackProfit / Margn / MarginLens) with no wedge showing in review text, stop S2. We do not have those quarters yet — do not pretend we do.

### 2.3 When S2 should **win** over S1

- App Store is the channel **and**
- P1’s Monday question is “did we keep dollars?” not “what was blended ROAS?” **and**
- The founder will staff Missing-COGS support **and**
- The listing lead is **offline + claim + flat**, not “we also have CM3.”

Otherwise S2 is ego: the review corpus is a siren.

### 2.4 S2 revised note

Wave B Money 4 assumed the aisle prints cash. Kleio $29 means **our** Money on a me-too waterfall is **3** at best (same wallet, worse price). Sum would fall to **15** if scored today. Still not the worst option — still not the 19.

---

## 3. S3 — Agency scoreboard (best CURRENT_RELIGION fit)

**Thesis:** paste-first is native for agencies (r/PPC [1qgb8mg](https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/); SyncWith). Sell **N stores, one close pack, client-safe slides**, priced per **portfolio**, not $39 × 30.

**Religion:** `KEEP` paste (OAuth optional as *their* MCC/System User). No pixel sermon on the client PDF.

**Wave B:** 16/25 (Money 4 · Love **2** · Ease 3 · Feasibility 3 · Religion-flex 4). Love 2 is App Store love. Agency love can still be Slack.

### 3.1 What S3 actually is

| In | Out |
| --- | --- |
| Multi-shop workspace | Pixel, MTA |
| Ingest the sheet they already have (or CSV) | Re-typing 12 clients |
| Monday pack: till, spend, cash ROAS, BE, completeness | “Cut Meta 20%” from ∝ |
| White-label numbers | “Your Ads Manager is lying” on **client** slides |
| Isolation: Shop A ≠ Shop B (Meta §10.g) | Shared lake, shared token |
| Price: $X / portfolio / month | $39/store unless they insist |

Evidence of the SKU shape (not our forecast): Metorik multi-store from $75 / 5 stores · BeProfit Plus $249 unlimited shops · Polar unlimited users @ $750. SyncWith **$4.99** is the **kill price** we must beat on **time saved**, not on connectors.

### 3.2 Kill S3

| ID | Kill | Why |
| --- | --- | --- |
| **S3-K1** | **5 agencies** (or every agency we actually pitch — do not invent 5) will not pay more than SyncWith + a tab | We are a tax. MASTER_PLAN discarded the connector zoo for this reason. |
| **S3-K2** | We cannot ingest their sheet and make them re-enter | Ease 3 assumed ingest. Without it we are S6 × N. |
| **S3-K3** | Isolation fails once (wrong client’s spend on a PDF) | Compliance + the agency fires us. See landmines §5. |
| **S3-K4** | Founder becomes unpaid CS / media-ops for 12 stores | MASTER_PLAN discarded consulting as core. S3 slides into it. |
| **S3-K5** | We run S3 **and** a hostile 0-review listing **and** no outbound | Wave B R11: don’t do neither. S3 **requires** outbound. If the founder will not sell, S3 is dead on arrival. |
| **S3-K6** | App Store is declared the **primary** channel and we still pick S3 | Incoherent. Agencies do not print 899 listing reviews. Pick S1/S2 or admit the store is a brochure. |

### 3.3 When S3 should **win**

- Founder will do outbound (LinkedIn, existing ads relationships).  
- App Store is a brochure.  
- Design partners are **agencies**, not single-store P1s.  
- We will not build Meta Advanced Access **in order** to get S3 (they already have MCC).

S3 is the only option that makes **today’s paste-first code** a feature. That is its entire intellectual case. It is also how the public listing stays at 0 forever.

---

## 4. S5 — Pixel company · S5b — partner

### 4.1 S5 rebuild (not recommended)

**Thesis:** Shopify already files us next to Parkour. Become CAPI + cash desk. Freemium pixel, paid governor.

**Wave B:** 14/25 (Money 4 · Love 4 · Ease 4 · Feasibility **1** · Religion-flex **1**). Anti-patterns AP7/AP6/AP11.

**Evidence of WTP:** Parkour Free 4.9/191 · WeTracked 4.8/125 · Analyzify 4.7/313 · Elevar 4.7/168 from $225 · entire TW/Polar industry.

**Evidence of death:** WeTracked 1★ cannot evidence accuracy vs native · TW 16% 1★ · compete with **Free** · MASTER_PLAN kill-on-contact · PCD Level 2 firehose.

#### Kill S5 (should already be dead)

| ID | Kill | Why |
| --- | --- | --- |
| **S5-K1** | MASTER_PLAN §1 still says pixels are theater **and** the founder will not rewrite it | Agents must refuse. |
| **S5-K2** | We cannot beat Parkour on **price** (they are $0) or Elevar on **infra** | Review rail is free. Paid pixel needs a miracle. |
| **S5-K3** | First EMQ / consent / iOS ticket we cannot close in a week | Support is the product. We don’t have Juan. |
| **S5-K4** | We use pixel data to “prove” cash ROAS | Hypocrisy. Brand suicide. WeTracked-shaped 1-star. |
| **S5-K5** | $250 capital vs a measurement company | Feasibility 1. This is how founders die of scope. |

**Only reopen S5 if** the founder explicitly amends MASTER_PLAN §1–§2 **and** raises capital **and** accepts becoming a tracking vendor. That is a different repo.

### 4.2 S5b partner (cheap hedge, not a strategy)

**Thesis:** listing “Works with Parkour / Elevar.” Do not ingest their events.

**Modifier (Wave B):** +1 Love / +1 Ease on S1, Feasibility 4, Religion-flex 4.

#### Kill S5b

| ID | Kill | Why |
| --- | --- | --- |
| **S5b-K1** | We ingest the partner event stream | That’s S5. PCD + ToS. |
| **S5b-K2** | Partner is WeTracked-class and we **vouch** for accuracy | Their 1★ becomes ours. |
| **S5b-K3** | Works-with logos without a working deep link / install path | Listing fiction (we already have LTV fiction). |

S5b is a **checkbox**. If S1 is chosen, do it. If S3 is chosen, skip it.

---

## 5. The other menu items (short kills, so they cannot sneak back)

### 5.1 S4 — Suite overlay

**Kill S4-K1:** cannot get **one** finance lead to put Mcfly in the board pack next to TW/NB.  
**Kill S4-K2:** we imply we are the books (liability).  
**Keep as a sentence** on the site, not as a company. Wave B sum 13.

### 5.2 S6 — Stay narrow + course

**Kill S6-K1:** 30 days post-launch, 0 reviews **and** Partner views do not convert (founder dashboard). Launch was **2026-09-07**; the clock started.  
**Kill S6-K2:** we use “religion” to avoid MASTER_PLAN’s own weekly-open kill.  
Wave B sum **9**. Live product scores **10**. This is the default if every other option is refused.

### 5.3 S7 — Free / 14-day

**14-day:** do with S1/S2. Kill nothing.  
**Forever-free:** **S7-K1** light only after a real TTV exists **and** 14-day still yields 0 reviews. **S7-K2** if free produces install-and-uninstall churn we are not willing to eat (TSC MARKET_REPORT — gossip, but directionally the fear).  
**S7-K3:** review unlock / paid stars. Official policy. Instant strategy death.

---

## 6. Cross-option decision tree (founder, later)

```text
Is App Store the primary acquisition channel?
  NO  → Will we outbound to agencies / finance?
          NO  → S6. Accept silence. Kill criterion S6-K1 is a calendar.
          YES → Agencies? S3 (watch S3-K1, S3-K5).
                Finance overlay? S4 sentence + S4-K1.
  YES → May we OAuth spend-only (no pixel)?
          NO  → S6 or S3. Ease stays 1. Death D.
          YES → Must the loved number be net profit?
                  YES → Have a wedge vs Kleio $29 AND TrueProfit 899?
                          NO  → Kill S2-K1. Do not build.
                          YES → S2. Watch S2-K2..K5.
                  NO  → S1 Ring 1 (QL till, spend OAuth, paste-claim, Monday, 14-day).
                        Watch S1-K1..K6.
                        S5b logos. No S5.
                        S7 = 14-day now; forever-free only as fuse.
```

**Forbidden combinations**

- S1 + “we are not amending MASTER_PLAN.”  
- S2 + no wedge + $39.  
- S3 + App Store as only motion.  
- S5 + $250 + current religion.  
- S5b + event ingest.  
- Any option + listing LTV/Goals that are not shipped.  
- Any option + Fly production from this research branch.

---

## 7. Scoreboard after Wave E stress-test

| Option | Wave B | Wave E note | Still on menu? |
| --- | --- | --- | --- |
| S1 | 19 | **14–16** if paste-claim + Kleio priced in + Meta §10.d | **Yes**, Ring 1 only, App Store path |
| S1 + 14-day | 19 | Billing hygiene, not a new product | Yes, with S1 |
| S2 | 16 | **~15** vs Kleio $29; Feasibility still 2 | Yes **only** with wedge |
| S3 | 16 | Unchanged; isolation is the real feasibility | Yes **only** with outbound |
| S5 | 14 | Unchanged; should be dead | **No** |
| S5b | modifier | Unchanged | Yes as checkbox |
| S4 | 13 | Sentence, not company | Brochure |
| S6 | 9 | Current state | Default if founder refuses gates |
| S7 forever-free | fuse | Unchanged | After TTV only |

**There is no 19.** The 19 was Religion-flex 5 plus an Ease 4 that assumed frictionless OAuth and an API lie-card. Both assumptions failed contact with Kleio’s token docs and Meta’s mix rule.

---

## 8. What we still must not invent

- That we have 30 design partners, 5 agencies, or any install graph.
- Time-to-review as a number of days we “will” hit.
- Northbeam / Polar prices as gospel.
- That killing S1 this week is required because Kleio exists — Kleio **narrows** S1; it does not auto-kill it.
- Production scope from this file.

---

## 9. One paragraph

S1 remains the least-incoherent App Store path, but Wave B’s 19/25 does not survive Kleio’s $29 desk, Meta’s 60-day token, or the mix-data clause that sits on top of the claims card. Kill S1 if reviews refuse us or the wedge cannot ship legally; do not kill it because a P&L app exists. S2 is the review-max option and the clone-death option — kill it the moment the wedge sentence is weak. S3 is the religion-pure money option and the services-company option — kill it if five (or all) agencies won’t beat SyncWith or if nobody will sell. S5 is how a $250 founder builds Parkour badly; leave it dead; S5b is a logo row. The only dishonorable kill is refusing every gate and calling the resulting silence a strategy.
