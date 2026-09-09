# Personas — who actually buys the adjacent category

**Date:** 2026-09-09  
**Rule:** Personas are inferred from **public listings, reviews, forums, and vendor marketing**. No invented “we interviewed 40 CFOs.” Each persona lists: job, Monday question, current stack pattern, willingness-to-pay **signals** (not dollar forecasts), love/ease failure modes, and Mcfly fit vs RESEARCH_OPTION.

Four-score lens: money · love · ease · real problem.

---

## P1 — Owner-operator / founder (sub-scale to ~low-seven-figure)

**Monday question:** “Did ads make us money this week, or am I kidding myself?”

**Where they talk (public):**
- Shopify Community profit-tracking thread: https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805 — “spreadsheets / an app / just guessing”
- r/shopify profit-per-month: https://www.reddit.com/r/shopify/comments/1pzy8iv/app_or_plugin_to_calculate_profit_each_month/
- r/shopify Meta ROAS: https://www.reddit.com/r/shopify/comments/1rpjuk0/best_way_to_track_meta_ads_roas_in_shopify/

**Current stack pattern (public, not private data):**
- Shopify Analytics for sales.
- Meta Ads Manager + Google Ads for “ROAS.”
- A Google Sheet that is “always a week behind” (Community 657805).
- Maybe a free pixel (Parkour 4.9/191 Free — https://apps.shopify.com/parkour-pixel) or Clarity (4.6/2,125 Free — https://apps.shopify.com/microsoft-clarity).
- If they pay, the modal paid app in this band is **TrueProfit $35+** (5.0 / 899 — https://apps.shopify.com/trueprofit) or Lifetimely free/S $49 (4.9 / 535).

**WTP signals:**
- They already pay $35–$149 for **net profit**, not for a philosophy.
- They install **free** pixels/heatmaps at huge volume (Clarity 2,125 reviews).
- They bounce off Triple Whale / Kendall as “pretty expensive” (https://www.reddit.com/r/shopify/comments/1jpb8cy/sales_attribution_tracking/).

**Love / ease:**
- Love = “I opened it and saw if I made money.” TrueProfit review language: “must need to see how much you're actually making” (GowiLab, 2026-05-26, listing).
- Hate = manual CSV every Monday. Mcfly’s paste-first religion is **developer-easy, founder-hard**.

**Mcfly today (`CURRENT_RELIGION`):**
- Answers blended Total ROAS vs break-even if they paste spend.
- Does **not** auto-pull COGS, fees, shipping, or ad APIs.
- $39 sits **next to** TrueProfit Basic $35 — same wallet, thinner job.

**RESEARCH_OPTION:** Become the “Monday cash + costs” app (profit-lite): Shopify sales + total spend + optional COGS/fees. Evidence: Community 657805 contribution-margin recipe. Risk: collide with TrueProfit’s 899-review moat.

---

## P2 — Media buyer / growth operator (in-house)

**Monday question:** “What do I scale in Ads Manager today without lying to the founder about cash?”

**Where they talk:**
- r/PPC Meta≠Shopify: https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/
- r/PPC holistic view: https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/
- r/PPC D2C founders: https://www.reddit.com/r/PPC/comments/1r2pvgy/question_for_d2c_founders_on_shopify_running_meta/

**Current stack pattern:**
- Live in Meta/Google/TikTok UIs all day.
- Shopify Admin as **backend truth** for revenue + refunds.
- Server-side / CAPI so the **algorithm** gets events (Elevar 4.7/168 from $225 — https://apps.shopify.com/gtm-datalayer-by-elevar; WeTracked 4.8/125; Analyzify 4.7/313).
- Triple Whale if the brand will pay for a daily OS (listing Free / $219 / $749 — https://apps.shopify.com/triplewhale-1).
- Northbeam if spend is large enough that a ~$1,500 floor is not a joke (MARKET_REPORT, not official card).
- Homegrown: “single daily table (channel, campaign, spend, sessions, orders, revenue, new/returning)” — r/PPC 1qgb8mg.

**WTP signals:**
- They will pay **hundreds to thousands** when the tool changes **how they bid** (pixels, CAPI, Apex, Sonar).
- They will **not** pay $39 for a desk they must feed by CSV if Ads Manager already shows a (lying) ROAS.
- WeTracked 5★: “I can track inside of Meta ad manager and I do not have to use another dashboard” (isella, 2026-09-01). That is a **kill shot against Mcfly’s extra-desk thesis**.

**Love / ease:**
- Love = fewer tabs + algorithm fed.
- Ease = OAuth + pixel, not paste.
- Hate = another login that does not write back to Meta.

**Mcfly today:**
- Useful as the **cash governor** the founder forces on the buyer.
- Useless as the buyer’s daily tool unless spend syncs itself.

**RESEARCH_OPTION A — OAuth spend sync (not pixel):** pull spend only, still refuse path credit. Evidence: TrueProfit bullet “Real-time sync ad spends from Facebook, Google, TikTok…” on https://apps.shopify.com/trueprofit. Risk: Meta/Google App Review calendar; becomes a connector shop.
**RESEARCH_OPTION B — pixel/CAPI (`CURRENT_RELIGION` forbids):** evidence of WTP is overwhelming (Parkour Free 191 reviews; Elevar $225+). Risk: become theater, compete with free apps, violate brand.

---

## P3 — Agency / multi-brand operator

**Monday question:** “How do I show 8 clients a comparable scoreboard without 8 Triple Whale seats and 8 arguments?”

**Where they talk:**
- SyncWith reviews (affiliate sheets, multi-store exports): https://apps.shopify.com/syncwith — Spool And Spindle uses it to share “real time sales data with affiliates.”
- Polar listing: “Omnichannel reporting: One view across brands, stores, markets and channels” — https://apps.shopify.com/polar-analytics
- BeProfit 1★ Adrienne Landau (2026-04-22): someone installed in 2023, company paid **$720/year never used**, cancel/refund ignored — agency/ops landmine.
- r/PPC 1qgb8mg: agency at $200k+/mo client spend builds **Sheets blended ROAS** + incrementality pauses.

**Current stack pattern:**
- Google Sheets as the agency OS (SyncWith / Supermetrics / Coupler).
- Per-client Triple Whale or Polar when the retainer can absorb it.
- Looker Studio when the client wants a “deck.”
- Manual Monday slides.

**WTP signals:**
- SyncWith Shopify listing is **$4.99 Premium** (LIVE) — cheap pipe, not a decision product. Older Mcfly `COMPETITORS.md` $25–$150 ladder is likely a different (Workspace) SKU. Flag contradiction.
- Polar $750+ GMV is an agency-unfriendly **client-GMV tax**.
- Agencies already pay connector tax; they will pay for a **white-label Monday scoreboard** if it is faster than Sheets.

**Love / ease:**
- Love = one login, many stores, export to Slack/PDF, client-safe language.
- Hate = per-store $39 * 30 clients if they cannot resell / seat it.

**Mcfly today:**
- Listing is **per store $39**. No agency plan on https://mcflyads.com/pricing.
- Paste-first is actually **agency-native** (they already live in Sheets). This is the one persona for whom CURRENT_RELIGION is not insane.

**RESEARCH_OPTION:** Agency workspace: N stores, shared template, client-safe Total ROAS pack, billed per seat or per portfolio. Evidence: Polar unlimited users; Metorik multi-store from $75 (5 stores) — https://apps.shopify.com/metorik. Risk: support load; becomes SyncWith.

---

## P4 — Finance / controller / fractional CFO

**Monday question:** “What number do I put in the board pack that I can reconcile to Shopify payouts and the bank?”

**Where they talk:**
- Community recon: https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364
- Community 657805: contribution vs full P&L; “cost incomplete” flag preferred to fake precision.
- A2X public positioning (MARKET_REPORT): settlement → QuickBooks/Xero/Sage/NetSuite. https://eightx.co/blog/compare/reviews/a2x-for-ecommerce-review
- TW 1★ Kove Footwear: **VAT included in revenue** — finance will torch a tool for this.

**Current stack pattern:**
- Shopify payouts + Payments reports.
- A2X / Taxomate / Finaloop → QuickBooks or Xero (r/shopify 1h27sj3).
- NetSuite at mid-market+ (A2X NetSuite docs exist: https://support.a2xaccounting.com/en/articles/7211660-connecting-a2x-to-netsuite).
- Native Shopify “Profit by product” if Cost per item is maintained.
- They do **not** trust Ads Manager ROAS. They may not trust Triple Whale either (VAT, modeled revenue).

**WTP signals:**
- A2X is a paid, review-dense finance category (Eightx cites 4.9/329 — verify). This is **real WTP** for recon, not for MER poetry.
- Better Reports 5.0 / 1,199 — https://apps.shopify.com/betterreports — priced to **Shopify plan** ($19.90–$299.90). Finance-adjacent “give me the report I cannot get in Admin.”
- They will not pay for MTA. They will pay for **definitions**.

**Love / ease:**
- Love = audit trail: sales definition, tax treatment, refund timing, spend source, margin source.
- Hate = “Total ROAS” if it is not specified as net vs gross, VAT in/out, shipping in/out.

**Mcfly today:**
- Formula is clean (sales ÷ spend) but **underspecified for finance** (which Shopify sales field? taxes? returns? gift cards?).
- Live site says “Shopify Total Sales after returns” on the SAMPLE — good. Listing says “store sales.” Repo mer-core does not encode tax policy.
- No payout recon. No QB/NetSuite. No VAT toggle.

**RESEARCH_OPTION:** Finance-grade cash desk: explicit sales definition, tax toggle, spend ledger with source docs, export journal. Evidence: Community recon thread + TW VAT 1-star. Risk: become a worse A2X; accounting is a different buyer.

---

## P5 — Mid-market / enterprise DTC pod (growth + finance + creative)

**Monday question:** “Which measurement system is the court of appeal, and who is allowed to change spend?”

**Where they talk / are sold:**
- TW vs Polar vendor pages (2026): https://www.triplewhale.com/blog/triple-whale-vs-polar-analytics · https://www.polaranalytics.com/vs/triple-whale · https://www.letstalkshop.com/blog/triple-whale-vs-polar-analytics
- Northbeam: https://www.northbeam.io/ + Apex docs https://docs.northbeam.io/docs/northbeam-apex
- Polar listing review (Chicory, 2025-09-24): “multi-touch attribution and incrementality testing have been especially valuable.”
- Elevar review (Old Bones Therapy, 2026-06-23): “backbone of our tracking stack” — audit of GA4/Meta/Google/Reddit dedupe.

**Current stack pattern (public patterns only — no invented private stacks):**
Observed **patterns**, not a census:

| Pattern name | Public ingredients | Who it serves |
| --- | --- | --- |
| **TW OS** | Triple Pixel + Moby + Compass + Sonar; Free→$219→$749 listing floors, GMV-scaled behind the slider | Operator-led $1M–$40M narrative (Talk Shop / TW blog) |
| **Polar warehouse** | Dedicated Snowflake story + 45+ connectors + Polar Pixel + Causal Lift; App Store from $750 | Data-mature / multi-store / EU-friendly (FR/DE languages on listing) |
| **Northbeam court** | MTA + MMM + incrementality + Apex passback; ~$1.5k floor MARKET_REPORT | High media spend; finance-defensible second opinion |
| **Sheets + Domo/Looker** | Shopify + ad connectors + semantic model in BI | Teams that already have a data person; Community 134251 started here |
| **Elevar + suite** | Server-side events into Meta/GA4/Klaviyo, then TW/Polar/NB on top | Brands that treat tracking as infrastructure, measurement as a second buy |
| **Profit + pixel split** | TrueProfit/Lifetimely for cash; Parkour/WeTracked/Analyzify for algorithms | Cost-conscious operators who refuse a $750 OS |

**WTP signals:**
- They already pay **$219–$1,250+/mo per tool**, often **two tools** (tracking + measurement).
- Polar 4.9/116 and Elevar 4.7/168 reviews are **onboarding/CS love**, not DIY.
- TW 4.1/91 with 16% 1★ shows the hangover: AI credit meters, CS, VAT.

**Mcfly today:**
- Not in their consideration set. Shopify files Mcfly next to **free pixels**, not Polar.
- $39 is **below the seriousness line** for this persona (can read as “toy”).
- Anti-pixel religion is a **feature** for the CFO and a **disqualifier** for the media lead.

**RESEARCH_OPTION:** Sell Mcfly as the **cash overlay** that sits on top of TW/NB/Polar — “the number finance signs.” Evidence: r/PPC already uses MER as North Star while keeping a suite. Risk: they already get MER as a tile (Polar lists MER; TW has a MER definition that `docs/COMPETITORS.md` claims is inverted — re-verify before attacking).

---

## P6 — Wholesale + DTC / multi-store / omnichannel (adjacent, not core)

**Monday question:** “Which channel is carrying the brand — DTC ads, Amazon, wholesale, POS?”

**Signals:**
- Polar: Amazon + Shopify + markets (listing).
- Lifetimely: Shopify+Amazon; Amazon add-on **$75/mo** (listing).
- Metorik: Shopify + Woo, multi-store from Level 2.
- BeProfit: “across all your shops”; Plus = unlimited shops $249.
- A2X: wholesale B2B sync (LetsMetrix description).

**Mcfly today:** Shopify-only, single store, ads-only spend. Wholesale margin structure is a **different MER**.

**RESEARCH_OPTION:** Channel P&L (DTC vs Amazon vs wholesale vs POS) with ad spend only on the channels that actually spent. Evidence: Lifetimely/Polar Amazon language. Risk: inventory/COGS hell.

---

## Persona × four scores (research judgment)

| Persona | Money if Mcfly wins them | Love likelihood now | Ease of current Mcfly | Real problem match |
| --- | --- | --- | --- | --- |
| P1 Founder | Medium ARPU, high volume if reviews exist | Low until auto-spend or profit | Poor (CSV) | Partial (they want profit) |
| P2 Media buyer | High if OAuth or pixel | Low (they want Ads Manager) | Poor | Strong (Meta≠Shopify) but unsolved daily |
| P3 Agency | Highest LTV if portfolio SKU | Medium (Sheets-native) | Medium | Strong (scoreboard) |
| P4 Finance | High ARPU, slow sales cycle | Medium if definitions tighten | Medium | Strong (recon/tax) — product thin |
| P5 Enterprise pod | Highest ARPU, worst win-rate as replacement | Low as replacement; medium as overlay | Low | Strong as overlay |
| P6 Omni | High, late | Low | Low | Weak today |

**Uncomfortable conclusion:** The persona who most loves CURRENT_RELIGION (anti-pixel cash desk) is **P4 finance** and the **P3 agency that already lives in Sheets**. The persona who generates App Store review velocity is **P1 via profit** and **P2 via pixels**. Mcfly is currently packaged for a hybrid that barely reviews.

---

## Messaging that each persona actually uses (quote bank)

Do not put testimonials on the App Store listing (Shopify req 4.3.7 — https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements). Use on site / sales only, attributed.

| Voice | Quote / paraphrase | Source |
| --- | --- | --- |
| Founder | “I feel like I’m always missing something and my ‘profit’ numbers never feel accurate.” | Community 588628 |
| Community builder | “Revenue is native, true net profit has to be assembled.” | Community 657805 |
| Operator | “The dashboard discrepancy between Meta and [Shopify] drives everyone crazy, it will never sync up.” | r/shopify 1rpjuk0 |
| Operator | “use backend revenue or blended MER as the reality check” | r/PPC 1pqv5kh |
| Agency | “I ignore platform attribution completely and build blended ROAS dashboards in Google Sheets” | r/PPC 1qgb8mg (commenter) |
| Finance | VAT-in-revenue is a 1-star event | TW listing, Kove Footwear, 2026-07-06 |
| Buyer | “I can track inside of Meta ad manager and I do not have to use another dashboard.” | WeTracked listing, isella, 2026-09-01 |

That last line is the **strategic threat**: the market’s loved products disappear into Ads Manager or into a profit number. Mcfly insists on being a third desk.

---

## Wave 2 — decision rights

See **`DEEP_DIVE_BUYERS.md`**. Short version:

- **App Store reviewer** = founder-operator (P1).  
- **Budget mover** = media buyer (P2) or CMO (P5).  
- **Veto** = finance (P4) on VAT / definitions.  
- **Agency (P3)** recommends; **client store** pays and reviews.  
- Some mid-market pods run **TW + Polar** (D2C Times MARKET_REPORT). Mcfly as replacement is cope; Mcfly as overlay is a motion (S4).

Kleio is now the P1 peer. Polar remains the P5 peer. Do not write one listing for both.
