# Problem bank — from public reviews

Each row is a **job-shaped pain**, not a feature request. Evidence is paraphrased and cited. No invented quotes.

**Fit tags**

- `CURRENT_RELIGION` — cash MER (Shopify sales ÷ **total** ad spend), break-even, allocation; anti-path.
- `RESEARCH_OPTION` — would expand or contradict locked religion; still a real market job.
- `NON_GOAL` — copy the vendor’s failure mode (do not ship).

Full teardown: [REVIEW_MINING.md](./REVIEW_MINING.md). Machine rows: [db/problems.csv](./db/problems.csv).

---

## P-001 — Profit dashboards that hide unattributed ad spend

| | |
| --- | --- |
| **Pain** | A “net profit” tile that only subtracts spend it can stitch via UTM / converted traffic. Unmatched Google/PMax spend vanishes → profit is fiction. |
| **Who** | Merchant + finance (hurt). Media buyer (may *like* the prettier number). Vendor (defends “attribution quality”). |
| **Evidence** | A Farley Country Attire: fully connected Google Ads imported **~15%** of spend; live chat said this is **by design**. “A profit tool must always show total ad spend, even if attribution is imperfect.” 2026-01-07. https://taranker.com/shopify-beprofit-profit-tracker-app-customer-reviews · listing https://apps.shopify.com/beprofit-profit-tracker/reviews?ratings%5B%5D=1 |
| **Also** | Shopify Community: “Whatever tool you pick, make sure it pulls your TOTAL ad spend from Google and Meta, not just attributed spend.” https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628 |
| **JTBD** | When I close the week, I need **all cash that left for ads** against **all cash Shopify recorded**, so I do not scale a lie. |
| **Mcfly** | `CURRENT_RELIGION` — this is the product. Show unmatched spend as spend, not as a hole. Recon: platform export vs MER denominator. |
| **Anti** | `NON_GOAL` — “smarter” spend that drops unmatchable PMax. That *is* BeProfit. |

---

## P-002 — VAT / tax silently in (or out of) “revenue”

| | |
| --- | --- |
| **Pain** | Marketing suites treat tax-gross Shopify totals as revenue. Finance treats VAT as a pass-through. Nobody labels the definition. EU/UK operators discover it late. |
| **Who** | Finance (hurt). Media (inflated ROAS). Merchant in VAT countries. |
| **Evidence** | Kove Footwear (TW, 2026-07-06): “includes VAT in your revenue (revenue should never be including VAT). I wonder how many people don't even realize this.” https://appnavigator.io/app/triplewhale-1/reviews/2272366 · https://apps.shopify.com/triplewhale-1/reviews?ratings%5B%5D=1 |
| **Also** | VocaSpark (TrueProfit, 2026-07-04): app “doesn't track VAT collection.” Vendor reply 2026-07-08: “Shopify VAT is excluded from Net Profit.” Same war, opposite default. https://apps.shopify.com/trueprofit/reviews?ratings%5B%5D=1 |
| **JTBD** | When I send a number to the accountant (or a Dutch/German buyer), I need **ex-VAT sales**, tax collected, and a written definition. |
| **Mcfly** | `RESEARCH_OPTION` if we only ship one unlabeled “Shopify sales.” `CURRENT_RELIGION` if we **name** the cash definition and offer ex/inc. Do not silently match TW. |
| **Anti** | Hide the toggle. Pretend one formula works in US + NL. |

---

## P-003 — Success tax (orders / GMV / “you grew, pay more”)

| | |
| --- | --- |
| **Pain** | Analytics bill spikes because the store had a good month — the moment they most need the tool. Sometimes **without notice**. |
| **Who** | Founder + finance. Agency (passes through or eats it). |
| **Evidence** | bamtoo (TrueProfit, 2024-12-21): two-month sales uplift → **quadruple** the usual fee **plus** subscription; no notification that extra orders cost money. https://taranker.com/shopify-trueprofit-app-customer-reviews?filter-by=1 |
| **Also** | The Brooklyn Singapore (TrueProfit, 2026-01-20): 3-year legacy user, **1-week notice**, accept **400%** hike or be banned. Chef Preserve (Lifetimely, 2025-07-09): **$600/mo** volume pricing vs **$30** under the founder. Polar Trustpilot (Maja, 2025-11-07): Shopify list price ≠ post-install sales quote (higher). https://www.trustpilot.com/reviews/690da52c91938d8e1b9286b7 |
| **JTBD** | Pay a **flat, knowable** desk fee that does not punish a viral week. |
| **Mcfly** | `CURRENT_RELIGION` — master plan already refuses GMV tax (~$79 flat narrative). Reviews say **publish the overage rules or have none**. |
| **Anti** | Per-order surcharge “with a cap” that still surprises (TrueProfit, some GoProfit tiers). |

