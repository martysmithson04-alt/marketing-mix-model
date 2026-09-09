# Research log — competitive 2026-09

**Mode:** research only. No production shipping.  
**Branch:** `research/competitive-2026-09`  
**Agent environment:** Cursor Cloud (not founder laptop).

Convention: every fetch is dated. `LIVE` = page retrieved this run. `MARKET_REPORT` = third-party writeup, not Mcfly-invented, still not gospel. `UNVERIFIED` = do not publish. Star-split percentages on Shopify listings are **rounded by Shopify’s listing UI**, not exact counts.

---

## 2026-09-09 — session 1: live Mcfly + category leaders

### Live Mcfly listing

- **URL:** https://apps.shopify.com/mcfly-analytics-public
- **Fetched:** 2026-09-09
- **Price:** $39/month, 7-day free trial
- **Reviews:** 0.0 (0 reviews)
- **Launched:** September 7, 2026
- **Hero:** “See ad spend next to store sales — including billboards. Total ROAS = sales ÷ spend you added.”
- **Refuse line:** “No pixels. No path credit.”
- **Shopify “More apps like this”:** Microsoft Clarity (4.6 / 2,125 / Free), WeTracked (4.8 / 125 / Free to install), Parkour Pixel (4.9 / 191 / Free)
- **Data access shown:** customers, orders, device/activity, store owner
- **Developer:** 7533 S Center View Ct STE N, West Jordan, UT, 94084, US

**Contradiction vs repo:** `docs/APP_STORE_LISTING.md` and `docs/MASTER_PLAN.md` still say free design-partner → ~$79 later. Live listing and live site (`https://mcflyads.com`, `https://mcflyads.com/pricing`) say **$39 / 7-day trial**. Live wins.

**Contradiction vs site repo `/site`:** local `site/index.html` still has schema.org Offer price `"0"` and “Free during early access. $79/mo flat at launch.” Live mcflyads.com has already moved. Treat `/site` as stale marketing draft.

### Live marketing site

- https://mcflyads.com — Total ROAS desk, SAMPLE Harbor Home Co lock ($23,414 spend / $82,068 sales / 3.51× / BE 2.50× @ 40%). $39/mo · 7-day trial. Paste/CSV/type-a-bill. Billboards OK.
- https://mcflyads.com/pricing — $39/store/mo; also **MDS Made Easy $79 one-time course**. Explicit anti-GMV-tax copy vs TW/Polar/Northbeam-class shapes. Does **not** publish competitor SKUs as gospel.
- https://mcflyads.com/product — formula Total ROAS = sales ÷ spend; BE ≈ 1 ÷ profit margin; paste-first; SyncWith optional (you pay them); **no ad-account OAuth**.

### Live competitor listings (same day)

| App | URL | Price (listing) | Rating | Reviews | Launched |
| --- | --- | --- | --- | --- | --- |
| Triple Whale | https://apps.shopify.com/triplewhale-1 | Free; Foundation $219/mo or $2,190/yr; Automate $749/mo or $7,490/yr; **external charges may apply** | 4.1 | 91 | 2020-12-04 |
| Polar Analytics | https://apps.shopify.com/polar-analytics | Core from $750/mo, GMV-based; external charges may apply | 4.9 | 116 | 2020-10-28 |
| Lifetimely | https://apps.shopify.com/lifetimely-lifetime-value-and-profit-analytics | Free (≤50 orders) / $49 / $149 / $299 by order volume; Amazon +$75 | 4.9 | 535 | 2019-02-19 |
| TrueProfit | https://apps.shopify.com/trueprofit | $35 / $60 / $100 / $200 + per-order surcharge | 5.0 | 899 | 2019-07-31 |
| Analyzify | https://apps.shopify.com/analyzify | $145 / $175 / $275 / $375 by order volume | 4.7 | 313 | 2021-01-28 |
| SyncWith | https://apps.shopify.com/syncwith | Free; Premium $4.99/mo | 4.5 | 10 | 2021-08-10 |
| BeProfit | https://apps.shopify.com/beprofit-profit-tracker | $49 / $99 / $149 / $249 by orders + shops | 4.5 | 202 | 2020-09-22 |
| Metorik | https://apps.shopify.com/metorik | $25 / $75 / $150 / $250 by orders | 5.0 | 48 | 2020-09-10 |
| Better Reports | https://apps.shopify.com/betterreports | $19.90 / $39.90 / $149.90 / $299.90 **tied to Shopify plan** | 5.0 | 1,199 | 2017-02-24 |
| Microsoft Clarity | https://apps.shopify.com/microsoft-clarity | Free | 4.6 | 2,125 | 2025-07-17 |
| WeTracked Connect | https://apps.shopify.com/wetracked-io-connect | Free to install; **external charges** | 4.8 | 125 | 2025-10-27 |
| Parkour Pixel | https://apps.shopify.com/parkour-pixel | Free | 4.9 | 191 | 2024-10-18 |
| Elevar | https://apps.shopify.com/gtm-datalayer-by-elevar | $225 / $650 / $1,250 + per-order overage | 4.7 | 168 | 2018-09-26 |

