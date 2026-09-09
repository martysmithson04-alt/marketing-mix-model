# Master index — how to use this research system

**Output root:** `docs/research/competitive-2026-09/`  
**Branch this file lives on:** `research/competitive-2026-09-full`  
**Base:** `research/competitive-2026-09`  
**Rule:** do not wipe prior files. This index is the map. The DB is the system of record.

**Wake here first:** [`GROKBOT_CURSOR_HANDOFF.md`](./GROKBOT_CURSOR_HANDOFF.md) — complete Grok Bot → Cursor dump (mission locks, live product state 2026-09-09, PR bank #5–#16, conclusions, Mac steps, human gates, standing orders).  
**Repo-root pointer:** [`docs/CURSOR_STANDING_ORDERS.md`](../../CURSOR_STANDING_ORDERS.md)

This branch is the **merged research bank**. Unique artifacts from PRs #5–#6 and #8–#17 are on disk here (PR #7 portfolio excluded). Source PRs may still be OPEN on GitHub; do not wipe them.

---

## 0. If you have 15 minutes

| You want… | Open |
| --- | --- |
| **Everything Grok Bot learned (start here)** | [`GROKBOT_CURSOR_HANDOFF.md`](./GROKBOT_CURSOR_HANDOFF.md) |
| The whole niche as maps/tables | [`ENTERPRISE_LANDSCAPE.md`](./ENTERPRISE_LANDSCAPE.md) |
| What to do next week / quarter / kill | [`DECISION_BRIEF.md`](./DECISION_BRIEF.md) |
| JTBD for operator / agency / CFO | [`NICHE_CANVAS.md`](./NICHE_CANVAS.md) |
| Every URL we actually fetched | [`SOURCE_BIBLIOGRAPHY.md`](./SOURCE_BIBLIOGRAPHY.md) |
| Queryable facts | [`db/SCHEMA.md`](./db/SCHEMA.md) → `db/competitive.sqlite` |

Religion tags (`CURRENT_RELIGION` / `RESEARCH_OPTION` / `EVIDENCE` / `RISK`) are defined in [`README.md`](./README.md) and restated in the handoff.

---

## 1. Pull requests this corpus synthesizes

These PRs are included on `research/competitive-2026-09-full` (content merge / import). Source PRs may still be OPEN. **Append, do not wipe.**

| PR | Title | Branch | What it added (use these files) |
| --- | --- | --- | --- |
| [#5](https://github.com/martysmithson04-alt/marketing-mix-model/pull/5) | Review mining — real people problems | `cursor/review-mining-6cd7` | [`REVIEW_MINING.md`](./REVIEW_MINING.md) · [`PROBLEM_BANK_FROM_REVIEWS.md`](./PROBLEM_BANK_FROM_REVIEWS.md) · [`SOURCES.md`](./SOURCES.md) · `db/reviews.csv` `problems.csv` `themes.csv` `stakeholder_conflicts.csv` |
| [#6](https://github.com/martysmithson04-alt/marketing-mix-model/pull/6) | Shopify App Store + monetization | `cursor/shopify-app-store-research-2b7a` | [`MARKET_STRUCTURE.md`](./MARKET_STRUCTURE.md) · [`MONETIZATION_PATTERNS.md`](./MONETIZATION_PATTERNS.md) · [`WHITE_SPACE.md`](./WHITE_SPACE.md) |
| [#8](https://github.com/martysmithson04-alt/marketing-mix-model/pull/8) | 2026-09 competitive deep-dive vs live listing | `research/competitive-2026-09` | Wave A core: README, SYNTHESIS, PERSONAS, PROBLEM_BANK, REVIEW_THEMES, COMPETITOR_CARDS, listing teardowns, `db/*.jsonl` |
| [#9](https://github.com/martysmithson04-alt/marketing-mix-model/pull/9) | Deeper wave — forums, buyers, five apps, VAT/returns, distribution | `cursor/deeper-wave-research-740f` | [`DEEP_DIVE_FORUMS.md`](./DEEP_DIVE_FORUMS.md) · [`DEEP_DIVE_BUYERS.md`](./DEEP_DIVE_BUYERS.md) · [`DEEP_DIVE_FIVE_APPS.md`](./DEEP_DIVE_FIVE_APPS.md) · [`DEEP_DIVE_INTERNATIONAL.md`](./DEEP_DIVE_INTERNATIONAL.md) · [`DEEP_DIVE_RETURNS_LTV_SUBS.md`](./DEEP_DIVE_RETURNS_LTV_SUBS.md) · [`DEEP_DIVE_DISTRIBUTION.md`](./DEEP_DIVE_DISTRIBUTION.md) |
| [#10](https://github.com/martysmithson04-alt/marketing-mix-model/pull/10) | Wave B — money + love product thesis | `cursor/deeper-wave-b-0ae0` | [`MONEY_MODEL.md`](./MONEY_MODEL.md) · [`LOVE_LOOPS.md`](./LOVE_LOOPS.md) · [`ONBOARDING_BATTLE.md`](./ONBOARDING_BATTLE.md) · [`ANTI_PATTERNS.md`](./ANTI_PATTERNS.md) · [`VNEXT_OPTION_SCORECARD.md`](./VNEXT_OPTION_SCORECARD.md) |
| [#11](https://github.com/martysmithson04-alt/marketing-mix-model/pull/11) | Wave E — S1 vs Kleio, pipes, policy | `cursor/wave-e-architecture-22c8` | [`KLEIO_GAP_ANALYSIS.md`](./KLEIO_GAP_ANALYSIS.md) · [`S1_PRD_LITE.md`](./S1_PRD_LITE.md) · [`INTEGRATION_MAP.md`](./INTEGRATION_MAP.md) · [`COMPLIANCE_LANDMINES.md`](./COMPLIANCE_LANDMINES.md) · [`STRATEGY_KILL_CRITERIA.md`](./STRATEGY_KILL_CRITERIA.md) |
| [#12](https://github.com/martysmithson04-alt/marketing-mix-model/pull/12) | Wave C — 65-app matrix, pricing, topology, policy, autopsies | `cursor/wave-c-competitive-matrix-e09e` | [`WAVE_C.md`](./WAVE_C.md) · [`COMPETITIVE_MATRIX.md`](./COMPETITIVE_MATRIX.md) · [`PRICING_LADDERS.md`](./PRICING_LADDERS.md) · [`CATEGORY_TOPOLOGY.md`](./CATEGORY_TOPOLOGY.md) · [`PARTNER_POLICY.md`](./PARTNER_POLICY.md) · [`FAILURE_AUTOPSIES.md`](./FAILURE_AUTOPSIES.md) |
| [#13](https://github.com/martysmithson04-alt/marketing-mix-model/pull/13) | Wave D — merchant psychology + sales | `cursor/wave-d-merchant-psych-7e69` | [`POSITIONING_WARS.md`](./POSITIONING_WARS.md) · [`OBJECTIONS.md`](./OBJECTIONS.md) · [`CONTENT_GEO.md`](./CONTENT_GEO.md) · [`INTERVIEW_SCRIPTS.md`](./INTERVIEW_SCRIPTS.md) · [`FIRST_CUSTOMERS_PLAYBOOK.md`](./FIRST_CUSTOMERS_PLAYBOOK.md) · `db/objections.jsonl` `positioning.jsonl` `content_topics.jsonl` `interviews.jsonl` `first_customer_plays.jsonl` |
| [#14](https://github.com/martysmithson04-alt/marketing-mix-model/pull/14) | PRIMARY_SOURCE_HARVEST — 214 App Store cards | `cursor/primary-source-harvest-0171` | [`PRIMARY_SOURCE_HARVEST.md`](./PRIMARY_SOURCE_HARVEST.md) · `db/harvest_listings.jsonl` `harvest_threads.jsonl` `harvest_docs.jsonl` `harvest_sources.jsonl` `harvest_primary.py` `render_harvest.py` |
| [#15](https://github.com/martysmithson04-alt/marketing-mix-model/pull/15) | Decision systems — war room, threats, unit econ | `cursor/decision-systems-463a` | [`WAR_ROOM.md`](./WAR_ROOM.md) · [`COMPETITIVE_THREAT_BOARD.md`](./COMPETITIVE_THREAT_BOARD.md) · [`UNIT_ECONOMICS_SCENARIOS.md`](./UNIT_ECONOMICS_SCENARIOS.md) · [`UNANSWERED_QUESTIONS.md`](./UNANSWERED_QUESTIONS.md) |
| [#16](https://github.com/martysmithson04-alt/marketing-mix-model/pull/16) | Enterprise landscape — whole niche (+12k) | `cursor/enterprise-landscape-0791` | [`ENTERPRISE_LANDSCAPE.md`](./ENTERPRISE_LANDSCAPE.md) · [`DECISION_BRIEF.md`](./DECISION_BRIEF.md) · [`NICHE_CANVAS.md`](./NICHE_CANVAS.md) · [`SOURCE_BIBLIOGRAPHY.md`](./SOURCE_BIBLIOGRAPHY.md) · `db/assemble_enterprise.py` |
| [#17](https://github.com/martysmithson04-alt/marketing-mix-model/pull/17) | GrokBot full learning handoff into Cursor | `cursor/grokbot-cursor-handoff-4f0f` | [`GROKBOT_CURSOR_HANDOFF.md`](./GROKBOT_CURSOR_HANDOFF.md) · [`docs/CURSOR_STANDING_ORDERS.md`](../../CURSOR_STANDING_ORDERS.md) · this index (handoff first) |

PR [#7](https://github.com/martysmithson04-alt/marketing-mix-model/pull/7) is a personal portfolio — **not** part of this corpus.

---

## 2. Every research file (this folder)

### Handoff + standing orders (read first)

| File | What it is for |
| --- | --- |
| [`GROKBOT_CURSOR_HANDOFF.md`](./GROKBOT_CURSOR_HANDOFF.md) | **Start here.** Full Grok Bot → Cursor learning dump |
| [`docs/CURSOR_STANDING_ORDERS.md`](../../CURSOR_STANDING_ORDERS.md) | Short standing orders; points at the handoff |

### Enterprise layer (PR #16)

| File | What it is for |
| --- | --- |
| [`ENTERPRISE_LANDSCAPE.md`](./ENTERPRISE_LANDSCAPE.md) | Whole-market maps: segments, buyers, money flows, incumbents, white space, Mcfly, ranked opportunities |
| [`MASTER_INDEX.md`](./MASTER_INDEX.md) | This file |
| [`SOURCE_BIBLIOGRAPHY.md`](./SOURCE_BIBLIOGRAPHY.md) | 100+ primary URLs actually fetched + one-line proof |
| [`DECISION_BRIEF.md`](./DECISION_BRIEF.md) | Next week / quarter / religion flex / kill criteria |
| [`NICHE_CANVAS.md`](./NICHE_CANVAS.md) | JTBD canvases with evidence IDs |

### Wave A — core (PR #8)

| File | What it is for |
| --- | --- |
| [`README.md`](./README.md) | Method, live Mcfly snapshot, four-score, non-goals |
| [`RESEARCH_LOG.md`](./RESEARCH_LOG.md) | Dated fetches, contradictions, open questions (append-only) |
| [`SYNTHESIS.md`](./SYNTHESIS.md) | S1–S7 strategic menu (pre-Kleio scoring — read Wave E after) |
| [`RELIGION_FLEX.md`](./RELIGION_FLEX.md) | CURRENT vs OPTION for R1–R12 |
| [`APP_STORE_MARKET.md`](./APP_STORE_MARKET.md) | Discovery, reviews, trials, pricing psychology |
| [`PERSONAS.md`](./PERSONAS.md) | P1–P6 |
| [`PROBLEM_BANK.md`](./PROBLEM_BANK.md) | 15 problems ranked by public WTP |
| [`MERCHANT_PROBLEMS.md`](./MERCHANT_PROBLEMS.md) | Voice index — their sentences + URLs |
| [`NICHE_MER.md`](./NICHE_MER.md) | MER / blended ROAS / till vs Ads Manager |
| [`REVIEW_THEMES.md`](./REVIEW_THEMES.md) | Visible review sample + star histograms |
| [`ENTERPRISE_WORKFLOWS.md`](./ENTERPRISE_WORKFLOWS.md) | Sheets / TW / Polar / NB / Elevar / A2X / Admin |
| [`OPPORTUNITY_MAP.md`](./OPPORTUNITY_MAP.md) | A–F opportunities scored |
| [`COMPETITOR_CARDS.md`](./COMPETITOR_CARDS.md) | Long cards for the original 21 |
| [`LISTING_PATTERN_BANK.md`](./LISTING_PATTERN_BANK.md) | 25 listing patterns |
| [`LISTING_TEARDOWNS.md`](./LISTING_TEARDOWNS.md) | vs live Mcfly listing |
| [`MCFY_GAP_MATRIX.md`](./MCFY_GAP_MATRIX.md) | Capability × four scores |

### Parallel / later waves (PRs #5–#6, #9–#15)

| File | Wave | What it is for |
| --- | --- | --- |
| [`REVIEW_MINING.md`](./REVIEW_MINING.md) | #5 | Method for review → problem IDs |
| [`PROBLEM_BANK_FROM_REVIEWS.md`](./PROBLEM_BANK_FROM_REVIEWS.md) | #5 | P-001… problems from reviews |
| [`SOURCES.md`](./SOURCES.md) | #5 | Early source list (superseded by bibliography) |
| [`MARKET_STRUCTURE.md`](./MARKET_STRUCTURE.md) | #6 | What the App Store is; two economies |
| [`MONETIZATION_PATTERNS.md`](./MONETIZATION_PATTERNS.md) | #6 | Pricing patterns |
| [`WHITE_SPACE.md`](./WHITE_SPACE.md) | #6 | Crowded vs underserved jobs |
| [`DEEP_DIVE_FORUMS.md`](./DEEP_DIVE_FORUMS.md) | #9 | Community + Reddit close reads |
| [`DEEP_DIVE_BUYERS.md`](./DEEP_DIVE_BUYERS.md) | #9 | Who signs / vetoes / reviews |
| [`DEEP_DIVE_FIVE_APPS.md`](./DEEP_DIVE_FIVE_APPS.md) | #9 | Five-app teardowns |
| [`DEEP_DIVE_INTERNATIONAL.md`](./DEEP_DIVE_INTERNATIONAL.md) | #9 | VAT / EU / multi-currency |
| [`DEEP_DIVE_RETURNS_LTV_SUBS.md`](./DEEP_DIVE_RETURNS_LTV_SUBS.md) | #9 | Returns, LTV, subs |
| [`DEEP_DIVE_DISTRIBUTION.md`](./DEEP_DIVE_DISTRIBUTION.md) | #9 | How apps actually get found |
| [`MONEY_MODEL.md`](./MONEY_MODEL.md) | #10 | Take-rate math + ARPU *shapes* (no Mcfly MRR) |
| [`LOVE_LOOPS.md`](./LOVE_LOOPS.md) | #10 | What makes a merchant reopen / review |
| [`ONBOARDING_BATTLE.md`](./ONBOARDING_BATTLE.md) | #10 | Minute-10 TTV vs 7-day CSV |
| [`ANTI_PATTERNS.md`](./ANTI_PATTERNS.md) | #10 | AP1–AP11 (attributed-only spend, meters, …) |
| [`VNEXT_OPTION_SCORECARD.md`](./VNEXT_OPTION_SCORECARD.md) | #10 | S1=19 etc. **then read Wave E** |
| [`WAVE_C.md`](./WAVE_C.md) | #12 | Wave C one-screen |
| [`COMPETITIVE_MATRIX.md`](./COMPETITIVE_MATRIX.md) | #12 | 65-app matrix |
| [`PRICING_LADDERS.md`](./PRICING_LADDERS.md) | #12 | Public menus as tables |
| [`CATEGORY_TOPOLOGY.md`](./CATEGORY_TOPOLOGY.md) | #12 | Analytics aisle vs Marketing navbar |
| [`PARTNER_POLICY.md`](./PARTNER_POLICY.md) | #12 | BFS, reviews, revenue share |
| [`FAILURE_AUTOPSIES.md`](./FAILURE_AUTOPSIES.md) | #12 | Stocky / Metrilo / Glew / BeProfit / clones |
| [`KLEIO_GAP_ANALYSIS.md`](./KLEIO_GAP_ANALYSIS.md) | #11 | **Read before choosing S1** |
| [`S1_PRD_LITE.md`](./S1_PRD_LITE.md) | #11 | S1 specified hard enough to kill; score → 14–16 |
| [`INTEGRATION_MAP.md`](./INTEGRATION_MAP.md) | #11 | ShopifyQL / spend APIs / claim card |
| [`COMPLIANCE_LANDMINES.md`](./COMPLIANCE_LANDMINES.md) | #11 | Meta §10.d, App Review, listing honesty |
| [`STRATEGY_KILL_CRITERIA.md`](./STRATEGY_KILL_CRITERIA.md) | #11 | Observable kills for S1–S5 |
| [`POSITIONING_WARS.md`](./POSITIONING_WARS.md) | #13 | Nouns the aisle is fighting over |
| [`OBJECTIONS.md`](./OBJECTIONS.md) | #13 | Sales objections + evidence |
| [`CONTENT_GEO.md`](./CONTENT_GEO.md) | #13 | Where merchants already read |
| [`INTERVIEW_SCRIPTS.md`](./INTERVIEW_SCRIPTS.md) | #13 | What to ask DPs (do this week) |
| [`FIRST_CUSTOMERS_PLAYBOOK.md`](./FIRST_CUSTOMERS_PLAYBOOK.md) | #13 | Outbound / first-store motion (research) |
| [`PRIMARY_SOURCE_HARVEST.md`](./PRIMARY_SOURCE_HARVEST.md) | #14 | 214 live listing cards + threads + docs |
| [`WAR_ROOM.md`](./WAR_ROOM.md) | #15 | Weekly cadence if fighting for money + love |
| [`COMPETITIVE_THREAT_BOARD.md`](./COMPETITIVE_THREAT_BOARD.md) | #15 | 30/90/365 kill paths |
| [`UNIT_ECONOMICS_SCENARIOS.md`](./UNIT_ECONOMICS_SCENARIOS.md) | #15 | Scenario tables only. Labeled assumptions |
| [`UNANSWERED_QUESTIONS.md`](./UNANSWERED_QUESTIONS.md) | #15 | 20 strategy-changing unknowns |

---

## 3. Database

| Path | What |
| --- | --- |
| [`db/SCHEMA.md`](./db/SCHEMA.md) | Field dictionary + counts |
| [`db/build_db.py`](./db/build_db.py) | Rebuilds `competitive.sqlite` from JSONL |
| [`db/fetch_live.py`](./db/fetch_live.py) | Live URL fetcher (PR #16) |
| [`db/assemble_enterprise.py`](./db/assemble_enterprise.py) | Merges waves + live fetch into JSONL (PR #16) |
| [`db/harvest_primary.py`](./db/harvest_primary.py) | Primary harvest fetcher (PR #14) |
| [`db/render_harvest.py`](./db/render_harvest.py) | Renders harvest markdown (PR #14) |
| `db/*.jsonl` | System of record (competitors, problems, quotes, sources, harvest, …) |
| `db/*.csv` | PR #5 review-mining tables (kept; also folded into JSONL on #16) |
| `db/fetch_raw.jsonl` | Raw fetch log (status, excerpt, extracted fields) |

Rebuild (already done on this branch; re-run only if JSONL changes):

```bash
cd docs/research/competitive-2026-09/db
python3 assemble_enterprise.py   # refresh JSONL from waves + fetch
python3 build_db.py              # rebuild sqlite
```

---

## 4. Repo docs this research must **not** silently overwrite

| File | Role |
| --- | --- |
| [`docs/MASTER_PLAN.md`](../../MASTER_PLAN.md) | Locked religion for *shipping* |
| [`docs/COMPETITORS.md`](../../COMPETITORS.md) | Older competitor memo (2026-07; stale vs live listing) |
| [`docs/APP_STORE_LISTING.md`](../../APP_STORE_LISTING.md) | Listing draft (stale vs live $39 / Total ROAS) |
| [`docs/AGENTS.md`](../../AGENTS.md) | Agent directives |

Live listing + live site win when they conflict. Founder amends MASTER_PLAN; agents do not.

---

## 5. Recommended read paths

**Newly woken Cursor / Cloud Agent:** [`GROKBOT_CURSOR_HANDOFF.md`](./GROKBOT_CURSOR_HANDOFF.md) then standing orders.  
**Founder, decide this week:** Landscape §0 + Decision brief §0–§2 + Kleio gap §0–§1.  
**Founder, Path A:** S1 PRD-lite + Integration map + Compliance landmines + Kill criteria.  
**Founder, Path B:** Problem bank + Kleio gap rows 8–9 + Anti-patterns AP1/AP4 + TrueProfit/Lifetimely cards.  
**Founder, Path C:** Deep dive buyers + First customers playbook + Objections + Money model Shape 1.  
**Listing copy:** Listing teardowns + Pattern bank + Category topology.  
**Analyst / later agent:** SCHEMA + sqlite + bibliography. Do not re-invent reviews.

---

## 6. What is still empty on purpose

- Mcfly Partner Dashboard views/installs/churn — **not in git**
- First-party interview transcripts — scripts exist; rows are placeholders until you run them
- Northbeam / Hyros / Wicked official price cards — **no listing**; do not invent
- Any TAM, “X% of merchants,” or Mcfly MRR
- Admin smoke Result — **blank**; do not invent
- App Store reviews — **0**; do not invent
