# Interview scripts — operators, agencies, CFOs

**Date:** 2026-09-09  
**Wave:** D (append). Does not replace [`PERSONAS.md`](./PERSONAS.md) or [`MERCHANT_PROBLEMS.md`](./MERCHANT_PROBLEMS.md).  
**Rule:** Every question is grounded in a **public** review, forum, or vendor-FAQ sentence. Do not invent “we interviewed 40 CFOs.” These scripts are how you *start* interviewing. Until you run them, Mcfly has **zero primary voice**.

Religion tags: `CURRENT_RELIGION` · `RESEARCH_OPTION` · `EVIDENCE` · `RISK`.

---

## 0. Why this file exists (silence death)

Mcfly launched September 7, 2026. Live listing: **0.0 / 0 reviews**. https://apps.shopify.com/mcfly-analytics-public

The category does not have a discovery problem. It has a **conversation problem**.

| Who already talks | Proof | What they hear |
| --- | --- | --- |
| Founders asking “what’s my profit” | Community 657805 (335 views) · r/shopify 1pzy8iv | TrueProfit / Lifetimely / “spreadsheet always a week behind” |
| Operators asking “Meta ≠ Shopify” | r/PPC 1u81q7r · r/shopify 1rpjuk0 | “use blended MER” / “it will never sync up” |
| Agencies building Sheets | r/PPC 1qgb8mg | “I ignore platform attribution completely” |
| Finance reconciling payouts | Community 577364 · A2X 5.0/359 | Settlement → QB/Xero, not Total ROAS |
| Kleio’s first 20 reviewers | https://apps.shopify.com/kleio | “goodbye TripleWhale” · named 2-hour founder calls |

Mcfly is **not in any of those conversations**. The listing is a brochure with no witnesses. Kleio, which **also refuses attribution**, has 20 written 5★ because Mathias sat on Slack and two-hour calls (ZEDE Paris / Gentleman’s Gazette / MYYK — LetsMetrix + getkleio.com testimonial block). That is the bar.

**If you will not run these scripts this week, do not write more positioning copy.** Copy without interviews is how you stay at 0.

---

## 1. Method (non-negotiable)

Adapted from Rob Fitzpatrick, *The Mom Test* (publicly summarized: talk about **their past**, not your idea). Practitioner recap used this wave: https://www.koji.so/blog/mom-test-customer-interviews-2026 — `MARKET_REPORT` on adoption, not a Mcfly study.

**Banned questions (they produce polite lies):**
- “Would you use a cash MER desk?”
- “Do you think anti-attribution is important?”
- “Would you pay $39?”
- “Is Total ROAS a good name?”
- Anything that starts with a Mcfly demo.

**Allowed questions:** specific last-Monday / last-month events, tools they already pay for, workarounds they already built, fights they already had, numbers they already put in a board pack.

**What counts as a signal (commitments, not compliments):**

| Signal | Counts | Does not count |
| --- | --- | --- |
| Money already spent | TrueProfit $35+ · TW $219+ · Polar $750 · SyncWith $4.99 · agency hours | “I’d pay for that” |
| Time already spent | Weekly Sheet, Looker connectors (Community 134251), 2-hour Kleio onboarding | “I’d try it” |
| Intro | “I’ll put you on a call with our controller / media buyer” | “Send me a link” |
| Data | They paste last week’s spend+sales on the call | They watch SAMPLE Harbor Home Co |
| Calendar | Recurring Monday 20-min | “Keep me posted” |

**How to open (do not pitch):**  
“I’m trying to understand how Shopify brands close the week when Ads Manager and Admin disagree. I’m not selling on this call. Can I ask what you actually did last Monday?”

**How to close:** one commitment ask (see §7). Then shut up.

**Recording:** ask. Notes in their words. Tag each answer with persona P1–P6 from [`PERSONAS.md`](./PERSONAS.md).

