# DEEP_DIVE — Who decides, who buys, who uses

**Date:** 2026-09-09  
**Wave:** deeper (extends `PERSONAS.md` + `ENTERPRISE_WORKFLOWS.md`; does not replace them)  
**Honesty:** No private org charts. Decision-rights are inferred from **public listings, reviews, vendor marketing, Community/Reddit, and 2026 practitioner writeups**. Inferred rows are tagged `INFERRED`. Vendor quotes are `MARKET_REPORT` / `VENDOR_CLAIM`.

Four scores: money · love · ease · real problem.

---

## 0. The uncomfortable split

`PERSONAS.md` already named P1–P6. This file answers a different question: **who has the badge to sign, who has the badge to veto, and whose Monday number actually moves spend.**

Public pattern (repeated, not a census):

| Role | Typical Monday number | Can they **buy**? | Can they **kill**? | Will they **review** on the App Store? |
| --- | --- | --- | --- | --- |
| Brand operator / media buyer | Ads Manager ROAS, TW Summary, creative | Often **recommends**; sometimes has card | Uninstalls what slows bidding | Sometimes, if TTV is daily |
| Founder-operator (sub-scale) | “Did we make money?” | **Yes** — they are the buyer | Yes | **Yes** — this is review velocity |
| Agency lead | Client blended / deck | Recommends; client pays | Switches clients to Sheets | Rare (client store owns the review) |
| Finance / controller / fractional CFO | Bank, payouts, VAT, contribution | Veto / second seat | **Yes** — VAT 1-star, “not books” | Rare (not in Admin all day) |
| CMO / VP Growth | Board MER + incrementality | Signs Polar/NB | Yes at renewal | Almost never |
| Procurement / Plus ops | SOC2, DPA, seats | Paperwork | Security veto | Never |

**`CURRENT_RELIGION`** packages Mcfly as if founder + finance share one brain.  
**`EVIDENCE`:** they do not. TW vs Polar 2026 writeups exist *because* the media buyer and the CFO want different objects.  
**`RISK`:** one listing cannot recruit all six. The App Store listing recruits **founder-operators**. Outbound recruits **finance / agency**.

---

## 1. Decision-rights map (public)

### 1.1 Brand-operator / in-house media buyer

**Job:** scale/kill in Ads Manager today.

**Where they talk:** r/PPC 1u81q7r, 1r2pvgy, 1pqv5kh; WeTracked 5★ “I stay in Ads Manager.”

**What they will approve:**
- Pixel / CAPI that makes Events Manager less wrong (Parkour, Elevar, WeTracked).
- A daily OS if the founder already pays (TW Free → Foundation).
- Anything that **writes back** (Apex / Sonar).

**What they will ignore:**
- A third desk they must paste into.
- A sermon that their ROAS is theater — unless the founder forces a governor.

**Buy path `INFERRED`:** Operator trials TW Free or a pixel in an afternoon. Card is founder’s. Operator becomes the **champion** if the tool changes bids.

**Mcfly today:** useless as their daily tool. Useful only if the **founder mandates** the cash number.

**`RESEARCH_OPTION`:** OAuth spend + claims-vs-cash so the operator can **see the lie next to the bid**, not in a weekly CSV. Evidence: TrueProfit “sync ad spends”; r/PPC already uses MER as reality check. Risk: still not Ads Manager.

### 1.2 Founder-operator (the App Store human)

**Job:** sleep. Pocket P&L.

**Where they talk:** Community 657805, 588628, r/shopify 1pzy8iv.

**Buy path (public, repeated):**
1. Spreadsheet week-lag.
2. Install a **profit** app ($25–$49).
3. Optionally keep a **free pixel**.
4. If they were sold TW early, they later call it overkill (588628, ~$15–20k/mo store).

**Decision rights:** they **are** CEO, CMO, and AP. One click. This is why TrueProfit has 899 reviews and Polar has 116.

**`EVIDENCE`:** review volume is a **buyer-identity** signal, not a quality-only signal.  
**`RESEARCH_OPTION`:** package for this human (profit-lite + total spend) if App Store is the channel.  
**`RISK`:** TP moat.

### 1.3 Agency

**Job:** one comparable scoreboard across clients; protect the retainer.

