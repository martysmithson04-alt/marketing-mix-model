# Shopify App Store category topology — where Mcfly sits vs where money is

**Fetched:** 2026-09-09  
**Official taxonomy:** https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories  
**Live Analytics aisle:** https://apps.shopify.com/categories/store-management-operations-analytics/all (**1,546 apps** stated on page)  
**Live Store management hub:** https://apps.shopify.com/categories/store-management

Religion is flexible. Topology is not: Shopify’s graph already filed Mcfly next to free pixels (`README.md` live snapshot).

---

## 1. Two maps that people confuse

### A. Developer taxonomy (what you pick on the listing form)

Seven **top-level categories** (official table):

1. Sales channels  
2. Finding products  
3. Selling products  
4. Orders and shipping  
5. Store design  
6. **Marketing and conversion**  
7. **Store management**

**Analytics is not a top-level category.** Official placement:

> Store management → Operations → **Analytics**  
> “Apps that analyze and generate insights or recommendations for a store.”

Finances (accounting / taxes) is a **sibling subcategory** under Store management, not under Analytics.

**Marketing and conversion** is the paid-traffic / email / checkout / upsell / reviews / loyalty tree. Ads, affiliate, email, SMS, abandoned cart, product reviews, loyalty live **here**, not under Analytics.

Shopify’s own tip on that page: research similar apps and use *their* categories; QA can reclassify you. Appeals exist if capabilities change.

### B. Merchant-facing chips on a listing

Mcfly live listing chips (WAVE A snapshot, re-confirmed in HTML 2026-09-09): **Marketing and sales · Visuals and reports**.

Those are **feature groups inside Analytics**, not the top-level “Marketing and conversion” category. Proof from live Kleio listing feature links:

- `https://apps.shopify.com/categories/store-management-operations-analytics/all?feature_handles[]=cf.analytics.marketing_and_sales.roas`
- `https://apps.shopify.com/categories/store-management-operations-analytics/all?feature_handles[]=cf.analytics.visuals_and_reports.analytics_dashboard`

So “Marketing and sales” on Mcfly’s card means **the ROAS / profit-insights / purchase-tracking feature cluster of the Analytics aisle**. It does **not** put Mcfly on the Marketing and conversion navbar next to Klaviyo / TikTok / Smile.

`CURRENT_RELIGION` mistake: reading the listing chips as “we are in marketing.”  
`EVIDENCE`: feature_handles namespace is `cf.analytics.*`.  
`RISK` of leaving it: Shopify’s similarity graph already clustered Mcfly with Clarity / WeTracked / Parkour (free pixels). Same aisle, same merchandising.

---

## 2. What the Analytics aisle actually merchandises

Live page title: **“Best Analytics Apps For 2026”**. Copy: “Stay on top of what's working…” **1,546 apps.**

Visible first screen (order as fetched; not a ranking Mcfly invented):

| Visible card | Reviews (page-stated) | Price chip | Job |
| --- | --- | --- | --- |
| Parkour: Facebook Pixel & Feed | 191 | Free | Meta Pixel + CAPI |
| MIDA Replay, Heatmap & Insight | 561 | Free plan | Replays / heatmaps |
| IndexGPT: AI SEO for ChatGPT | 142 | Free plan | LLM SEO — **not finance** |
| Propel Replay, Survey, Heatmap | 676 | Free plan | Replays / heatmaps |
| Microsoft Clarity | **2,125** | Free | Replays / heatmaps |
| Grapevine Post Purchase Survey | 221 | Trial | Attribution *surveys* |
| (unnamed survey, 549) | 549 | Free plan | Post-purchase / NPS |
| TA MAPPY Store Locator | 440 | Free plan | Maps — **not finance** |
| Ⓩ Facebook Pixel Tiktok Pixel | 166 | Free plan | Pixels |
| Sort'd Prime Collection Sort | 143 | Free plan | Collection merchandising |
| (pixel/CAPI, 397) | 397 | Free plan | Meta/TikTok pixel |
| Parkour TikTok Pixel | 30 | Free | TikTok CAPI |
| Juicy-class profit (76) | 76 | Free plan | Profit + ROAS |
| **Report Pundit** | **2,026** | Free plan | Custom reports |
| Meta & Facebook Pixels by Nabu | 116 | Free to install | Meta pixel |
| wetracked.io Connect | 125 | Free to install | Ad tracking pipe |
| Mipler Advanced Reports | 633 | Free plan | Custom reports |
| ∞ Facebook/TikTok Pixel | 257 | Free plan | Pixels |
| TiXel | 88 | Free plan | Pixels |
| RealtimeStack | 107 | Free plan | Live store analytics |
| Escalafy (ES) | 79 | Free plan | “Dejá el Excel” |
| **TP: True Profit Analytics** | **899** | Trial | Net profit |

