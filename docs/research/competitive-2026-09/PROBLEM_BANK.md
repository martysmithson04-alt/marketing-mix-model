# Problem bank — ranked by public willingness-to-pay signals

**Date:** 2026-09-09  
**Method:** Rank problems by *observable* WTP proxies, not by Mcfly theology.

**WTP proxies we allow (no invented $):**
1. Live App Store **review count** + **paid price shown** (people paid and stayed long enough to review).
2. **Free-but-massive** review count (love / ease; money is indirect — data, upsell, ads).
3. Public forum **repeat complaints** (Community + Reddit).
4. Vendor SKUs that exist because someone buys them (Amazon add-on $75, Elevar $225+, Polar $750, A2X settlement SKUs).

**We do not use:** imagined TAM, “every store has this pain,” unpublished install counts, Mcfly waitlist (none in this repo).

Religion tags: `CURRENT_RELIGION` = Mcfly already claims this. `RESEARCH_OPTION` = adjacent or conflicting. `OUT_OF_SCOPE_TODAY` = real, paid, not Mcfly.

---

## Ranked problems

### 1. “I cannot see true net profit after COGS, fees, shipping, and ads”

| | |
| --- | --- |
| **WTP signal** | **Strongest paid cluster in the adjacent market.** TrueProfit 5.0 / **899** from $35; Lifetimely 4.9 / **535** free→$49–$299; BeProfit 4.5 / **202** from $49; Metorik 5.0 / **48** from $25. Community 657805 (335 views) + 588628. |
| **Who** | P1 founder, P4 finance, some P2 |
| **What they pay for** | Autopilot costs + ad spend **sync**, product-level profit, P&L, LTV |
| **Mcfly today** | Break-even from a **typed margin %**. No COGS, no fees, no shipping, no SKU profit. |
| **Tag** | `RESEARCH_OPTION` (expand) vs `CURRENT_RELIGION` (margin % is enough) |
| **Evidence** | https://apps.shopify.com/trueprofit · https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics · https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805 |
| **Risk if we take it** | Feature race against 899-review TrueProfit. Historical COGS, VAT, refund reopen — Community 657805 lists the landmines. |
| **Risk if we refuse** | $39 for a thinner job than $35 TrueProfit. High churn after trial once they notice. |
| **Four scores** | Money high · Love high · Ease medium (needs cost data) · Real problem **#1** |

---

### 2. “My Meta/Google pixel is broken / iOS ate my conversions / I need CAPI”

| | |
| --- | --- |
| **WTP signal** | **Highest review gravity in Mcfly’s own “more like this” row.** Clarity 4.6 / **2,125** Free; Parkour 4.9 / **191** Free; WeTracked 4.8 / **125** Free-to-install + external; Analyzify 4.7 / **313** from $145; Elevar 4.7 / **168** from $225. Shopify merchandises Mcfly **here**, not in Polar’s aisle. |
| **Who** | P2 media buyer, P1 founder who lives in Ads Manager |
| **What they pay for** | Event match quality, server-side, “ROAS went up” stories (WeTracked 5★ “ROAS got up 30%” — **reviewer claim**, not a study) |
| **Mcfly today** | Explicitly **refuses**. Listing: “No pixels. No path credit.” |
| **Tag** | `CURRENT_RELIGION` refuse · `RESEARCH_OPTION` add pixel or partner |
| **Evidence** | https://apps.shopify.com/mcfly-analytics-public (adjacency) · https://apps.shopify.com/parkour-pixel · https://apps.shopify.com/wetracked-io-connect · https://apps.shopify.com/gtm-datalayer-by-elevar |
| **Risk if we take it** | Compete with **free**. Support is EMQ/debug hell. Brand becomes theater. |
| **Risk if we refuse** | Discovery stays in the pixel cluster with **0 reviews**. Buyers install Parkour, not Mcfly. |
| **Four scores** | Money via upsell uncertain · Love very high if free · Ease high · Real problem for **algorithm**, not for cash |

---

### 3. “Shopify Analytics cannot put ad spend next to sales / I need blended ROAS or MER”

