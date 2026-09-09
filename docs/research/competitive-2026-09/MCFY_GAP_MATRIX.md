# Mcfly gap matrix

**Date:** 2026-09-09  
**How to read:** each row is a capability or market object. `Have` is live listing + live site + this repo (conflicts flagged). Scores are research judgment, not metrics. Tags: `CURRENT_RELIGION` / `RESEARCH_OPTION` / `GAP`.

---

## A. Capability gaps

| Capability | Mcfly have | Who has it (live) | Money | Love | Ease | Real | Tag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Period-matched sales ÷ spend | Yes (core) | Sheets DIY; Polar MER tile; some profit apps | M | M | M | H | CURRENT |
| Break-even from margin | Yes (typed %) | Calculators; profit apps do it via costs | M | M | H | H | CURRENT |
| Named offline / billboard / retainer | Yes (hero) | Rare as first-class | L | H* | H | M | CURRENT |
| Manual / CSV spend | Yes | Everyone as fallback | L | L | L | M | CURRENT |
| Auto ad-spend OAuth | **No** (site: “no OAuth”; MASTER_PLAN Phase 2 yes) | TrueProfit, Lifetimely, Metorik, TW, Polar | H | H | H | H | RESEARCH_OPTION |
| Platform-claim vs till gap | Site footer link; not proven in app | Suites; r/PPC sheets | H | H | M | H | GAP |
| Tax / VAT / sales definition toggle | Underspecified | TW failed this (1★); A2X exists for tax rules | M | H | M | H | GAP |
| Dual clock (delivery vs accrual) | No | Apex “accrual”; A2X payout dates | M | M | L | H | GAP |
| COGS / fees / shipping | No (typed margin) | TrueProfit, Lifetimely, BeProfit, Metorik, A2X | H | H | M | H | RESEARCH_OPTION |
| Cash CAC / LTV:CAC | **Listing claims**; repo inventory does not | Lifetimely, TrueProfit, Polar, TW | M | H | M | H | GAP / integrity |
| Goals / pacing board | Listing claims | TW, Polar, Lifetimely | M | M | H | M | ? verify |
| Allocation 7/14/28 | Yes (rules; sales∝spend if no contrib) | Suites via MTA/Moby; r/PPC pause tests | M | L–M | H | M | CURRENT (weak math) |
| Monday email / Slack / PDF | No | Better Reports, Metorik, Lifetimely Slack | M | H | H | M | RESEARCH_OPTION |
| Sheets companion | Scaffold in repo; not product | SyncWith $4.99, Better Reports | M | H | M | H | RESEARCH_OPTION |
| Multi-store / agency | No | Polar, Metorik, BeProfit Plus | H | H | L | H | RESEARCH_OPTION |
| Pixel / CAPI | Refuse | Parkour Free, WeTracked, Analyzify, Elevar, TW, Polar | H | H | H | disputed | CURRENT refuse |
| Passback / Apex / Sonar | Refuse | NB, TW, Polar | H | H | L | disputed | CURRENT refuse |
| MCP / ChatGPT | No | Polar, TrueProfit, Lifetimely, Margins | L | M | M | L | RESEARCH_OPTION |
| Heatmaps | No | Clarity 2125 | L | H | H | other | out |
| Custom report builder | No | Better Reports 1199 | M | H | M | H | out |
| GL / NetSuite / QB | No | A2X 359 | H | H | L | H | out (export only) |
| Creative analytics | No | TW Automate | M | M | L | M | out |
| AI agent OS | No | TW Moby; Polar agents | H | mixed | L | mixed | out |
| Free plan | No | TW, Lifetimely, Clarity, Parkour, Margins | M | H | H | n/a | RESEARCH_OPTION |
| 14-day trial | **7-day** | Profit cluster 14; A2X 30 | M | M | H | M | RESEARCH_OPTION |
| Works-with logos | **None** | Everyone serious | M | M | H | n/a | GAP |
| Reviews | **0** | 10–2125 | H | H | n/a | n/a | GAP |
| Magic summary | Impossible until 100 | Polar, A2X | M | H | n/a | n/a | GAP |
| BFS badge | No | unknown set | H | M | n/a | n/a | later |
| Languages | EN | Polar 3; Clarity 14 | L | M | M | M | later |

\*Love high only for the minority with offline spend.

---

## B. Religion inconsistencies inside Mcfly (fix in research, not by pretending)

