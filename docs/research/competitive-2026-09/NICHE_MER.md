# The niche — MER / blended ROAS / till vs Ads Manager

**Date:** 2026-09-09  
**Purpose:** Define the problem space Mcfly *says* it owns, with public evidence, without pretending it is the largest paid niche.

---

## 1. Definitions in the wild (do not invent a standard)

| Term | How public sources use it | Caution |
| --- | --- | --- |
| **ROAS** | Channel return: attributed revenue ÷ channel spend. Ads Manager / Google Ads native. | Platform-attributed. Over-claims. |
| **Blended ROAS** | Total store revenue ÷ total ad spend. r/shopify 1rpjuk0 “spreadsheet tracking total ad spend vs total Shopify revenue weekly.” | Sometimes still called ROAS, which confuses. |
| **MER** | Marketing Efficiency Ratio, usually **revenue ÷ spend** (same math as blended ROAS). Polar lists “ROAS, MER” as separate words on https://apps.shopify.com/polar-analytics and https://www.polaranalytics.com/integrations/reddit-ads | `docs/COMPETITORS.md` claims TW once defined MER as spend÷revenue. **Re-verify on a live TW UI before attacking.** |
| **Total ROAS** | Mcfly live listing/site: Shopify sales ÷ spend you added. | Unique Mcfly branding. Risk: sounds like Ads Manager. |
| **Cash MER** | Mcfly repo: same formula, “cash” to mean till, not paths. | Not a widely searched public term in this fetch. |
| **Break-even ROAS / MER** | ≈ 1 / contribution margin. Mcfly site table. Community 657805 contribution recipe. | Margin source is the fight (typed % vs assembled). |
| **Contribution margin** | Net sales − direct costs (COGS, ship, fees) **before or after** ads depending on writer. Community 657805 layers ads as blended daily, not per-order CAC. | Say which. |
| **Incrementality** | Lift vs holdout. Polar Causal Lift; Northbeam incrementality; r/PPC pause tests. | Not MER. Complementary. |
| **MTA** | Path credit across touches. TW / Polar / NB / Klar. | Not cash. |

**Mcfly formula (live + repo, aligned):**  
`Total ROAS or MER = Shopify sales (period) ÷ ad spend (same period)`  
`Break-even ≈ 1 ÷ contribution margin`

---

## 2. Why the niche exists (official + community)

**Shopify Admin will not do the job.**

- Community 134251: “Shopify definitely doesn’t measure the spend. You will need a third-party app.”
- Marketing reports only attribute **trackable** marketing (UTM / admin campaigns). Help Center snippet: sales in that report **can differ** from other sales reports.
- 30-day lookback: historical attributed sales **move** (Community 180915).
- Shop Campaigns have native spend+ROAS in ShopifyQL `shop_campaign_insights` — **Shop Campaigns only**, not Meta/Google/billboards.
- Profit by product needs Cost per item and still **excludes ads** (Community 657805).

**Platforms will not do the job honestly.**

- r/shopify 1rpjuk0: Meta vs Shopify “will never sync up.”
- r/PPC 1u81q7r: scaled the wrong campaigns for months.
- r/PPC 1r2pvgy: treat Shopify as revenue truth; Meta as directional; watch blended MER.
- r/PPC 1pqv5kh: platforms for optimization; backend / blended MER as reality check.
- Northbeam homepage exists to sell “independent” results vs platforms (`VENDOR_CLAIM` stats).
- Polar Reddit Ads page: MER after “overclaiming is removed” — **via Polar Pixel**, i.e. they agree platforms lie and then sell a third model.

---

## 3. How people actually run the niche today