| | |
| --- | --- |
| **WTP signal** | **Theologically Mcfly’s home. Commercially under-owned as a standalone paid app.** Community 134251: Shopify staff/community confirm Admin **does not ingest spend**. r/PPC and r/shopify treat blended MER as the *honest* number — usually in **Sheets**, not a $39 app. Polar lists MER as one KPI among many. No large-review App Store specialist for “cash MER only” was found this run. |
| **Who** | P2, P3, P4, literate P1 |
| **What they pay for** | Today: they pay Polar/TW/TrueProfit and *get MER as a side effect*, or they pay SyncWith $4.99 and build it. |
| **Mcfly today** | `CURRENT_RELIGION` core. Listing hero. |
| **Tag** | `CURRENT_RELIGION` |
| **Evidence** | https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4 · https://www.reddit.com/r/PPC/comments/1pqv5kh/how_are_you_handling_ad_attribution/ · https://apps.shopify.com/mcfly-analytics-public |
| **Risk if we stay narrow** | Correct problem, **insufficient surface** to generate reviews vs profit/pixel apps. |
| **Risk if we blur it** | Become a worse TW. |
| **Four scores** | Money medium if packaged with auto-spend · Love medium (nerds) · Ease low (paste) · Real problem **real but already DIY** |

---

### 4. “Meta ROAS and Shopify revenue will never match — I scaled the wrong campaigns”

| | |
| --- | --- |
| **WTP signal** | Recurring r/PPC / r/shopify. Suites exist to sell a **third number**. Northbeam ~$1.5k floor MARKET_REPORT; TW GMV-tax; Polar pixel+MTA. Commenters also say the $0 version is a weekly spend-vs-sales sheet. |
| **Who** | P2, P5, burned P1 |
| **What they pay for** | Either (a) a court of appeal (Northbeam/Polar) or (b) the courage to ignore platforms and use MER. |
| **Mcfly today** | Answers (b). Does not visualize the **gap** (Ads Manager claim vs till) as a first-class object — site has “Platform variance” link in pricing footer; treat as marketing page, not verified shipped feature. |
| **Tag** | `CURRENT_RELIGION` (cash) · `RESEARCH_OPTION` (claims-vs-cash recon card) |
| **Evidence** | https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/ · https://www.reddit.com/r/shopify/comments/1rpjuk0/best_way_to_track_meta_ads_roas_in_shopify/ |
| **Risk** | Showing the gap requires **pulling platform-reported conversions** (API or paste). That’s a toe into attribution theater even if you label it “their claim, not truth.” |
| **Four scores** | Money high at mid-market · Love high if the gap is visceral · Ease medium · Real problem **acute** |

---

### 5. “I need custom reports / exports / Sheets because Admin reports are wrong or incomplete”

| | |
| --- | --- |
| **WTP signal** | Better Reports **5.0 / 1,199** $19.90–$299.90 (Shopify-plan-priced) — https://apps.shopify.com/betterreports. Report Pundit cited 5.0 / **2,026** on TrueProfit’s “more like this.” SyncWith 4.5 / 10 at $4.99. r/shopify 1p1fogj UTMs+Sheets. |
| **Who** | P3 agency, P4 finance, ops |
| **Mcfly today** | Spend CSV **in**. Weak **out**. No scheduled email, no Sheets add-on shipped (MASTER_PLAN Phase 5). |
| **Tag** | `RESEARCH_OPTION` (Sheets companion / scheduled Monday pack) |
| **Evidence** | https://apps.shopify.com/betterreports · https://apps.shopify.com/syncwith |
| **Risk** | Become a report builder. Better Reports has a **complimentary custom report service** — that’s why they have 1,199 reviews. |
| **Four scores** | Money medium · Love high · Ease high if we email a PDF · Real problem high |

---

### 6. “I need LTV, CAC, cohorts — not just this week’s ROAS”

| | |
| --- | --- |
| **WTP signal** | Lifetimely identity (4.9/535). TrueProfit LTV on Basic. Polar listing LTV/cohorts. TW Foundation: cohort + SQL $219+. Mcfly listing **claims** “LTV/Acquisition (Cash CAC · LTV:CAC)” as a paid-plan add. |
| **Who** | P4, P5, subscription brands (Lifetimely works with Recharge/Skio) |
| **Mcfly today** | Listing claims it. Repo `APP_FEATURES.md` does not list LTV as shipped. **Verify product vs listing.** |
| **Tag** | `CURRENT_RELIGION` if actually shipped · else listing-risk |
| **Evidence** | https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics · https://apps.shopify.com/mcfly-analytics-public |
| **Risk** | Cash CAC using **total spend / new customers** is honest and easy. Full cohort LTV is a different product (Lifetimely’s decade). |
| **Four scores** | Money high · Love high for subscription · Ease low (needs order history + definition) · Real problem high |