---

## P-004 — Cost basis that rots (COGS, variants, missing products)

| | |
| --- | --- |
| **Pain** | Profit is only as honest as unit cost. Reinstalls stale variants; products vanish so costs cannot be entered; supplier price changes rewrite history. |
| **Who** | Merchant + finance. Ops (3PL / supplier changes). |
| **Evidence** | VocaSpark: reinstall → variants outdated, **no refresh without support**. PuppyPad (BeProfit, 2024-03/04): products not appearing → cannot add costs → “all my data is skewed”; week+ of escalation. Community: if today’s cost is applied to old orders, **historical P&L is wrong** — timestamp at order time. |
| **JTBD** | When a supplier price changes Tuesday, **Monday’s orders keep Monday’s cost**. I can rebuild a variant table without a ticket. |
| **Mcfly** | `RESEARCH_OPTION` for SKU/order COGS ledger. `CURRENT_RELIGION` for **contribution margin %** as an explicit input — but reviews say a single % is what they are trying to *escape*. |
| **Anti** | Silent average COGS. Support-only recost. |

---

## P-005 — Post-purchase upsell / order-edit / returns break the till

| | |
| --- | --- |
| **Pain** | Shopify’s order is not one immutable row. Upsells, Loop exchanges, edits move money across days. Apps either ignore it or park it on the wrong date. |
| **Who** | Merchant + finance. Ops. |
| **Evidence** | Koss Design (Lifetimely, 2024-11-28): with post-purchase upsell, numbers “not relevant at all”; support closes tickets fast. TW vendor doc: edits/returns → **Shopify day ≠ TW day**. https://triplewhale.readme.io/docs/why-do-my-order-based-sales-metrics-not-match-between-shopify-and-triple-whale |
| **JTBD** | Period sales in MER must match a **reconciliation view** I can export: original, edits, refunds, with dates. |
| **Mcfly** | `CURRENT_RELIGION` if Shopify Admin sales for the period already include edits the way finance expects — **prove it**. `RESEARCH_OPTION`: edit/refund ledger. |
| **Anti** | A second “order revenue” definition that nobody can audit. |

---

## P-006 — Spreadsheet is the real incumbent (and it is already lying)

| | |
| --- | --- |
| **Pain** | $15–20k/mo operators spend 30 minutes/day stitching fees, ads, shipping. Numbers never feel right. Suites feel like a fighter jet. |
| **Who** | Solo merchant / lean founder. |
| **Evidence** | Shopify Community OP, ~2026-02: messy Sheets; paying TW; “overkill and expensive”; wants **real net profit per order**. Replies: TW built for $50k+/mo ad spend; accuracy = COGS quality; many $49–$149 apps fail the price test. Omni Wave / Rooted Threads (BeProfit 5★): Excel was slow and wrong; auto Meta + COGS. |
| **JTBD** | Replace the sheet **without** buying an OS. |
| **Mcfly** | `CURRENT_RELIGION` — this is the wedge band. Monday ritual beats Moby. |
| **Anti** | Feature parity with TW to “win” this buyer. Kleio $29 5-stars say they already defected on **price + simplicity**. https://apps.shopify.com/kleio |

---

## P-007 — Cannot leave (billing, contracts, history prison)

| | |
| --- | --- |
| **Pain** | Uninstall ≠ cancel. Annual debit after “timely cancel.” Monthly invoice is a monthly **contract**. History is the hostage. |
| **Who** | Merchant ops + finance (AP). |
| **Evidence** | Adrienne Landau: $720/yr unused since 2023. STADIUMDREAMS: annual taken after cancel. Girl Stitch: chat will not deactivate. ETHNIK LIVING (TW): no refund, hard cancel. BrickHelmets (TrueProfit): uninstall as instructed, charged again. Tooltekt (TW): monthly pay = monthly contract; 60-day guarantee dead. BioPower Pet: would switch but **historical data invested**. |
| **JTBD** | Leave in one Shopify uninstall; data export; no hostage history. |
| **Mcfly** | `CURRENT_RELIGION` (trust / enterprise-ready). Research: **export + definition card** so lock-in is not the moat. |
| **Anti** | Side-channel trials that auto-bill (Dibsies / BeProfit). |

