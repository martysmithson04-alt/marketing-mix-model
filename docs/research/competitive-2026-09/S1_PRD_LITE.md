# S1 PRD-lite — Cash governor (RESEARCH_OPTION)

**Date:** 2026-09-09  
**Wave:** E (architecture stress-test)  
**Mode:** RESEARCH ONLY. This is **not** a ship order and does **not** amend `docs/MASTER_PLAN.md`.  
**Score inherited:** Wave B `VNEXT_OPTION_SCORECARD.md` scored S1 **19 / 25** (Money 3 · Love 4 · Ease 4 · Feasibility 3 · Religion-flex 5).  
**This file’s job:** specify S1 hard enough that a founder can kill it. Then downscore it.

Companion files in this wave: `KLEIO_GAP_ANALYSIS.md` · `INTEGRATION_MAP.md` · `COMPLIANCE_LANDMINES.md` · `STRATEGY_KILL_CRITERIA.md`.

---

## 0. One-sentence product

A period-matched **cash desk**: Shopify sales (explicit definition) ÷ **total** ad spend (OAuth or paste), a labeled **Ads Manager claim vs till** card, tax/shipping/returns modes a bookkeeper can recite, and a **Monday Close** artifact that visits the merchant.

Not a pixel. Not a P&L suite. Not a connector zoo. Not Triple Whale.

**Critical correction vs Wave B:** Kleio already ships the commercially adjacent product at **$29 / 14-day / 5.0 (20)** with hourly Meta/Google spend, a published CM1–CM3 waterfall, a tax toggle, order-date vs accounting-date clocks, campaign-name spend filters, and an MCP server. S1 at $39 is not “the empty chair.” It is a **late, thinner Kleio** unless the claims-vs-cash card and offline ledger are actually first-class and actually used.

---

## 1. Why S1 existed (and why 19/25 is generous)

Wave B’s 19 rests on **Religion-flex 5**. That axis rewards “MASTER_PLAN already wanted Phase 2 OAuth.” It does **not** reward uniqueness, money expansion, or legal cleanliness.

| Axis | Wave B | Stress-test | Why the original score is soft |
| --- | --- | --- | --- |
| Money | 3 | **2** | $39 flat still has no ladder. Kleio is **$10 cheaper** with a bigger desk. Money theory is “conversion + retention,” which is a MARKET_REPORT hope (TSC), not a public Mcfly metric. |
| Love | 4 | **3** | Monday email is a *hypothesized* Better Reports loop. Kleio’s 5-stars are for a **daily P&L pulse**, not a weekly sermon. Push without a loved number is spam. |
| Ease | 4 | **3–4** | OAuth can hit ≤10 min **if** tokens stay alive. Kleio’s own docs: Meta user tokens **expire in 60 days and cannot be auto-refreshed**. That is the product. |
| Feasibility | 3 | **2** | Two App Reviews (Meta Advanced Access + Google Ads developer token / Basic Access) + Shopify PCD if we keep `read_orders` + claims-vs-cash that pulls platform **conversions** (Meta ads-data mix rule — see `COMPLIANCE_LANDMINES.md`). Not “one worker.” |
| Religion-flex | 5 | **4** | Spend-only OAuth is the authorized bend. Pulling Ads Manager **purchase value** to draw the lie is a second bend: it is still not MTA, but it **is** platform theater on our glass, and it may be a Meta policy problem. |
| **Sum** | **19** | **14–16** | S1 remains the least-incoherent App Store path. It is no longer the obvious default once Kleio is priced into the room. |

**Keep S1 on the menu if** the founder will own App Review calendar and will **not** compete with Kleio on P&L depth.  
**Kill S1 as “the product” if** the loved number must be net profit (that is S2) or if App Store is abandoned (that is S3).

---

## 2. Problem, buyer, non-goals

### 2.1 Job to be done

> “Admin has sales. Ads Manager has a ROAS. They will never match. I need **one cash number** for the same days, and I need to see **how big the lie is**, without becoming the third attribution model.”

Public evidence (already in the corpus):