| Topic | MASTER_PLAN / repo | Live listing / site | Implication |
| --- | --- | --- | --- |
| Price | Free DP → ~$79 | **$39** + 7-day; course $79 | Docs stale |
| Metric name | Cash MER | **Total ROAS** | Pick one in public |
| OAuth | Phase 2 planned | Product page **no ad OAuth** | Religion already flexible |
| LTV / Goals | Features doc: later / planned | Listing **claims now** | Integrity risk |
| Freemium | “Do not market forever free” | No free plan (aligned) | vs TSC review physics |
| MER formula | sales ÷ spend | same | Aligned |
| Pixels | Kill-on-contact | “No pixels” | Aligned |
| Allocation | mer-core ships | listing claims 7/14/28 | Aligned if UI exists |

---

## C. Four-score gap vs named rivals

| Rival | They beat Mcfly on | Mcfly can beat them on | If we do nothing |
| --- | --- | --- | --- |
| TrueProfit | reviews, autopilot spend, costs, MCP, 14-day | offline channels, flat fee, anti-claim copy | lose same-wallet buyers |
| Lifetimely | free tier, LTV, 535 reviews | simplicity, billboards | lose “source of truth” buyers |
| TW | distribution, pixel, daily OS | price, tax honesty, not being an OS | never in consideration |
| Polar | CS, warehouse, 4.9, MER as one tile | $39 vs $750, formula | ignored |
| Northbeam | court + Apex | $39 cash question | ignored |
| Parkour/Clarity | free, 191–2125 reviews, 2-min TTV | being a different job | App Store rail starves Mcfly |
| SyncWith | $4.99, already in Sheets | opinionated desk | they remain the DIY default |
| Better Reports | 1199 reviews, push reports | spend÷sales religion | they own “Admin but usable” |
| A2X | 359 reviews, bank truth | not a GL | finance never calls Mcfly |
| Sheets | $0, flexibility | less error, BE + allocation | default forever |
| Margins (Finaloop) | Free + profit-ROAS + banks | brand/religion | **watch** — if they execute, cash-ROAS becomes free |

---

## D. Problem-coverage score (from PROBLEM_BANK)

| Problem # | Mcfly coverage today | Gap type |
| --- | --- | --- |
| 1 Net profit | Thin (margin %) | Product |
| 2 Pixel/CAPI | Refuse | Strategic |
| 3 Spend next to sales | Core | Ease (manual) |
| 4 Platform ≠ till | Partial / marketing | Product |
| 5 Custom reports / Sheets | Weak | Product |
| 6 LTV/CAC | Claimed | Integrity / product |
| 7 Passback | Refuse | Strategic |
| 8 Heatmaps | None | Ignore |
| 9 GL recon | None | Export only |
| 10 Offline spend | Core wedge | Discovery |
| 11 Allocation | Heuristic | Honesty |
| 12 Multi-entity | None | Packaging |
| 13 Creative | None | Ignore |
| 14 AI OS | None | Optional thin |
| 15 Monday ritual | Positioning | Push artifact |

**Coverage count:** 2 cores (3, 10), 2 thin (1, 11), 1 claimed (6), rest empty or refused.

---

## E. What “maximum four scores” would close first

If the founder wants **money + love + ease + real problems** (religion flexible):

1. **Ease:** auto spend (A1) or 14-day + wizard — without this, reviews stay 0.  
2. **Real problem:** profit-lite (B1/B2) or claims-vs-cash (A2) — without this, TrueProfit wins the wallet.  
3. **Love:** Monday push + human onboarding + review modal after first computed period.  
4. **Money:** agency SKU + keep $39 flat; do not GMV-tax.

If the founder wants **religion purity**:

1. Accept App Store death spiral risk (0 reviews, pixel rail).  
2. Sell outbound to P3/P4.  
3. Still must fix listing integrity (LTV claim, mailto, paid-plan wording) and tax definition.

There is no path that maximizes all four scores **and** keeps paste-only + no costs + 7-day + 0-review. That combination scores **L/L/L/M**.

---

## Wave 2 gap addendum

| Capability | Mcfly have | Who has it (live 2026-09-09) | Tag |
| --- | --- | --- | --- |
| $29–$39 flat profit + ads + no MTA | No (ROAS only) | **Kleio 5.0/20** | GAP vs cousin |
| Human/scheduled report close | No | Report Pundit 2026; Better Reports 1199 | RESEARCH_OPTION |
| Refund vs exchange vs credit lines | No | Loop + Community 637409 | GAP |
| Shop-currency / Markets | No | Report Pundit Advanced; Polar | GAP |
| Subscription new vs returning numerator | No | TW/Polar/Recharge/Apex | RESEARCH_OPTION later |
| Legal Reviews API after first close | No | Official; Kleio founder replies | FIT_NOW |
| App Store Ads | No | Official first-price CPC | Wait |

Kleio is now the **primary gap** in the $29–$39 aisle. Polar remains a different buyer. See `DEEP_DIVE_FIVE_APPS.md`.