---

## P-008 — Onboarding theater, production silence

| | |
| --- | --- |
| **Pain** | Sales / CSM week 1 is world-class. Week 12 a critical bug sits for days–months. Highest plan still gets bots. |
| **Who** | All. Worst for **agencies** (client SLA) and **media** (spend is on). |
| **Evidence** | Zamage (TW, 2025-12-12): polished onboarding; CSM “I’ll ask someone else.” G2: **>$600/mo**, 3 months, “working on it.” Cloudflops (BeProfit): highest plan, bot chat, 2 weeks. Chef Preserve: 30 chats / 10 emails / 20 days; AMP bureaucracy vs founder-era 5-minute fixes. Analyzify Watch Factory: premium window **expired because they delayed**. |
| **JTBD** | When Friday spend is wrong, a human who can **change a number** answers in-hours, not a ticket closer. |
| **Mcfly** | Ops, not a feature. `CURRENT_RELIGION` already refuses an AI OS that then **sells credits** (Kove / Cocaine Coffee). |
| **Anti** | Named-hero support as the only reliability story. |

---

## P-009 — Tracking priesthood: platforms over-claim, the “fix” can nuke the account

| | |
| --- | --- |
| **Pain** | Meta and Google claim the same sale. Merchants hire server-side / pixel vendors. Implementations duplicate GA4, fail Google Ads, or ban the ads account. |
| **Who** | Media + agency (job). Founder (cash risk). |
| **Evidence** | Sacred Rituel Beauty (Analyzify 5★, 2025-07-29): hired after **over-attribution between Google and Meta**. Duckfeet (1★, 2025-04-13): ≥4 GA4 properties, Embed+Customer Events, **Google Ads disapprovals**, “significant revenue loss”; stay native Shopify. Diluu (TW, 2024-10-23): Google Ads **banned after pixel**. Ennebiservice update: 90% traffic / 95% revenue drop after GA4/Ads admin work. Tameson: six licenses, five months to beta, then silent prod bug. |
| **JTBD (media)** | Feed algorithms “accurate” conversions. |
| **JTBD (founder)** | Do not let a tag manager take the store offline. |
| **Mcfly** | Pain of over-claim = `CURRENT_RELIGION`. Shipping CAPI/GTM = `RESEARCH_OPTION` / refuse under master plan. **Possible Mcfly:** a **claims-vs-cash** card (platform ROAS vs till) without installing a pixel. |
| **Anti** | Become Analyzify. Paid implementation as a recurring hostage (Tech Instrumentation, Good Health Co, NVMOS lifetime rebill). |

---

## P-010 — Multi-store / Amazon / shared warehouse identity

| | |
| --- | --- |
| **Pain** | One merchant brain, N Shopify shops, sometimes Amazon, sometimes one warehouse. Tools either **multiply inventory**, **charge N licenses**, or sell a buggy Amazon add-on at full price. |
| **Who** | Multi-brand merchant + **agency**. |
| **Evidence** | Polar Trustpilot Maja: 6 stores, 1 warehouse, inventory **×6**, “unusual setup,” 1.5 months. Tameson: 6 stores, one GTM, 6 licenses. carnivoro (Lifetimely): Amazon add-on as expensive as Shopify app, still buggy after cancel/return. Ecolino / RETRO CLASSIC (BeProfit 5★): multi-shop merge is the reason they stay. Bio-First: 4 stores Shopify+Amazon, wants Lifetimely-class LTV. |
| **JTBD** | One desk, many storefronts, **one stock**, one spend rollup. |
| **Mcfly** | `RESEARCH_OPTION` (master plan: multi-brand only if revenue pulls). Agency license design is a **monetization** research item — do not copy Polar’s GMV × complexity. |
| **Anti** | Per-shop GMV stack. |

---

## P-011 — LTV / CAC payback that analysts could not build

