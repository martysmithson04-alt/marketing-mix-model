# Unanswered questions that would change strategy

**Date:** 2026-09-09  
**Mode:** RESEARCH ONLY. A question earns a row only if **an answer would change** outreach, listing, pricing, religion, or the S1–S7 menu (`SYNTHESIS.md`). Trivia stays out.

**How to learn (only these verbs):**

| Verb | Means | Do not |
| --- | --- | --- |
| **Interview** | Named conversation with a merchant, buyer, agency, bookkeeper, or installer | Invent a persona quote |
| **Scrape** | Re-fetch a public URL, Partner Dashboard export, changelog, or listing | Invent review counts |
| **Experiment** | Change one live object (listing copy, trial length, onboarding, ask) and read a cell | Run three listing theologies at once |

Religion is flexible. If an answer kills a CURRENT_RELIGION row, that is a feature of this file.

Canonical leftovers from `RESEARCH_LOG.md` are included. New Kleio/Margn/take-rate gaps from session 6 are included.

---

## Scoreboard

| ID | Question | If answered this way… | …strategy changes to | Learn by | Time-to-learn |
| --- | --- | --- | --- | --- | --- |
| Q1 | What are Mcfly listing views / installs / trials / paid / uninstalls? | Views=0 vs views>0 installs=0 vs TTV fail | War-room tree (`WAR_ROOM.md` §6): outbound vs listing vs product | **Scrape** Partner Dashboard | 30 min |
| Q2 | Will a real merchant complete a computed week on paste-only? | No ×3 named humans | C5 OAuth or S3/S4 outbound; S6 dead | **Interview** + **Experiment** sit-with-them | 14 days |
| Q3 | Does the live app ship LTV + Goals as the listing claims? | No | Integrity rewrite **this week** or ship the feature; trust risk | **Scrape** the running app / `APP_FEATURES.md` vs listing | 1 hour |
| Q4 | Is the job they want net profit or sales÷spend? | “Net profit” ×3 | S2/C6 in play; R12 flips | **Interview** P1/P4 | 5 convos |
| Q5 | Will they pay $39 vs Kleio $29 / TP $35 / Sheet $0–$5? | No at $39 | Price experiment (Table H) or walk away from App Store | **Interview** + **Experiment** (do **not** A/B price on listing blindly) | 5 convos |
| Q6 | Can we OAuth spend-only inside founder calendar? | App Review > runway | Stay paste + outbound; do not promise auto-sync on listing | **Experiment** (dev store) + Shopify/Meta review docs | weeks |
| Q7 | Exact Built for Shopify numeric gates? | Far above current N | Stop talking BFS; prep checklist only | **Scrape** https://shopify.dev/docs/apps/launch/built-for-shopify + Partner UI | 1 hour |
| Q8 | Is 2.9% already on payouts? Reduced-share registered? | Not registered / unexpected fees | Fix Partner settings before any paid conversion | **Scrape** Partner payouts + https://shopify.dev/docs/apps/launch/distribution/revenue-share | 30 min |
| Q9 | Kleio 364 stores — true? | Yes vs marketing | Treat Kleio as the default noun now, not a 20-review toy | **Scrape** (weak) + **Interview** Kleio users from public reviews | days |
| Q10 | Will Margn get the first reviews in the 0-review profit cohort? | Yes | Leave cohort this month or abandon profit aisle | **Scrape** https://apps.shopify.com/margn-1 weekly | Monday ritual |
| Q11 | Does Shopify plan to ingest Meta/Google spend? | Yes / rumored | S4 overlay or exit; air supply gone | **Scrape** changelog + Community 134251 | weekly |
| Q12 | Who is the design-partner human (Juan/Bryce/Nora equivalent)? | No one named | Love path is closed; stop comparing to TP CS | **Interview** (founder names them) | today |
| Q13 | Is App Store the primary channel? | No | S3/S4 week; listing = brochure | **Interview** founder (decision, not research) | 15 min |
| Q14 | Polar $400 vs $750 vs ~$720? | Materially lower | Do not use $750 as gospel on site | **Scrape** Polar listing + vs page same day | 20 min |
| Q15 | SyncWith $4.99 Shopify vs $25–$150 Workspace? | Workspace is the real agency price | S3 kill criterion changes | **Scrape** Workspace Marketplace + **Interview** P3 | 1 day |
| Q16 | TW MER inverted in-product? | No | Delete that attack line | **Scrape** TW app/docs or **Interview** a TW user | 1 session |
| Q17 | VAT / sales definition: what will we default? | Unspecified | Copy TW 1-star landmine | **Interview** P4 + **Experiment** toggle | 2 weeks |
| Q18 | Course $79: any buyers? Billing path? | 0 sales / Stripe vs Shopify | Kill course-as-strategy | **Scrape** Stripe/Shopify + site analytics | 30 min |
| Q19 | Allocation without channel sales: will buyers accept sales∝spend? | No | R8: refuse to advise or require channel sales | **Interview** P2 + **Experiment** warning copy | 5 convos |
| Q20 | Partner pixel (Parkour/Elevar) — will they list “works with”? | Yes / no | S5b listing vs isolation | **Interview** partner + **Experiment** Works-with | 2 weeks |