- Shopify does not ingest Meta/Google/billboard spend — Community [134251](https://community.shopify.com/t/which-ppc-reporting-tool-to-use-for-multiple-advertising-channels/134251/4).
- Operators already do this in a weekly Sheet — r/shopify [1rpjuk0](https://www.reddit.com/r/shopify/comments/1rpjuk0/best_way_to_track_meta_ads_roas_in_shopify/); r/PPC [1qgb8mg](https://www.reddit.com/r/PPC/comments/1qgb8mg/how_do_you_build_a_reliable_holistic_view_across/).
- People who scaled the wrong campaign because Meta ≠ Shopify — r/PPC [1u81q7r](https://www.reddit.com/r/PPC/comments/1u81q7r/my_shopify_and_meta_numbers_have_never_matched/).
- Finance hates VAT-in-revenue — Triple Whale 1★ (Kove Footwear, NL) on [triplewhale-1](https://apps.shopify.com/triplewhale-1).

### 2.2 Personas S1 claims

| Persona | What S1 must do for them | What S1 must not pretend |
| --- | --- | --- |
| **P1 founder** | One number vs break-even by Monday | That Total ROAS is net profit |
| **P2 media buyer** | Spend appears without CSV; claim vs till is a screenshot they can Slack | That Mcfly will change how they bid (that is pixel/CAPI) |
| **P4 finance** | Named sales definition, tax mode, spend source, export | That Mcfly posts to QuickBooks (A2X’s job) |

P3 (agency) and P5 (enterprise overlay) are **later SKUs**, not S1 v1. If those are the real buyers, pick S3/S4 instead of dressing them as S1.

### 2.3 Explicit non-goals (S1)

| Out | Why | If you want it |
| --- | --- | --- |
| Pixel / CAPI / MTA | Religion + Parkour Free 191 + WeTracked 1★ evidence failure | S5 / S5b |
| Assembled COGS / fees / shipping P&L | Years-long cost engine; Kleio/TrueProfit already own it | S2 |
| Multi-store portfolio billing | Different packaging | S3 |
| Dual-clock accrual vs payout as a *company* | A2X 5.0/359 | S4 sentence, not S1 core |
| Connector zoo (TikTok+Snap+Pinterest+Microsoft+AppLovin+ShipHero+Klaviyo) | Kleio already lists these. Copying them is how S1 becomes S2 without the wedge. | Kill |
| Allocation that assumes sales ∝ spend without a warning | Already shipped; media buyers will 1-star it | Tighten or hide |

---

## 3. Scope (three rings)

S1 is easy to over-scope because Wave B bundled A1+A2+A3+A6+B3. That bundle is a **company**. Split it.

### 3.1 Ring 0 — already shipped (do not rebuild)

From `docs/APP_FEATURES.md` + `app/prisma/schema.prisma` + `packages/mer-core`:

- Embedded Shopify app, `read_orders`, GDPR webhook stubs.
- Manual Meta / Google / Other spend (`SpendEntry`).
- MER = sales ÷ spend; BE ≈ 1 / typed `marginPct`.
- `suggestAllocation()` with silent sales∝spend if no `salesContribution`.
- Overnight `SyncRun` + `MerSnapshot` + 5% recon kill (MASTER_PLAN §11).
- Connector **stubs** (`MockMetaSpendClient` / `MockGoogleSpendClient`).

**Integrity hole S1 inherits:** live listing claims LTV + Goals; repo says Later / Planned. S1 must **not** add more listing fiction.

### 3.2 Ring 1 — S1-minimum (the only honest “governor”)

Ship-or-kill unit if S1 is ever chosen:

1. **Spend ingest:** Meta + Google **spend-only** OAuth **or** paste/CSV. Same `SpendDay` fact table. TikTok is not Ring 1.
2. **Sales definition v1:** stop summing raw `orders.totalPriceSet` without a named mode (see §5). Default published.
3. **Claims-vs-cash v1:** one card, one period, Meta **and/or** Google **purchase/conversion value they report** vs Shopify till. Labeled **their claim**. Paste allowed if API conversion pull is blocked by policy.
4. **Tax mode v1:** include-tax / exclude-tax toggle that changes the till number and is printed on the Monday artifact.
5. **Monday Close v1:** email (not Slack) with the five numbers in §8. Unsubscribe. No install-time review nag.
6. **14-day trial** (billing config). Works-with: Shopify Admin, Meta Ads, Google Ads, CSV. Review modal **after** first period with spend>0.

Ring 1 is still a **religion bend** (live site currently says “no ad-account OAuth”). Founder must amend MASTER_PLAN §1–§4 before any of this is production.

### 3.3 Ring 2 — S1-plus (only after Ring 1 is loved)

- TikTok spend OAuth.
- Slack / PDF of the same Monday artifact.
- Cash CAC = total spend ÷ new customers (Shopify `customer.numberOfOrders == 1` **or** first-seen-in-period — pick one, disclose).
- Campaign **include/exclude by name** (Kleio already has this; copy only if multi-account / multi-geo stores churn without it).
- Manual `salesContribution` required before allocation **cut/shift** (already planned in APP_FEATURES).
- Agency seat (that is S3 creeping in — price it separately).

### 3.4 Ring 3 — not S1 (kill if it appears in an S1 PR)

COGS engine, ShipHero, Klaviyo, MCP write-back, product draft-from-AI, GL export, pixel, GMV tax, order meter, “explain this number” credits.

---

## 4. Data model (proposed — research, not a migration)

Today’s schema cannot express S1. `SpendEntry` is a **blob of money over a range**. `MerSnapshot` has one `sales` float and no definition. `Settings` has a typed margin and nothing else.

### 4.1 Facts (append-only where possible)

```text
Shop
  Settings                 — margin fallback, target MER, tax_mode, sales_basis, clock
  SpendAccount             — one connected ad account (platform, external_id, status)
  SpendDay                 — grain: shop × account × campaign? × utc_date × source
  ClaimDay                 — grain: shop × account × utc_date × window (optional)
  SalesDay                 — grain: shop × utc_date × definition_id
  Definition               — versioned sales/tax/clock recipe (immutable once used)
  CloseArtifact            — Monday email payload + delivery log
  MerSnapshot              — keep; add definition_id + recon fields
```

#### SpendAccount

| Field | Notes |
| --- | --- |
| `platform` | `meta` \| `google` \| `tiktok` \| `manual` |
| `external_account_id` | act_… / customer id |
| `oauth_status` | `connected` \| `expiring` \| `expired` \| `revoked` \| `error` |
| `token_expires_at` | Meta user tokens: **60 days** (Kleio docs, LIVE). Treat expiry as a first-class UX, not a Sentry surprise. |
| `scope` | stored string; S1 must **not** request `ads_management` write |
| `currency` | account currency; FX is Ring 2 |
| `include_filter` / `exclude_filter` | optional campaign-name contains; default empty = all spend (AP1: **total** spend) |

#### SpendDay

| Field | Notes |
| --- | --- |
| `date` | account timezone **or** shop timezone — pick one, print it |
| `amount` | cash spend, **not** attributed spend |
| `source` | `oauth` \| `csv` \| `typed` \| `mock` |
| `campaign_id` / `campaign_name` | nullable; Ring 1 can roll to account-day |
| `ingested_at` | freshness |
| `superseded_by` | late conversions / spend restatements |

**Religion constraint:** spend is **what left the ad account**, not “spend Meta associated with a purchase.” Community [588628](https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628): attributed-only spend **understates** cost.

#### ClaimDay (the dangerous table)

| Field | Notes |
| --- | --- |
| `date` | same clock as SpendDay |
| `claimed_revenue` | platform-reported conversion value |
| `claimed_purchases` | optional |
| `attribution_window` | e.g. Meta `7d_click` / `1d_view` — **must be printed** |
| `source` | `oauth` \| `paste` |
| `label` | always `"platform_claim"` — never `"sales"` |

If Meta’s “do not mix advertising data across platforms” rule blocks storing ClaimDay next to Google spend in one merchant-facing card, **S1 Ring 1 degrades to paste-a-claim**. That is still a product. See `COMPLIANCE_LANDMINES.md` §Meta.

#### SalesDay

| Field | Notes |
| --- | --- |
| `date` | shop timezone |
| `gross_sales` | product (+ shipping if mode says so) |
| `discounts` | |
| `returns` | |
| `shipping_revenue` | |
| `tax` | |
| `gift_cards` | include/exclude |
| `till` | **the number that enters MER** after Definition |

Mcfly today: paginate `orders { totalPriceSet.shopMoney.amount }` (`app/app/lib/shopify-sales.server.ts`). That is **order total as Shopify stored it**, usually tax-in, shipping-in, refunds **not** netted unless the order object already reflects them. It will **not** match Shopify Finance Summary the way Kleio’s docs claim to. S1 without SalesDay is a 1-star factory.

#### Definition (immutable recipe)

```text
id, version, created_at
sales_basis:     order_date | accounting_date
tax_mode:        include | exclude
shipping_in_till: true | false
gift_cards_in_till: true | false
returns_mode:    net_in_period | attach_to_order_date
currency:        shop
notes:           one sentence a bookkeeper can read aloud
```

Snapshots and Monday artifacts store `definition_id`. Changing a toggle **does not rewrite history**; it computes a new series. TW VAT 1-star is what happens when you silently include tax and call it revenue.

### 4.2 Derived (never stored as source of truth)

```text
MER              = SalesDay.till(period) / sum(SpendDay.amount)
BE_MER           = 1 / marginPct          // S1 still typed; assembled margin is S2
claim_gap        = ClaimDay.claimed_revenue - SalesDay.till     // $ 
claim_ratio      = ClaimDay.claimed_revenue / SalesDay.till     // ×
cash_cac         = spend / new_customers  // Ring 2 only
```

Do **not** store “channel MER” unless `salesContribution` is manual. Silent ∝ is already in `allocation.ts` and is a credibility bomb (`RELIGION_FLEX.md` R8).

### 4.3 What we refuse to model in S1

- Path / session / click IDs
- Pixel event match quality
- SKU-level ad allocation
- Bank payouts as the till (that is A2X / ShopifyQL `payouts`, a different clock)

---

## 5. Shopify sales definition (the finance surface S1 actually is)

Kleio’s public metrics doc is the adult version of this section: [getkleio.com/docs/getting-started/metrics](https://getkleio.com/docs/getting-started/metrics). They match Shopify **Total sales** when tax is included, and they **document every row that does not match** Finance Summary. S1 that cannot do that sentence will lose P4 in week one.

### 5.1 Shopify’s own split (LIVE ShopifyQL)

From [ShopifyQL `sales` schema](https://shopify.dev/docs/api/shopifyql/latest/schemas/sales_revenue/sales):

```text
total_sales = net sales + additional fees + duties + shipping charges + taxes
```

`payouts` is a **different schema**: deposits Shopify sent, not sales. Using payouts as MER sales is an S4/A2X confusion. S1 must not.

### 5.2 Tax modes (S1 v1)

| Mode id | Till | When to default | Landmine |
| --- | --- | --- | --- |
| `tax_in` | Shopify Total sales (tax + shipping as Shopify defines) | US stores that display tax-in; “match Admin Total sales” | EU/UK 1-stars if this is the only mode (TW Kove) |
| `tax_out` | Total sales − net tax on products and shipping | VAT/GST markets; “cash that isn’t the taxman’s” | Must net **refunded tax** or the number drifts |
| `product_only` | Product net sales, no shipping, no tax | Rare; operators who want “goods MER” | Understates till vs bank; label loudly |

**v1 default:** inherit the shop’s tax-display setting (Kleio does this) and show a one-line “Till = Shopify Total sales, tax {in\|out}.”  
**v1 required toggle:** `tax_in` ↔ `tax_out` on the desk **and** on the Monday artifact.  
**v1 out:** per-country VAT rates, OSS, marketplace facilitator — that is A2X.

### 5.3 Shipping and returns

| Question | S1 v1 answer | Not v1 |
| --- | --- | --- |
| Is shipping revenue in the till? | **Yes** in `tax_in`/`tax_out` (it is cash). Optional `product_only`. | Analyzing shipping as a lever (Kleio’s reason for folding it into Gross Sales) |
| Are refunds netted in the period they happen? | **Yes** (`accounting_date`) as default — matches “what hit the till this week” | Order-date attach + E(return) forecast (Kleio `(O)` and `E(CM3)`) |
| Gift cards | **Exclude** from till (not cash from goods) | Gift-card liability aging |
| Tip / duties / additional fees | Include if Shopify `total_sales` includes them; disclose | Line-item museum |

**Dual clock:** S1 v1 ships **one** clock (`accounting_date`) plus a footnote: “Refunds land on the day they were processed.” Order-date + expected-return model is Kleio’s acquisition page, not S1 Ring 1. Adding it is how S1 becomes S2.

### 5.4 Implementation options (research)

| Source | Grain | PCD | Reliability | S1 fit |
| --- | --- | --- | --- | --- |
| Current: paginate `orders.totalPriceSet` | Order | Level 1 (orders **are** PCD) | Breaks on refunds, pagination cost, definition opacity | **Replace** |
| ShopifyQL `FROM sales SHOW total_sales, taxes, … TIMESERIES day` | Day | Reports scope (`read_reports`) — still commerce data | Matches Admin reports; one query | **Preferred till** |
| ShopifyQL `FROM payouts` | Payout | Payments | Wrong clock for MER | Refuse as till |
| Order webhook + local warehouse | Order | Level 1–2 if PII stored | Needed for LTV/CAC (Ring 2) and S2 | Not Ring 1 |

S1 Ring 1 should **prefer ShopifyQL sales**, not rebuild Kleio’s order warehouse. That is the feasibility save.

---

## 6. Spend OAuth surfaces

Detail and cost in `INTEGRATION_MAP.md`. This section is the **product** surface.

### 6.1 Connections page (replace the stub)

Current: `/app/connections` is a Phase 2 stub (`APP_FEATURES.md`).

S1 Connections is a **status board**, not a logo wall.

| Row | States | Merchant action |
| --- | --- | --- |
| Shopify sales | `live` / `error` / `definition_changed` | Open definition sheet |
| Meta spend | `connected` / `expiring (<14d)` / `expired` / `needs_review` | Connect · Reconnect · Paste CSV |
| Google spend | same | same |
| Manual / billboard | `has_rows` / `empty` | Add / CSV |
| Claim (Meta) | `oauth` / `paste` / `off` | Optional |
| Claim (Google) | same | Optional |

**Copy rule:** “Connect spend. We do not place a pixel. We do not write campaigns. We do not send conversions to Meta.”

### 6.2 OAuth ask (minimum)

**Meta**

- Permission: `ads_read` (and Insights fields: `spend`, `campaign_id`, `campaign_name`, `date_start`).
- Do **not** request `ads_management` (write) in S1. Over-scoping is a documented App Review reject reason.
- Advanced Access required to read **other people’s** ad accounts ([Marketing API access levels](https://developers.facebook.com/docs/marketing-apis) / Partner practice: Standard = own assets, Advanced = third-party).
- Business Verification.
- Token: user long-lived ≈ **60 days**. Kleio documents they **cannot auto-refresh** and they **email before expiry**. S1 must do the same or the Monday number lies.
- System User tokens do not expire but require the merchant to add a system user in **their** BM — worse UX than 60-day reconnect for SMB. Agency (S3) is the System User case.

**Google Ads**

- Developer token on a **manager** account ([official](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)).
- Access: Explorer (2,880 ops/day production) → Basic (15,000; typical review **5 business days** claimed) → Standard (unlimited; **10 business days** + demo if external tool).
- Permissible use: **Reporting** (Search / SearchStream only) — do not apply for ad creation.
- OAuth scope: `https://www.googleapis.com/auth/adwords` (read via token; still a broad brand-feeling consent screen).
- Brand verification of the GCP project may be required for Basic Access.
- MCC / `login-customer-id` header: merchants under an agency MCC will fail without it. This is the #1 “Google connect is hard” support ticket in every profit app. Budget a help article **before** launch.
- Metric: `metrics.cost_micros / 1_000_000` by `segments.date` at campaign or account grain.

**TikTok:** Ring 2. Kleio lists it as OAuth Beta. Do not let “parity with Kleio’s logo row” pull S1.

### 6.3 Reconciliation (already a kill criterion)

MASTER_PLAN §11: Meta + Google spend within **~5% of Ads Manager for 14 days** or hard pivot.

S1 must expose:

| Check | Fail look |
| --- | --- |
| Coverage | Days with sales and **zero** spend while accounts are `connected` |
| Drift | `sum(SpendDay)` vs merchant-pasted Ads Manager total (optional weekly confirm) |
| Currency | Account currency ≠ shop currency without FX note |
| Timezone | Account TZ vs shop TZ (Meta midnight ≠ Shopify midnight) |
| Token | `expiring` / `expired` blocks the Monday send or stamps it `INCOMPLETE` |

`MerSnapshot.reconDelta` already exists. Wire it to **SpendDay**, not to vibes.

### 6.4 CSV / paste (does not go away)

S1 without CSV is a religion break against billboards (live listing hero). Template:

```text
date,channel,amount,currency,note,source_doc
2026-09-01,billboard,2400,USD,Q3 transit,invoice-441
2026-09-01,meta,0,USD,,  # do not double-count OAuth days
```

Rules:

- OAuth days **win** for that platform unless the merchant marks `override`.
- CSV for Meta on a day that also OAuth’d is a conflict row, not a silent sum.
- Attributed-only exports (Ads Manager “results” spend) are rejected with a sentence, not ingested.

---

## 7. Claims-vs-cash UX (the only S1 wedge Kleio does not publish)

Kleio’s public FAQ is **anti-attribution** and **pro-platform-optimization**: “Meta is extremely good at what they do… no reason to believe a third party… can consistently provide better attribution.” ([getkleio.com](https://getkleio.com/)) They pull **spend**. They do **not**, on any public doc fetched this wave, productize “Ads Manager said $X, Shopify said $Y, here is the gap.”

That gap is Mcfly’s **only** non-price differentiation that is still on-religion.

### 7.1 The card (one screen)

```text
PERIOD     2026-09-01 → 2026-09-07   clock: shop TZ, accounting_date
TILL       Shopify sales    $82,068   tax_out · shipping in · gift cards out
SPEND      Ads + billboards $23,414   Meta OAuth + Google OAuth + $2,400 CSV
CASH       Total ROAS         3.51×   BE 2.50× @ 40% typed margin

THEIR CLAIM (not cash)
  Meta purchase value     $104,200    window: 7d click / 1d view
  Google conv. value      $ 61,400    data-driven, click
  Sum of claims           $165,600    ⚠️ claims are allowed to overlap
  Claim ÷ till              2.02×     platforms claimed 2× the till
```

**Copy that must be on the card, not in a tooltip:**

1. Platform numbers are **their claim**. They can overlap. Summing Meta+Google claims is **theater math** shown only to prove the overlap.
2. Cash uses **till ÷ spend**, never claim ÷ spend.
3. Attribution window is printed. Changing it changes the claim, not the till.

### 7.2 Interaction

| Action | Result |
| --- | --- |
| Toggle tax | Till and cash ROAS move; claim does not |
| Toggle window (if API allows) | Claim moves; till does not |
| “Hide claim” | Card collapses to cash only (P1 default after week 1) |
| Export | CSV of till, spend, claim, gap, definition_id |
| Screenshot mode | SAMPLE watermark if demo numbers |

### 7.3 What we will be tempted to do, and must not

| Temptation | Why it dies |
| --- | --- |
| “True ROAS” = till ÷ platform-attributed spend | Understates cost (Community 588628) |
| Allocate the gap to campaigns with the biggest claim | That is MTA-by-shame |
| Pass the till back into Meta as a conversion | Apex/Sonar; S5; App Review + CAPI | 
| Show claim_gap as a single “lie %” without overlap warning | Lies about the lie |

### 7.4 Policy fork (must be decided before engineering)

Meta Developer Policies, Ads / Data Collection and Use (fetched 2026-09-09 from [developers.facebook.com/devpolicy](https://developers.facebook.com/devpolicy)):

> Don’t mix data obtained from us with advertising campaigns on different platforms (unless the terms for that product allow it explicitly).

A card that places **Meta purchase value** on the same glass as **Google spend/claim** and **Shopify till** is the product. It may also be a **policy violation**. Legal-shaped options (not legal advice):

| Option | Product | Risk |
| --- | --- | --- |
| A. API claim, Meta-only card | Weak | Lower mix risk; still “assess campaign performance” |
| B. API claim, combined card | S1 as specified | Highest mix risk |
| C. **Paste-only claim** | Still a governor | No Meta conversion data stored; merchant typed the lie |
| D. Drop claim from S1 | S1 becomes “OAuth spend + tax toggle + email” | **Kleio already is this, cheaper, with a P&L** |

**Research call:** Ring 1 ships **C** (paste-a-claim) until counsel or a Partner/Meta review says B is allowed. Do not silently pick B because it scores higher on Ease. If C is the product, **Ease drops** and S1’s 19 was fantasy.

---

## 8. Monday artifact

MASTER_PLAN kill: design partners will not **open weekly** after 30 days of accurate MER.

Better Reports (5.0 / 1,199) earned reviews on **scheduled email + they built the report**. Metorik/Lifetimely advertise Slack. Kleio’s 5-stars mention **daily pulse** and MCP-into-Claude scheduled reports (Trek Light, Hummii Snacks — [apps.shopify.com/kleio](https://apps.shopify.com/kleio)).

### 8.1 What Monday Close is

An **email** (Ring 1) that lands Monday 08:00 **shop local** containing:

| Line | Rule |
| --- | --- |
| Subject | `{Shop} week {ISO}: {ROAS}× vs BE {BE}× {OK\|BELOW}` |
| Till / spend / cash ROAS / BE | Numbers, tabular |
| Tax mode + clock + definition_id | One line |
| Spend completeness | `Meta live · Google expired · CSV $x` |
| Claim gap | Only if a claim exists; else omitted |
| Allocation | **Hold / watch only** unless manual channel sales exist. No “cut Meta 20%” from ∝ |
| CTA | Open desk · Fix expired connection · Unsubscribe |

Not in v1: Slack, PDF slide, WhatsApp, “AI summary,” review ask in the same email (AP12 / Shopify review policy).

### 8.2 Failure modes (design these, or the email is a 1-star)

| Failure | Artifact behavior |
| --- | --- |
| Token expired | Subject prefix `INCOMPLETE` · no ROAS presented as truth |
| Spend drift >5% | Subject prefix `RECON` · MASTER_PLAN kill path |
| No spend all week, sales >0 | “Desk is empty. Paste or reconnect.” Not a 0.00× ROAS |
| Definition changed mid-week | Print both definition ids; do not compare silently |
| Uninstall | `shop/redact` already required; stop sending |

### 8.3 Why email, not Slack, in Ring 1

Email is one vendor (Shopify transactional or a single ESP). Slack is OAuth + workspace admin + another token-rot story. Better Reports proves email. Do not let “Polar has Slack” pull scope.

---

## 9. UX map (embedded app)

| Route | S1 Ring 1 | Notes |
| --- | --- | --- |
| `/app` | Cash desk + claim card + completeness | Today’s dashboard plus definition chip |
| `/app/spend` | Ledger: OAuth rows (read-only) + CSV + billboard | Conflict rows visible |
| `/app/connections` | Status board §6.1 | Replaces stub |
| `/app/definition` | Tax / shipping / gift cards / clock | New. Printable. |
| `/app/close` | Preview of Monday email + send-test | New |
| `/app/allocation` | Warning banner if no manual channel sales | Do not delete; disarm |
| `/app/settings` | Margin %, target MER, close weekday | Keep typed margin (S2 replaces this) |

Empty state after install (the 7-day killer):

1. Shopify till appears **immediately** (sales exist).
2. Sample Harbor numbers only if labeled SAMPLE.
3. Primary button: **Connect Meta spend** · Secondary: **Paste last week**.
4. No review modal. No pixel upsell.

---

## 10. Packaging (inside S1, not a new company)

| Lever | S1 call | Evidence |
| --- | --- | --- |
| Price | Keep **$39 flat** | Live site anti-GMV; Kleio $29 is the price war we already lost on entry |
| Trial | **14 days** | Category default; Shopivibe 2026; Mcfly 7 + blank spend = uninstall |
| Free SKU | **Not in S1** | S7 fuse only after TTV exists (`VNEXT_OPTION_SCORECARD.md`) |
| Agency | Later SKU | S3 |
| Course $79 | Side door | Do not let it become the company |
| Listing | Total ROAS **or** cash MER, not both; remove mailto / unpaid LTV | `LISTING_TEARDOWNS.md` |

**Money honesty:** S1 does not raise ARPU. It tries to raise **conversion and 30-day keep**. If that is not enough vs Kleio $29, S1’s Money 3 was already the confession.

---

## 11. Build sequence *if* chosen later (still not a ship order)

Human-only gates stay human: Partner login, Meta/Google app review, production secrets.

| Step | Outcome | Kill if |
| --- | --- | --- |
| 0 | Founder amends MASTER_PLAN OAuth sentence + public name | Won’t amend — S1 is fanfic |
| 1 | SalesDay via ShopifyQL + tax toggle | Cannot match Admin Total sales ±1% on a design-partner week |
| 2 | SpendDay + Meta/Google OAuth + 60-day reconnect UX | App Review refused or 14-day drift >5% |
| 3 | Paste-a-claim card (policy-safe) | Merchants will not paste; API-claim still blocked |
| 4 | Monday email | 30 DPs will not open it (MASTER_PLAN) |
| 5 | 14-day + listing integrity + Works-with | Still 0 reviews and Partner views do not convert |

Do not start Step 2 before Step 1. OAuth on a lying till is how you automate a 1-star.

---

## 12. Acceptance tests (research — write these before code)

1. Harbor SAMPLE: tax_in till matches a frozen fixture; tax_out = tax_in − fixture tax.
2. Refund Tuesday: accounting_date moves money to Tuesday; MER that week drops; we do **not** rewrite Monday’s sent artifact.
3. Meta OAuth day + Meta CSV day: conflict, not $2× spend.
4. Google MCC without `login-customer-id`: error string names the MCC, not “unknown.”
5. Token T-14: Connections = `expiring`; Monday subject `INCOMPLETE` if expired.
6. Claim paste $100k vs till $50k: card shows 2.00× claim/till; cash ROAS unchanged.
7. Allocation with no manual channel sales: **no** cut/shift percentages.
8. `customers/redact`: no order PII in DB (Ring 1 ShopifyQL aggregates). If we later warehouse orders, webhook must delete them (today’s handler comments that we don’t).
9. Uninstall + 48h: `shop/redact` deletes Shop, SpendDay, tokens.
10. Spend recon: fixture Ads Manager $10,000 vs SpendDay $10,600 → `RECON` + kill path.

---

## 13. Risks S1 still cannot talk away

1. **Kleio.** Same rail (Clarity / WeTracked / Parkour). Cheaper. Anti-attribution FAQ. Daily P&L. 20 reviews vs 0. See `KLEIO_GAP_ANALYSIS.md`.
2. **TrueProfit.** $35 + 899 reviews + spend sync + costs. S1 is thinner on purpose; that purpose is only defensible if the **gap card** is loved.
3. **Sheets + SyncWith $4.99.** The incumbent implementation of S1’s job.
4. **Meta mix-data rule.** May force paste-a-claim and erase Ease 4.
5. **Two calendars.** Meta App Review + Google token. A $250-capital founder dies here more often than in CSS.
6. **Listing integrity.** LTV/Goals already claimed. S1 that ships without them is still a policy/trust problem.
7. **Religion inconsistency.** Live site forbids OAuth; MASTER_PLAN plans it; this file specifies it. Until the founder writes one sentence in MASTER_PLAN, S1 is a research ghost.

---

## 14. Decision

S1 is the **specification of a governor**, not a proof that Mcfly should become one.

- If App Store is the channel **and** the loved number may stay sales÷spend **and** the founder will sit App Review: keep S1, **Ring 1 only**, paste-a-claim first, expect **14–16 / 25** not 19.
- If the loved number is profit: S1 is a delay tactic. Read S2 in `STRATEGY_KILL_CRITERIA.md`.
- If the buyer is an agency: do not build S1’s Meta Advanced Access to get there. Read S3.
- If the founder will not reconnect Meta every 60 days on behalf of customers: S1’s Ease 4 is a lie.

No production code. No Fly deploy. Founder amends MASTER_PLAN if this ever leaves the research folder.
