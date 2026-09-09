# Kleio vs Mcfly gap list — line by line

**Date:** 2026-09-09  
**Wave:** E  
**Mode:** RESEARCH ONLY. Public pages only. No invented installs, GMV, or “X% of merchants.”  
**Gap list:** `MCFY_GAP_MATRIX.md` §A (capability rows) plus the religion / four-score / problem-coverage sections that a founder would actually use.  
**Kleio live sources (fetched this wave):**

| Surface | URL | Fetched |
| --- | --- | --- |
| App Store listing | https://apps.shopify.com/kleio | 2026-09-09 LIVE |
| Marketing site | https://getkleio.com/ | 2026-09-09 LIVE |
| Metrics | https://getkleio.com/docs/getting-started/metrics | LIVE |
| Recommended setup | https://getkleio.com/docs/getting-started/recommended-setup | LIVE |
| Ad integrations | https://www.getkleio.com/docs/integrations/ad-integrations | LIVE |
| MCP | https://getkleio.com/docs/integrations/mcp-server | LIVE |
| COGS | https://getkleio.com/docs/costs/cogs-and-variable-costs | LIVE |

Wave A `COMPETITOR_CARDS.md` did **not** include Kleio. Wave B scored S1 with Kleio in the room. This file is the missing card **and** the gap audit.

---

## 0. Kleio, as publicly shipped (not as we wish they were)

### 0.1 Listing card (LIVE)