---

## Q1 — Partner Dashboard funnel (binds every other question)

| | |
| --- | --- |
| **Unknown** | Listing views, install count, trial starts, paid conversions, uninstalls, charges. **Not in this repo.** |
| **Why it changes strategy** | `WAR_ROOM.md` §6 is a tree. Views=0 ⇒ stop blaming product. Views>0 + 0 installs ⇒ listing. Installs + no spend ⇒ TTV. Everything else is decoration until these cells exist. |
| **Current evidence** | Live listing 0 reviews, launched 2026-09-07 — https://apps.shopify.com/mcfly-analytics-public. Age ≠ views. |
| **How to learn** | **Scrape:** Partner Dashboard → App → Metrics / Billing. Write the five numbers into the week scoreboard (private if needed). |
| **Do not** | Infer views from GitHub traffic or mcflyads.com analytics. Those are not the listing. |
| **Kill / flip** | If 30 days of views>0 and 0 paid **and** 0 computed weeks → S6 kill (`SYNTHESIS.md`). |

---

## Q2 — Paste-only TTV (binds C5 vs S3)

| | |
| --- | --- |
| **Unknown** | Will a non-founder merchant export Meta/Google/TikTok (and type a billboard) inside 7 days? |
| **Why it changes strategy** | If no: 7-day trial is a churn machine (`APP_STORE_MARKET.md` §7); OAuth (R3) or outbound-only. If yes: C5 can wait; C1/C3 first. |
| **Current evidence** | Live site: real store starts blank until spend — https://mcflyads.com/product. Loved peers sync spend (TP, Kleio, Margn Pro). Community 134251: people already hate connector cost, not paste as a product. |
| **How to learn** | **Experiment:** sit-with-them on first CSV (Kleio-shaped labor). **Interview:** ask “show me last Monday’s Sheet.” If they cannot produce a CSV in the call, paste-only is dead. |
| **Sample size** | 3 named stores, not 1 friend. |
| **Kill / flip** | 3/3 fail to compute a week → C2 (14-day) is necessary but not sufficient; C5 becomes the product bet. |

---

## Q3 — Listing vs shipped LTV / Goals (integrity)

| | |
| --- | --- |
| **Unknown** | Live listing bullets and plan card claim LTV / Cash CAC / Goals board. Repo `APP_FEATURES.md` / MASTER_PLAN still treat LTV as later. |
| **Why it changes strategy** | False claims are App Store requirement risk (pricing/features must be accurate) and 1-star fuel. Either the listing is lying or the docs are stale. |
| **Current evidence** | https://apps.shopify.com/mcfly-analytics-public — “Paid plan adds LTV… and Goals”; plan card “Customer LTV and Goals board.” |
| **How to learn** | **Scrape:** install on a dev store; click every claimed surface. Diff against repo. |
| **Kill / flip** | If not shipped → B2/C0 **this week** (`WAR_ROOM.md`). Do not add more claims. |

