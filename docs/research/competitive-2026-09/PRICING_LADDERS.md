# Pricing ladders — public App Store cards as text tables

**Fetched:** 2026-09-09 from live listing HTML (`#adp-pricing`).  
**These are listing cards, not quotes.** Vendor homepages that disagree are flagged.  
**No invented GMV bands.** If a site slider was not captured as a static table, it is marked `SLIDER / NOT A CARD`.

Trial language is what the listing card printed. Shopify also tracks trial days over 180 days (official billing docs).

---

## How to read

| Column | Meaning |
| --- | --- |
| Plan | `data-test-id="name"` on the listing card |
| List price | `aria-label` on the price group |
| Extra | `data-test-id="additional-charges"` if present |
| Trial | Footer on that card |

Mcfly control row is first in each relevant cluster.

---

## 0. Mcfly (control)

https://apps.shopify.com/mcfly-analytics-public · launched 2026-09-07 · **0.0 / 0 reviews** (JSON-LD)

| Plan | List price | Extra | Trial |
| --- | --- | --- | --- |
| Mcfly Analytics | **$39/month** | — | 7-day (listing header: “7-day free trial, then $39/month”) |

Site also sells **MDS Made Easy $79 one-time** (https://mcflyads.com/pricing). Repo drafts still say free DP → ~$79. Live listing wins.

---

## 1. Profit / P&L / LTV cluster (same wallet as $39)

### TP: True Profit Analytics — 5.0 / 899 — 14-day
https://apps.shopify.com/trueprofit · launched 2019-07-31

| Plan | List price | Extra | Included orders (card feature) |
| --- | --- | --- | --- |
| Basic | $35/month | $0.30 / extra order, max surcharge $300 | 300 / month |
| Advanced | $60/month | $0.20 / extra, max $500 | 600 / month |
| Ultimate | $100/month | $0.10 / extra, max $700 | 1,500 / month |
| Enterprise | $200/month | $0.07 / extra, max $1,000 | 3,500 / month |

### Lifetimely Profit Analytics — 4.9 / 535
https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics · launched 2019-02-19

| Plan | List price | Extra |
| --- | --- | --- |
| FREE | Free to install | Up to **50 orders / month** |
| S | $49/month | Up to 500 orders / month · 14-day trial |
| M | $149/month | Up to 3,000 · 14-day |
| L | $299/month | Up to 7,000 · 14-day |
| Amazon add-on | **+$75 / month** | Printed on S/M/L cards: “Add Amazon data for $75 / Month” |

### BeProfit Profit Analytics — 4.5 / 202 — 14-day
https://apps.shopify.com/beprofit-profit-tracker · launched 2020-09-22

| Plan | List price | Extra on card |
| --- | --- | --- |
| Basic | $49/month | (order/shop caps not in additional-charges field this fetch) |
| Pro | $99/month | — |
| Ultimate | $149/month | — |
| Plus (Enterprise) | $249/month | — |

WAVE A notes order+shop metering in listing copy. Card extras were empty this parse — do not invent caps.

### Metorik — 5.0 / 48 — **30-day**
https://apps.shopify.com/metorik · launched 2020-09-10

| Plan | List price |
| --- | --- |
| Level 1 | $25/month |
| Level 2 | $75/month |
| Level 3 | $150/month |
| Level 4 | $250/month |

WAVE A: multi-store from $75. Not re-printed on extras this fetch.

### Margins by Finaloop — 5.0 / 1 — Free
https://apps.shopify.com/margins · launched 2026-05-18  
Pricing section empty of plan cards this fetch. Header: **Free**.

### Kleio Analytics — 5.0 / 20 — 14-day
https://apps.shopify.com/kleio · launched 2025-02-19

| Plan | List price | Features on card |
| --- | --- | --- |
| Everything | **$29/month** | All features · unlimited users · 1,000,000 orders in database |

**This is the flat-price peer Mcfly should fear more than Polar.** Same job family, $10 cheaper, 20 reviews, 1M-order cap.

### Juicy Attribution & Profit — 4.9 / 76
https://apps.shopify.com/juicy · launched 2025-04-09

| Plan | List price | Trial |
| --- | --- | --- |
| Free | Free | Free |
| Starter | $29/month | 10-day |
| Advanced | $49/month | 10-day |

### GoProfit — 4.8 / 90
https://apps.shopify.com/go-profit · launched 2024-08-23

| Plan | List price | Extra |
| --- | --- | --- |
| Free | Free | — |
| Lite | $12/month | $0.20 / extra order, max $500 · 14-day |
| Pro | $59/month | same overage · 14-day |

### Profitario — 4.8 / 62
https://apps.shopify.com/profitario · launched 2019-11-22

| Plan | List price | Extra |
| --- | --- | --- |
| Free to install | Free | — |
| Starter | $30/month | +$0.30 / extra, max $300 |
| Growth | $55/month | +$0.20 / extra, max $500 · 14-day |
| Pro | $100/month | +$0.10 / extra, max $700 · 14-day |

TrueProfit-shaped surcharge, weaker reviews.

### Setpilot — 5.0 / 4
https://apps.shopify.com/setpilot · launched 2026-04-06

| Plan | List price | Extra |
| --- | --- | --- |
| Free | Free | (WAVE A/C listing copy: up to 50 orders — verify before attacking) |
| Start | $29.99/month | Up to 300 orders / month · 14-day |
| Grow | $79.99/month | Up to 1,000 · 14-day |
| Ultimate | $399.99/month | Unlimited · 14-day |

### Profit Calc — 5.0 / 67
https://apps.shopify.com/profit-calc · launched 2019-12-16

| Plan | List price |
| --- | --- |
| Starter | $39/month |
| Growth | $79/month |
| Pro | $149/month |
| Unlimited | $249/month |

**$39 Starter = Mcfly’s exact list price** with a 67-review head start.

### Bloom Profit Analytics — 5.0 / 39
https://apps.shopify.com/bloom-analytics · launched 2024-10-15

| Plan | List price | Extra |
| --- | --- | --- |
| Sprout | $20/month | Unlimited orders · 14-day |
| Grow | $40/month | Unlimited · 14-day |
| Flourish | $80/month | Unlimited · 14-day |

### CD: CashDash — 5.0 / 7
https://apps.shopify.com/cashdash-pro · launched 2024-02-05

| Plan | List price |
| --- | --- |
| Awesome | **$5.99/month** · 14-day · “Unlimited Orders” on listing copy |

### ClearProfit — 5.0 / 7
https://apps.shopify.com/clearprofit · launched 2026-01-20

| Plan | List price |
| --- | --- |
| COD Intelligence | $29/month |

Community already discussed this app: https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628

### Margn — 0.0 / 0
https://apps.shopify.com/margn-1 · launched 2026-08-18

| Plan | List price | Trial |
| --- | --- | --- |
| Starter | $19/month | 7-day |
| Growth | **$39/month** | 7-day |
| Pro | $79/month | 7-day |

**Same $39 + 7-day shape as Mcfly**, two weeks older, still 0 reviews. Copy: “total ad spend — never attributed-only.”

### TrackProfit — 0.0 / 0
https://apps.shopify.com/trackprofit-1 · launched 2025-07-28

| Plan | List price |
| --- | --- |
| PRO Unlimited | $29.99/month |
| Lifetime Unlimited | **$239 one-time** |

Lifetime SKU is rare in this aisle. 0 reviews after ~13 months is a signal, not a feature.

### ProfitIQ — 0.0 / 0
https://apps.shopify.com/profitiq · launched 2026-08-14

| Plan | List price | Trial |
| --- | --- | --- |
| Free | Free | — |
| growth | $19/month | 3-day |
| Pro | $49/month | 3-day |
| Pro Plus | $89/month | 3-day |

**3-day trial** — shorter than Mcfly. Still 0 reviews.

### MarginLens AI — 0.0 / 0
https://apps.shopify.com/marginlens-ai-powered · launched 2026-05-14

| Plan | List price |
| --- | --- |
| Starter | $9.99/month · 14-day |
| Growth | $14.99/month · 14-day |
| Unlimited | $29.99/month · 14-day |

### ProfitMetrics — 3.5 / 8
https://apps.shopify.com/profitmetrics · launched 2022-10-24

| Plan | List price |
| --- | --- |
| ProfitMetrics | $32/month |

Low rating + 8 reviews after four years = dying-on-the-vine (see `FAILURE_AUTOPSIES.md`).

### Profit Panel — 0.0 / 0
https://apps.shopify.com/profit-panel · launched 2025-12-04

| Plan | List price |
| --- | --- |
| Starter | $18/month |
| Growth | $30/month |
| Ultimate | $50/month |
| Enterprise | $150/month |

### Repeat Customer Insights — 5.0 / 14
https://apps.shopify.com/repeat-customer-insights · launched 2016-05-30

| Plan | List price |
| --- | --- |
| Entrepreneur | $59/month |
| Growth | $99/month |
| Peak | $249/month |

LTV specialist, not a spend desk.

---

## 2. Suites / measurement OS

### Triple Whale — 4.1 / 91
https://apps.shopify.com/triplewhale-1 · launched 2020-12-04  
Listing header: Free plan · **external charges may apply**

| Plan | List price |
| --- | --- |
| Free | Free |
| Foundation | $219/month (listing also showed $2,190/yr in WAVE A) |
| Automate | $749/month (WAVE A: $7,490/yr) |

Site https://www.triplewhale.com/pricing = **GMV slider**. Listing numbers are **entry floors**, not the bill. `SLIDER / NOT A CARD`.

### Polar Analytics — 4.9 / 116
https://apps.shopify.com/polar-analytics · launched 2020-10-28

| Plan | List price | Notes |
| --- | --- | --- |
| Core Plan, from | **$750/month** | Listing: “Pricing based on online GMV” |

Own vs page still claims ~$400 (WAVE A conflict). **Do not publish a Polar price as gospel.**

### Klar Analytics — 0.0 / (no ratingCount in JSON-LD)
https://apps.shopify.com/klar-analytics · launched 2023-12-24

| Plan | List price |
| --- | --- |
| Free | Free to install · “Additional charges may apply” |

~33 months, **no review object**. Sales-led / off-store. Autopsy in `FAILURE_AUTOPSIES.md`.

### Daasity — 4.6 / 51
https://apps.shopify.com/daasity · launched 2020-05-13

| Plan | List price | Extra |
| --- | --- | --- |
| App Starting At: | **$1,899/month** | “Usage charges are based on an annualized rolling 3 month average of your total revenue.” · 14-day |

### Rockerbox — 4.5 / 12
https://apps.shopify.com/rockerbox · launched 2019-10-25

| Plan | List price |
| --- | --- |
| Paid Subscription | Free to install (price off-card) |

### Segmetrics — 0.0 / (no ratingCount)
https://apps.shopify.com/segmetrics · launched 2021-12-08

| Plan | List price | Extra |
| --- | --- | --- |
| Ecom Intelligence | $197/month | Includes 10K contacts · 14-day |
| Ecom Business | $397/month | Includes 10K contacts · 14-day |

### Attribuly — 4.7 / 168
https://apps.shopify.com/attribuly · launched 2022-03-04

| Plan | List price |
| --- | --- |
| FREE | Free |
| Capture | $450/month · 14-day |
| Recapture | $500/month · 14-day |

### Lebesgue (Advertising Insights) — 4.9 / 132
https://apps.shopify.com/advertising-insights · launched 2021-01-07

| Plan | List price |
| --- | --- |
| Free | Free |
| Ultimate | $79/month |
| Ultimate AI | $149/month · 14-day |

MARKET_REPORT (AnalysisGPT blog): “attribution pixel priced separately and scales with revenue” — **not on these cards**. Do not publish a pixel surcharge.

### Northbeam
No Shopify listing (`apps.shopify.com/northbeam` 404). Homepage https://www.northbeam.io/ prints **no dollar card**. WAVE A MARKET_REPORT ~$1,500 floor remains unverified. **No table.**

---

## 3. Pixel / CAPI / behavior

| App | URL | Plans on card | Reviews |
| --- | --- | --- | --- |
| Microsoft Clarity | /microsoft-clarity | Free Forever | 4.6 / 2,125 · launched 2025-07-17 |
| Parkour Pixel | /parkour-pixel | (no priced cards; header **Free**) | 4.9 / 191 · 2024-10-18 |
| WeTracked Connect | /wetracked-io-connect | Free to install (external platform charges) | 4.8 / 125 · 2025-10-27 |
| Analyzify | /analyzify | Standard T1 $145 (5k orders) · T2 $175 (10k; $225 for 20k) · Plus T1 $275 (50k) · Plus T2 $375 (100k; $575 for 300k). Yearly includes $295 implementation. 2-year price guarantee | 4.7 / 313 |
| Elevar | /gtm-datalayer-by-elevar | Core $225 + $0.50/order after 2,000 · Advanced $650 + $0.15 after 10,000 · Premium $1,250 + $0.10 after 30,000 · 15-day | 4.7 / 168 |
| Littledata | /littledata | Flex: Free to install, **$0.35 / tracked order** · Scale $199 (1,500 incl.; $0.15 then $0.06) · Plus $990 (10,000 incl.; $0.03 then $0.02) · **30-day** | 4.8 / 140 |
| Lucky Orange | /lucky-orange | Free · Launch $19 · Build $39 · Grow $89 | 4.7 / 878 |
| Hotjar | /hotjar | BASIC $0.99 · PRO $2.99 | 4.3 / 89 |
| FullStory | /fullstory | Free (to install) | 0.0 · launched 2025-06-13 |

---

## 4. Reports / pipes

### Better Reports — 5.0 / 1,199
https://apps.shopify.com/betterreports · launched 2017-02-24

| Plan | List price | Extra |
| --- | --- | --- |
| Basic | $19.90/month | “For stores currently on the Basic plan” |
| Grow | $39.90/month | Grow plan |
| Advanced | $149.90/month | Advanced plan |
| Plus | $299.90/month | Plus plan |

**Priced to the Shopify plan name**, not orders. Mcfly $39 sits on Grow.

### Report Pundit — 5.0 / **2,026**
https://apps.shopify.com/report-pundit · launched 2019-08-13

| Plan | List price | Extra |
| --- | --- | --- |
| Free Plan | Free | — |
| Basic | $9/month | Basic Shopify plan |
| Grow | $19/month | Shopify plan |
| Advanced | $35/month | Advanced Shopify plan · 14-day |

Highest-review **custom reports** object in the Analytics aisle.

### Mipler Advanced Reports — 5.0 / 633
https://apps.shopify.com/advanced-reports · launched 2019-08-15

| Plan | List price |
| --- | --- |
| FREE | Free |
| Basic | $14.99/month |
| Pro | $29.99/month |

### Report Toaster — 4.9 / 218
https://apps.shopify.com/report-toaster · launched 2021-04-13

| Plan | List price |
| --- | --- |
| Free | Free |
| For Basic/Grow | $18/month |
| For Advanced | $60/month |
| For Plus | $150/month |

### EZ Exporter — 5.0 / 99
https://apps.shopify.com/ez-exporter · launched 2016-12-07

| Plan | List price |
| --- | --- |
| Standard | $29.95/month |
| Advanced | $49.95/month |
| Premium | $149.95/month |

### Data Export — 5.0 / 2,009
https://apps.shopify.com/data-export · launched 2016-02-03

| Plan | List price |
| --- | --- |
| Basic | $12/month |
| Grow | $25/month |
| Advanced Shopify | $35/month |
| Plus | $50/month |

Utility, not a religion. Review physics: **export + free/cheap**.

### SyncWith — 4.5 / 10
https://apps.shopify.com/syncwith · launched 2021-08-10

| Plan | List price |
| --- | --- |
| Free | Free |
| Premium | $4.99/month |

### Coupler.io — 2.9 / 6
https://apps.shopify.com/coupler-io · launched 2022-12-06

| Plan | List price |
| --- | --- |
| Starter | $32/month |
| Active | $132/month |
| Pro | $259/month |

### Supermetrics — 2.0 / (no ratingCount)
https://apps.shopify.com/supermetrics · launched 2022-12-22

| Plan | List price |
| --- | --- |
| Starter | $37/month |
| Growth | $199/month |
| Pro | $499/month |
| Enterprise | $899/month |

Pipe without App Store love.

---

## 5. Finance recon

### A2X — 5.0 / 359 — 30-day
https://apps.shopify.com/a2x · launched 2019-07-12

| Plan | List price |
| --- | --- |
| Mini | $29/month |
| Basic | $45/month |
| Professional | $79/month |
| Advanced | $115/month |

WAVE A: Mini ≤200 orders. External charges may apply.

### Finaloop — 4.8 / 73
https://apps.shopify.com/finaloop · launched 2022-02-07

| Plan | List price |
| --- | --- |
| Start-ups | $245/month · 14-day |
| Growth | $995/month · 14-day |

WAVE A search snippet “starts at $995” was the **Growth** card, not the floor. Floor is **$245**.

### Synder — 4.8 / 217
https://apps.shopify.com/synder · launched 2020-09-02

| Plan | List price |
| --- | --- |
| Basic | $65/month |
| Essential | $129/month |
| Pro | $299/month |
| Pro Max | $599/month |

### Link My Books — 4.8 / 43
https://apps.shopify.com/linkmybooks · launched 2021-12-16

| Plan | List price |
| --- | --- |
| Starter 200 Lite | $21/month |
| 1K Lite | $41/month |
| 5K Lite | $60/month |
| 10k Lite | $100/month |

---

## 6. Ads OS / official channels (price is not the product)

| App | Plans | Reviews |
| --- | --- | --- |
| Facebook | Free to install | 3.8 / 5,648 |
| TikTok | Free to install | 4.8 / 15,912 |
| Microsoft Advertising | Free to install | 3.0 / 348 |
| AdScale | Basic $169 · Growth $249 · Elite $329 | 4.7 / 372 |
| Madgicx | Free to install | 4.1 / 16 |
| Prediko (inventory, Stocky refugee) | Enterprise Free to install · Starter $49 · Scale-up $119 · Growth $199 | 4.9 / 248 |

---

## 7. Zombie / sales-led leftovers on the store

| App | Plans | Reviews | Read |
| --- | --- | --- | --- |
| Metrilo | Essential $119 · Pro $199 · Premium $299 | **5.0 / 2** · launched 2017-08-03 | Acquired; listing not dead, demand is |
| Voluum | (no cards; header Free) | 0.0 · 2023-06-26 | Tracker, not Shopify-native |

---

## 8. Ladder patterns (evidence, not advice dressed as fact)

Observed on **live cards only**:

| Pattern | Who uses it | Mcfly today |
| --- | --- | --- |
| Flat one SKU | Kleio $29 · CashDash $5.99 · Mcfly $39 · ClearProfit $29 | Yes |
| Order meter + overage | TrueProfit, Profitario, GoProfit Lite/Pro, Setpilot paid | No |
| Free ≤ N orders | Lifetimely 50 · Setpilot Free · Juicy / GoProfit / Profitario / Bloom peers | No |
| Shopify-plan pricing | Better Reports, Report Pundit, Report Toaster, Data Export | No |
| GMV / revenue | Polar Core, TW site slider, Daasity $1,899 + rolling revenue | Explicitly refused on mcflyads.com |
| Per-order tracking tax | Littledata Flex $0.35 · Elevar overage | No |
| Lifetime | TrackProfit $239 | No |
| External / sales-led | TW, WeTracked, Klar, Rockerbox, Northbeam (no listing) | No |
| 14-day trial (cluster default) | TrueProfit, Lifetimely paid, BeProfit, Kleio, Bloom, Setpilot, A2X is 30 | **7-day** |
| 7-day trial | Mcfly, Margn | Same as a 0-review twin |
| 3-day trial | ProfitIQ | Worse |

`CURRENT_RELIGION`: $39 flat, anti-GMV, 7-day.  
`RESEARCH_OPTION`: keep flat (Kleio proves the shape); **move to 14-day**; do not copy TrueProfit’s surcharge (BeProfit 1★ + WAVE A zombie billing).  
`EVIDENCE`: tables above.  
`RISK`: 14-day without TTV still churns; Shopify 180-day trial window stops reset-shopping.

**Do not raise to $79 on a 0-review listing.** Profit Calc already owns $39/67 reviews. Kleio owns $29/20. Margn owns $39/0. The price is not the differentiator.