---

### 7. “I need the algorithm fed (passback / CAPI / Apex / Sonar) so I can spend more”

| | |
| --- | --- |
| **WTP signal** | This is how suites **justify** $219–$1,500. Northbeam Apex docs: https://docs.northbeam.io/docs/northbeam-apex. TW Sonar on Foundation. Polar “Advertising Signals.” Elevar $225+ is *only* this job. |
| **Who** | P2, P5 |
| **Mcfly today** | Refused. |
| **Tag** | `CURRENT_RELIGION` refuse · `RESEARCH_OPTION` partner or lightweight CAPI |
| **Evidence** | Apex docs · Polar listing “enriching ads for better ROAS with server-side attribution” · Elevar listing |
| **Risk** | Capital, partnerships, Meta review. Also: you start optimizing **their** model. |
| **Four scores** | Money highest ARPU · Love from buyers · Ease low to build · Real problem = “make ads cheaper,” not “know cash” |

---

### 8. “Heatmaps / replays / why won’t they checkout”

| | |
| --- | --- |
| **WTP signal** | Clarity **2,125** Free. Lucky Orange 4.7/878 (Clarity “more like this”). Not Mcfly’s job. |
| **Tag** | `OUT_OF_SCOPE_TODAY` |
| **Evidence** | https://apps.shopify.com/microsoft-clarity |
| **Note** | Shopify thinks Mcfly is adjacent. That is a **category error** Mcfly must correct in listing copy, or exploit by staying visible in that rail. |

---

### 9. “Shopify payouts do not match QuickBooks / Xero / NetSuite”

| | |
| --- | --- |
| **WTP signal** | Dedicated category (A2X). Community 577364. r/shopify Finaloop / Taxomate. Eightx 2026 review: worth it above ~$500K GMV MARKET_REPORT. |
| **Who** | P4, P5 finance |
| **Mcfly today** | None. |
| **Tag** | `OUT_OF_SCOPE_TODAY` as GL · `RESEARCH_OPTION` as **export definitions** finance can journal |
| **Evidence** | https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364 · https://support.a2xaccounting.com/en/articles/7211660-connecting-a2x-to-netsuite |
| **Four scores** | Money high, different buyer · Love high when it works · Ease low · Real problem high |

---

### 10. “Offline / billboard / retainer / podcast / CTV spend is invisible”

| | |
| --- | --- |
| **WTP signal** | Weak as a **standalone** paid app. Strong as a **wedge line** on Mcfly’s live listing (“including billboards”). Northbeam MARKET_REPORT writeups mention offline-heavy mixes as a fit reason. Polar/TW are paid-media OAuth first. |
| **Who** | P3, P5, brands with agency retainers |
| **Mcfly today** | `CURRENT_RELIGION` differentiator. Paste any named channel. |
| **Tag** | `CURRENT_RELIGION` |
| **Evidence** | https://apps.shopify.com/mcfly-analytics-public hero · https://mcflyads.com/product channel list (billboard, retainer, affiliate, Amazon…) |
| **Risk** | Tiny search volume vs “Facebook pixel.” Good **story**, bad **discovery keyword**. |
| **Four scores** | Money niche · Love from the few who have the problem · Ease high (paste) · Real problem real for a minority |

---

### 11. “Allocate next dollar / cut the loser / protect break-even”

| | |
| --- | --- |
| **WTP signal** | Weak as standalone. Mcfly lists “Spend Allocation (7/14/28).” Repo `allocation.ts` is rules-based and, without per-channel sales, **assumes sales ∝ spend** — which is circular. Suites sell Moby/Apex as the allocator. |
| **Who** | P2 (if they trust it), P1 (if simple) |
| **Mcfly today** | `CURRENT_RELIGION`. Auditability is the honest part. The math is a heuristic. |
| **Tag** | `CURRENT_RELIGION` · `RESEARCH_OPTION` incrementality-lite (pause tests) |
| **Evidence** | Repo `packages/mer-core/src/allocation.ts` assumedSalesForChannel · r/PPC 1qgb8mg lift-test practice |
| **Risk** | Advising cuts from spend-share efficiency **without** channel sales is how you look stupid to a media buyer. |
| **Four scores** | Money as a feature, not a product · Love if it matches gut · Ease high · Real problem medium |