**Where they talk:** r/PPC 1qgb8mg; Polar “for agencies” site module (https://getklar.com/pricing also has an agencies block); SyncWith affiliate-sheet review; Polar unlimited users.

**Decision rights (public pattern, `INFERRED`):**
- Agency **recommends** the stack in the pitch / audit.
- **Brand pays** the SaaS (TW/Polar on the client’s GMV).
- Agency **refuses** tools that create a second argument with the client (“your pixel says 4.2, Shopify says 2.1”).
- Agency **owns** the Sheets pack when they do not want to defend a vendor.

**Who reviews?** The **client store**. Agency love does not print App Store stars unless the client writes.

**WTP:**
- Polar $750 Core is an **agency-unfriendly client-GMV tax** unless the retainer absorbs it.
- SyncWith $4.99 is the pipe they already understand.
- Klar site: “kickback and eCom strategy consulting for mutual clients” (`VENDOR_CLAIM` — https://getklar.com/pricing).

**Mcfly today:** paste-first is agency-native; **per-store $39 × N** is not a portfolio SKU; no white-label pack.

**`RESEARCH_OPTION`:** agency workspace (already C4 / S3). Evidence: Metorik multi-store from $75; Polar unlimited users; Report Pundit multi-store on Advanced $35.  
**`RISK`:** become SyncWith; support N tenants.

**Buy-sign reality:** the agency rarely “buys Mcfly.” They **put it on the client’s Monday slide**. Distribution is **sales**, not search.

### 1.4 Finance / controller / fractional CFO

**Job:** a number that survives the bank and the auditor.

**Where they talk:** Community 577364; TW VAT 1★; Eightx TW review “not your books”; A2X / Taxomate listings.

**Decision rights:**
- Often **cannot** install apps (no Admin habit).
- **Can** veto a dashboard that includes VAT in revenue or moves when re-pulled (180915).
- **Will** keep A2X/Taxomate/Finaloop regardless of what marketing buys.

**Eightx (MARKET_REPORT):** https://eightx.co/blog/compare/reviews/triple-whale-for-ecommerce-review — treat TW as decision-support; reconcile to books, do not reconcile books to TW.

**Buy path `INFERRED`:** finance does not browse “Visuals and reports.” They arrive via accountant peer, A2X rail, or a board-pack disaster.

**Mcfly today:** formula is clean, **definitions are not**. No payout recon. No VAT toggle.

**`RESEARCH_OPTION`:** finance-grade cash desk (A3) as an **overlay**, not a GL. Evidence: TW 1★ + Eightx. Risk: worse A2X.

**They will not review** unless they are also the founder.

### 1.5 CMO / VP Growth / “the pod”

**Job:** court of appeal + who may change spend.

**Where they are sold:** TW vs Polar vs NB pages; Talk Shop; Fairview; D2C Times 2026.

**Public quote (MARKET_REPORT, paraphrase):** Kelp / Teel on D2C Times — TW = media buyer home; Polar = CFO + CMO agree; some clients run **both**.  
**URL:** https://d2c-times.com/polar-analytics-vs-triplewhale-in-2026-which-dtc-intelligence-layer-wins/

Fairview 2026: TW for operator-accessible daily dashboard under ~$5M GMV; Polar for data-mature $5M+ with warehouse ownership.  
**URL:** https://getfairview.com/blog/polar-analytics-vs-triple-whale

Talk Shop: TW = act; Polar = own/customize.  
**URL:** https://www.letstalkshop.com/blog/triple-whale-vs-polar-analytics

**Decision rights `INFERRED`:**
- CMO signs Polar/NB **after a demo + CS**, not from the App Store card.
- Media lead can **block** a tool that removes their daily cockpit.
- Finance can **block** a tool that cannot explain tax.
- Renewal is the real buy (GMV slider / spend gate).

**Mcfly today:** below the seriousness line. $39 reads as toy. Pixel-refuse reads as disqualifier to the media lead and as a feature to finance.

**`RESEARCH_OPTION`:** S4 overlay — “the number finance signs after TW.” Evidence: r/PPC already uses MER as North Star beside a suite. Risk: Polar already lists MER as a tile.

### 1.6 Procurement / Plus / security (brief)

**Public signals:** Elevar / Polar / NB SOC2, GDPR host-in-EU (Klar listing: GDPR, EU host). Mcfly listing: West Jordan mailbox, English only, 0 reviews, customers+orders+device scopes.

**`INFERRED`:** Mcfly will lose Plus RFPs on process, not on formula. Do not pretend otherwise.

---

## 2. RACI for a typical mid-market DTC stack (composite, `INFERRED`)

Not a real company. Built from the public patterns above.

| Decision | Media buyer | Founder | Agency | Finance | CMO |
| --- | --- | --- | --- | --- | --- |
| Install free pixel | A/R | I | C | I | I |
| Pay TrueProfit $35–$100 | C | A/R | C | C | I |
| Pay TW Foundation $219+ | R | A | C | C (VAT) | A if pod |
| Pay Polar $750+ | C | A | C | C | A/R |
| Pay Northbeam ~$1.5k MARKET_REPORT | C | A | C | C | A/R |
| Keep Sheets MER | R | A | A/R | C | I |
| Sign A2X / Taxomate | I | A | I | A/R | I |
| Change Meta budget today | A/R | I | R (if retained) | I | I |
| Change monthly media mix | C | A | C | C | A/R |
| App Store review | R | A/R | — | — | — |

R = does the work · A = accountable / pays · C = consulted · I = informed.

**Read it twice:** Mcfly’s **user** (finance / founder) and Mcfly’s **reviewer** (founder / operator) are not always the same human as Mcfly’s **budget-mover** (media buyer). S1 (governor) is the only option that tries to sit on the **intersection**.

---

## 3. Who pays which wallet

| Wallet | Examples (live listings 2026-09-09) | Buyer |
| --- | --- | --- |
| Marketing / growth | TW, Polar, Elevar, Analyzify, Klar off-store | Operator / CMO |
| Ops / profit | TrueProfit, Lifetimely, BeProfit, Kleio, Metorik | Founder |
| Reports / admin | Better Reports, Report Pundit | Ops / finance-adjacent |
| Finance / GL | A2X, Taxomate | Bookkeeper / CFO |
| Subscriptions | Recharge $25–$499 + take-rate | Retention / CMO |
| Returns | Loop $155 / $340 | CX / ops |
| DIY | Sheets + SyncWith $4.99 | Agency / founder |

Mcfly $39 is priced in the **ops/profit wallet** and merchandised in the **marketing/pixel rail**. That is a **category error** (already in README). This file adds: it is also a **buyer-error**. The person who searches “ROAS” is not the person who pays for profit.

---

## 4. Agency vs brand vs CFO — three buying motions

### Motion A — Founder self-serve (App Store)

Search → card → trial → review.  
Winners: free pixels, $25–$49 profit, Report Pundit free≤1000 orders.  
Mcfly: 0 reviews + 7-day + paste = **structurally excluded**.

### Motion B — Agency-led recommendation

Audit → “you need a scoreboard” → Sheets **or** TW if retainer fat → agency does not write the review.  
Mcfly fits **if** PDF/Slack + multi-store. Does not fit if the agency’s product is TW resale.

### Motion C — Finance-led / board-led

Pain (VAT, recon, board pack) → accountant peer → A2X/Polar/NB demo → annual contract.  
Mcfly fits as **overlay** only after definitions exist. Will not start here at $39 with no SOC2 story.

---

## 5. Conflict table (who fights whom)

Sibling PR #5 started stakeholder conflicts. This wave adds **decision-rights** conflicts:

| Conflict | Public spark | Who wins | Mcfly stance |
| --- | --- | --- | --- |
| Operator ROAS vs founder cash | r/PPC 1u81q7r | Whoever owns the ad account | Governor card (`RESEARCH_OPTION`) |
| Agency Sheets vs brand TW | r/PPC 1qgb8mg | Agency if they own the deck | Agency SKU |
| Finance VAT vs suite “Sales” | TW 1★ + KB vs docs | Finance at close; suite daily | Definitions or lose EU |
| CMO Polar vs buyer TW | D2C Times both-stack | Often **both** (two wallets) | Do not try to replace either |
| Subscription LTV vs ad CAC | Recharge analytics vs TW | Split: retention owns LTV | Do not clone Recharge |
| Returns ops vs marketing ROAS | Community 199943 | Ops owns Loop; ads stay optimistic | Show refund lag |

---

## 6. Religion from this file

| ID | Topic | CURRENT | OPTION | EVIDENCE | RISK | Call |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | Primary buyer | Hybrid sermon | Pick App Store founder **or** outbound finance/agency | Review volumes vs Polar CS motion | Other persona starves | **Pick a motion** |
| B2 | Media buyer | Ignore / lecture | Governor they did not ask for but founder mandates | WeTracked 5★; r/PPC | Still a third desk | S1 |
| B3 | Agency | Per-store $39 | Portfolio + pack | Polar unlimited; Report Pundit multi-store | Support | S3 later |
| B4 | CFO | Formula only | Tax/refund/payout definitions | TW VAT; 577364 | A2X creep | Overlay, not GL |
| B5 | Dual-stack | “We replace TW” | Sit beside TW | D2C Times both; Eightx | Tiny ARPU | **S4 is real** |

---

## 7. Practical implication (research, not a ship order)

If four scores matter:

1. **App Store copy** must speak to the **founder-operator** (profit / total spend / bicycle), not to the CMO.  
2. **Product** must still be usable by the **media buyer** (auto spend, claims-vs-cash) or the founder cannot force it.  
3. **Outbound one-pager** must speak to **finance** (definitions).  
4. Do not spend App Store Ads against “attribution / pixel” keywords aimed at operators who want Parkour Free (see `DEEP_DIVE_DISTRIBUTION.md`).

---

*No invented interviews. Re-verify vendor quotes before using on mcflyads.com.*
