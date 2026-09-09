# Failure autopsies — dead, dying, acquired, or 1-star-storm analytics apps

**Date:** 2026-09-09  
**Rule:** An autopsy needs a **public URL**. Silence is not a shutdown. A 404 is not a death certificate (wrong handle).  
**Clusters:** official sunset · acquisition-then-zombie · 1-star storm still alive · store-dead sales-led · crowded 0-review clones · Shopify killing its own analytics tiles.

Religion tags apply to **what Mcfly should refuse to copy**.

---

## 1. Official sunset — Stocky (Shopify-owned)

**Not an analytics peer.** Included because it is the cleanest 2026 **public obituary** of a first-party ops/analytics-adjacent app, and it shows how Shopify treats data after a kill.

| Fact | Source |
| --- | --- |
| Removed from App Store **2026-02-02** — no new installs | https://www.inflowinventory.com/blog/stocky-shopify-app-sunsetting/ |
| Full shutdown **2026-08-31**; APIs stop | same + https://www.finaloop.com/blog/stocky-discontinued-in-2026-what-shopify-merchants-should-do |
| Official Help: Stocky no longer available as of Aug 31, 2026; **read-only ≥90 days**; historical POs **do not import** into Admin; supplier records not exportable | https://help.shopify.com/en/manual/products/inventory/transitioning-from-stocky |
| Motive (vendor blogs): Admin consolidation / POS | Inflow, Prediko, Sumtracker — `MARKET_REPORT` |

**Autopsy:** Shopify will **eat a category** and leave merchants with a worse export. Third parties (Prediko 4.9/248, Finaloop InventoryIQ) harvest the refugee wave.

`RESEARCH_OPTION`: do not build features Shopify has announced it will native. Inventory forecasting is now that list. **Spend ingest is not** (Community 134251 still: Admin will not take Meta/Google spend).  
`EVIDENCE`: Help Center Stocky page + Community 134251.  
`RISK`: if ShopifyQL ever grows a first-party MER tile, Mcfly’s whole aisle compresses the way Stocky did. No public evidence that tile exists today.

---

## 2. Acquisition → zombie listing — Metrilo

| Fact | Source |
| --- | --- |
| Founded ~2014, Sofia. Analytics + CRM + email for ecom | listing + CB Insights |
| **Acquired by Sendinblue / Brevo 2021-09-21** (with Chatra, PushOwl) | https://www.brevo.com/blog/sendinblue-acquires-metrilo-chatra-pushowl/ · https://www.cbinsights.com/company/metrilo |
| Shopify listing **still up** 2026-09-09: launched **2017-08-03**, plans **$119 / $199 / $299**, JSON-LD **5.0 / 2 reviews** | https://apps.shopify.com/metrilo |
| Woo plugin “last updated 5 years ago”, 200+ installs, untested on current WP | https://wordpress.org/plugins/metrilo-woocommerce-integration/ |

**Autopsy:** The product was bought for **retention/email capability**, not for a standalone analytics religion. The Shopify listing was **not unpublished**. It sits at $119+ with **two reviews across nine years**. That is not a competitor. It is a **tombstone that still bills**.

`CURRENT_RELIGION` lesson: a live listing ≠ a living product.  
`RESEARCH_OPTION`: never read “5.0” without the **denominator**. 5.0/2 is noise. 5.0/899 is TrueProfit.  
`RISK`: Mcfly can become Metrilo-shaped (listing live, nobody home) without an acquirer.

---

## 3. Acquisition → enterprise retreat — Glew

| Fact | Source |
| --- | --- |
| Founded 2014, Charlotte. Commerce data cloud, 170+ connectors (vendor) | https://www.glew.io/ |
| **Acquired by Everest Group ~2026-03-10** | https://apnews.com/press-release/ein-presswire-newsmatics/everest-group-acquires-commerce-data-and-ai-platform-glew-io-an-it-exchangenet-transaction-fe5dbf4a14c4f63a30a289a74311b907 · https://www.bizjournals.com/charlotte/news/2026/03/11/glew-acquired-everest-group-e-commerce-ai-tech.html |
| Site still live, sales-led | https://www.glew.io/ |
| `apps.shopify.com/glew` and `/glew-io` **did not yield a usable listing card** this fetch | WAVE C fetch log |

**Autopsy:** 12-year BI brand **exits the self-serve App Store motion** (or hides the handle) after a PE/consulting sale. Polar/Daasity/TW now own the “warehouse + 40 connectors” story on the store.

Do **not** write “Glew shut down.” Write: **acquired, store presence unverified, site still selling.**

`RESEARCH_OPTION`: connector-zoo at Glew scale is an **exit to PE**, not a path to 5★/899. Matches `RELIGION_FLEX.md` R9 (refuse zoo).  
`EVIDENCE`: acquisition wires + 404/empty listing this wave.  
`RISK`: citing Glew prices from memory. **No live card. No table.**