---

### 12. “Multi-store / Amazon + Shopify / wholesale + DTC”

| | |
| --- | --- |
| **WTP signal** | Polar listing omnichannel; Lifetimely Amazon +$75; Metorik multi-store; BeProfit Plus $249 unlimited shops. |
| **Who** | P3, P5, P6 |
| **Mcfly today** | Per-store $39. No portfolio. |
| **Tag** | `RESEARCH_OPTION` |
| **Evidence** | https://apps.shopify.com/polar-analytics · Lifetimely pricing block · https://apps.shopify.com/metorik |
| **Four scores** | Money high ARPU · Love high for agencies · Ease hard · Real problem high for a subset |

---

### 13. “Creative reporting — which ad actually worked”

| | |
| --- | --- |
| **WTP signal** | TW Automate $749 listing includes “Creative generation.” TW blog sells Creative Analytics as a TW-vs-Polar win. Not a huge standalone App Store category in this fetch. |
| **Who** | P2, P5 |
| **Mcfly today** | None. |
| **Tag** | `OUT_OF_SCOPE_TODAY` |
| **Four scores** | Money inside a suite · Love for buyers · Ease low · Real problem real, different product |

---

### 14. “AI that does the job / Slack agent / MCP into ChatGPT”

| | |
| --- | --- |
| **WTP signal** | TW Moby is the listing hero. Polar MCP on $750 Core. TrueProfit MCP to ChatGPT/Claude on listing. Lifetimely “AI Profit Agent” + Slack. TW 1★: AI **credits** extra; 5★: “give more warning about AI usage limitations.” |
| **Who** | P2, P5, trend-following P1 |
| **Mcfly today** | None. Course $79 is human religion. |
| **Tag** | `RESEARCH_OPTION` (thin: “explain this Monday number”) not Moby |
| **Evidence** | https://apps.shopify.com/triplewhale-1 · TrueProfit listing · TW reviews 2026-07-20 and 2026-07-06 |
| **Risk** | Metered AI is a 1-star factory. |

---

### 15. “Monday close / board pack / ritual”

| | |
| --- | --- |
| **WTP signal** | Soft. Mcfly site sells a 10-minute ritual. Better Reports scheduled email is the **paid** version of ritual. r/PPC weekly blended sheet is the DIY version. |
| **Who** | P1, P3, P4 |
| **Mcfly today** | Positioning, not proven habit. Kill criterion in MASTER_PLAN: partners won’t open weekly after 30 days. |
| **Tag** | `CURRENT_RELIGION` |
| **Evidence** | https://mcflyads.com/product · Better Reports “Schedule automatic reports” |
| **Four scores** | Money as retention, not acquisition · Love if the email is the product · Ease high · Real problem medium |

---

## Cross-tab: problem × Mcfly stance × what the market already sold

| # | Problem | Market winner (live) | Mcfly stance | Recommended research posture |
| --- | --- | --- | --- | --- |
| 1 | Net profit | TrueProfit / Lifetimely | Thin (margin %) | **Seriously consider** profit-lite |
| 2 | Pixel/CAPI | Free Parkour + paid Elevar | Refuse | Partner, don’t rebuild |
| 3 | Spend next to sales | Unowned standalone | Core | Keep, but **auto the spend** |
| 4 | Platform ≠ till | Suites + Sheets | Partial | Productize the **gap** |
| 5 | Custom reports | Better Reports / Report Pundit | Weak | Monday pack, not a builder |
| 6 | LTV/CAC | Lifetimely | Listing claims | Ship cash CAC or stop claiming |
| 7 | Passback | NB Apex / TW Sonar / Polar | Refuse | Only if selling mid-market overlay |
| 8 | Heatmaps | Clarity | Accidental neighbor | Fix listing adjacency with copy |
| 9 | GL recon | A2X | None | Export, don’t post journals |
| 10 | Offline spend | Mcfly wedge | Core | Keep as proof of cash religion |
| 11 | Allocation | Heuristic / Moby | Core | Don’t oversell |
| 12 | Multi-entity | Polar / Metorik | None | Agency SKU |
| 13 | Creative | TW | None | Ignore |
| 14 | AI OS | TW / Polar | None | Explain-the-number only |
| 15 | Ritual | Sheets + Better Reports | Positioning | Make the email the app |