---

## Q4 — Job-to-be-done: profit vs MER

| | |
| --- | --- |
| **Unknown** | For the humans Mcfly can actually reach, is the Monday question “sales÷spend vs BE” or “did I make cash after COGS/fees/shipping/ads”? |
| **Why it changes strategy** | Public WTP is **profit** (`PROBLEM_BANK.md` #1; TP 900; Kleio 20). If *our* buyers say MER, S1 is enough. If they say profit, R12/S2. |
| **Current evidence** | Forums: Community 657805, r/shopify 1pzy8iv. Not a substitute for *our* five conversations. |
| **How to learn** | **Interview:** listen for the noun. If they say “TrueProfit / Kleio / Sheet P&L,” they want profit. If they say “Meta doesn’t match Shopify,” they want Q4’s cousin (claims-vs-cash) — still not typed margin %. |
| **Kill / flip** | 3× “I need net profit” → C6 enters the war-room bet list. 3× “I already have TP” → overlay or walk. |

---

## Q5 — Willingness to pay $39 in *this* competitive set

| | |
| --- | --- |
| **Unknown** | Will they pay $39 when Kleio is $29 + reviewed, TP is $35 + autopilot, Margn Growth is $39 + costs, SyncWith is $4.99, Admin is $0? |
| **Why it changes strategy** | Unit-econ Table K: Mcfly keeps more per seat than Kleio **if** it gets the seat. Price is not the hole unless interviews say it is. If they will pay $39 for a *thinner* job, we were wrong about ease. |
| **Current evidence** | No Mcfly paid cohort. Category paid entries sit $25–$49 (`APP_STORE_MARKET.md` §6). |
| **How to learn** | **Interview:** “What do you pay now?” then “Would you pay $39 for paste-only?” Honest no is data. **Experiment:** do **not** yo-yo the public list price weekly (trust + billing). Test **value** (C1/C3) before $29. |
| **Kill / flip** | 5× “I’d use Kleio” → stop pretending uniqueness; pick a wedge or S3. 5× “$39 is fine if it fills itself” → C5, not a price cut. |

---

## Q6 — OAuth spend-only feasibility (calendar, not theology)

| | |
| --- | --- |
| **Unknown** | Wall-clock for Meta/Google/TikTok spend-read App Review + token ops, given ~$250 and one founder. |
| **Why it changes strategy** | R3 is the highest four-score bend (`RELIGION_FLEX.md`). If it cannot land inside the next review-quarter, S1 is a slogan. Then S3/S4/S6 only. |
| **Current evidence** | MASTER_PLAN Phase 2 already planned OAuth; live product page forbids it. TP/Kleio/Margn Pro list spend sync as shipped. |
| **How to learn** | **Experiment:** scope the smallest Meta spend-read on a dev store. **Scrape:** current Shopify/Meta app-review queues (public docs only — do not invent SLAs). |
| **Kill / flip** | If review calendar exceeds “still 0 reviews and no outbound” → outbound is the company. |

---

## Q7 — Built for Shopify gates

| | |
| --- | --- |
| **Unknown** | Numeric install / review / rating thresholds. Official page: usefulness criteria include mins, **numbers unpublished**. |
| **Why it changes strategy** | Repo `APP_STORE_LISTING.md` “~50 paid + 5 reviews” is a **founder heuristic**. Chasing BFS too early wastes the only review-application attempts (fail 3× ⇒ 3-month suspend). |
| **Current evidence** | https://shopify.dev/docs/apps/launch/built-for-shopify |
| **How to learn** | **Scrape:** official page + Partner BFS checklist UI. **Interview:** other app founders (public podcasts/TSC) as `MARKET_REPORT` only. |
| **Kill / flip** | If gates are clearly above 0-review reality → BFS is a **checklist**, not a Q4 2026 goal. |

---

## Q8 — Actual Shopify take on Mcfly payouts

| | |
| --- | --- |
| **Unknown** | Is the Partner account registered ($19)? Does the payout CSV show **2.9%** now and **0%** share? Any extra regional fee? |
| **Why it changes strategy** | Tables B–G assume T7/T8/T16. If share is still 20%, or 2.9% is applied twice, contribution math in G4 flips. |
| **Current evidence** | Official page only — https://shopify.dev/docs/apps/launch/distribution/revenue-share. No Mcfly payout in repo. |
| **How to learn** | **Scrape:** Partner → Settings (registration) → Payouts CSV. Compare one test charge. |
| **Kill / flip** | Unregistered → register before first paid. Unexpected 20% → use old `APP_STORE_MARKET.md` §10 until fixed. |

---

## Q9 — Kleio scale (364 stores)

| | |
| --- | --- |
| **Unknown** | getkleio.com claims **364 stores / 47.4M+ orders / 1 in 3 Plus**. Listing shows **20** reviews. |
| **Why it changes strategy** | If ~364 is true, Kleio is already a small incumbent (review:store ~5%). If it is homepage theater, Kleio is a loved-but-tiny peer — still dangerous, less “default noun.” |
| **Current evidence** | `VENDOR_CLAIM` on https://getkleio.com/ (2026-09-09). 20 reviews LIVE on https://apps.shopify.com/kleio. |
| **How to learn** | **Scrape:** cannot verify store count from listing. **Interview:** public reviewers (Trek Light, EMME, Hummii, Gentleman’s Gazette) if reachable without harassment. **Scrape:** BuiltWith / app-install graphs only if a **public** source exists — else leave `UNVERIFIED`. |
| **Kill / flip** | Treat 364 as **unverified** in all public Mcfly copy regardless. Internally: if interviews confirm “everyone I know uses Kleio,” S1-without-costs is dead. |

---

## Q10 — Margn review race

| | |
| --- | --- |
| **Unknown** | Will Margn leave the 0-review cohort before Mcfly? |
| **Why it changes strategy** | Same $39 Growth SKU, profit aisle, costs + “never attributed-only.” First 10 reviews in that aisle get BeProfit-adjacent traffic Mcfly does not get. |
| **Current evidence** | https://apps.shopify.com/margn-1 — 0 reviews, launched 2026-08-18. Mcfly 0 reviews, launched 2026-09-07. |
| **How to learn** | **Scrape:** Monday watch cell (`WAR_ROOM.md` §7). |
| **Kill / flip** | Margn > 0 and Mcfly = 0 → listing experiment A + TTV this week, not “ignore clones.” |

---

## Q11 — Native spend ingest (existential)

| | |
| --- | --- |
| **Unknown** | Will Admin / Sidekick / ShopifyQL grow from Shop Campaigns spend into Meta/Google/TikTok? |
| **Why it changes strategy** | Community 134251 is Mcfly’s air supply. If Shopify closes it, paste-desks die; overlays (definitions, offline, claims-vs-cash) might live (S4). |
| **Current evidence** | Shop Campaigns already have spend/ROAS — https://shopify.dev/docs/api/shopifyql/latest/schemas/marketing/shop_campaign_insights. Help Center profit reports = Cost per item only (403 from this cloud; Community 657805). |
| **How to learn** | **Scrape:** shopify.dev changelog weekly; Community 134251; Partner Editions posts. Do not trust rumor blogs without a primary URL. |
| **Kill / flip** | Official ingest announced → stop S6 immediately; decide S4 vs exit. |

---

## Q12 — Named human for love

| | |
| --- | --- |
| **Unknown** | Who answers at human speed? Kleio = Mathias. TP = Vani/Durra. TW = Juan (and 1-stars when Juan is missing). BR = they build the report. |
| **Why it changes strategy** | Love in this category is **named CS**, not anti-attribution copy. If no one is on the inbox, C3 and reviews will not happen. |
| **Current evidence** | Site says “human inbox.” No public named responder on the Mcfly listing. |
| **How to learn** | **Interview:** founder assigns a name and SLA. That is a decision, then an **Experiment** (reply-time log). |
| **Kill / flip** | Unnamed + >24h reply → do not compare Mcfly to Kleio’s love. |

---

## Q13 — Channel choice (founder decision)

| | |
| --- | --- |
| **Unknown** | Is App Store the primary acquisition channel? (`RELIGION_FLEX.md` R11; `SYNTHESIS.md` §7 checklist) |
| **Why it changes strategy** | Yes → S1/S2/S7 + listing fight. No → S3/S4 outbound; accept 0 reviews. **Neither** is the current implied state. |
| **Current evidence** | Listing is live; site points to it; 0 reviews; no documented outbound quota. |
| **How to learn** | **Interview:** founder answers the checklist in `SYNTHESIS.md` §7. Research cannot answer this. |
| **Kill / flip** | Unanswered after another week of research = **default to war-room money+love path** (outbound + listing integrity + TTV). |

---

## Q14 — Polar price conflict

| | |
| --- | --- |
| **Unknown** | App Store Core **$750** vs polaranalytics.com/vs/triple-whale “~$400” vs Talk Shop ~$720. |
| **Why it changes strategy** | Site contrast copy. Using the wrong floor makes Mcfly look sloppy (same class as repo $79 vs live $39). Does **not** change S1 vs S2. |
| **Current evidence** | Flagged in `RESEARCH_LOG.md` / `COMPETITOR_CARDS.md`. |
| **How to learn** | **Scrape** both URLs the same day before any public Polar dollar. |
| **Kill / flip** | Until resolved: say “Polar lists Core from $750; other Polar pages disagree” or say **no dollar**. |

---

## Q15 — SyncWith real agency price

| | |
| --- | --- |
| **Unknown** | Shopify card is Free + **$4.99**. Older `docs/COMPETITORS.md` lists ~$25–$150 refresh ladder (likely Workspace). |
| **Why it changes strategy** | S3 kill: “won’t pay more than SyncWith $4.99 + tab.” If agencies already pay $100+ for pipes, Mcfly $99 3-pack is easier. If they pay $4.99, S3 is ugly. |
| **Current evidence** | https://apps.shopify.com/syncwith LIVE $4.99. Workspace not re-fetched this run. |
| **How to learn** | **Scrape** Google Workspace Marketplace SyncWith pricing. **Interview** one P3: “what do you pay SyncWith / Supermetrics?” |
| **Kill / flip** | Workspace ≥ $50 and agencies pay it → S3 still alive. Only $4.99 → S3 must sell **decision**, not pipe. |

---

## Q16 — Triple Whale MER definition

| | |
| --- | --- |
| **Unknown** | `COMPETITORS.md` claims TW sometimes inverts MER (spend÷revenue). Not live-checked in this folder. |
| **Why it changes strategy** | Attack line on mcflyads.com. If false, it is a self-own. If true, it is a **finance** wedge for S4. |
| **Current evidence** | Internal doc only. TW listing does not print a MER formula (2026-09-09). |
| **How to learn** | **Scrape** TW help/docs if public. **Interview** a TW user: “show me the MER tile.” Screenshot or drop the claim. |
| **Kill / flip** | Unverified → **do not publish**. |

---

## Q17 — Tax / VAT default

| | |
| --- | --- |
| **Unknown** | What does Mcfly call “sales”? Incl. VAT? Shipping? Gift cards? Returns timing? |
| **Why it changes strategy** | TW 1★ Kove Footwear: VAT in revenue. TP 1★: VAT not in net profit. Bookkeepers 1-star definition fights. P4 will not love a desk that is silent. |
| **Current evidence** | Underspecified in live listing. `MCFY_GAP_MATRIX.md` A3. |
| **How to learn** | **Interview** one EU and one US operator. **Experiment:** a labeled toggle with a written default (ex-VAT, net sales). |
| **Kill / flip** | Ship a default **before** EU installers exist. Do not “figure it out after a 1-star.” |

---

## Q18 — Course economics

| | |
| --- | --- |
| **Unknown** | Any $79 course sales? Stripe vs Shopify? Cannibalize the desk? |
| **Why it changes strategy** | If the course is the only cash, Mcfly is consulting again (MASTER_PLAN discarded). If zero, stop spending craft on the side door. |
| **Current evidence** | SKU exists on https://mcflyads.com/pricing. No revenue figure in repo. |
| **How to learn** | **Scrape** Stripe / Shopify / site checkout logs (founder). |
| **Kill / flip** | 0 sales after 90 days of a live listing → course is brochure. Keep or kill; do not let it set the roadmap. |

---

## Q19 — Allocation honesty

| | |
| --- | --- |
| **Unknown** | Will P2 accept `suggestAllocation()` when channel sales are missing (sales ∝ spend)? |
| **Why it changes strategy** | That assumption is a credibility bomb (`SYNTHESIS.md` fact 9; `RELIGION_FLEX.md` R8). If buyers reject it, hide advice or require channel sales. If they want it, label it. |
| **Current evidence** | Code: `packages/mer-core/src/allocation.ts`. Listing claims 7/14/28 allocation. r/PPC prefers pause tests (1qgb8mg). |
| **How to learn** | **Interview** P2 with a screenshot of the assumption. **Experiment:** warning copy vs silent advice; watch whether they trust the desk. |
| **Kill / flip** | First “this is circular” objection → ship R8-A immediately. |

---

## Q20 — Partner pixel (S5b) without becoming a pixel company

| | |
| --- | --- |
| **Unknown** | Will Parkour / Elevar / WeTracked accept a “works with” relationship? Does Shopify allow those logos if there is no technical link? |
| **Why it changes strategy** | Mcfly is already merchandised *as* those apps. S5b is the cheap hedge (`SYNTHESIS.md`). S5 rebuild is the brand-suicide path (`RELIGION_FLEX.md` R1-A). |
| **Current evidence** | Adjacency LIVE. WeTracked 1★ evidence failure (elife). Elevar $225 infrastructure. |
| **How to learn** | **Interview** partner BD / public partner programs. **Scrape** App Store “works with” rules. **Experiment:** listing logos **only if true**. |
| **Kill / flip** | No partner and no OAuth → App Store rail stays a graveyard; outbound required. |

---

## Questions deliberately **not** listed

| Tempting question | Why it does not change strategy this month |
| --- | --- |
| Northbeam official price | Not in Mcfly’s install path (`LISTING_TEARDOWNS.md` §10) |
| TW 60,000 brands true? | `VENDOR_CLAIM`; Free plan + 91 reviews suffice |
| Exact TSC conversion for Mcfly | We will **measure** (Q1), not adopt gossip as ours |
| “What % of merchants want MER?” | Unknowable; WTP proxies already ranked in `PROBLEM_BANK.md` |
| Kleio founder’s personal P&L | Irrelevant; product + reviews are public |

---

## Learning cadence (binds the war room)

| When | Learn |
| --- | --- |
| **Today** | Q1 scrape · Q3 scrape · Q8 scrape · Q12 name · Q13 founder checkbox |
| **This week** | Q2 sit-with-them · Q4–Q5 interviews (start the 5) · Q10 Margn cell · Q17 default draft |
| **This month** | Q6 OAuth wall-clock · Q15 Workspace · Q16 TW MER · Q18 course ledger · Q19 allocation warning |
| **Every Monday** | Q1 cells · Q10 · Q11 changelog · Kleio review count (Q9 context) |
| **Only if Q13 = App Store** | Q7 BFS checklist · Q20 works-with |

If Q1 is still blank next week, this file was theater. Fill Q1 first.