| Method | Cost signal | Public home | Failure |
| --- | --- | --- | --- |
| Weekly Sheet | $0–$5 (SyncWith $4.99) | r/shopify 1rpjuk0; r/PPC 1qgb8mg; Community 134251 | Stale, error-prone, no BE/allocation product |
| Profit app | $25–$299 | TrueProfit, Lifetimely, BeProfit, Metorik | MER is a side effect of net profit; order meters |
| Suite | Free–$750+ | TW, Polar, NB | MER is a tile; GMV/spend tax; pixel religion |
| Mcfly | $39 | listing 2 days old | Manual; 0 reviews; wrong App Store rail |
| Margins by Finaloop | Free | https://apps.shopify.com/margins | N=1 review; “True ROAS based on profit”; **watch** |

**The niche is real. The standalone paid app for *only* this niche is not proven.** People pay for **profit** or **attribution** and get blended as a byproduct, or they DIY.

---

## 4. Agency vs operator vs finance inside the niche

| Role | Uses MER/blended to… | Will pay Mcfly if… | Else they buy |
| --- | --- | --- | --- |
| Operator | Cap daily scaling | Number is automatic and next to Ads Manager | TW / pixel / ignore |
| Agency | One scoreboard for clients | Multi-store + pack | Sheets |
| Finance | Sign the board pack | Definitions + tax + recon export | A2X + TP |
| Founder | Sleep | Sees “we made money” | TrueProfit |

Monday close is the **ritual name** Mcfly gave a weekly blended check. Better Reports made the ritual an **email**. That is the productization gap.

---

## 5. Vanity ROAS vs till — the argument, with humility

**What we can say (sourced):**
- Platforms optimize to their own conversions (Apex/Sonar/CAPI exist *because* of this).
- Shopify attributed marketing ≠ total sales (Help Center + Community).
- Commenters claim Meta ROAS reads 20–40% higher than Shopify last-click (r/shopify 1rpjuk0) and that summing platforms can exceed 100% of revenue (r/PPC 1qgb8mg). **Those percents are commenter claims, not studies.**

**What we must not say:**
- “Every store’s Meta ROAS is X% inflated.”
- “Northbeam raised ROAS 37%” as fact (homepage `VENDOR_CLAIM`).
- “WeTracked raised ROAS 30%” as fact (reviewer claim).

**Mcfly’s honest sentence:**  
*We do not know which click won. We do know what Shopify recorded and what you paid. Those two should sit on the same days.*

That sentence is the niche. It is enough — **if** entering “what you paid” is not homework.

---

## 6. Spend allocation inside the niche

Public practice:
- Suites: model → Moby/Apex → change bids.
- r/PPC: pause a channel, watch Shopify revenue, learn incrementality the ugly way.
- Mcfly: rules engine; without channel sales, **sales ∝ spend** (`allocation.ts`).

**Critical:** allocation from blended MER can only say “cut total spend” or “you are below BE.” It cannot honestly say “cut Meta 20%, shift to Google” unless the operator supplies channel sales **or** you run a test. Shipping the latter as science is how you become the theater you attack.

`RESEARCH_OPTION`: allocation vNext = (1) portfolio cut/hold from blended vs BE, (2) optional pause protocol, (3) optional manual channel sales. Not (4) silent ∝.

---

## 7. Profit vs vanity ROAS

Community 657805 is the adult version of Mcfly’s sermon: contribution first, blended ads second, full P&L third. TrueProfit industrialized that and got 899 reviews.

Mcfly industrialized **only** the blended-ads slide. That is why $39 vs $35 is a bad trade for a founder.

Religion flex (R12): **job = money, method = sales÷spend.** If the job stays “MER education,” the course is the product. If the job is “did we keep dollars,” profit-lite or governor+costs is the product.

---

## 8. Search / discovery implication

Merchants search (inferred from listing language, not from keyword tools we don’t have): “profit,” “ROAS,” “pixel,” “Facebook,” “report,” “LTV.”  
They do not search “billboard MER.”

Mcfly’s unique noun (billboard) is a **story**, not a query. Keep it in the hero *after* spend-vs-sales.

---

## Related files

- Problems ranked: `PROBLEM_BANK.md`
- Personas: `PERSONAS.md`
- Workflows: `ENTERPRISE_WORKFLOWS.md`
- Strategy: `SYNTHESIS.md`