| Field | Kleio | Mcfly (control) |
| --- | --- | --- |
| Handle | [apps.shopify.com/kleio](https://apps.shopify.com/kleio) | [mcfly-analytics-public](https://apps.shopify.com/mcfly-analytics-public) |
| Price | **$29 / month**, one plan (“Everything”) | **$39 / month** |
| Trial | **14-day** | 7-day |
| Reviews | **5.0 / 20** · 100% 5★ (listing UI) | **0.0 / 0** |
| Launched | **February 19, 2025** | September 7, 2026 |
| Developer | Klosterport 9, 4., Aarhus C, 8000, **DK** | West Jordan, UT |
| Works with | AppLovin, GoAffPro, **Google Ads**, **Meta Ads**, ShipHero | *(none on listing)* |
| Categories | Analytics · Customer behavior · Marketing and sales · Visuals and reports | Marketing and sales · Visuals and reports |
| “More like this” | Clarity (4.6/2125 Free), WeTracked (4.8/125), Parkour (4.9/191 Free) | **Same rail** |

**Brutal line:** Shopify files Kleio and Mcfly in the **same pixel/heatmap cluster**. Kleio escaped 0 reviews. Mcfly has not. The rail is not destiny; the desk is.

### 0.2 Site claims (VENDOR_CLAIM unless noted)

From [getkleio.com](https://getkleio.com/) 2026-09-09:

- “$29/m for everything… unlimited users… unlimited orders… unlimited revenue.”
- Homepage counter: **364 stores · 47.4M+ orders · 1 in 3 on Shopify Plus** — **VENDOR_CLAIM**, not App Store. Do not repeat as Mcfly-measured fact. Listing does **not** print store count.
- Comparison table last checked **August 22, 2026**: TW $219–$4,199 · Lifetimely $79–$999 · Kleio $29. Kleio column: Attribution **✗ on purpose**.
- Setup: “You’re set up in 5 minutes.” Reviewer The Nerve Brand: “less then 5 mins” (listing).
- Founder: Mathias / @MattiSchroder; “10 years running ecom brands”; uses Kleio daily on own brands.
- Uninstall: “deletes everything we hold about your store… Not archived, not anonymised. Gone.”

Listing vs site contradiction to flag: listing plan says **“1,000,000 orders in database”**; site FAQ/plan says **unlimited orders**. Do not pick a side in public Mcfly copy.

### 0.3 What the docs actually specify (stronger than marketing)

**P&L waterfall** (metrics doc) — this is a *definition sheet*, not a vibe:

```text
Gross Sales
− Discounts
= Sales
− Returns + Return Fees
= Revenue          ≈ Shopify Total sales (tax-in)
− Tax
− COGS
= CM1
− Variable costs   (shipping, returns handling, payment, customs, fulfillment, other, agency % of spend)
= CM2
− Ad Spend
= CM3
− Fixed costs
= Net Profit
```

**Tax toggle:** Gross Sales → Revenue can be tax-in or tax-out. **Below Revenue, tax is always excluded.**

**Dual clock:**

- Default: **accounting / event date** (refund today hits today).
- Acquisition: **order-date** metrics `(O)` move refunds back to the order.
- Forecast: `E(CM3) (O)` models returns not yet observed (last 14 days, per-product history).

**Ad spend:**

| Platform | Connection | Data (docs) |
| --- | --- | --- |
| Meta | OAuth | Hourly campaign spend; last 13 months hourly, daily beyond |
| Google Ads | OAuth | Hourly campaign spend; permission = authenticating user’s access |
| TikTok | OAuth (Beta) | Hourly campaign spend |
| Snapchat | OAuth (Beta) | Hourly campaign spend |
| AppLovin | API key | Hourly spend, **no** campaign grain; 30-day backfill window |
| GoAffPro | API token | Daily affiliate commissions (cost, not media) |
| Pinterest | OAuth (Beta) | Campaign spend @ 06:00 / 12:00 / 18:00 shop time |
| Microsoft Ads | OAuth (Beta) | Same thrice-daily refresh |

**Meta token (docs, not gossip):** “Access tokens expire after **60 days** and cannot be auto-refreshed. You’ll need to reconnect manually… Kleio will notify you when your token is about to expire.”

**Spend filters (campaign-name contains):** Exclude · Include (mutex) · Exclude from new-customer calc · `kleio_allocate_nc_XX` in the campaign name · Exclude from online channel · Subscription campaigns. This is **not** MTA. It is operator-disclosed allocation of **spend**, including a PMax % split. Mcfly religion can live with disclosed spend splits. It cannot live with silent path credit. Kleio’s PMax tag is the former.

**COGS:** Shopify cost · Custom COGS (product/variant, date range, country, currency, quantity tiers) · Override-all % · Missing-data queue · Deleted-product costs · Fallback %.

**Variable costs:** Shopify Payments fees auto; everything else merchant-defined (per order, line, refund, weight, % of sales/COGS/shipping/spend).

**MCP:** `https://app.getkleio.com/api/mcp` — Claude Desktop / Claude Code / ChatGPT / any HTTP MCP. **Reads** P&L, products, LTV, cohorts, inventory. **Writes** product price/content/tags/status/channels/metafields/cost/weight. Setup help: paste rate cards / bank statements → create costs. Access-token revoke for leaked AI clients. “Analytics Playbook” shipped on the server.

**Attribution stance (FAQ, site + docs):** they refuse third-party MTA. Reasons: models are opinions; optimization stays inside the ad platform anyway; incentive to look different from Ads Manager; late conversions after ads are off. They **praise Meta’s optimizer**. This is **not** Mcfly’s “platforms are lying” voice. It is “platforms are lying *as a reporting court*, but they are the right *bidder*.” Close cousin. Different enemy.

### 0.4 Visible reviews (do not invent the rest)

Listing showed 20 reviews, 100% 5★. Visible bodies this fetch:

| Reviewer | Date | Tenure | What they actually praised |
| --- | --- | --- | --- |
| Trek Light (US) | 2026-08-12 | 5 months | MCP + Claude; left **Triple Whale**; price |
| EMME (US) | 2026-08-11 | 8 months | “Better than TW, cheaper than TW, $29, what do you have to lose?” |
| Hummii Snacks (US) | 2026-04-23 | ~2 months | Daily P&L pulse; MCP into a **scheduled daily report** |

Site republishes additional App Store quotes (MYYK, Njord Gear, ZEDE Paris, BLURRD, Joolca, Cancha, Rainier Watch, PawSafe, Gentleman’s Gazette, Agador’s, Watery.dk, etc.). Treat site-hosted quotes as **vendor-selected**. The three listing-visible rows are the ones we will defend.

**Pattern:** defection from TW/Lifetimely · founder Slack/calls · daily profit pulse · MCP as Monday artifact · price as the closer. **Not one visible review asks for a pixel or path credit.**

---

## 1. Capability matrix — Mcfly gap list × Kleio public × S1

Legend: **Ships** = documented or listing-claimed as current. **Partial** = exists in a weaker form. **No** = not found on public pages this wave. **Refuse** = they say they will not.

| # | Mcfly gap-list capability (`MCFY_GAP_MATRIX` §A) | Mcfly have | Kleio public | S1 Ring 1 (`S1_PRD_LITE.md`) | Who wins the row | Implication |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Period-matched sales ÷ spend | **Yes** (core) | **Ships** as blended / NC ROAS (aMER) on the dashboard mock + spend in the waterfall | Yes | Kleio (auto spend) | Mcfly’s theology is not unique. Kleio productized the *easy* version. |
| 2 | Break-even from margin | **Yes** (typed %) | **Ships computed** CM1/CM2/CM3 / net profit — BE is implicit in “did CM3 stay black” | Typed only | Kleio | Typed BE is a toy next to a waterfall. |
| 3 | Named offline / billboard / retainer | **Yes** (hero) | **Partial** — “Other Marketing” = fixed marketing (agency, banner ads) allocated into ad spend; no billboard religion | CSV/other remains | **Mcfly** (story) | Only durable wedge if operators with offline spend *exist and pay*. Wave A already called this tiny SEO. |
| 4 | Manual / CSV spend | **Yes** | **Partial** — ShipHero CSV of carrier rates; costs can be pasted via MCP; not positioned as the desk | Yes | Tie | CSV is table stakes. |
| 5 | Auto ad-spend OAuth | **No** (site forbids; MASTER_PLAN Phase 2) | **Ships** Meta + Google + 6 more | The S1 bet | **Kleio, today** | This is the row S1 spends a calendar year trying to tie. |
| 6 | Platform-claim vs till gap | Site footer only | **No public card.** Anti-MTA FAQ. They do **not** visualize Ads Manager revenue vs Shopify. | The S1 wedge (paste-first if policy) | **Mcfly if shipped** | The only capability Kleio structurally refuses *and* Mcfly can still claim without becoming TW. |
| 7 | Tax / VAT / sales definition toggle | Underspecified | **Ships** tax-in/out + Finance Summary reconciliation table | S1 Ring 1 | **Kleio** | Mcfly currently sums `orders.totalPriceSet` with no mode (`shopify-sales.server.ts`). Kleio already wrote the 1-star prevention doc. |
| 8 | Dual clock (delivery vs accrual) | No | **Ships** accounting date vs order-date `(O)` + E(return) forecast | Explicitly **out** of S1 Ring 1 | **Kleio** | If P4 is the buyer, S1 is already behind. That is S2/S4. |
| 9 | COGS / fees / shipping | Typed margin only | **Ships** Shopify COGS + custom + fees auto + shipping/fulfillment/returns/customs/agency | Out of S1 (that is S2) | **Kleio** | S2 vs Kleio is a late clone at **+$10**. |
| 10 | Cash CAC / LTV:CAC | **Listing claims**; repo does not | **Ships** blended CAC, NC ROAS (aMER), LTV, cohorts, LTV:CAC on CM2, payback; hides LTV:CAC when product-filtered (honest) | Ring 2 cash CAC only | **Kleio** | Mcfly listing integrity risk vs a product that actually has cohorts. |
| 11 | Goals / pacing board | Listing claims | Not found as a named “goals board” this fetch | Not Ring 1 | Unknown | Do not compete on a claim we may not ship. |
| 12 | Allocation 7/14/28 | Yes (∝ spend) | Campaign-name **spend** filters + `kleio_allocate_nc_XX`; no “cut Meta 20%” science | Disarm ∝ | Kleio more honest | Mcfly’s allocator is the weaker religion. |
| 13 | Monday email / Slack / PDF | No | **Partial** — no first-party email product found; reviewers **schedule Claude via MCP** as the Monday artifact | Email is S1 Ring 1 | Open | Kleio outsourced the ritual to MCP. Better Reports still owns push-native. |
| 14 | Sheets companion | Scaffold | Not found | Not Ring 1 | Mcfly (vapor) / SyncWith (real) | Kleio does not need Sheets because the desk is the sheet. |
| 15 | Multi-store / agency | No | **Partial** — unlimited **users**; campaign Include `US_` for one store vs UK spend; not a billed portfolio SKU | Out | Unclear | Unlimited users at $29 undercuts Polar’s “unlimited users @ $750.” |
| 16 | Pixel / CAPI | Refuse | **Refuse** (Attribution ✗) | Refuse | Tie on religion | Both can partner (S5b). Neither should build. |
| 17 | Passback / Apex / Sonar | Refuse | **Refuse** (optimization stays in-platform) | Refuse | Tie | Kleio’s FAQ is the cleaner “why we don’t pass back.” |
| 18 | MCP / ChatGPT | No | **Ships** (read + **product write**) | Out of S1 | **Kleio** | Trek Light / Hummii 5-stars are MCP 5-stars. Polar/TP/Lifetimely also list MCP. Mcfly “later” is late. |
| 19 | Heatmaps | No | No | Out | Clarity | Ignore. |
| 20 | Custom report builder | No | Customizable dashboard (not Better Reports) | Out | Better Reports | Ignore. |
| 21 | GL / NetSuite / QB | No | No. Gentleman’s Gazette review *hopes* for Finaloop. | Export only | A2X | Complementary, not a rival. |
| 22 | Creative analytics | No | No | Out | TW | Ignore. |
| 23 | AI agent OS | No | MCP + playbook; not Moby credits | Out | TW (hate) / Kleio (thin) | Do not meter. |
| 24 | Free plan | No | No (paid + 14-day) | No | Lifetimely / TW / Parkour | Kleio and Mcfly share “paid-only.” Kleio still has 20 reviews. Free is sufficient, not necessary. |
| 25 | 14-day trial | 7-day | **Ships** | S1 packaging | **Kleio** | Cheap billing config. Mcfly chose the harder trial. |
| 26 | Works-with logos | None | **Five** on listing | S1 packaging | **Kleio** | Empty Works-with is a conversion tax. |
| 27 | Reviews | 0 | **20 / 5.0** | Prerequisite, not a feature | **Kleio** | ~19 months live vs Mcfly 2 days. Directionally they executed the love loop. |
| 28 | Magic summary | Impossible | Not on (needs 100 written + 4.0) | n/a | Polar / A2X | Neither has it. |
| 29 | BFS badge | No | Not observed | later | — | Don’t chase. |
| 30 | Languages | EN | EN | EN | Polar / Clarity | Later. |

**Row score (public, research judgment):** Kleio **wins or ties 22 of 30**. Mcfly uniquely wins **#3 offline hero** (unproven demand) and **#6 claim-vs-till** (unshipped). S1 tries to win #5, #7, #13, #25, #26 — four of those Kleio already has.

---

## 2. Religion inconsistencies — Kleio as a mirror

`MCFY_GAP_MATRIX.md` §B, applied to both products.

| Topic | Mcfly repo | Mcfly live | Kleio public | Mirror |
| --- | --- | --- | --- | --- |
| Price | Free DP → ~$79 | **$39** | **$29** flat, anti-GMV in spirit | Kleio already ran Mcfly’s moral price **and undercut it** |
| Metric name | Cash MER | Total ROAS | Revenue, CM3, NC ROAS **(aMER)** | Kleio is willing to say MER. Mcfly runs two names. |
| OAuth | Phase 2 | “No ad-account OAuth” | OAuth is the product | Mcfly’s live refuse is the thing Kleio’s 5-stars bought |
| LTV / Goals | Later | Listing claims **now** | LTV + cohorts **documented** | Mcfly’s integrity hole is Kleio’s shipped page |
| Freemium | No forever-free | No free | No free | Aligned; Kleio still got reviews |
| Formula | sales ÷ spend | same | CM3 / aMER **and** spend÷sales style ROAS | Kleio did not stop at the ratio |
| Pixels | Kill-on-contact | “No pixels” | Attribution ✗ | Same refuse, different sermon (they defend Meta-the-optimizer) |
| Allocation | mer-core ∝ spend | 7/14/28 | Disclosed spend filters | Kleio’s allocator is *labeled*. Ours is circular unless sales are typed |

Kleio is the existence proof that **anti-attribution + flat cheap + App Store** can get to 20 five-stars **if the desk is a P&L with OAuth**. Mcfly’s CURRENT_RELIGION is closer to Kleio’s FAQ than to MASTER_PLAN’s “we are not a profit tracker.” The gap is execution, not theology.

---

## 3. Four-score gap vs Kleio (`MCFY_GAP_MATRIX` §C style)

| They beat Mcfly on | Mcfly can still beat them on | If we do nothing |
| --- | --- | --- |
| Price ($29 vs $39) | Billboard / retainer as first-class **if** we keep it and they don’t market it | Lose the “cheap honesty” shopper to Kleio |
| Reviews (20 vs 0) | Claims-vs-cash card (they refuse the visualization) | Remain the unpaid sermon |
| Auto spend (8 platforms) | US founder voice / offline ledger | Same rail, they get the install |
| Tax definition + dual clock | Simpler “one formula” *if* P4 is not the buyer | P4 never calls |
| COGS / CM waterfall | Not becoming a cost-engine company (capital) | S2 suicide if we chase |
| MCP (read **and** write) | Not letting AI draft products (scope + PCD) | Fashion, but their reviews already mention it |
| 14-day + Works-with | Listing integrity *after* we stop claiming LTV we don’t have | Trust |
| Founder Slack (Mathias) | Named human of our own | Love loops without a name are `noreply` |
| DK entity / GDPR posture (address) | — | Not a feature; see `COMPLIANCE_LANDMINES.md` |

**Kill-shot that is fair:** “We show the Ads Manager lie next to the till. They won’t, on purpose.”  
**Kill-shot that is cope:** “We replace Kleio.” You don’t, at $39, thinner, 0 reviews.  
**Kill-shot that is suicide:** “We also have CM1–CM3, cohorts, ShipHero, MCP write.” That is S2 + a year.

---

## 4. Problem-coverage (`MCFY_GAP_MATRIX` §D) — Kleio column added

| Problem # | Mcfly today | Kleio public | Gap type if S1 only |
| --- | --- | --- | --- |
| 1 Net profit | Thin (margin %) | **Core** (CM3 + net) | S1 refuses the #1 paid job |
| 2 Pixel/CAPI | Refuse | Refuse | Shared; rail still pixel |
| 3 Spend next to sales | Core, manual | Core, **auto** | S1 ties the row, late |
| 4 Platform ≠ till | Partial / marketing | Spend yes; **gap card no** | S1’s only unique close |
| 5 Custom reports / Sheets | Weak | Dashboard + MCP | Unowned |
| 6 LTV/CAC | Claimed | **Ships** | Integrity vs product |
| 7 Passback | Refuse | Refuse | Shared |
| 8 Heatmaps | None | None | Ignore |
| 9 GL recon | None | None (Finaloop wish) | Export only |
| 10 Offline spend | Core wedge | Other Marketing bucket | Thin wedge |
| 11 Allocation | Heuristic ∝ | Named spend filters | Honesty |
| 12 Multi-entity | None | Filters + unlimited users | Packaging |
| 13 Creative | None | None | Ignore |
| 14 AI OS | None | MCP + playbook | Optional thin |
| 15 Monday ritual | Positioning | Daily desk + MCP cron | S1 email vs their habit |

**Coverage count restated:** Mcfly 2 cores (3, 10). Kleio cores **1, 3, 6, 11-as-filters, 14-thin, 15-as-daily**. S1 adds ease on 3 and a bet on 4+15. It does **not** pick up problem 1. Wave A already said refusing #1 is refusing the review corpus.

---

## 5. What Kleio does **not** ship (hunt for a wedge)

Public pages this wave do **not** show:

1. **Claims-vs-cash / platform variance card.** Closest is the anti-MTA essay. They will not be the court that exhibits the lie; they will be the P&L that ignores it.
2. **Billboard / podcast / retainer as a named channel** in the hero. “Other Marketing” is a leftover bucket.
3. **Native Monday email / Slack.** Reviewers built it with Claude.
4. **MTA / pixel / CAPI / Apex.** Refused.
5. **Order-meter or GMV tax.** Structural (same as Mcfly’s public moral).
6. **QuickBooks / Xero posting.** Hoped Finaloop connection (reviewer), not shipped.
7. **Magic summary / 100 reviews.**
8. **US-first support hours.** CET “one working day” (site). A US afternoon founder waits.

Wedges that **survive contact with Kleio:**

| Wedge | Durable? | Condition |
| --- | --- | --- |
| Claims-vs-cash | **Yes, if shipped and legal** | Paste-first if Meta mix-rule bites |
| Offline ledger as first-class | Maybe | Need buyers; not a listing-only noun |
| US-hours human | Weak | Mathias already does Slack calls (reviews) |
| $39 vs $29 | **No** | We are more expensive |
| “Cash MER religion” | **No** | They already refuse attribution, in public, at length |
| Governor-not-OS | Weak | They are already not an OS; they are a cheaper P&L |

---

## 6. Line-by-line S1 collision

If Mcfly ships S1 Ring 1 as specified:

| S1 piece | Kleio today | Collision |
| --- | --- | --- |
| Meta/Google spend OAuth | Hourly, campaign, 8 platforms | **Direct.** We are a subset. |
| Tax toggle | Tax-in/out + Finance Summary table | **Direct.** Their docs are better than our code. |
| Monday email | MCP-scheduled | **Indirect.** We might win “no Claude required.” |
| Paste-a-claim card | Absent | **Our only white space** |
| 14-day / Works-with | Already | Hygiene, not a wedge |
| $39 flat | $29 | We lose the scan |
| No COGS | Full waterfall | They win P1; we look unfinished |
| Billboard CSV | Other Marketing | Ours to lose by neglect |

**Research call:** do not pitch S1 as “what Kleio is missing” except **the claim card**. Pitch S1 as “governor for people who already have (or refuse) a P&L.” That is a **narrower** market than Wave B’s 19 implied. It is closer to S4 (overlay) wearing S1’s clothes.

---

## 7. What we still must not invent

- Kleio install count, churn, or “364 stores” as ours to repeat without the VENDOR_CLAIM tag.
- That Kleio’s 20 reviews are a Magic summary (they are not).
- That Kleio stores order-level PII (likely yes for LTV — **not confirmed** beyond “uninstall deletes orders”).
- That Kleio’s Meta token limit is a bug they will “fix” — they documented it as product behavior.
- Any Mcfly review, install, or conversion number.

---

## 8. One paragraph

Kleio is the product Wave A’s opportunity map described as G1+G2 and Wave B scored as S1/S2, except it shipped in February 2025 at **$29**, refuses attribution **on purpose**, auto-pulls spend, publishes the finance definitions Mcfly still underspecifies, and already collects 5-stars from people leaving Triple Whale. The Mcfly gap list is, line by line, mostly a Kleio **have** list. The leftover white space is a **claims-vs-cash** exhibit and a first-class offline ledger — neither of which is proven to print reviews. S1 that is only OAuth + tax + email is a late Kleio without CM3. S2 that is a waterfall at $39 is a late Kleio plus ten dollars. Religion did not prevent Kleio. Scope and a 14-day OAuth desk did.