**TW star split (listing UI):** 79% 5★ · 1% 4★ · 2% 3★ · 1% 2★ · **16% 1★**. This is the only suite in the set with a visibly toxic 1-star pile. Polar 3% 1★, Lifetimely 2%, TrueProfit 1%, BeProfit 6%, Elevar 7%, Clarity 6%, WeTracked 4%.

**Shopify adjacency (TW listing “more like this”):** same Clarity / WeTracked / Parkour cluster as Mcfly. Polar’s cluster is **pixel apps** (Parkour, Nabu, another CAPI). TrueProfit’s cluster is **reports + profit** (Report Pundit 5.0/2,026; SyncWith reports; unnamed 4.9/76 profit+ROAS). Better Reports clusters with TrueProfit + Report Pundit.

---

## 2026-09-09 — session 2: App Store market mechanics (official)

### Shopify developer docs (LIVE)

- App Store overview: https://shopify.dev/docs/apps/launch/app-store-review
  - Listing is the **single source** for browse, admin recommendations, and Sidekick.
  - Billing must go through Shopify App Pricing / Billing API.
  - Reduced revenue share: 15% (from 20%); 0% on first $1,000,000 USD for eligible developers.
  - Built for Shopify is the promotion gate.
- Reviews: https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews
  - Only installed merchants (or within **45 days of uninstall**) can review.
  - Overall rating is **not a simple average** — weighted for recent / useful / trustworthy.
  - AI review summary requires **≥100 reviews with body text** and **≥4.0** rating; up to 14 days to appear.
  - Asking for *positive* reviews, incentives, install-time review nags = policy violation / possible demotion / unpublish.
  - Deep-link: `https://apps.shopify.com/[handle]#modal-show=WriteReviewModal`
- Built for Shopify: https://shopify.dev/docs/apps/launch/built-for-shopify
  - Benefits: listing highlight, card badge, search filter, **search ranking boost**, homepage/category eligibility, admin “Picked for you,” Sidekick, story pages, App Store ads plan-targeting, priority review.
  - Mandatory usefulness criteria include **minimum installs, reviews, rating** (exact thresholds not published on this page).
  - Repo `APP_STORE_LISTING.md` says “Do not chase Built for Shopify until ~50 paid-plan installs + 5 reviews.” Official page does **not** publish those numbers. Treat repo numbers as founder heuristic, not Shopify law.
- Listing requirements (fetched): https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements
  - Must bill through Shopify. Pricing must be accurate and complete (incl. trial).
  - **Do not include reviews/testimonials in listing copy or images.**
- Trials: https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials
  - Trial days configurable per plan.
  - Shopify **tracks trial days over a 180-day period** to stop reinstall-to-reset-trial abuse.
  - Trials only attach to **new** subscriptions.

### MARKET_REPORT (not official Shopify; do not treat as Mcfly metrics)

- Taylor Sicard / TSC, 2026 listing conversion: https://taylorsicard.com/blog/shopify-app-listing-conversion
  - Claims view-to-install ~3–8% for a “well-positioned” listing.
  - Claims <25 reviews → ~1–2%; 200+ reviews → ~5–8%.
  - First 50 reviews framed as the early-life investment.
- TSC pricing: https://taylorsicard.com/blog/shopify-app-pricing-strategy
  - Practitioner consensus (algorithm **not public**): install velocity, review velocity, uninstall rate.
  - Argues 14-day full-product trial > forever-free for qualified pipeline.
- Shopivibe pricing 2026: https://shopivibe.app/how-to-price-shopify-app
  - 14-day trial as default; 7-day if time-to-value is immediate; 30-day if value is slow.
  - Listed prices must match Billing API.
- GapQuery category pricing 2026: https://www.gapquery.com/blog/shopify-app-pricing-by-category
  - Claims median paid Shopify app entry **$9.99/mo**; average ~$31 pulled by premium tail.
  - Treat as MARKET_REPORT. Analytics/profit category live listings we fetched sit **well above** $9.99 (TrueProfit $35, BeProfit $49, Mcfly $39, Lifetimely $49 paid).