**Shopify Community / Reddit hygiene:** if you later post help, disclose you built Mcfly. Community 643974 and AdsX first-100 both say: help for weeks, mention once, disclose always. `EVIDENCE`

---

## 2. Script A — Owner-operator / in-house media buyer (P1 + P2)

**Who:** founder who still runs ads, or hired buyer who lives in Ads Manager.  
**Length:** 25–35 minutes.  
**Where they talk publicly:** r/shopify 1rpjuk0 · r/PPC 1u81q7r · 1pqv5kh · 1r2pvgy · Community 134251 · 657805 · 588628.

### A0. Filter (90 seconds)

If they spend **$0** on ads and have no offline/retainer spend, this is the wrong script. Thank them. Do not force a MER conversation onto a wholesale-only shop.

Ask: “Roughly — last month, did you spend money to get customers (ads, agency, affiliates, billboards, anything)?”  
If no → Script C (finance) only if they have a books problem; else end.

### A1. Last Monday (the only scene that matters)

Ground: Mcfly’s own site sells a “Monday” ritual (`https://mcflyads.com/product`). Community 657805: spreadsheets “always a week behind.” Better Reports sells scheduled email.

1. **“Walk me through last Monday morning. What did you open first — Shopify, Meta, Google, a Sheet, Slack, something else?”**  
   *Listen:* order of tabs = religion. If Ads Manager is first, you are talking to P2 (WeTracked kill shot: “I do not have to use another dashboard” — isella, https://apps.shopify.com/wetracked-io-connect). If Shopify payouts / a P&L app is first, you are closer to P1/P4.

2. **“What number did you need before you changed spend — or did you change spend without a number?”**  
   *Listen:* “ROAS” (platform) vs “did we make money” (profit) vs “blended” (MER). Do not correct them.

3. **“Show me, if you can, the tab or screenshot you actually used. I don’t need the dollars.”**  
   *Commitment test.* If they refuse to show even a redacted Sheet, they are being polite, not in pain.

### A2. The discrepancy (do not preach)

Ground: r/shopify 1rpjuk0 — “The dashboard discrepancy between Meta and [Shopify] drives everyone crazy, it will never sync up.” r/PPC 1u81q7r — scaled the wrong campaigns for months.

4. **“When did Meta and Shopify last disagree by enough that you noticed? What did you do that day?”**  
   *Good answer:* paused a campaign, emailed the agency, built a Sheet, bought TW/TrueProfit, yelled.  
   *Polite lie:* “Yeah that happens, we just know.”

5. **“Who won the argument — Ads Manager or the till? Who had to eat it?”**  
   *Listen for power:* founder forces cash; buyer forces platform; nobody decides (chaos).

6. **“Did you ever scale a campaign that looked good in-platform and then the bank didn’t move?”**  
   Ground: r/PPC 1u81q7r. If yes, ask for the month and the rough miss. That story is the listing headline they will write if Mcfly ever earns a review.

### A3. The current stack (money already leaving)

7. **“What do you pay for, today, that is supposed to solve this? App Store apps, TW, Polar, TrueProfit, Kleio, Sheets connectors, an agency retainer — list them.”**  
   Write dollars if they offer. Do not suggest Mcfly as a replacement yet.

8. **“What did you uninstall in the last year? Why?”**  
   Ground: r/shopify 1h27sj3 (TrueProfit bugs → Finaloop/Taxomate); Kleio reviews “goodbye TripleWhale”; BeProfit 1★ zombie $720/year (Adrienne Landau). Uninstalls are more honest than installs.

9. **“If I took away every paid analytics app tomorrow, what would you still do on Friday?”**  
   *Listen:* the Sheet is the real product. Mcfly must beat **that**, not TW.

### A4. Costs they mentally include (religion stress test)

Ground: Community 657805 — “Revenue is native, true net profit has to be assembled.” Community 588628 — “always missing something.” TrueProfit GowiLab — “must need to see how much you're actually making in profit.”

10. **“When you say ‘we were profitable last week,’ which costs are in that sentence — COGS, Shopify fees, shipping labels, payment fees, agency retainer, creative, software, refunds, VAT?”**  
    Tick them. The list **is** the product they will compare you to. Mcfly today: typed margin %. `CURRENT_RELIGION` is thinner than this list. `RESEARCH_OPTION`: assemble + flag incomplete (RELIGION_FLEX R7).

11. **“Do you pull **total** ad spend or only the spend the platform says is attributed?”**  
    Ground: Community 588628 warning — attributed-only understates cost. If they don’t know the difference, they are not your cash-desk buyer yet.

12. **“Billboards, podcasts, retainers, affiliates, Amazon ads — do any of those exist in your mix, and where do they live today?”**  
    This is Mcfly’s wedge (`CURRENT_RELIGION`). If the answer is “no, just Meta/Google,” Kleio/TrueProfit already win on auto-sync. Do not pretend the wedge applies.

### A5. Native Admin (the free enemy)

Ground: Community 134251 — “Shopify definitely doesn’t measure the spend.” Polar 2026 plan table: no ad-spend ingest on any plan — https://www.polaranalytics.com/post/shopify-attribution-models-explained-which-one-should-you-use. Help Center: marketing activity “Cost” exists for **Shopify-created** ads, not Meta/Google/billboards — https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/marketing-performance.

13. **“Have you tried Shopify’s ‘Sales attributed to marketing’ as the weekly number? What broke?”**  
    *Listen:* numbers move after 30 days (Community 180915); no spend; Basic plan may not even show sales-attributed (Polar table — `VENDOR` but consistent with plan gating).

14. **“If Shopify shipped spend-next-to-sales tomorrow, what would you still buy?”**  
    Honest kill test for Mcfly. If the answer is “nothing” or “still TrueProfit for COGS,” write it down. That is the real TAM.

### A6. Commitment (only if pain was specific)

15. **“Would you paste last week’s Meta+Google totals and let me compute sales÷spend with you on a shared screen — 15 minutes, this week?”**  
    If no → they were being nice.  
    If yes → that person is a design partner. Do **not** ask for a review on this call (policy). See [`FIRST_CUSTOMERS_PLAYBOOK.md`](./FIRST_CUSTOMERS_PLAYBOOK.md).

---

## 3. Script B — Agency / multi-brand operator (P3)

**Who:** media agency, Shopify partner agency, or in-house pod running ≥3 stores.  
**Length:** 30–40 minutes.  
**Public homes:** r/PPC 1qgb8mg ($200k+/mo clients, Sheets blended ROAS, 2-week pause tests); Polar “one view across brands”; SyncWith affiliate-sheet reviews; BeProfit multi-store 4★; TW founder claim agencies ≈ 1/3 revenue (Hampton 2023 — `FOUNDER_RETELL`).

### B1. The Monday pack

1. **“How many client scoreboards do you produce this week, and in what — Slides, Looker, Sheets, TW, Polar, Notion?”**  
   Count artifacts. The artifact **is** the product (Better Reports 1,199 reviews exist because of scheduled reports).

2. **“What is the one number you are willing to put in a client Slack that you can defend if they open Ads Manager?”**  
   If they say platform ROAS, Mcfly is a fight. If they say blended / MER / contribution, you have a shot.

3. **“Walk me through the last time a client forwarded a Meta screenshot that contradicted your report. What did you send back?”**  
   Ground: r/PPC 1qgb8mg — ignore platform attribution; pause tests. Steal their reply email. That copy belongs on mcflyads.com, not a sermon.

### B2. Tool tax

4. **“Per client, what do you pay for measurement — TW seat, Polar, Kleio, TrueProfit, Supermetrics, SyncWith, your own time?”**  
   Polar listing floor $750 GMV-tax is **agency-hostile**. Kleio $29 unlimited users is **agency-bait**. Mcfly $39 **per store** with no agency SKU is worse than Kleio on the one persona CURRENT_RELIGION fits ([`PERSONAS.md`](./PERSONAS.md) P3).

5. **“Have you ever installed a tool on a client store that they never used, and the invoice kept going?”**  
   Ground: BeProfit 1★ Adrienne Landau — $720/year never used. Agencies remember this. Your cancel path is a sales objection. See [`OBJECTIONS.md`](./OBJECTIONS.md) O-BILL.

6. **“If a store has billboards or a monthly creative retainer, where does that spend go in your model today?”**  
   Mcfly wedge. If they already have a “offline” tab in Sheets, you are replacing a cell, not a religion.

### B3. Incrementality vs MER

Ground: r/PPC 1qgb8mg pause tests; Polar Chicory review praises MTA + incrementality; Kleio FAQ refuses attribution on purpose — https://getkleio.com/

7. **“Do you run holdouts / pause tests, or do you only use blended?”**  
   If they run pause tests, Mcfly allocation (`sales ∝ spend` in `packages/mer-core/src/allocation.ts`) will look stupid. Disclose or don’t advise. `RESEARCH_OPTION` R8.

8. **“Would you let a $39 desk be the **client-safe** number while you keep TW/Polar for the buyer?”**  
   Overlay sale (SYNTHESIS S1/S5). If they say “clients won’t pay for two,” you lose on money. If they say “I need a number finance won’t laugh at,” you win on real problem.

### B4. Commitment

9. **“Name one client where the Sheet is late every week. I’ll sit with your analyst and close **their** last 14 days — no listing, no review ask.”**  
   One named client > ten “interested” agencies.

10. **“If that close works, will you intro two more operators in your Slack?”**  
    Intros are the TW Twitter-DM equivalent for 2026. AdsX: one warm agency > 100 cold emails — https://www.adsx.com/blog/shopify-app-marketing-first-100-installs `MARKET_REPORT`

---

## 4. Script C — Finance / controller / fractional CFO (P4)

**Who:** controller, bookkeeper, fractional CFO, founder who “is” finance.  
**Length:** 35–45 minutes. They will punish vague metrics.  
**Public homes:** Community 577364 · 657805 · TW 1★ Kove Footwear VAT · A2X listing · Eightx Shopify-CFO playbook https://eightx.co/blog/cfo-for-shopify-brands · cfoexpertise interview questions https://cfoexpertise.com/cfo-interview-questions/

Eightx (fractional CFO firm; treat metrics as **practitioner**, not Mcfly research): they tell brands to use **blended CAC**, **MER = revenue / total marketing spend**, **blended ROAS**, LTV:CAC, CAC payback — and **not** platform ROAS. That is the language. Use it.

cfoexpertise screens CFO hires with: contribution margin line-by-line; which costs get stripped before “profit”; LTV by cohort not blended; cash vs profit. Steal the **questions**, not their retainers.

### C1. Definitions before tools

1. **“Which Shopify sales field is ‘revenue’ in your board pack — total sales, net sales, after returns, after tax, after gift cards?”**  
   Mcfly live SAMPLE says “Shopify Total Sales after returns.” Listing says “store sales.” If they flinch, you are underspecified. `RESEARCH_OPTION` A3 finance defs.

2. **“VAT / sales tax — in or out of the revenue you show the CEO?”**  
   Ground: Kove Footwear 1★ on TW (2026-07-06) — VAT included in revenue. This is a fireable error. If Mcfly cannot toggle it, do not sell to EU/UK finance.

3. **“When an order refunds in month 2, which month’s MER / profit does it hit?”**  
   Ground: Community 657805 refunds reopening orders; Kleio review Gentleman’s Gazette — refunds attributed to original order (LetsMetrix). Finance has a preferred clock. Ask before you invent one.

### C2. Assembly vs theater

4. **“Walk me through how last month’s contribution margin was assembled. What was still a guess?”**  
   Ground: Community 657805 contribution-margin-first; “cost incomplete” preferred to fake precision. If they want a **flag**, Mcfly typed % is an insult.

5. **“Do you reconcile Shopify payouts to the bank / QB / Xero / NetSuite? With what?”**  
   If A2X/Taxomate/Finaloop — Mcfly is **not** that job. `OUT_OF_SCOPE`. Sell export definitions, not journals. Polar/TrueProfit also don’t replace A2X (Price Geek FAQ says this explicitly — https://www.thepricegeek.com/profit-analytics/best-shopify-profit-tracker/).

6. **“What number are you willing to sign — MER, contribution after marketing, net profit, cash?”**  
   Eightx stack: all of them, different jobs. If they only sign net profit, you are in TrueProfit/Kleio’s house.

### C3. Governance

7. **“Who is allowed to raise spend, and what number do they have to beat?”**  
   P5 overlay. If there is no governor, MER is a poster. If there is a governor, Mcfly can be the lock.

8. **“Have you ever killed a channel because the attribution tool kept crediting it after you paused?”**  
   Kleio FAQ claims this pattern and links “an example” — `VENDOR_CLAIM`. Still a useful question. If they nod, they are in Kleio’s religion, not TW’s.

### C4. Commitment

9. **“Send me (redacted) last month’s pack page that has the marketing number. I’ll mark where Mcfly would agree, where it would disagree, and where it is silent.”**  
   A markup of **their** PDF is the enterprise demo. SAMPLE Harbor Home Co is a toy.

10. **“If the markup is useful, will you put the formula in the appendix of next month’s pack as a one-line recon?”**  
    That is the Polar RSVP-Paris motion: “I now use Polar to report to our board members” — https://www.polaranalytics.com/case-studies/rsvp-paris `VENDOR_CASE`. Mcfly needs **one** such sentence in the wild. Zero exist.

---

## 5. Script D — 12-minute listing / trial intercept (not a research interview)

Use only **after** install, when they have **one computed week**. This is a sales call, not Mom Test.

Ground: Shopify — request a review at the end of a successful workflow, not at first open. https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews  
BigMoves: gate by eligibility, not sentiment; never ask for stars; never incentivize. https://www.bigmoves.marketing/blog/get-more-shopify-app-reviews-without-breaking-shopifys-rules-guide

1. “What number did you expect to see?”  
2. “What’s still missing for this to replace your Monday Sheet?”  
3. “Who else in the company needs this number?”  
4. Neutral: “If you’ve used it, Shopify lets merchants leave a review — here’s the link. No pressure, no discount.” Deep link form: `https://apps.shopify.com/mcfly-analytics-public#modal-show=WriteReviewModal`

If they have **not** computed a week, **do not ask**. You will get silence or a 1-star “empty app.” That is how 0 stays 0.

---

## 6. Question bank by problem (cheat sheet)

Use when a call drifts. Each maps to [`PROBLEM_BANK.md`](./PROBLEM_BANK.md).

| # | Problem | Ask | Evidence |
| --- | --- | --- | --- |
| 1 | Net profit | “Which costs were you still guessing last close?” | Community 657805 · TP 899 |
| 2 | Pixel/CAPI | “Do you need the algorithm fed, or the till explained?” | WeTracked isella · Elevar $225 |
| 3 | Spend next to sales | “Where does Meta spend sit next to Shopify sales today?” | Community 134251 |
| 4 | Platform ≠ till | “Last time you scaled the wrong thing — what was the miss?” | r/PPC 1u81q7r |
| 5 | Reports / email | “What artifact leaves the building on Monday?” | Better Reports 1199 |
| 6 | LTV/CAC | “Is CAC total-spend/new-customers or platform CAC?” | Eightx · Lifetimely 535 |
| 7 | Passback | “Does any tool write back into Meta today?” | Apex / Sonar / Elevar |
| 9 | GL recon | “Who ties payouts to the bank?” | A2X · Community 577364 |
| 10 | Offline | “What spend never appears in Ads Manager?” | Mcfly hero · Kleio has no billboard religion |
| 11 | Allocation | “Do you advise cuts from blended, or from tests?” | r/PPC pause tests |
| 12 | Multi-store | “One login or 12?” | Polar · Metorik · Kleio unlimited users |
| 14 | AI/MCP | “Does anyone already pull P&L into Claude?” | Kleio Trek Light / Hummii |
| 15 | Ritual | “If the email didn’t arrive, who would notice?” | Better Reports · Polar Slack |

---

## 7. Commitment ladder (end every call on one rung)

From weakest to strongest. Climb one rung per person. Polite “cool product” is **below** rung 1.

1. They show a redacted Sheet or Ads Manager vs Admin screenshot.  
2. They paste last week’s spend+sales and sit through a 15-minute compute.  
3. They intro the buyer **or** the controller (the other brain).  
4. They install on a **real** store (not a partner test store).  
5. They put the number in a client Slack or board appendix.  
6. They remain installed past trial (7 days today — structurally short vs Kleio/TP 14).  
7. They leave a review **unprompted-for-stars** after a successful week.

Mcfly is stuck at rung **0**. Kleio’s visible reviews sit at 5–7 (MCP in Claude, daily P&L, goodbye TW). That gap is not a feature gap. It is a **calendar** gap.

---

## 8. Anti-patterns (you will be tempted)

| Anti-pattern | Why it dies | Evidence |
| --- | --- | --- |
| Demo SAMPLE Harbor Home Co first | It’s fiction. Finance smells it. | Listing forbids testimonials anyway (req 4.3.7) |
| Argue attribution theology | They have heard Kleio’s FAQ already, better written | getkleio.com “Why don’t you offer attribution?” |
| Ask “would you pay $39?” | They will say yes and never install | Mom Test |
| Interview only other developers | X/Twitter Shopify-app scene ≠ merchants | AdsX first-100: build-in-public ≠ installs |
| Promise LTV/Goals if not shipped | Listing already claims them; repo `APP_FEATURES.md` lags | RESEARCH_LOG contradiction |
| Offer a discount-for-review | Policy + 2026 crackdown | TSC · Shopify manage-reviews |
| Talk to people who don’t spend | No denominator | NICHE_MER |

---

## 9. How many calls before you are allowed to change copy

Research judgment, not a law:

- **0 calls:** you may not change listing theology. You may only fix lies (LTV claimed vs shipped).  
- **5 calls with rung-2 commits:** you may rewrite the **first 50 words** of the listing to match **their** Monday sentence.  
- **10 calls spanning P2 + P3 + P4:** you may pick S1 vs S2 vs overlay (see [`SYNTHESIS.md`](./SYNTHESIS.md)).  
- **0 reviews after 10 rung-4 installs:** the product, not the script, is wrong. Kill or bend R3/R7 (OAuth spend, assembled costs).

---

## 10. Outreach one-liners (personal, not spray)

AdsX: 20 researched emails/week, open with a store-specific observation, ask for a **reply** not an install. Community 643974: “Ten personal messages will get you more installs than waiting for the algorithm.”

**Operator (after you actually looked at their ads):**  
“Saw you’re running Meta + Google on [store]. Shopify still won’t put that spend next to sales (Community thread on this is years old). I’m mapping how operators close that gap on Mondays — 20 minutes, no pitch. Worth it?”

**Agency:**  
“Do you still rebuild a blended ROAS Sheet for each client because Polar/TW is a GMV tax? I want the ugly version of that workflow, not a demo.”

**CFO:**  
“When Meta ROAS and Shopify net sales disagree in the pack, which number do you sign? I’m collecting definitions, not selling software on this call.”

If you cannot name something **specific** about their store, do not send the email. Spray is how you burn the domain and still sit at 0 reviews.

---

*Owner: research agent. Founder runs the calls. Scripts without calendar invites are literature.*
