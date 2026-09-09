# DEEP_DIVE — International: VAT/GST, multi-currency, multi-store

**Date:** 2026-09-09  
**Wave:** deeper. Session 1 flagged TW VAT 1★ as an open landmine. This file is that landmine plus GST, Markets, FX, and multi-store.

**Rule:** do not invent tax law. Cite public product docs, listings, and merchant posts. Tax treatment is a **definition problem**, not a legal opinion.

---

## 0. Why this kills trust faster than a wrong ROAS model

A media buyer will argue models forever. A Dutch or UK founder will **1-star you in a day** if revenue includes VAT they must remit.

**Live existence proof:** Kove Footwear, NL, 1-day review on https://apps.shopify.com/triplewhale-1 (wave 1): VAT included in revenue; “revenue should never be including VAT.”

That is not a feature request. It is a **religion** in EU commerce. Get it wrong and you are done in that market.

---

## 1. VAT / GST — the definition war

### 1.1 Triple Whale: help center vs docs vs review

| Source | Date on page | Claim (paraphrase) |
| --- | --- | --- |
| https://kb.triplewhale.com/en/articles/10201911-is-vat-international-sales-tax-included-in-the-sales-metric | 2026-07-26 | VAT is **not** in the Sales metric. Add VAT as a **custom variable expense** if you want it in. |
| https://triplewhale.readme.io/docs/order-revenue | live fetch | Order Revenue = Gross + **Shipping + Taxes** − Discounts (before refunds) |
| https://triplewhale.readme.io/docs/total-sales | live fetch | Total Sales = Gross + Shipping + **Taxes** − Discounts − refunded sales/shipping/tax |
| App Store 1★ Kove Footwear | 2026-07-06 (wave 1) | VAT is included in revenue; should never be |

**`EVIDENCE`:** a global suite can publish **three incompatible stories** about tax. Merchants will believe the number they see, then the bookkeeper, then the 1-star.

**`RESEARCH_OPTION`:** never ship a metric named “Sales” without a subtitle: `ex-VAT` / `inc-VAT` / `Shopify Total Sales (tax-in)`. Default by shop country **or** force a first-run toggle.  
**`RISK`:** US merchants think Shopify Total Sales = the truth (tax-in). EU merchants think tax-in is fraud. There is no universal default.

### 1.2 TrueProfit / EU dropshippers

**URL:** https://www.reddit.com/r/dropshipping/comments/1s3mx43/how_do_you_guys_actually_calculate_your_real/

**Paraphrase:** OP — TrueProfit pulls Shopify and does not account for VAT; numbers ≠ bank; fell back to Excel. Commenter — VAT can be **activated** in TrueProfit; ask CS.

Sibling PR #5 already flagged TP excluding VAT from net without showing collection. This wave adds: **even when the toggle exists, discoverability is a CS ticket.** Hidden tax toggles = 1-stars.

**`CURRENT_RELIGION`:** typed margin, no tax policy in mer-core (wave 1).  
**`RESEARCH_OPTION`:** first-class `tax_mode` on every desk. Evidence: Reddit + TW 1★ + Klar pricing **net of taxes**.  
**`RISK`:** Shopify tax lines (inclusive vs exclusive, Markets, VAT OSS) are a swamp. Do not claim compliance.

### 1.3 Klar’s pricing language (packaging, not law)

https://getklar.com/pricing — monthly fee is based on last-12-month **net revenue after returns and taxes**.

They sell **controlling**. They priced on the same definition finance wants. Mcfly’s anti-GMV page can steal the **phrase** (“we never count VAT as a sale”) without stealing the GMV meter.

### 1.4 Taxomate / A2X — the actual VAT products

**Taxomate listing (LIVE search + listing card):** https://apps.shopify.com/xero-taxomate  
- From **$14/mo** (200 orders) / $24 / $44 / $79 · 14-day · **5.0 / 6** on Shopify (tiny). Site claims 200+ reviews on other stores (`VENDOR_CLAIM`).  
- Features on card: tax rates, multi-currency, **EU (VAT)** registration language.  
- Job: Shopify Payments **payout summaries** → Xero/QB (sales, discounts, refunds, fees, shipping, taxes).  
- Reviews (visible older): cheaper than A2X; multi-marketplace; CS onboarding.

**A2X:** already carded 5.0/359 from $29. NetSuite/QB/Xero/Sage.

**`EVIDENCE`:** finance will **keep** a GL connector regardless of Mcfly. Mcfly must **agree** with the GL’s tax treatment or lose.  
**`RESEARCH_OPTION`:** export a definition pack a bookkeeper can tick: tax-in/out, shipping-in/out, gift cards, refunds. Do **not** post journals.  
**`RISK`:** becoming Taxomate.

### 1.5 GST / other sales taxes (do not invent)

No Community thread in this fetch that is GST-specific at the same signal strength as VAT. Treat **GST (AU/NZ/SG/IN/CA)** as the **same product problem**: inclusive vs exclusive, remit vs keep, Markets.

Avalara appears on **Recharge** Works-with. International tax engines sit **under** subscription and checkout, not inside MER apps. Mcfly should **read Shopify tax lines**, not compute nexus.

**`UNVERIFIED`:** do not publish “Mcfly handles GST.”

---

## 2. Multi-currency — FX is a silent ROAS lie

### 2.1 What listings already admit