---

## 4. 1-star storm, still shipping — BeProfit after Viably

**Alive.** 4.5 / **202** on 2026-09-09 (JSON-LD). Not dead. The storm is the lesson.

| Fact | Source |
| --- | --- |
| Viably acquires BeProfit **2024-10-14** to bolt profit onto ecommerce banking | https://www.einpresswire.com/article/750779451/viably-announces-strategic-acquisition-of-beprofit-to-enhance-ecommerce-banking-solution |
| 6% 1★ on listing UI (WAVE A) | https://apps.shopify.com/beprofit-profit-tracker |
| Aggregated 1★ themes: charged after cancel; bot support; “app is dying”; ad-spend import wrong | https://appnavigator.io/app/beprofit-profit-tracker/reviews/?rating=1 · https://letsmetrix.com/app/beprofit-profit-tracker · https://www.thepricegeek.com/profit-analytics/beprofit-review/ |
| Official-looking replies admit the acquisition and “relaunching support” | AppNavigator 1★ thread (merchant-visible) |

WAVE A already logged a **zombie $720/yr billing 1★**. That is the same disease: **order-metered SaaS + weak cancel path**.

`CURRENT_RELIGION`: stay flat; do not meter orders (`RELIGION_FLEX.md` R5).  
`EVIDENCE`: BeProfit 1★ corpus + TrueProfit’s own surcharge (still 5.0/899 — meter alone does not kill; **meter + cancel hell** does).  
`RISK`: copying TrueProfit’s $0.30/order because “they have 899 reviews.” The reviews predate the hangover; BeProfit is the hangover.

**Do not call BeProfit dead.** Call it **acquired, support-stripped, still priced $49–$249**.

---

## 5. 1-star storm, still shipping — Triple Whale

**Alive.** 4.1 / 91. WAVE A star split: **16% 1★** — the only suite in the original set with a visibly toxic pile.

Visible 1★ themes (WAVE A + listing): AI credits not disclosed on Foundation; CS unreachable; **VAT included in revenue**.

`CURRENT_RELIGION`: no metered AI (`RELIGION_FLEX.md` R10).  
`RESEARCH_OPTION`: productize **tax/shipping/returns definition** so we never eat the VAT 1★.  
`EVIDENCE`: TW listing reviews (WAVE A sample: Kove Footwear).  
`RISK`: “we are not TW” is cope if we later ship credits.

TW is not dying. It is **expensive and resented**. Polar 4.9/116 is the counter-example: same GMV religion, cleaner scars.

---

## 6. Store-dead / sales-led (listing is a brochure)

These apps are **not confirmed shut down**. Their **Shopify listing is not a growth engine**.

| App | Live listing fact | Read |
| --- | --- | --- |
| **Klar Analytics** | Launched 2023-12-24 · Free to install · external charges · JSON-LD **0.0 / no ratingCount** | Polar-class EU product that **never printed a review object** in ~33 months. Distribution failure, not a product autopsy. https://apps.shopify.com/klar-analytics |
| **Segmetrics** | Launched 2021-12-08 · $197 / $397 · 10k contacts · **0.0 / no ratingCount** | Funnel CRM that abandoned the store as a review surface. https://apps.shopify.com/segmetrics |
| **FullStory** | Launched 2025-06-13 · Free to install · **0.0** | Enterprise replay; listing is a door, not a funnel. |
| **Supermetrics** | $37–$899 · **2.0 / no ratingCount** | Serious pipe, dead store. |
| **Coupler.io** | $32–$259 · **2.9 / 6** | Pipe without a religion. SyncWith 4.5/10 is the same shape, slightly less hated. |
| **Northbeam** | **No listing** (handle 404) | Intentional. Homepage prints no dollars. |
| **Voluum** | Header Free · 0.0 · 2023-06-26 | Ad tracker tourist. |

`RESEARCH_OPTION`: if Mcfly chooses S3/S4 outbound (`SYNTHESIS.md`), Klar/Northbeam are the **existence proof** that a measurement product can skip the store. They also prove you then **own sales**.  
`EVIDENCE`: Klar 0 reviews; Northbeam 404.  
`RISK`: doing a hostile 0-review store **and** no outbound (WAVE A R11). Klar did the store-as-brochure. Mcfly is currently doing store-as-channel with 0 reviews — worse.

---

## 7. Crowded 0-review profit clones (dying-on-arrival)

Not dead. **Born into a full aisle.**

| App | Launched | Price | Reviews |
| --- | --- | --- | --- |
| TrackProfit | 2025-07-28 | $29.99 or $239 life | **0** |
| Profit Panel | 2025-12-04 | $18–$150 | **0** |
| MarginLens | 2026-05-14 | $9.99–$29.99 | **0** |
| ProfitIQ | 2026-08-14 | Free · $19 · **3-day** | **0** |
| Margn | 2026-08-18 | $19 / $39 / $79 · **7-day** | **0** |
| Mcfly | 2026-09-07 | $39 · **7-day** | **0** |