Store management **hub** Analytics module (https://apps.shopify.com/categories/store-management) repeats the same merchandising: Parkour, MIDA, IndexGPT, Propel, **Clarity 2,125**, Grapevine, MAPPY, pixel apps.

**Brutal topology fact:** Shopify’s Analytics shelf is a **pixel / heatmap / replay / survey / maps** supermarket. Profit P&L is a **late card**. Custom reports (Report Pundit 2,026; Mipler 633) out-review most profit trackers because they are **utilities with free plans**.

TrueProfit is the highest-review **paid profit** object that appears on that first fetch. Mcfly does not appear. Mcfly cannot appear: 0 reviews.

---

## 3. Where the review-money actually is (adjacent trees)

These are **not** Analytics. They are where merchants already have the habit of installing and reviewing.

| Surface | Example live listing | Rating / reviews | Price chip | Why it matters |
| --- | --- | --- | --- | --- |
| Official ad channel | [TikTok](https://apps.shopify.com/tiktok) | 4.8 / **15,912** | Free to install | Channel apps print reviews Mcfly will never match |
| Official ad channel | [Facebook](https://apps.shopify.com/facebook) | 3.8 / **5,648** | Free to install | Volume + **hate** (3.8) — merchants review channels |
| Official ad channel | [Microsoft Advertising](https://apps.shopify.com/microsoft-advertising) | 3.0 / **348** | Free to install | Low love, still more reviews than Polar |
| Loyalty | [Smile.io](https://apps.shopify.com/smile-io) | 4.9 / **4,568** | Free plan | Retention/LTV *habit* lives here, not in Analytics |
| Email | [Omnisend](https://apps.shopify.com/omnisend) | 4.7 / **3,179** | Free to install | Marketing and conversion money |
| Loyalty | [LoyaltyLion](https://apps.shopify.com/loyaltylion) | 4.6 / **532** | Free to install | LTV-adjacent, different aisle |
| Page builders | GemPages 4.9/4,220 · Shogun 4.8/1,972 | paid + free | Store design review gravity |
| Heatmaps *inside* Analytics | Clarity 4.6/2,125 · Lucky Orange 4.7/878 | Free / $19+ | Same aisle as Mcfly, opposite TTV |

Navbar sibling: https://apps.shopify.com/categories/marketing-and-conversion — this is ads / email / checkout / reviews / loyalty. Mcfly is **not** in that tree unless Shopify reclassifies the listing.

`RESEARCH_OPTION`: pick feature tags that match **profit insights + COGS + custom reports**, and screenshot a P&L-ish desk, so collaborative filtering has a chance to leave the Parkour rail.  
`EVIDENCE`: TrueProfit’s WAVE A rail was Report Pundit + profit apps, not Clarity. Live Analytics page still *shows* TrueProfit among pixels — the aisle is mixed — but TrueProfit has 899 reviews to pull the graph.  
`RISK`: we do not control the algorithm. Copy changes without reviews will not move the shelf.

---

## 4. Feature-handle map Mcfly can actually tick

From live Kleio / ScaleAble / Signal CRO listings, Analytics feature handles include:

**Customer behavior:** real-time tracking, activity, events, segmentation, page views, **LTV**, loyalty analysis, cohort analysis  

**Marketing and sales:** AI insights, marketing attribution, checkout analytics, **ROAS**, **profit insights**, purchase tracking, funnel, UTM, abandoned cart, **pixel tracking**

**Visuals and reports:** analytics dashboard, custom dashboards, multi-store, custom reports, data export, historical analysis, forecasting, scheduling, notifications, GDPR

Mcfly’s live listing already claims LTV + Goals as paid extras (`README.md`). Ticking **pixel tracking** or **marketing attribution** to chase the rail would be **factual-listing fraud** (requirements 1.1.4) unless the app ships them.

`CURRENT_RELIGION`: no pixels, no path credit. Then **do not tick pixel tracking / MTA feature handles**.  
`RESEARCH_OPTION`: tick **profit insights + ROAS + historical analysis + data export** and make the first screenshot look like a till, not an ads graph.  
`EVIDENCE`: feature URLs above; App Store requirements 1.1.4.  
`RISK`: QA can still reclassify; “More like this” may stay pixel until reviews exist.

---

## 5. Money vs love vs aisle (research judgment, not a metric)

| Aisle | What Shopify merchandises | Who prints reviews | Who prints dollars |
| --- | --- | --- | --- |
| Analytics (1,546 apps) | Free pixels + heatmaps first | Clarity / Report Pundit / Propel | TrueProfit $35–$200; Polar $750; Elevar $225–$1,250; Daasity $1,899 |
| Marketing and conversion | Ads, email, reviews, loyalty | TikTok / Smile / Omnisend | Klaviyo-class (listing not fetched this wave) |
| Finances | Accounting / taxes | A2X 5.0/359; Synder 4.8/217 | A2X $29–$115; Finaloop $245 / $995; Synder $65–$599 |
| Native Admin | Free | No App Store reviews | Included in Shopify plan |

Mcfly’s **wallet** is the profit cluster ($29–$49 entry). Mcfly’s **shelf** is the pixel cluster (Free). That mismatch is the distribution failure WAVE A named. WAVE C adds: the mismatch is **structural in the taxonomy**, not a one-week glitch.

---

## 6. Ongoing.AI category counts — MARKET_REPORT only

https://ongoing.ai/categories claims 122 niches, snapshot **June 12, 2026**, ranked by review volume (SEO, product reviews, upsell, email first; Analytics further down). **Do not publish those counts as Mcfly metrics.** Use only as a pointer that **review volume is not in Analytics**.

---

## 7. Native Analytics is also moving (Shopify as competitor)

- Benchmark Comparisons in Analytics **removed May 19, 2026**. https://changelog.shopify.com/posts/benchmark-comparisons-in-analytics-will-be-removed-on-may-19th — replacement: Metric Targets + Sidekick.
- ShopifyQL / App Events / analytics-queryable metafields: https://shopify.dev/docs/apps/build/analytics — Shopify is inviting apps to **put metrics inside Admin Analytics**, not only in a third-party iframe.
- Merchant revolt on “New Analytics”: https://community.shopify.com/t/shopify-needs-to-revert-back-to-old-analytics/418200 (2025–2026 thread; staff reply cites Lifetimely and Report Pundit as workarounds).

`RESEARCH_OPTION`: ship Mcfly numbers as ShopifyQL-compatible / Admin-embedded cards (BFS 3.1.4 + new Analytics platform). That is a **distribution** play, not an MTA play.  
`EVIDENCE`: official Analytics building-blocks page.  
`RISK`: App Events registry is standard-event only; cash MER / billboard spend may not have a standard handle. Do not invent one.

---

## 8. Mcfly placement — one sentence

Mcfly is a **2-day-old, 0-review, $39** card whose feature chips put it in a **1,546-app Analytics aisle that Shopify’s own homepage merchandises as free pixels**, while the money Mcfly wants sits in a **profit-insights / finances / custom-reports** minority of that aisle plus an outbound Polar/Northbeam market that barely uses the store.
