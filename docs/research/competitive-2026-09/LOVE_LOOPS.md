# Love loops — what creates weekly habit / reopen in Admin

**Date:** 2026-09-09 (Wave B)  
**Mode:** RESEARCH ONLY. No ship order.  
**Question:** What actually makes a merchant *reopen an analytics app inside Shopify Admin* every week — and why Mcfly, as it exists today, almost certainly will not.

Love here is not a brand feeling. It is a **repeat behavior** that later becomes a 5-star review. If the merchant does not reopen, they cannot love you. If they reopen only to paste a CSV, they will resent you.

---

## 0. Brutal Mcfly read (today)

Live Mcfly ([apps.shopify.com/mcfly-analytics-public](https://apps.shopify.com/mcfly-analytics-public), re-fetched 2026-09-09): **$39/mo, 7-day trial, 0 reviews, launched Sept 7.** The marketing site sells a **10-minute Monday ritual** (`site/product.html`: “confirm margin, paste Meta + Google from Sheets, read net sales ÷ spend vs break-even — about 10 minutes”).

The shipped Admin app (`app/app/routes/app._index.tsx`) does this on first open:

1. Authenticate.
2. Pull Shopify sales for MTD/QTD/YTD.
3. Show **MER** (repo name) next to **Ad spend (manual)**.
4. If spend is empty: *“Add spend entries to compute MER”* + a link to `/app/spend`.

That is not a loop. That is a **blank cash register**. The merchant already has sales in Admin → Analytics. Mcfly adds a second sales number and then **asks them to do homework** before the headline metric exists.

MASTER_PLAN §11 already named the kill: *“Design partners won’t open weekly after 30 days of accurate MER.”* The product has not earned the right to test that kill. There is no public evidence anyone has opened it weekly. There is no review, no named human, no push artifact.

`CURRENT_RELIGION` treats the Monday paste as the product. Public evidence says the loved products **remove the paste** and then **visit the merchant** (email, Slack, MCP scheduled pull). Mcfly does neither.

---

## 1. What a “love loop” is (and is not)

A love loop is a **closed circuit** with four parts. If any part is missing, you get a one-time install, not a habit.

| Part | Meaning | Mcfly today |
| --- | --- | --- |
| **Trigger** | A clock or a ping the merchant already obeys (Monday standup, daily “did we make money,” inbox) | None. No email, Slack, SMS, Admin badge, or scheduled report. |
| **Action** | One cheap reopen (click the Admin app, or — better — click the email) | Must remember Mcfly exists, then paste spend. |
| **Reward** | A number that **changed since last time** and answers a question they already ask | Reward is gated on homework. Empty spend → no MER. |
| **Investment** | Something they put in that makes leaving costly (history, COGS, a board pack, a Slack ritual) | No history worth keeping. No costs. No pack. CSV is *their* investment in *their* Sheet — they can leave Mcfly and keep the Sheet. |

This is not Nir Eyal fanfic. It is what the **review corpus** already describes (see `REVIEW_THEMES.md`, sibling PR #5 `REVIEW_MINING.md` when merged).

**Not a love loop:**

- A pixel that fires and then disappears into Ads Manager (Parkour / WeTracked). That is **install love**, then **reopen somewhere else**.
- A sermon (“platforms are lying”) with no new number this week.
- Allocation advice that assumes sales ∝ spend (`packages/mer-core` / listing “Spend Allocation 7/14/28”) when the merchant has not even entered spend.

---

## 2. Observed loops in the aisle (public, dated)

Five loops print reviews. Mcfly is in none of them.

### Loop A — Daily “did I make money?” (profit desk)

**Who:** TrueProfit, Lifetimely, BeProfit, Kleio.  
**Trigger:** morning / end of day curiosity. Not Monday. **Daily.**  
**Action:** Open Admin app (or email). Number is already there because **ad spend OAuth + COGS/fees** ran overnight.  
**Reward:** Net profit / P&L pulse. Kleio review, Hummii Snacks, 2026-04-23: *“daily pulse on our P&L”* + MCP pull into a **scheduled daily report** ([apps.shopify.com/kleio](https://apps.shopify.com/kleio)). TrueProfit GowiLab (visible 2026-05-26): *“must need to see how much you're actually making in profit.”* Lifetimely Nikura: *“source of truth… simple and fast and not bloated.”*  
**Investment:** Cost configuration. Leaving means rebuilding COGS.

**Evidence of the ritual being the job, not a feature:** PR #5 mining (Taranker / listings) — Rooted Threads on BeProfit: Facebook spend + COGS used to be a **daily spreadsheet chore**. Omni Wave: Excel was time-consuming. The app **retired the sheet**.

**Mcfly:** sells a **weekly** ritual for a market that reviews **daily profit**. Wrong clock. See `ENTERPRISE_WORKFLOWS.md` clock table.

### Loop B — The artifact visits them (push report)

**Who:** Better Reports (5.0 / **1,198–1,199**, scheduled email or Google Sheets — [apps.shopify.com/betterreports](https://apps.shopify.com/betterreports), [betterreports.com](https://www.betterreports.com/)); Lifetimely automated email reports (ATTN Agency 2026 review; Price Geek 2026 feature table); TrueProfit “Customize Email Report” from Advanced $60 ([trueprofit.io/pricing](https://trueprofit.io/pricing)); Metorik automated emails (Wave A card).  
**Trigger:** the inbox, not memory.  
**Action:** open email / Sheet. Reopen in Admin is **optional**.  
**Reward:** the report they already need for standup.  
**Investment:** schedule + recipients. Better Reports even meters **scheduled runs** (docs: Basic/Grow/Advanced 1,000 runs/mo included; extra runs $0.03–$0.04 — [docs.betterreports.com](https://docs.betterreports.com/article/179-scheduled-report-run-allowance)). The habit **is** the SKU.

This is the only loop MASTER_PLAN already half-named (kill = won’t open weekly). Better Reports proved you can get **1,199 reviews** by making the open happen **outside** Admin.

**Mcfly:** no schedule tab. No email. The Monday Close is copy on `/product`, not a worker.

### Loop C — Named human + Slack (enterprise CS loop)

**Who:** Polar (4.9/116, Magic summary: support + onboarding); Elevar reviews name Sourabh / Raphael / Darshak in the first 11 days; Lifetimely higher tiers: dedicated Slack (Price Geek 2026); Kleio 5-stars name **Mathias** and Slack.  
**Trigger:** a person in the calendar / Slack.  
**Action:** they reopen because onboarding is unfinished or the AM sent a number.  
**Reward:** “someone is doing this with me.”  
**Investment:** three months of Polar history (Valabasas ~2 years; Chicory incrementality).

Polar’s 1-stars are the inverse: **could not start without a sales call** (dryoasisplants, 6 minutes, 2024-10-01). CS loop without self-serve = love for those who get through, hate for those who don’t.

**Mcfly:** “Support: a human inbox” on the site. 0 reviews means 0 named humans. At $39 you cannot staff Polar. You can still **sign the 72-hour rescue email with a first name** (TSC onboarding, MARKET_REPORT).

### Loop D — Feed the algorithm, never come back (pixel)

**Who:** Parkour 4.9/191 Free (“Setup takes just 2 minutes”); WeTracked 4.8/125; Clarity 4.6/2,125.  
**Trigger:** install / EMQ panic.  
**Action:** reopen only when tracking breaks.  
**Reward:** Ads Manager looks better (WeTracked 5★ isella, 2026-09-01: *“I can track inside of Meta ad manager and I do not have to use another dashboard.”*).  
**Investment:** pixel / CAPI. Uninstall is scary (theme leftovers — see `ANTI_PATTERNS.md`).

This loop **creates reviews** and **kills desks**. It is why Shopify files Mcfly next to Clarity / WeTracked / Parkour. Those neighbors trained the graph that “ads analytics” = install a tracker and leave.

**Mcfly religion is correct that this is not cash.** Mcfly is incorrect that this loop will send those merchants into a $39 CSV desk. They already have a dashboard: Ads Manager.

### Loop E — MCP / Claude as the daily reopen (new, small-n, real)

**Who:** Kleio (5.0 / **20**, launched 2025-02-19, **$29 flat**, 14-day, unlimited users, 1,000,000 orders in database — live listing 2026-09-09). Polar MCP on Core; TrueProfit MCP; Lifetimely MCP on paid.  
**Trigger:** the merchant’s existing Claude / ChatGPT schedule.  
**Action:** they may never open Admin. Trek Light (2026-08-12): *“Paired the MCP with my Claude setup… Kleio made it easy to say goodbye to TripleWhale.”* Hummii Snacks: MCP in a **scheduled daily report**.  
**Reward:** the number appears where they already think.  
**Investment:** the prompt / MCP connection.

This is the 2026 version of Better Reports email. Mcfly has no MCP. Listing-adjacent TrueProfit / Lifetimely / Polar already do.

`RESEARCH_OPTION`: read-only MCP of **one** cash number beats another empty Admin tile. Risk: fashion; do not meter tokens (TW AI-credit 1-stars).

---

## 3. What creates *weekly* reopen **in Admin** specifically

Admin reopen is a **worse** habit surface than email. A $5M brand runs **6 apps** on average (StoreLeads via Craftberry / TSC 90-day playbook, MARKET_REPORT). TSC: a $5M brand may have **30–50** apps; the average merchant runs **6**. Either way, Mcfly is one tile in Settings → Apps. Weekly reopen inside Admin happens when at least one of these is true:

| # | Mechanism | Public proof | Mcfly |
| --- | --- | --- | --- |
| 1 | **The number changed overnight without them** | TrueProfit “real-time sync ad spends”; Kleio “connect ad channels… real-time”; Lifetimely attribution + daily P&L | Fail. Manual spend. |
| 2 | **They need a definition they cannot get in Analytics** | Community 657805: revenue is native, **net profit must be assembled**; Community 134251: Admin **will not ingest spend** | Partial. Spend is the gap — but they can assemble it in Sheets for $0 / SyncWith $4.99. |
| 3 | **A meeting forces the tab** | Agency Monday pack; Polar unlimited users; Better Reports emailed to the team | Fail. Single store, no pack. |
| 4 | **Pin / nav / embedded home is the default Monday surface** | Official: primary workflows stay in Admin ([shopify.dev onboarding](https://shopify.dev/docs/apps/design/user-experience/onboarding); BFS in-admin). Apps that look “working” on homepage get reopened. | Fail. Homepage is not “working” until spend exists. Official: homepage must show the app is working **and, if possible, how well** — not a static welcome. |
| 5 | **Fear of a wrong definition** | TW VAT 1-star (Kove Footwear); BeProfit attributed-spend 1-star (A Farley: ~15% of Google spend). Operators reopen to **check the lie**. | Fail. Mcfly has one unlabeled sales field and no claims-vs-cash card. |

**Weekly** is the founder’s preferred clock (`site/product.html`, MASTER_PLAN §13). **Daily** is what reviewers praise. If Mcfly stays weekly, the artifact **must leave Admin** (email/Slack) because nobody opens a blank MER tile on Monday out of loyalty.

r/shopify `1rpjuk0` and r/PPC `1qgb8mg` already run the weekly blended sheet **without Mcfly**. The habit exists. Mcfly is a **tax on the habit they already have** (paste the sheet into the app). That is the opposite of a loop.

---

## 4. Why “10 minutes every Monday” is a lie in the current product

The site’s four-step ritual (confirm margin → paste spend → read Total ROAS → one budget move) assumes the merchant:

1. Already exported Meta + Google (+ TikTok + email + billboard) into a Sheet **this week**.
2. Already has a Mcfly CSV template filled (`site/product.html` #spend-csv: download blank → Sheets Import → fill → download CSV → paste).
3. Trusts a **typed margin %** as break-even (finance does not — Community 657805).
4. Will take an allocation suggestion that may assume sales ∝ spend.
5. Will do this **inside a 7-day trial** before they have a full week of their own spend in the desk.

That is not 10 minutes. That is **the weekly job they already fail to do**, plus a second system of record. Community 657805: spreadsheets are *“always a week behind.”* Mcfly does not fix lateness. It **inherits** it.

Compare Kleio’s first-session promise on the listing: connect ads, see P&L, rank products. 14-day trial. $29. Twenty 5-stars in ~19 months, several **explicitly leaving Triple Whale**. Same adjacency rail as Mcfly (Clarity / WeTracked / Parkour). Kleio is what the graph thinks Mcfly is, except Kleio **ships the profit loop**.

---

## 5. Activation vs habit (do not confuse them)

TSC (MARKET_REPORT, May–June 2026):

- Activation = first value moment that predicts 90-day paid retention.
- Habit is **weeks 2–4** after activation ([90-day save playbook](https://taylorsicard.com/blog/shopify-app-churn-90-day-save-playbook)).
- ~75% of users who will churn go quiet in **week one** (Shno 2026, cited by TSC).
- After 7 days without activation, recovery is “statistically unlikely.”

Mcfly has not defined an activation event. A research hypothesis (not measured — Partner Dashboard does not exist in this repo):

| Candidate activation | Predicts habit? | Why |
| --- | --- | --- |
| Installed the app | No | TSC: install ≠ trial start |
| Saw Shopify sales on the desk | No | They already have this in Admin |
| Entered **any** spend and saw MER/Total ROAS ≠ blank | **Minimum** | First time Mcfly is not Analytics |
| Completed one Monday with spend > 0 and a written definition | Better | Matches MASTER_PLAN kill |
| Received a **push** Close they did not request | Best habit proxy | Better Reports / Lifetimely pattern |

Until (c) happens inside the **7-day** trial, there is no loop to measure. That is why 7-day + paste is a **love killer**, not an honesty badge.

---

## 6. Religion-flex: which loops we can steal without becoming Triple Whale

| Loop | Steal? | Tag | Why |
| --- | --- | --- | --- |
| A Daily profit pulse | Steal the **clock and the auto-spend**, not the full P&L on day one | `RELIGION_BEND` | OAuth spend is MASTER_PLAN Phase 2 already. Daily number can still be sales÷spend. |
| B Push artifact | **Yes. Highest love / lowest religion cost.** | `STRETCH` | Email/Slack of the same formula. Better Reports proof. |
| C Named human | Yes for first 20 paid | `STRETCH` | Elevar/Polar reviews. Do not productize $750 CS. |
| D Pixel | Partner only | `RELIGION_BEND` (B) / `BREAK` (build) | See `RELIGION_FLEX.md` R1. Pixel loop does not reopen *Mcfly*. |
| E MCP | Thin, later | `STRETCH` | Kleio’s 5-stars are daily pulse + MCP, not MTA. |

**Do not steal:** Moby, AI credits, GMV tax, “source of truth” without a written sales definition (that 1-stars you — `ANTI_PATTERNS.md`).

---

## 7. What would have to be true for Mcfly to be loved

Not a roadmap. A test.

1. A merchant can see **a non-blank, dated, defined number** in the first session without exporting Ads Manager. (OAuth **or** a labeled SAMPLE that flips to live sales immediately — official homepage pattern: show working + how well.)
2. Something they already open (inbox, Slack, Claude) **brings them the number** on a clock. Admin reopen becomes optional.
3. The number includes **total** spend, not attributed spend (BeProfit anti-pattern).
4. A human with a first name answers when the number looks wrong.
5. After one real week, a **neutral** review ask (official Reviews API; never at install) — [manage app reviews](https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews).

Until those are true, Mcfly is a **brochure of a ritual**. Rituals that exist only in copy do not create reopen. They create uninstalls that never write a review — or, after day 8, a billing 1-star.

---

## Sources (Wave B fetches)

- Live listings 2026-09-09: Mcfly, Kleio, Better Reports, TrueProfit, Lifetimely (see `RESEARCH_LOG.md` session 6).
- Shopify onboarding: https://shopify.dev/docs/apps/design/user-experience/onboarding
- Shopify reviews policy: https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews
- TSC onboarding / churn / 90-day (MARKET_REPORT): https://taylorsicard.com/blog/shopify-app-onboarding-benchmarks · https://taylorsicard.com/blog/shopify-app-churn-symptom-not-problem · https://taylorsicard.com/blog/shopify-app-churn-90-day-save-playbook
- Better Reports schedule docs: https://docs.betterreports.com/article/230-navigate-the-schedule-tab
- TrueProfit pricing: https://trueprofit.io/pricing
- Lifetimely / AMP pricing: https://useamp.com/pricing/
- Community / Reddit / Wave A review themes: `REVIEW_THEMES.md`, `ENTERPRISE_WORKFLOWS.md`, `PERSONAS.md`
- Sibling (do not overwrite): PR #5 `REVIEW_MINING.md`, PR #6 `MONETIZATION_PATTERNS.md` §5
