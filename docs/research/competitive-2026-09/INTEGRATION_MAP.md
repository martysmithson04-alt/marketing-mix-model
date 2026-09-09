# Integration map — Meta / Google Ads vs Shopify Finance vs CSV

**Date:** 2026-09-09  
**Wave:** E  
**Mode:** RESEARCH ONLY. Cost = calendar + support + compliance load for a ~$250-capital, one-founder shop — **not** a dollar TAM. No production wiring from this file.  
**Pairs with:** `S1_PRD_LITE.md` (what the pipes feed) · `COMPLIANCE_LANDMINES.md` (why a pipe can be illegal) · `KLEIO_GAP_ANALYSIS.md` (who already paid this tax).

---

## 0. The job, restated as data

```text
MER = Till(period, definition) ÷ Spend(period, total, not attributed)
```

Three families of pipe can feed that fraction. They are **not interchangeable**. Mixing their clocks is how finance 1-stars you.

| Family | Feeds | Clock | Typical grain | S1 role |
| --- | --- | --- | --- | --- |
| **Shopify commerce / “Finance”** | Till (sales, tax, shipping, returns) | Order event or report day · **not** payout day | Day or order | Numerator |
| **Ads APIs** | Spend (and, optionally, **claim**) | Ad-account timezone, often delayed / restated | Account / campaign / hour | Denominator · optional claim |
| **CSV / paste** | Anything the APIs refuse (billboards, retainers, expired tokens, “their claim”) | Whatever the merchant typed | Row | Override + offline + policy-safe claim |

Shopify **payouts** (ShopifyQL `FROM payouts`) are a **fourth** family: bank deposits after fees and reserve. That is A2X’s religion, not MER’s. This map includes it so S1 does not “helpfully” use it as sales.

---

## 1. Scoreboard (research judgment)

Axes: **Cost to stand up** (calendar + human gates) · **Complexity** (ongoing engineering + support) · **Reliability** (will Monday’s number match the source UI) · **Religion fit** · **PCD / ads-policy heat**.

1 = cheap/simple/reliable/cool. 5 = expensive/hairy/fragile/hot.

| Pipe | Stand-up cost | Complexity | Unreliability | Religion | Compliance heat | S1? |
| --- | --- | --- | --- | --- | --- | --- |
| ShopifyQL `sales` (till) | 2 | 2 | 2 | 1 | 2 (reports; still commerce) | **Preferred numerator** |
| Admin `orders` pagination (current) | 1 (already shipped) | 3 | 4 | 2 | 3 (orders = PCD) | **Replace** |
| ShopifyQL `payouts` | 2 | 3 | 3 (wrong clock) | 5 if used as till | 3 | **Refuse as till** |
| Shopify Payments / balance txs | 3 | 4 | 3 | 5 as till | 3–4 | S4/A2X only |
| Cost per item (COGS) | 2 | 4 (history, variants) | 4 | 3 (S2) | 2 | S2, not S1 |
| Meta Insights `spend` | 4 | 4 | 3 (token + TZ + restatement) | 1 | 3 (`ads_read`) | **S1 denominator** |
| Meta Insights `action_values` | 4 | 4 | 4 (windows) | 3 (claim) | **5** (mix/use rules) | Paste-first; API later |
| Google Ads `cost_micros` | 5 | 4 | 3 (MCC + token + micros) | 1 | 3 | **S1 denominator** |
| Google Ads conversion value | 5 | 4 | 4 | 3 | 4 | Same as Meta claim |
| TikTok / Snap / Pinterest / MSFT / AppLovin | 4–5 each | 4 each | 3–4 | 2 (zoo) | 3 each | **Not S1** |
| CSV spend | 1 | 2 | 2 (human) | 1 | 1 | **Always** |
| CSV claim | 1 | 1 | 2 | 2 | **1** | **S1 claim v1** |
| Sheets (SyncWith etc.) | 1 for them | 2 | 3 | 2 | 1 | Companion, not brain |

**Read the table twice:** the cheapest reliable S1 is **ShopifyQL sales + CSV spend**. That is what Mcfly already almost is, and it scores Ease 1 on the Wave B rubric because **founders will not CSV**. The expensive S1 is **ShopifyQL + Meta + Google**. The illegal-feeling S1 is **that plus API claims on one glass**.

---

## 2. Shopify surfaces (numerator and the fake numerator)

### 2.1 What “Shopify Finance” actually is

Merchants say “Finance” and mean three different products:

| Merchant phrase | Official object | Use in MER |
| --- | --- | --- |
| “Finance → Payouts” | Shopify Payments payouts, ShopifyQL [`payouts`](https://shopify.dev/docs/api/shopifyql/latest/schemas/finance_and_payments/payouts) | **Bank truth.** Fees already deducted. Ads are **not** in here. Wrong denominator *and* usually wrong numerator. |
| “Finance summary / Total sales” | Admin analytics + ShopifyQL [`sales`](https://shopify.dev/docs/api/shopifyql/latest/schemas/sales_revenue/sales) | **Till.** Kleio’s Revenue target. |
| “Order total” | Admin GraphQL `Order.totalPriceSet` | What Mcfly sums today. Closest to an order’s sticker price, worst as a period P&L. |

Kleio’s metrics doc is the public Rosetta stone: Revenue **equals Total sales to the cent** when tax-in; Gross sales / Discounts / Returns / Shipping **will not** line up row-for-row because Shopify excludes shipping from some of those rows.

### 2.2 ShopifyQL `FROM sales` — preferred S1 till

**Official:** [`shopifyqlQuery` on Admin GraphQL](https://shopify.dev/docs/api/shopifyql/latest) · schema [`sales`](https://shopify.dev/docs/api/shopifyql/latest/schemas/sales_revenue/sales).

```text
FROM sales
SHOW total_sales, taxes, total_shipping_charges, total_returns
TIMESERIES day
SINCE <from> UNTIL <to>
```

Documented identity:

```text
total_sales = net sales + additional fees + duties + shipping charges + taxes
```

| | |
| --- | --- |
| **Stand-up** | App scope: need `read_reports` (and still a PCD story if the app also has `read_orders`). Query is one round-trip per range, not N pages of orders. |
| **Complexity** | Learn ShopifyQL; version it; snapshot `definition_id`. Tax-out = `total_sales − taxes` **after** confirming taxes include shipping tax and refunded tax behaves. |
| **Reliability** | Designed to match Admin reports. Still moves when Shopify restates (Community [180915](https://community.shopify.com/t/sales-attributed-to-marketing-report-numbers-change-over-time/180915) is **marketing attribution** lookback — different report — but the lesson stands: **store the series you displayed**). |
| **Cost** | Days, not months. No third-party App Review. |
| **Failure modes** | Missing `read_reports`; Plus-only metrics (verify per metric); gift-card / POS / B2B channels in or out without a sentence; timezone = shop. |
| **Religion** | Perfect. This **is** the till. |

**S1 call:** replace `fetchShopifySales` pagination with ShopifyQL day grain into `SalesDay`. Keep `read_orders` only if Ring 2 cash CAC needs new-customer counts. Every extra order field is PCD heat (`COMPLIANCE_LANDMINES.md`).

### 2.3 Admin `orders` pagination — current Mcfly

`app/app/lib/shopify-sales.server.ts`:

- Query `orders(first: 100)` with a date search string.
- Sum `totalPriceSet.shopMoney.amount`.
- No refunds, no tax split, no shipping split, no gift-card policy.

| | |
| --- | --- |
| **Stand-up** | Already done. Scope `read_orders` in `shopify.app.toml`. |
| **Complexity** | Pagination on a busy store is a **timeout** waiting to happen (YTD × 100). Overnight worker inherits this. |
| **Reliability** | **Low** as finance. Refunds, edits, cancelled orders, test orders, $0 100%-off orders (Kleio has a skip toggle because Shopify still counts them). Currency: `shopMoney` is shop currency — good. |
| **PCD** | **Orders are protected customer data** even without name/email ([official PCD types](https://shopify.dev/docs/apps/launch/protected-customer-data)). Live Mcfly listing already shows Customers + Orders. |
| **S1 call** | Freeze as legacy. Do not add LTV on top of this query and call it Ring 1. |

### 2.4 ShopifyQL `FROM payouts` — the trap

[Official `payouts` schema](https://shopify.dev/docs/api/shopifyql/latest/schemas/finance_and_payments/payouts): “deposits Shopify sends you, **not** the individual transactions inside them.”

| | |
| --- | --- |
| **Why P4 asks** | “Did we get paid?” Community [577364](https://community.shopify.com/t/does-anyone-know-how-to-handle-financial-reconciliation/577364). |
| **Why MER dies** | Payout day ≠ order day. Shopify Payments fees already netted. Amazon/PayPal/Klarna may never appear. Ad spend **never** appears. MER using payouts as sales is a smaller, later, fee-netted numerator against gross ad spend — a nonsense ratio. |
| **S1 call** | Optional **footnote** “Shopify deposited $X this week (not the till).” Never the fraction. |

### 2.5 Shopify Payments fees / transactions

Needed for **S2** (assembled contribution) and for A2X-class recon. Kleio: “automatically pulls in Shopify Payment transaction fees; other gateways you define.”

| | |
| --- | --- |
| **Stand-up** | Payments scopes; not all shops use Shopify Payments. |
| **Complexity** | Multi-gateway (PayPal, Shop Pay installments, COD). Community 657805: late adjustments. |
| **S1 call** | Out. Typed margin covers the hole badly and honestly. |

### 2.6 Cost per item

Shopify product `unitCost` / inventory cost. Native Profit-by-product uses it (Community 657805) and still cannot see ads.

| | |
| --- | --- |
| **Reliability** | Historical cost changes, variants, deleted SKUs, dropship quantity breaks — Kleio built Custom COGS + deleted-product costs **because this pipe lies**. |
| **S1 call** | Out. S2’s first landmine. |

### 2.7 Shop Campaigns only (`shop_campaign_insights`)

[ShopifyQL marketing schema](https://shopify.dev/docs/api/shopifyql/latest/schemas/marketing/shop_campaign_insights): spend + ROAS for **Shop Campaigns**. Community 134251 still holds: **no Meta/Google ingest**.

Do not advertise “Shopify already has ad spend” without that qualifier.

---

## 3. Meta Marketing API (denominator, optional claim)

### 3.1 What we would call

Insights on an ad account (documented pattern across Meta’s Insights API):

```text
GET /act_{AD_ACCOUNT_ID}/insights
  ?level=campaign|account
  &time_increment=1
  &fields=spend,campaign_id,campaign_name,date_start,impressions
  &time_range={since,until}
```

For **claim** (policy-hot): `actions`, `action_values` + `action_attribution_windows` (e.g. `7d_click`, `1d_view`).

S1 Ring 1 needs **`spend` only**. Claim fields are how you walk into Developer Policy 10.

### 3.2 Access ladder (calendar, not code)

| Rung | What it means | S1 impact |
| --- | --- | --- |
| Dev app + Marketing API product | Founder, Meta Developers | Human gate (`packages/connectors/README.md`) |
| Standard access | Own / admin-role ad accounts | Design-partner only |
| **Advanced Access** | Other merchants’ ad accounts | **Required for a public Shopify app** |
| App Review for `ads_read` | Screencast, use case, often weeks | Over-asking `ads_management` is a known reject reason |
| Business Verification | Legal entity, docs | UT address on the listing; do it once |
| Data Use Checkup | Annual recertification | Forget = permissions die |
| Unused 30 days | Access can downgrade (Developer Policies: Ads) | A quiet app becomes a broken app |

Sources: [Meta Developer Policies — Ads](https://developers.facebook.com/devpolicy) (LIVE 2026-09-09); access-level practice as documented by Meta partners / 2026 practitioner writeups. Official Marketing API access pages should be re-opened at implementation time — **do not treat practitioner blogs as gospel for SLA**.

### 3.3 Tokens — the reliability story Kleio already confessed

| Token | Life | Fit |
| --- | --- | --- |
| Short-lived user | hours | Dev only |
| Long-lived user | **~60 days** | Kleio’s production path: **manual reconnect**, email before expiry, **cannot auto-refresh** ([their docs](https://www.getkleio.com/docs/integrations/ad-integrations)) |
| System User | can be set non-expiring | Merchant must create/assign in **their** Business Manager. Fine for agencies (S3). Hostile for P1. |

**Reliability implication:** a “set and forget OAuth” Ease 4 assumes System User or a refresh Meta does not give Kleio. Wave B’s Ease 4 did not price the reconnect email. **Monday Close must know `token_expires_at`.**

### 3.4 Reliability vs Ads Manager

| Drift source | Typical miss | Mitigation |
| --- | --- | --- |
| Timezone | Shop TZ ≠ ad account TZ | Store account TZ; convert or disclose |
| Restatement | Spend and results move for ~24–48h (and longer for claims) | `superseded_by`; don’t recon against a same-day screenshot |
| Level | Account vs campaign vs ad | Sum campaign ≠ account if deleted campaigns drop out |
| Attribution window | Claim only | Print the window |
| Currency | Ad account ≠ shop | FX or “mixed $” banner |
| Filtered campaigns | Kleio-style include `US_` | Default **all spend** (AP1) |
| Rate limits | Insights is heavy | Daily batch, not per-pageview; cache `SpendDay` |

MASTER_PLAN kill: **>5% vs Ads Manager for 14 days.** That test must use **account-level spend**, same TZ, T-2 (not today).

### 3.5 Cost / complexity

| Item | Load |
| --- | --- |
| Engineering | Token vault, refresh/reconnect, Insights pagination, account picker (users with 12 ad accounts), webhook `expired` |
| Support | “Which account?” · “Agency owns the BM” · “I reconnected and last week vanished” · 60-day email ignored |
| Calendar | App Review + BV: plan **weeks to a few months**, not a sprint |
| Cash | $0 API. Founder time is the bill. |
| Zoo creep | TikTok “while we’re here” — Kleio has 8 logos because they chose S2. S1 that copies the logo row dies of connectors (MASTER_PLAN R9). |

### 3.6 Religion

Spend-only = authorized bend (MASTER_PLAN Phase 2).  
`action_values` on the same dashboard as Google = **second bend + policy heat**. See §7 of `S1_PRD_LITE.md`.

---

## 4. Google Ads API (denominator, optional claim)

### 4.1 What we would call

Official reporting path: `GoogleAdsService.Search` / `SearchStream` + GAQL ([access levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels), [developer token](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)).

```text
SELECT
  segments.date,
  campaign.id,
  campaign.name,
  metrics.cost_micros
FROM campaign
WHERE segments.date BETWEEN '<from>' AND '<to>'
```

Till-side claim (hot): `metrics.conversions_value` (and the conversion action’s attribution model — often data-driven). Same “their claim” labeling rules as Meta.

`cost_micros / 1_000_000` = account currency.

### 4.2 Access ladder (official)

| Level | Production? | Daily ops | Review (Google’s stated typical) |
| --- | --- | --- | --- |
| Test Account | No | 15,000 | Signup |
| Explorer | Yes, cramped | **2,880** production | Sometimes auto |
| **Basic** | Yes | 15,000 | **~5 business days** + possible GCP **brand verification** |
| Standard | Yes | Unlimited (most services) | **~10 business days** + **demo login if external users** + Required Minimum Functionality |

Permissible use for S1: **Reporting** only (Search / SearchStream / read-only). Do not apply for Ad creation — it implies write and a bigger RMF surface.

**Explorer 2,880/day** can be enough for a handful of shops × one nightly pull. It is **not** enough for “refresh on every embedded page load.” S1 must be **worker-then-cache** or Basic is a launch gate.

### 4.3 OAuth / MCC — the support story

| Item | Reality |
| --- | --- |
| Consent screen | `adwords` scope looks like “manage my ads” to humans even when we only read |
| Refresh tokens | Exist (unlike Kleio’s Meta path). Still revoke on password change / sensitive action |
| `login-customer-id` | Required when the user authenticates through a **manager (MCC)**. Agencies will fail connect until we send the MCC id. Document this **before** the first ticket |
| Test vs prod accounts | Red “Test account” badge in Ads UI — tokens from the wrong MCC waste a week |
| One token per company | Google “usually grants one developer token per company.” New tools need a written use case |
| Contact email | They email the API Center address; an unread inbox = rejected token |

### 4.4 Reliability vs Google Ads UI

| Drift source | Notes |
| --- | --- |
| Micros | Off-by-1e6 is a guaranteed 1-star |
| Date range in account TZ | Same as Meta |
| Removed campaigns | Query must not silently drop spend |
| Parallel conversions vs conversion value | Claim field ≠ spend |
| PMax | Spend is real; claim is a blender. Do not “allocate” without a disclosed tag (Kleio’s `kleio_allocate_nc_XX` is the honest pattern — and it is still a model) |
| Quotas | System hourly limits exist **regardless** of access level |

### 4.5 Cost / complexity vs Meta

Google is **worse to stand up** (developer token + brand verification + MCC) and **better to keep alive** (refresh tokens). Meta is **easier to demo on your own BM** and **worse on day 61**.

S1 that ships **only Meta** because Google’s token is pending will look broken to every US brand that splits spend. Ring 1 is **both** or it is a CSV app with a Meta button.

---

## 5. CSV / paste (the pipe that does not need a lawyer)

### 5.1 Why it stays

- Live listing hero: billboards.
- Agency invoices lag (P3 / P4).
- Token expiry (Meta 60 days).
- Policy-safe **claim** (`S1_PRD_LITE.md` option C).
- MASTER_PLAN discarded a connector zoo.

### 5.2 Reliability

| Risk | Control |
| --- | --- |
| Human typo | Confirm sum vs “I meant $12,400” |
| Attributed-only export | Reject columns named `results` / `purchases` as spend |
| Double count vs OAuth | Conflict row, not sum |
| Timezone | Date = shop TZ, stated on the template |
| Currency | Column required |
| Stale file | `ingested_at` + Monday `CSV as of` |

Complexity is **product**, not API: template, validation, conflict UI. Wave A already said paste is developer-easy, founder-hard. CSV as the *only* denominator is S6. CSV as the *fallback* is S1.

### 5.3 Sheets as CSV-with-a-pulse

SyncWith $4.99 / 10 reviews ([listing](https://apps.shopify.com/syncwith)) already pipes Meta/Google into a sheet. Mcfly product page tells merchants to pay SyncWith.

| | |
| --- | --- |
| **Cost** | They pay SyncWith; we ingest a tab or they paste |
| **Reliability** | Their tokens, their drift |
| **Religion** | Fine if we sell the **definition**, not 40 connectors |
| **S1** | Optional import. Do not become SyncWith (MASTER_PLAN). |

---

## 6. Combined topologies (what a founder might actually run)

### T0 — Current Mcfly

```text
orders.totalPriceSet  +  typed SpendEntry  →  mer-core
```

Cost 1 · Reliability 4 (bad) · Ease 1. This is the 10/25 live product.

### T1 — S1 Ring 1, policy-conservative (research recommendation)

```text
ShopifyQL sales (definition)  +  Meta spend + Google spend + CSV other
Claim: pasted totals, not API
Monday email from MerSnapshot
```

Stand-up **4–5** (two ads reviews). Reliability **3** if reconnect UX exists. Compliance heat **2–3**. Unique vs Kleio: **claim card + offline + no CM engine**.

### T2 — S1 “Ease 4” as Wave B imagined it

```text
T1 + Insights action_values + Google conversions_value on one card
```

Same engineering as T1 plus **policy 5**. May be unshippable. Do not start here.

### T3 — S2

```text
T1 + Cost per item + Payments fees + shipping rules + custom expenses
```

This is Kleio/TrueProfit. Calendar **years**. See kill criteria.

### T4 — S3 agency

```text
CSV/Sheets in  +  N shops  +  PDF/email out
System User Meta tokens  +  MCC Google
```

Ads APIs become **their** problem (they already have MCC). Do not build T2 to win T4.

### T5 — S5 pixel

```text
Browser/server events → Meta/Google  +  (optional) till
```

Different company. Parkour Free already did the easy version.

---

## 7. Cost to a one-founder shop (no invented dollars)

| Workstream | Dominant tax | Parallelizable? |
| --- | --- | --- |
| ShopifyQL till + tax toggle | Engineering days + fixture tests | Yes |
| Meta Advanced Access | **Wait** + screencast + BV | Start day 0 |
| Google Basic + brand verify | **Wait** + MCC docs | Start day 0 |
| Token vault / reconnect / Monday `INCOMPLETE` | Engineering + copy | After first sandbox token |
| CSV template + conflicts | Engineering | Yes |
| Paste-a-claim card | Engineering (small) | Yes |
| API-claim card | Counsel + Meta review | **Serial, after T1 works** |
| TikTok “parity” | Repeat Meta’s calendar | **No. Kill.** |

**Critical path = Meta + Google calendars.** Everything else can be built against mocks (`packages/connectors` already has them). Shipping UI on mocks and calling it S1 is how Connections stays a stub.

Kleio’s existence does **not** shorten Meta’s queue. It proves the queue is survivable **if** the desk behind it is a P&L people open daily.

---

## 8. Reliability contract (write this on Connections)

A connection is **not** “green” because OAuth returned 200.

| Signal | Green | Yellow | Red |
| --- | --- | --- | --- |
| Last successful pull | < 26h | < 72h | older / never |
| Token | >14d life | ≤14d | expired / revoked |
| Recon vs last Ads Manager confirm | ≤5% | 5–10% | >10% or MASTER_PLAN 14-day fail |
| TZ / FX banner | none | mismatch disclosed | mismatch hidden |
| Coverage | every sales day has spend **or** explicit $0 | weekend holes | sales>0, spend null, status=connected |

Monday subject line uses this contract. A green logo with a red contract is the TW “VAT in revenue” class of lie.

---

## 9. Decision rules (research)

1. **Numerator:** ShopifyQL `sales`, versioned definition. Stop summing order stickers.  
2. **Denominator:** Meta + Google **spend** + CSV. No zoo.  
3. **Claim:** CSV/paste until counsel clears Insights `action_values` next to Google.  
4. **Payouts:** footnote or S4, never MER.  
5. **COGS / fees:** S2 or don’t.  
6. **If either ads review is refused:** S1 collapses to T0 + tax toggle + email = **S6 with better copy**. Kill S1; go S3 outbound or accept silence.

No production code. No Fly deploy.