| | |
| --- | --- |
| **Pain** | Founders pay analysts who still get lifetime-value logic wrong. They want cohort LTV by discount / first product / channel to decide **whether a customer is worth the CAC**. |
| **Who** | Growth + finance. Not the media buyer’s daily ROAS. |
| **Evidence** | organifi (Lifetimely 5★, 2026-07-13): “ungodly amount on data analysts who couldn't seem to understand the logic”; app does it by default; Sadie “understands… customer acquisition.” Armor Class 1★: **weighted LTV inaccurate** (so the job exists and can fail). |
| **JTBD** | Know payback months and which promo **destroys** LTV. |
| **Mcfly** | `RESEARCH_OPTION`. Not period cash MER. Could sit **beside** break-even (CAC vs contribution), not instead of it. |
| **Anti** | Predictive LTV as a black box billed like AMP AI. |

---

## P-012 — Payment fees modeled, not taken from Shopify

| | |
| --- | --- |
| **Pain** | Transaction fees are a formula. Shopify already has the actual. The P&L is then systematically off. |
| **Who** | Finance. |
| **Evidence** | WASABI Knives (TrueProfit, 2021-05-10): “calculated by a formula although this can be pulled directly from Shopify… Beprofit can pull the transaction fees directly.” https://apps.shopify.com/trueprofit/reviews?ratings%5B%5D=1 |
| **JTBD** | Fees on the desk = fees on the payout. |
| **Mcfly** | `CURRENT_RELIGION` if we stay at **sales ÷ spend** and treat fees inside **margin %**. `RESEARCH_OPTION` if we ship a full P&L (then pull Shopify actuals, never invent). |
| **Anti** | A clever fee model. |

---

## P-013 — Demo / work-email / sales-call gates

| | |
| --- | --- |
| **Pain** | Cannot evaluate the tool the way Shopify apps are evaluated (install, 10 minutes, uninstall). |
| **Who** | Lean merchant. Polar’s actual buyer (data team) may *want* a sales call — conflict. |
| **Evidence** | dryoasisplants: “before you can try — it requires a sales call.” Skechers.dk: verify email never arrives. Minseart: personal Gmail blocked. All Polar 1★. |
| **JTBD** | Self-serve truth in a trial, **then** talk to sales if we are an enterprise. |
| **Mcfly** | `CURRENT_RELIGION` (Shopify-first, install). Do not copy Polar’s gate for the cash desk. |
| **Anti** | “Talk to sales” as the only path to MER. |

---

## P-014 — AI / extra credits after the contract

| | |
| --- | --- |
| **Pain** | The suite sells “AI teammate,” then meters it. Support is the bot you already paid for. |
| **Who** | Merchant on Foundation/mid tiers. |
| **Evidence** | Kove Footwear: AI help needs credits. Cocaine Coffee (5★, 2026-07-20): TW should warn about **Foundation AI usage limits**. |
| **JTBD** | Either the desk answers the money question without a chatbot, or the chatbot is **in the plan**. |
| **Mcfly** | `CURRENT_RELIGION` — Monday ritual, not Moby. `RESEARCH_OPTION`: Kleio-style MCP at **flat** price (Trek Light 5★), not credit packs. |
| **Anti** | Ship an assistant, then sell tokens. |

---

## P-015 — Number fights (Shopify vs suite vs platform vs books)

| | |
| --- | --- |
| **Pain** | Four scoreboards. Meetings become theology. Finance will not sign a budget on a modeled number. Media will not accept MER that “hides their channel.” |
| **Who** | **The conflict is the product category.** |
| **Evidence** | TW vendor doc (dates/edits). Northbeam vendor doc (discrepancies expected). G2 Ash O. (~50% wrong source). Eightx: TW is not a system of record. Seller Stacked (secondary): Meta £47.2k vs TW £31.4k same window — framed as “overlap,” still a fight. Community: daily ad spend vs order-level profit is “the main thing that goes wrong.” |
| **JTBD (finance)** | One number that ties to payout. |
| **JTBD (media)** | One number that tells them what to bid. |
| **JTBD (founder)** | Stop hosting the argument. |
| **Mcfly** | `CURRENT_RELIGION`: **do not join the attribution court.** Be the till. Show the **gap** (claims vs cash) as a teaching tile. `RESEARCH_OPTION`: exportable recon pack for the CFO (Shopify sales, spend files, MER, break-even). |
| **Anti** | A seventh model named “Triple Attribution.” |