**Autopsy of the category, not of each founder:** the profit-tracker keyword is **saturated**. A new $39 card does not get a review for existing. Lifetimely’s free≤50 and TrueProfit’s 899 reviews are the **incumbent gravity**. Margn already copied “total spend / BE ROAS / data-health” and is still at 0.

`CURRENT_RELIGION` “prefer serious stores, no forever-free” + 7-day + $39 **places Mcfly in this table**, not in TrueProfit’s.

`RESEARCH_OPTION`: 14-day + a **free or ≤50-order on-ramp** (Lifetimely) **or** a Kleio-like $29 with a Monday artifact so someone writes the first review.  
`EVIDENCE`: this table + Lifetimely 535.  
`RISK`: freeloaders / uninstall ranking (TSC MARKET_REPORT). Official uninstall-rate weight is **unpublished**.

ProfitMetrics (3.5 / 8, launched 2022-10-24, $32) is the **four-year version** of the same story: launched, never loved, still listed.

---

## 8. Shopify killing its own analytics tiles

| Event | Date | Source |
| --- | --- | --- |
| Benchmark Comparisons in Analytics **removed** | 2026-05-19 | https://changelog.shopify.com/posts/benchmark-comparisons-in-analytics-will-be-removed-on-may-19th |
| Replacement named | Metric Targets + Sidekick | same |
| Merchant thread “revert Old Analytics” | 2025–2026 | https://community.shopify.com/t/shopify-needs-to-revert-back-to-old-analytics/418200 — staff/workaround names **Lifetimely** and **Report Pundit** |

**Autopsy:** first-party analytics is **unstable merchandising**. Third parties that **assembled profit or built the report for you** are what staff already recommend.

`RESEARCH_OPTION`: do not compete with Admin charts. Compete with the **gap Admin will not close** (ad spend ingest) and the **gap Admin keeps removing** (benchmarks — now a Sidekick upsell).  
`EVIDENCE`: changelog + Community 418200.  
`RISK`: ShopifyQL App Events (`shopify.dev/docs/apps/build/analytics`) lets Shopify pull “analytics apps” **into Admin**. A standalone iframe with no Admin tile is how Stocky-class products get replaced.

---

## 9. Changelog-abandon heuristic (what we could and could not prove)

We did **not** find a public “we are shutting down the Shopify analytics app” post for Segmetrics, Hyros, Wicked Reports, or Kissmetrics-on-Shopify this wave. Hyros / Wicked **404 on guessed handles** — treat as **sales-led / wrong handle**, not dead.

What we *can* use as an abandon signal without inventing:

| Signal | Example | Proven? |
| --- | --- | --- |
| Official sunset date | Stocky Aug 31, 2026 | Yes — Help Center |
| Acquisition press + 2 reviews / $119 | Metrilo | Yes |
| Acquisition press + missing listing card | Glew | Yes (card missing); product not proven dead |
| 1★ billing + “dying” in merchant voice | BeProfit | Yes — reviews; app still live |
| 16% 1★ | Triple Whale | Yes — listing UI |
| 0 reviews after ≥12 months at a real price | TrackProfit, Klar, Segmetrics | Yes — listing |
| 3.5 / 8 after 4 years | ProfitMetrics | Yes |
| Woo plugin 5 years stale | Metrilo WP | Yes |

**Do not** write a Kissmetrics / Heap / Amplitude / Mixpanel Shopify autopsy. No live listing fetch, no public Shopify obituary this wave.

---

## 10. What Mcfly should refuse to copy (religion)

| Failure mode | Who | Tag |
| --- | --- | --- |
| Order surcharge + ugly cancel | BeProfit 1★; TrueProfit surcharge still live | `CURRENT_RELIGION` keep flat |
| Metered AI credits | TW 1★ | `CURRENT_RELIGION` R10 |
| VAT in “revenue” | TW 1★ | `RESEARCH_OPTION` ship tax toggle |
| Listing live, product owned by email suite | Metrilo | Don’t become a feature inside someone else’s acq |
| Connector zoo as the company | Glew → PE | R9 refuse |
| Brochure listing, no reviews, no outbound | Klar / Mcfly-today | R11 — pick a channel |
| 7-day + $39 + 0 reviews in a 0-review peer set | Margn, Mcfly, ProfitIQ | `RESEARCH_OPTION` 14-day + TTV |
| Building what Shopify just announced it will native | Stocky class | Watch ShopifyQL, don’t clone Admin |

The aisle does not need another dead profit tracker. It needs a **first review**. Every autopsy above is a way to fail to get one, or to get the wrong ones.