**Implication for Mcfly:** 0 reviews + 7-day trial + $39 + paste-first time-to-value that is **not** day-1 unless the merchant already has a CSV. Discovery math is structurally worse than Clarity (free, 2,125 reviews) and TrueProfit (5.0, 899).

---

## 2026-09-09 — session 3: real merchant problems (public)

### Shopify Community (LIVE)

1. https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4
   - Merchant (Ed) wants ROAS across Google / Facebook / Microsoft. Looker Studio connector costs add up.
   - Staff/community: Shopify “Sales attributed to marketing” exists; **Shopify does not ingest ad spend**. “You will need a third-party app.”
   - Thread remains open; **no consensus tool**. 111 views (page-stated).
2. https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805
   - 335 views / 18 likes / 11 users (page-stated, 2026-09 fetch).
   - Consensus: native Profit-by-product exists **if** Cost per item is filled; still missing ad spend, payment fees, shipping labels, app subs.
   - “Revenue is native, true net profit has to be assembled.”
   - Contribution-margin-first recommendation; layer **blended** ad spend at day/channel, do **not** pretend every order has a perfect CAC.
   - Historical COGS, late carrier adjustments, refunds reopening orders, platform disagreement.
   - Spreadsheets “always a week behind.”
3. https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628
   - Spreadsheet mess: Shopify fees + gateways + Meta/Google spend + shipping. “Always missing something.”
   - Warning: pull **TOTAL** ad spend, not attributed-only (understates cost).
4. https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364
   - Shopify settlements vs ads vs refunds. Suggested paths: 4Seller export; dedicated recon apps. Manual never fully dies.
5. https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915
   - Q3 numbers moved when re-pulled in Q4. Community: **30-day attribution lookback**.

### Reddit (public; some fetches timed out — titles/snippets used, mark as PUBLIC_SNIPPET)

- https://www.reddit.com/r/shopify/comments/1rpjuk0/best_way_to_track_meta_ads_roas_in_shopify/
  - “Dashboard discrepancy between Meta and [Shopify] drives everyone crazy, it will never sync up.”
  - Shopify last-click “typically shows 20–40% lower ROAS than Meta” — **commenter claim, not measured by us**.
  - Bare-minimum advice: spreadsheet of **total ad spend vs total Shopify revenue weekly** = blended ROAS / MER.
- https://www.reddit.com/r/shopify/comments/1jpb8cy/sales_attribution_tracking/
  - Overlap across Meta / Google / email / SEO. Triple Whale and Kendall “pretty expensive.”
- https://www.reddit.com/r/shopify/comments/1pzy8iv/app_or_plugin_to_calculate_profit_each_month/
  - Profit = orders + COGS + ad spend + fees. TrueProfit cited ~$35/mo as #1 in the space (commenter).
- https://www.reddit.com/r/shopify/comments/1h27sj3/beprofit_vs_lifetimely_vs/
  - Switching off TrueProfit for bugs / weak mobile. Alternatives: Finaloop, Taxomate → QB/Xero.
- https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/
  - Operator scaled wrong campaigns for months because Meta ≠ Shopify. Commenters: MER as honest top-line; independent attribution for channel split.
- https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/
  - North Star = blended MER / CAC / profit. Shopify/CRM = revenue+refunds source of truth. Daily table: channel, campaign, spend, sessions, orders, revenue, new/returning.
  - Agency commenter: $200k+/mo clients → ignore platform attribution; Sheets blended ROAS; 2-week Meta pause lift tests. Claims platforms overlap credit 40–60% — **commenter claim**.
- https://www.reddit.com/r/PPC/comments/1r2pvgy/question_for_d2c_founders_on_shopify_running_meta/
  - Scale on Shopify revenue; treat Meta as directional. “If Meta says $200k but Shopify says $150k then your true ROAS is 25% lower” — **commenter arithmetic**, not a study.
- https://www.reddit.com/r/PPC/comments/1pqv5kh/how_are_you_handling_ad_attribution/
  - Platforms for optimization; backend / blended MER as reality check. TW / Segmetrics / Hyros / GA4 / Looker all “work to varying degrees.”

### Official Shopify analytics (403 on help.shopify.com from this cloud; secondary citations)

- Help Center marketing reports (blocked here): https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/marketing-reports
  - Search snippet: last non-direct click default; last click / first click / any click / linear available when sales metric + marketing dimension.
  - Sales attributed to marketing **only** includes trackable marketing (admin campaigns or UTM). **Can differ from other sales reports.**