---

## Willingness-to-pay heatmap (qualitative, sourced)

```
HIGH $          Northbeam court · Elevar CAPI · Polar warehouse
                TW Automate $749 · Polar $750
MED $           TW Foundation $219 · Analyzify $145 · Lifetimely M/L
                BeProfit $49–149 · TrueProfit $35–200
LOW $           Mcfly $39 · Metorik $25 · Better Reports $19.90
                SyncWith $4.99
$0 + LOVE       Clarity · Parkour · native Shopify reports · Sheets MER
```

**Mcfly is priced like a profit app and scoped like a spreadsheet ritual.** That is the core commercial contradiction.

---

## Founder implication (not a ship order)

If the goal is **maximum money + love + ease + real problems**, the evidence ranking is:

1. Solve #1 (profit assembly) **or** #3+#4 with **zero-paste spend** — otherwise $39 loses to TrueProfit.
2. Do not self-build #2; optionally **recommend** a pixel partner so P2 does not bounce.
3. Use #10 (billboards/retainers) as the **honest differentiator** against OAuth-only profit apps.
4. Treat #15 (Monday email) as the retention engine that Better Reports already proved with 1,199 reviews.

---

## Wave 2 problems (append)

### 16. “VAT/GST is inside the revenue number I scale on”

| | |
| --- | --- |
| **WTP signal** | TW 1★ Kove (NL); r/dropshipping 1s3mx43; Klar prices on **net after tax**; Taxomate EU VAT SKU |
| **Who** | P4 finance, EU/UK/AU founders |
| **Mcfly today** | Underspecified |
| **Tag** | `RESEARCH_OPTION` |
| **Evidence** | `DEEP_DIVE_INTERNATIONAL.md` · TW KB vs docs |
| **Four scores** | Money M · Love H (P4) · Ease M · Real **trust-kill** |

### 17. “Refunds, exchanges, and lookback move last month’s sales”

| | |
| --- | --- |
| **WTP signal** | Community 637409, 180915, 301853, 199943; Loop 4.6/442 |
| **Who** | Apparel ops + finance + media |
| **Mcfly today** | “After returns” on SAMPLE only |
| **Tag** | `RESEARCH_OPTION` |
| **Evidence** | `DEEP_DIVE_RETURNS_LTV_SUBS.md` |
| **Four scores** | Money M · Love H · Ease L · Real H |

### 18. “Subscription LTV and ad CAC live in two apps that do not join”

| | |
| --- | --- |
| **WTP signal** | Recharge 4.8/3118; Lifetimely 535; RCI 14 (LTV-only is weak) |
| **Who** | CPG / replenishment CMO |
| **Mcfly today** | Listing claims LTV |
| **Tag** | `CURRENT_RELIGION` claim · `RESEARCH_OPTION` to ship a split |
| **Evidence** | `DEEP_DIVE_RETURNS_LTV_SUBS.md` |
| **Four scores** | Money L–M · Love M · Ease L · Real M (subset) |

### 19. “I need a human or an email to close the week, not another login”

| | |
| --- | --- |
| **WTP signal** | Report Pundit 5.0/2026; Better Reports 1199; Kleio MCP-into-Claude daily report |
| **Who** | P1, P3, P4 |
| **Mcfly today** | Desk you remember |
| **Tag** | `RESEARCH_OPTION` (same as #15, now with RP evidence) |
| **Four scores** | Money M · Love H · Ease H · Real H |

### 20. “TW is a fighter jet; I wanted a bicycle”

| | |
| --- | --- |
| **WTP signal** | Community 588628; Kleio 20×5★ TW defections; r/PPC 1ohxwk6 |
| **Who** | P1 at ~$15–50k/mo |
| **Mcfly today** | Bicycle **without** gears (no auto spend, no P&L) |
| **Tag** | `CURRENT_RELIGION` wedge · `RESEARCH_OPTION` to actually be the bicycle (Kleio already is) |
| **Four scores** | Money M · Love H · Ease M · Real H |