---

## P-016 — Agency needs a rollup; vendor sells N products

| | |
| --- | --- |
| **Pain** | Agencies run many brands. They need one login, client-safe exports, and pricing that is not GMV × N. Suites optimize for the **brand seat**. |
| **Who** | Agency (hurt). Vendor finance (wins). Merchant (pays twice if agency + brand both subscribe). |
| **Evidence** | Ash O. G2: agency partner, performance pricing, attribution to source fails ~50%. Tameson: 6 licenses / 1 codebase. Ecommerce Times (secondary): TW agency dashboard latency; exports need cleanup; Northbeam prioritized agency UX. Ecolino 5★: multi-shop **is** the value. |
| **JTBD** | Run a Monday desk across a roster without six CSMs. |
| **Mcfly** | `RESEARCH_OPTION` — agency SKU. Current plan is brand-first. If we ever sell agencies, **one brain** (ARCHITECTURE already says this). |
| **Anti** | Partner program that exists because the product is too hard (Duckfeet on Analyzify). |

---

## Stakeholder conflict matrix

| Topic | Merchant | Agency | Finance | Media buyer |
| --- | --- | --- | --- | --- |
| Total vs attributed spend | Total | Often attributed (prettier client ROAS) | Total | Attributed / platform |
| VAT | Confused until a Kove moment | Ignore if US-heavy roster | Ex-VAT + collection | Gross if it lifts ROAS |
| Refresh cadence | Weekly cash is enough | Client wants “live” | Month close | Intraday |
| Price shape | Flat | Seat / roster, not GMV | Flat, no success tax | Will spend if it moves bids |
| Source of truth | “Does this match my bank?” | “Can I put this in the deck?” | Payout + COGS history | Pixel / CAPI |
| Switching | Fear of history loss | Fear of 20-account rebuild | Fear of two books | Fear of losing lookback |

**Mcfly pick (research recommendation, not a ship ticket):** serve **merchant + finance** in the conflict. Let agencies use the same till number in the deck. Do not sell media a prettier path.

---

## Possible Mcfly answers (including RESEARCH_OPTION)

| Pain | Current-religion answer | RESEARCH_OPTION |
| --- | --- | --- |
| P-001 hidden spend | Denominator = **all** connected spend; flag unmatched | — |
| P-002 VAT | Label sales definition on the dashboard | Ex/inc/collection modes |
| P-003 success tax | Flat ~$79; no order overage | Agency roster SKU |
| P-004 COGS rot | Honest margin % input | Timestamped variant costs |
| P-005 edits/upsells | Period Shopify sales + recon note | Edit/refund subledger |
| P-006 spreadsheet | Monday MER ritual | Order/SKU profit table |
| P-007 cancel prison | Shopify Billing + export | History export as a feature, not a hostage |
| P-008 support cliff | Small surface area (less to break) | Human SLA, no credit-gated bot |
| P-009 pixel priesthood | Claims-vs-cash teaching tile | Do **not** ship GTM (master plan) |
| P-010 multi-store | Later, if revenue pulls | Shared inventory identity |
| P-011 LTV | Out of v1 | Cohort payback beside break-even |
| P-012 fees | Inside margin % | Shopify fee actuals if P&L ships |
| P-013 sales gate | Install/trial | — |
| P-014 AI credits | No Moby | Optional MCP at flat fee (Kleio pattern) |
| P-015 number fight | One formula, screamed | CFO recon pack |
| P-016 agency | Brand-first | One-brain roster |

---

## Priority (research)

| Rank | IDs | Why |
| --- | --- | --- |
| 1 | P-001, P-015, P-006 | Smoking-gun reviews + community kill tests. On religion. |
| 2 | P-002, P-003, P-007 | Trust / EU finance / price honesty. Blocks paid conversion. |
| 3 | P-004, P-005, P-012 | Becomes real the minute we claim “profit,” not just MER. |
| 4 | P-010, P-016, P-011 | Agency / LTV / Amazon — revenue-pull only. |
| 5 | P-009, P-014 | Real pain; shipping it is how we become TW/Analyzify. |

Religion stays flexible **in this folder**. Shipping still needs a human rewrite of `docs/MASTER_PLAN.md` §1–§2.