- ShopifyQL `shop_campaign_insights` (LIVE): https://shopify.dev/docs/api/shopifyql/latest/schemas/marketing/shop_campaign_insights
  - Shop Campaigns only: sales, ad spend, ROAS, CAC. **Not** Meta/Google/TikTok spend ingest.
- ShopifyQL FROM/SHOW: https://shopify.dev/docs/api/shopifyql/latest/syntax/from-and-show
  - `marketing_engagements` = engagement/spend/order/sales **reported by marketing channels for marketing events**. Still not a cash desk for arbitrary billboards.

---

## 2026-09-09 — session 4: adjacent enterprise / finance

- A2X (MARKET_REPORT, not live-fetched listing this run):
  - Eightx review 2026-06-18: https://eightx.co/blog/compare/reviews/a2x-for-ecommerce-review — settlement-to-GL; QuickBooks / Xero / Sage / NetSuite; claimed $29–$1,039/mo per channel; claimed Shopify 4.9/329 (verify before publish).
  - LetsMetrix: https://letsmetrix.com/app/a2x — payout categorization; wholesale B2B; POS.
  - Official NetSuite connect: https://support.a2xaccounting.com/en/articles/7211660-connecting-a2x-to-netsuite
- Northbeam (LIVE homepage + docs; pricing = MARKET_REPORT):
  - https://www.northbeam.io/ — MTA + incrementality + MMM; Apex passback.
  - Apex docs: https://docs.northbeam.io/docs/northbeam-apex — Meta Custom Attribution; order-level CAPI; invite-only live optimization historically, broader rollout claimed June 2026.
  - Pricing writeups disagree on exact spend gates (mbuzz vs Botapolis). **Do not publish a Northbeam price sheet.** Safe statement: public third parties describe a **~$1,500/mo floor, spend-scaled, no free plan**.
- Polar MER language (LIVE marketing): https://www.polaranalytics.com/integrations/reddit-ads — blended ROAS, MER, CAC after “platform overclaiming is removed” via Polar Pixel. MER is a **tile inside a pixel religion**, not the product.
- Triple Whale vs Polar 2026 (vendor blogs; treat as marketing):
  - https://www.triplewhale.com/blog/triple-whale-vs-polar-analytics — TW claims 60,000 brands, Polar 4,000; G2 4.5/470+ vs 4.7/21.
  - https://www.polaranalytics.com/vs/triple-whale — Polar claims ~$400/mo start in this page (conflicts with App Store $750 Core). **Conflict flagged.**
  - Talk Shop: https://www.letstalkshop.com/blog/triple-whale-vs-polar-analytics — Polar free starter + Core ~$720; TW Foundation ~$219.
- TW pricing page (LIVE fetch saved): https://www.triplewhale.com/pricing — GMV slider; Foundation / Automate / Enterprise; 12-month contracts discussed; listing $219/$749 are **entry band** only. Venon 2026-07-26 snapshot of GMV bands: https://venon.io/blog/triple-whale-pricing (MARKET_REPORT).
- TW listing review sample (LIVE visible 3):
  - 5★ Cocaine Coffee (US, 2 days): world-class + support; **AI usage limits on Foundation not warned**.
  - 1★ Kove Footwear (NL, 1 day): CS unreachable; AI credits extra; **VAT included in revenue**.
  - 5★ Marielle Stokkelaar (NL, 2+ years): support praise.

---

## 2026-09-09 — session 5: finance listing + synthesis

- A2X LIVE: https://apps.shopify.com/a2x — **5.0 / 359** (Eightx MARKET_REPORT said 329 — stale). Mini $29 / Basic $45 / Pro $79 / Advanced $115; 30-day trial; Magic summary on; Works with Amazon, NetSuite, PayPal, QuickBooks, Sage, Xero. Rail includes TrueProfit.
- Northbeam homepage LIVE vendor claims: 1000+ companies; $130B attributed; $25B spend; 2.1T impressions; “37% ROAS / 14% CVR / 20% CAC” for Enterprise customers — **VENDOR_CLAIM**.
- Margins by Finaloop: https://apps.shopify.com/margins — **Free**, 5.0 / 1 review, “True ROAS… based on profit.”
- DB built: `db/competitive.sqlite` from JSONL (21 competitors, 22 review quotes, 50 sources, 15 problems).

---

## Enterprise landscape session (2026-09-09)

Imported unique artifacts from PRs #5–#13 without wipe. Live re-fetch:

- Mcfly listing **WebFetch 200**: still $39 / 7-day / **0.0 (0)** / launched Sept 7 2026 / Total ROAS hero / adjacent Clarity **2127**, WeTracked 125, Parkour 191.
- Kleio listing **WebFetch 200**: $29 / 14-day / **5.0 (20)** / 100% 5★ / Trek Light, EMME, Hummii visible.
- TrueProfit listing **WebFetch 200**: from $35 + surcharge / **5.0 (900)** — Wave A had 899.
- Analytics aisle **WebFetch 200**: still **1,546 apps**; first screen pixels/heatmaps; TrueProfit 900 visible on page.
- Official: revenue-share, BFS requirements, manage-app-reviews, offer-free-trials, listing categories — all 200.
- Community 134251 / 657805 / 588628 — 200; “Shopify doesn’t measure spend”; “revenue is native, true net profit has to be assembled”; “TOTAL ad spend not attributed-only”.
- Kleio / TrueProfit / Lifetimely / Northbeam / Hyros / Measured sites — 200. Northbeam/Hyros still **no public price**.
- Bulk `apps.shopify.com` crawl: **50 HTTP 429** after ~20 200s. Recorded. Wave C JSON-LD remains source for those handles.
- Guessed handles (hyros, stape, blotout, godmode, …): **404**. Sales-led sites fetched instead.
- Reddit HTML: bot challenge (`FETCH_FAILED` this wave).
- Triple Whale site pricing: one WebFetch **timeout**.
- Elevar.com/pricing resolved to an unexpected Audiense page — **do not cite**.
- DB assemble: **106 competitors · 61 problems · 80 quotes · 300 sources**.

## 2026-09-09 — session 6: PRIMARY_SOURCE_HARVEST (append-only)

- **Lane:** ENTERPRISE research support. Coordinates with ENTERPRISE_LANDSCAPE; does **not** rewrite landscape / synthesis / competitor cards.
- **Deliverable:** [`PRIMARY_SOURCE_HARVEST.md`](./PRIMARY_SOURCE_HARVEST.md) + `db/harvest_*.jsonl`.
- **Method:** live GET of Shopify listing pages (JSON-LD + visible price/trial/launched), Shopify Community + Reddit (paraphrase + URL), Kleio / TrueProfit / Polar / TW public docs.
- **Rule:** no card without a URL. Failed fetches stay `confidence=fetch_fail` and are not published as numbers.
- Fetcher: `db/harvest_primary.py` + `db/render_harvest.py`.
- **Live yield:** **214** listing cards · **9** Community threads (HTTP 200) · **13** Reddit rows (`public_snippet` — HTML/JSON 403 from this cloud) · **17** competitor-doc claims · **253** harvest source URLs.
- Price parser note: ignore Shopify chrome “Free to install” / “Free trial.” Mcfly live = **$39/month**, 7-day, 0.0/0. Polar listing still prints a Free card beside **$750/month** Core — do not resolve that conflict here.
- Sitemap used for discovery only: https://apps.shopify.com/sitemap_apps_en.xml

---

## Open questions (do not invent answers)

1. Actual Mcfly listing views / installs / trial starts — Partner Dashboard only. Not in this repo.
2. ~~Exact Built for Shopify numeric gates.~~ **Closed:** 50 net paid-plan installs + 5 reviews ([BFS requirements](https://shopify.dev/docs/apps/launch/built-for-shopify/requirements)). Rating number still unpublished.
3. Whether live Mcfly app already has LTV + Goals as claimed on the listing (repo `APP_FEATURES.md` still says LTV later). Listing still claims them 2026-09-09.
4. Northbeam official public price card — homepage does not print dollars. **Reconfirmed this wave.**
5. Polar $400 (own vs page) vs $750 (App Store) vs ~$720 (Talk Shop).
6. SyncWith Shopify $4.99 vs older `COMPETITORS.md` $25–$150 refresh-tax ladder (likely Workspace vs Shopify SKU split).
7. World-wide VAT handling — TW 1-star is a live landmine Mcfly must not copy.
8. First-party interviews — scripts exist; **zero** completed rows.

---

## Decision log (research, not product)

| Decision | Why |
| --- | --- |
| Live listing + live site override repo drafts | Founder-facing truth |
| Treat TSC conversion % as MARKET_REPORT | Not Shopify-official; useful as industry gossip |
| Rank WTP by **public review volume + price paid**, not by Mcfly theology | Maximize money/love/ease/real problems |
| Keep religion flexible in this folder | Founder instruction this run |
| Do not ship pixels/OAuth from this work | Research only |