- Report Pundit: **multi-store and currency**; Markets reports on Advanced $35.  
- Polar: markets / brands / stores (wave 1).  
- Klar site: multiple currencies & currency conversion (`VENDOR_CLAIM`).  
- Better Reports: Shopify-plan priced; POS + Markets in the same aisle.

### 2.2 Failure modes (`INFERRED` from product anatomy + Community recon)

| Failure | What happens | Who explodes |
| --- | --- | --- |
| Spend in USD, sales in EUR, ratio as if same | MER is garbage | Anyone with Markets |
| Shopify shop currency vs presentment currency | AOV and ads disagree | EU selling to US / vice versa |
| Ad accounts in local currency, Shopify in shop currency | Daily paste from Ads Manager is the wrong FX day | Mcfly paste-first **especially** |
| Refund in a later FX rate | Net sales ≠ original conversion value | Finance |

**`EVIDENCE`:** Mcfly paste-first **guarantees** FX error for any non-USD-only shop unless the CSV is shop-currency.  
**`RESEARCH_OPTION`:** lock desk to **shop currency**; convert spend with a dated rate or refuse to compute. Show `FX: not applied` rather than a quiet wrong 3.51×.  
**`RISK`:** FX API / ECB rates / “which rate” fights.

### 2.3 Shopify Markets

Report Pundit and Polar sell Markets as a **report dimension**. Mcfly is single-store, ads-only. A Markets brand has **several tills**. One blended MER across Markets without spend-by-market is how you scale the **wrong country**.

**`RESEARCH_OPTION`:** later — MER by Market if Shopify gives sales by Market and the merchant can tag spend.  
**`CURRENT_RELIGION`:** one till. Honest only for one-currency shops.

---

## 3. Multi-store / multi-entity

### 3.1 Who already sells it

| App | Live signal |
| --- | --- |
| Polar | “brands, stores, markets” · $750 · unlimited users |
| Metorik | Multi-store from $75 (5 stores) · 5.0/48 |
| BeProfit | Plus unlimited shops $249 |
| Report Pundit | Multi-store on Advanced $35 |
| Lifetimely | Amazon +$75 |
| Klar | Multi shop & business unit (site) |
| Kleio | Unlimited users; not clearly unlimited *shops* on the $29 card (1,000,000 orders) — **do not assume multi-store** |
| Mcfly | **$39 per store** · no portfolio |

### 3.2 Why multi-store kills a naive cash desk

- Transfer / wholesale between shops is not “sales.”  
- Shared ad accounts across two myshopify domains.  
- EU GmbH + US LLC: two VATs, one agency.  
- Agency scoreboard needs **comparable definitions** across clients (see `DEEP_DIVE_BUYERS.md`).

**`RESEARCH_OPTION`:** agency / portfolio SKU (C4) with **per-store currency + tax mode**.  
**`RISK`:** support load; Kleio $29 unlimited users already undercuts a seat story.

---

## 4. Language, hosting, GDPR — distribution, not features

| Signal | Klar | Polar | Mcfly |
| --- | --- | --- | --- |
| Listing languages | EN | EN, FR, DE | EN |
| Hosting story | EU + ISO 27001 claimed | FR roots / warehouse | US mailbox |
| Shopify reviews | 0 | 116 | 0 |
| Off-store reviews | OMR 129 (MARKET_REPORT) | G2 small | none |

Klar proves you can **skip the App Store review game** and still sell in DACH — **if** you have outbound + a local review site. Mcfly does not.

**`RESEARCH_OPTION`:** if EU is a target, GDPR/DPA one-pager + tax-ex-VAT default matters more than a FR translation.  
**`CURRENT_RELIGION`:** US founder-operator. Fine — then **do not** put “including billboards” next to a pixel rail and hope Munich finds you.

---

## 5. Problems that kill trust (checklist)

Use this as a design-partner interrogation, not as shipped scope:

1. Is “sales” **inc** or **ex** VAT/GST?  
2. Is shipping revenue in the numerator?  
3. Are gift cards sales or liability?  
4. Refund date vs order date?  
5. Exchange / store credit vs cash refund?  
6. Shop currency vs presentment vs ad-account currency?  
7. Which shop, if many?  
8. Does the number move when re-pulled (lookback)?  
9. Can a bookkeeper tick the same boxes in Xero?  
10. Is the toggle visible **without** a CS ticket?

Fail any of 1, 6, 8, 10 in the EU and you are Kove.

---

## 6. Religion

| ID | Topic | CURRENT | OPTION | EVIDENCE | RISK | Call |
| --- | --- | --- | --- | --- | --- | --- |
| I1 | Tax | Unspecified | `tax_mode` + subtitle | TW 1★ + KB vs docs; r/dropshipping 1s3mx43 | Support | **Do** |
| I2 | FX | Ignore | Shop-currency lock or refuse | RP Markets; paste FX | Rates | **Do lock** |
| I3 | Multi-store | Per store $39 | Portfolio | Polar/Metorik/RP | Support | S3 later |
| I4 | EU GTM | App Store EN | Outbound + DPA + ex-VAT default | Klar 0 Shopify reviews + OMR | Dilution | Only if EU is a goal |
| I5 | Price basis | Anti-GMV | Keep flat; steal Klar’s *net after tax* language | getklar.com/pricing | Accidental GMV | Language only |

Open question from RESEARCH_LOG #7 (world-wide VAT) is **not closed** — we now know it is a **product-definition** problem with public corpses, not a mystery.

---

*Not legal advice. Re-fetch TW KB if attacking VAT in public copy.*
