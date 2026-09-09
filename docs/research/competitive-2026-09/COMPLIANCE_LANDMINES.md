# Compliance landmines — PCD, GDPR, ads policy

**Date:** 2026-09-09  
**Wave:** E  
**Mode:** RESEARCH ONLY. This is **not legal advice**. It is a map of **public** rules that can reject an App Store review, revoke a Meta/Google token, or produce a 1-star that is really a regulator.  
**Options in scope:** the RESEARCH_OPTIONs a founder might still pick after Wave B’s scorecard — **S1, S2, S3, S4, S5/S5b, S7** — plus **live Mcfly (S6-shaped)** as the baseline we already inhabit.

Official anchors fetched this wave:

| Rule | URL |
| --- | --- |
| Shopify Protected Customer Data | https://shopify.dev/docs/apps/launch/protected-customer-data |
| Shopify privacy / mandatory webhooks | https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance |
| Meta Developer Policies (Ads §10) | https://developers.facebook.com/devpolicy |
| Google Ads API developer token + access | https://developers.google.com/google-ads/api/docs/api-policy/developer-token · https://developers.google.com/google-ads/api/docs/api-policy/access-levels |
| Shopify reviews / no paid stars | https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews |

Mcfly **already** has:

- Listing data access: **Customers, orders, device/activity, store owner** (live 2026-09-09).
- App scopes in repo: `read_orders` (`app/shopify.app.toml`).
- GDPR webhook subscription: `customers/data_request`, `customers/redact`, `shop/redact`.
- Handler (`app/app/routes/webhooks.compliance.tsx`): `shop/redact` deletes Session + Shop; customer topics **log and return 200** with a comment that we “store aggregates/spend, not a CRM.”

That last sentence is a landmine **if it is false after S1/S2**. Shopify’s rule is: complete the action within **30 days**, or refuse in writing if law requires retention.

---

## 0. How to read heat

| Heat | Meaning |
| --- | --- |
| **0** | No extra gate beyond being a listed app (webhooks + privacy policy). |
| **1** | Form + policy text. Founder can do it in a sitting. |
| **2** | Review queue. Weeks. Evidence pack. |
| **3** | Ongoing audits, annual recert, or a policy that can **unplug the product**. |
| **4** | Structural: the RESEARCH_OPTION *is* the regulated object (pixel, CAPI, profiles). |

Heat is **per option**, not “the company is good at security.” A $250 founder with no DLP policy already fails **PCD Level 2** on paper.

---

## 1. Shared floor (every listed option)

These apply even if we never OAuth an ad account.

### 1.1 Mandatory compliance webhooks (GDPR-shaped, global)

Shopify **standardizes** GDPR/CPRA-style rights for **all** personal data, regardless of customer location ([privacy-law-compliance](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance)).

| Topic | Must do | Live Mcfly risk |
| --- | --- | --- |
| `customers/data_request` | Provide stored customer data to the **store owner** | Handler does not collect or email anything. Fine **only if** we truly hold no customer records. `MerSnapshot` + order pagination **in memory** is OK. A future order warehouse is not. |
| `customers/redact` | Delete/redact those IDs; Shopify may **withhold 6 months** if the customer ordered recently | Same. If S2 stores `order_id` + email for LTV, this webhook becomes real work. |
| `shop/redact` | 48h after uninstall, erase the shop | Deletes Shop cascade. **Spend OAuth tokens** must die here too (not just Shopify session). Email ESP suppression list: stop Monday Close. |

HMAC fail → **401**. Missing URLs → App Store **reject**. Kleio’s public uninstall promise (“not archived, not anonymised, gone”) is the bar reviewers now screenshot.

### 1.2 Protected Customer Data (PCD)

[Official](https://shopify.dev/docs/apps/launch/protected-customer-data):

| Level | Data | Partner action |
| --- | --- | --- |
| 0 | No customer data | None |
| **1** | Customer-related types **without** name / address / phone / email | Request PCD access + Level 1 requirements |
| **2** | Includes name, address, phone, or email | Level 1+2 + possible **data protection review** |

**Orders, refunds, transactions, shipping rates tied to an order, customer webhooks** are PCD **even at Level 1**. Mcfly’s current `orders { id, totalPriceSet }` is already Level 1. The live listing’s “Customers” access implies a Partner Dashboard request was made or will be asked.

Level 1 minimums (paraphrase, official list is longer): minimize; tell the merchant why; purpose limitation; honor consent / opt-out of “sale” where applicable; DPA/privacy policy; **retention limits**; **encrypt at rest and in transit**.

Level 2 adds: encrypted backups; test/prod split; DLP; **least-privilege staff access**; strong passwords; **access logs**; **incident response policy**.

Shopify approves **minimum data required for the stated functionality**. Asking for email “for LTV personalization” on a cash-MER app is how you get redacted fields (`phone: null` + `errors[]`) or a reject.

**Data protection reviews** target: high installs, high customer-record volume, more Level 2 fields, long retention. S2+MCP+order warehouse is how a 20-shop app still looks “high volume.”

### 1.3 Privacy policy / DPA

Already a Phase 0 site page. S1+ must name:

- Shopify order/report data
- Ad-account spend (and claim, if any)
- Email address of the **merchant** for Monday Close (that is merchant PII, not PCD, but still GDPR if they are in the EEA)
- Subprocessors (Fly, ESP, Meta/Google as independent controllers of the ad account)

Kleio is **DK-based**. Mcfly listing is **UT**. Transfer story (EU merchant → US app) is a founder/counsel item, not an agent invention. Do not put “GDPR compliant” on the listing.

### 1.4 Shopify review / billing landmines (all options)

- No testimonials in listing images ([requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements)).
- No paid-for-reviews; no install-time nag ([manage-app-reviews](https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews)).
- Listed price must match Billing API. 7 vs 14 day is a **config**, not a promise in a screenshot.
- Trials counted across **180 days** (reinstall abuse).

S7 (forever-free) is cleaner than trial-reset games. S7 is worse for support.

---

## 2. Live Mcfly / S6-shaped (baseline)

| Surface | Heat | Landmine |
| --- | --- | --- |
| `read_orders` + listing “Customers” | **2** | PCD request must match **actual** fields. If we never read customer objects, drop the listing’s “Customers” or we look over-scoped. |
| In-memory order totals | 1 | Fine. Do not log full GraphQL bodies to Sentry. |
| GDPR handler | **2** | Comment ≠ implementation. A reviewer can POST `customers/data_request` and expect a process, not a shrug. Write the runbook even for “we hold nothing.” |
| Monday email | 0 (not shipped) | — |
| Ads OAuth | 0 (site forbids) | — |

**S6 does not escape PCD.** It already sits on orders. “We only do aggregates” is the defense — keep it true.

---

## 3. S1 — Cash governor

S1’s compliance story is **three vendors**: Shopify (till), Meta (spend), Google (spend), plus an ESP.

### 3.1 Shopify / PCD / GDPR

| Choice | Heat | Notes |
| --- | --- | --- |
| ShopifyQL `sales` only; no order warehouse | **1–2** | Still commerce reporting. Argue minimization: no names, no emails, no line items. Best S1 shape. |
| Keep `read_orders` “just in case” | 2 | Purpose limitation. If unused, drop it before review. |
| Ring 2 cash CAC via `customer.numberOfOrders` | **2–3** | Customer resource. May stay Level 1 if we never pull email. Do not store customer ids longer than the snapshot. |
| Monday Close to merchant email | 1 | Lawful basis: merchant account holder, not their shoppers. Unsubscribe. Stop on `shop/redact`. |
| Store `definition_id` + daily aggregates | 1 | Retention: 24 months is plenty for MER; “forever analytics” is how reviews get spicy. |

**Landmine:** `shop/redact` must delete **Meta/Google refresh tokens**, `SpendDay`, `ClaimDay`, and ESP records. Today’s cascade deletes Shop; **confirm Prisma `onDelete` once those tables exist** (they do not yet — research).

### 3.2 Meta ads policy (the S1-specific bomb)

Developer Policies, **§10 Ads — Data Collection and Use** ([devpolicy](https://developers.facebook.com/devpolicy), 2026-09-09):

> a. Don’t use Meta advertising data for any purpose, except on an **aggregate and anonymous** basis (unless the terms for that product allow it explicitly) and only to **assess the performance and effectiveness of the end advertiser’s campaigns**.  
> b. Only use data from an end-advertiser’s campaign to optimize or measure **that** end-advertiser’s Meta campaign.  
> c. Don’t use data to **retarget** on or off Meta.  
> d. **Don’t mix data obtained from us with advertising campaigns on different platforms** (unless the terms for that product allow it explicitly).  
> e. Don’t use Meta’s data to **build or augment user profiles**.  
> f. Only allow the end advertiser or people acting on their behalf to access Meta’s Platform data.  
> g. Keep Meta’s data … on behalf of one advertiser **separately** from that of other advertisers.

| S1 behavior | Policy read (research, not counsel) | Heat |
| --- | --- | --- |
| Pull `spend`, show next to Shopify till for **that** merchant | a + assess performance: **probably the intended use** of `ads_read` | 2 |
| Store spend per shop, encrypted, no cross-shop analytics | g | 2 |
| Staff support peeking at a shop’s Meta spend | f + Level 2-ish access log even if not PCD | 2 |
| **Claims-vs-cash card summing Meta purchase value + Google conv. value** | **d. mix across platforms** | **4** |
| Use Meta claim to drive `suggestAllocation()` toward Google | b + d | **4** |
| Train a model on many merchants’ Meta spend | a, e, g | **4** (we must never) |
| CAPI / pass till into Meta | Different product; Business Tools terms | That’s S5 |
| System User token sitting in our DB | Credential theft = every client’s ads data | 3 (security) |

**S1 research call (same as PRD):** Ring 1 **paste-a-claim**. API `action_values` on a multi-platform glass needs a written exception or a Meta-only card. Ease 4 in Wave B ignored this paragraph.

Other Meta heat: App Review, Business Verification, **annual Data Use Checkup**, unused-app downgrade (~30 days). `ads_management` write scope is unnecessary and increases reject odds.

### 3.3 Google Ads API policy

| Gate | Heat | Landmine |
| --- | --- | --- |
| Developer token use case | 2 | “Individual” + dead website can be rejected. mcflyads.com must describe the **reporting** tool. |
| Permissible use = Reporting | 1 | Do not write campaigns “as a treat.” |
| Brand verification of GCP | 2 | Can block Basic Access. |
| Standard Access + external users | 3 | They ask for **demo login** and Required Minimum Functionality. A stub Connections page fails. |
| Explorer 2,880 ops/day | 1 | Per-pageview Insights-style abuse will 429. Not a legal fail — a reliability fail that looks like a legal fail in support. |
| EU political advertising fields | 1 | Campaign reports include political flags; do not build a public “who ads” browser. |

Google’s data-use terms are less meme-famous than Meta’s mix rule but **still** restrict using Ads data to build user profiles or leak across advertisers. Same isolation: `SpendDay.shopId` is a compliance control, not just a schema nicety.

### 3.4 Email / CAN-SPAM / GDPR merchant mail

Monday Close is **requested product email**, not marketing — until we add a course pitch. One upsell line in the Close is how we become marketers and need consent. Ring 1: **numbers + unsubscribe only**.

### 3.5 S1 heat summary

| Layer | Heat |
| --- | --- |
| ShopifyQL-only till | 2 |
| Meta+Google spend OAuth | 3 (calendar + checkup + token vault) |
| API claims-vs-cash combined card | **4** |
| Paste claims-vs-cash | 1 |
| Monday email | 1 |

**Kill-shaped compliance event:** Meta rejects Advanced Access, or approves it and later cites §10.d on the combined card. Product must survive as spend-only + paste-claim.

---

## 4. S2 — Profit-lite desk

S2 is S1 **plus** an order-and-cost warehouse. That is where PCD goes from “we saw totals” to “we hold the store.”

| Addition | PCD | GDPR | Ads |
| --- | --- | --- | --- |
| Persist orders / line items / refunds | **Level 1 guaranteed**; Level 2 if you keep shipping address for landed cost | `customers/redact` must delete rows; 6-month delay is not a free pass to *use* the data in the meantime | — |
| Customer id for LTV / cohorts | Level 1 ids; **Level 2** the moment email/name is stored for “MCP personalization” | Data request must export the cohort join | — |
| Shopify cost + custom COGS | Low PCD (catalog). Still merchant confidential | Shop redact | — |
| Payment fees / gateway txs | Can include payer identifiers — treat as PCD | Same | — |
| ShipHero / 3PL invoices | Third-party DPA; warehouse addresses | Subprocessor list | — |
| MCP **read** P&L | Merchant secret; **not** shopper PCD if aggregates only | If the MCP can fetch order-level, it is a new disclosure | Meta **f**: AI tools acting *for* the advertiser are OK; **training** the model on Meta data is not |
| MCP **write** products (Kleio) | Catalog. Low PCD. High **blast radius** (AI drafts products) | — | — |
| Agency % of ad spend | — | — | Using Meta spend to compute a fee is still “assess performance”? Counsel. Do not send that fee model back into Meta. |

**Level 2 checklist Mcfly does not have today (public repo):** DLP, access logs, incident policy, backup encryption story, staff password policy. S2 that stores emails without those is a **Partner Dashboard fiction**.

**VAT landmine (not GDPR, still compliance-shaped):** publishing tax-in revenue as “profit” is how TW ate a 1-star. That is consumer-protection / accounting honesty, not Shopify PCD. It will still unpublish you socially.

**S2 heat:** Shopify **3–4** · Meta/Google same as S1 · **new** subprocessors.  
**Kill-shaped event:** data-protection review we cannot evidence; or `customers/redact` missed in a warehouse; or MCP token leak (Kleio already ships token revoke — copy the idea, not the write-scope).

---

## 5. S3 — Agency scoreboard

Different shape: **more shops**, **more tokens**, **less shopper warehouse** if the desk stays paste-first.

| Landmine | Heat | Why agencies trip it |
| --- | --- | --- |
| Meta **g** (separate advertisers) | **3** | One agency login must never see Shop A’s spend on Shop B’s slide. Row-level security is a **feature**, not a nice-to-have. |
| Meta **f** (only advertiser or people on their behalf) | 2 | Agency is “on behalf.” Freelance media buyer with no BM role is a gray user — they should OAuth as themselves. |
| System User tokens | 3 | Non-expiring keys in our DB = crown jewels. Rotation + `shop/redact` per store, not per agency. |
| Google MCC | 2 | `login-customer-id` + which child account. Demo for Standard Access if the tool is external. |
| White-label PDF | 1 | Do not include Meta **user-level** breakdowns in a PDF the brand then posts publicly. Aggregate. |
| Multi-store Shopify | 2 | Each shop is a separate install + separate `shop/redact`. Portfolio SKU is billing, not a data lake. |
| Outbound sales / Sheets ingest | 1 | Customer sheets can contain **shopper PII**. Ingesting a tab with emails upgrades S3 to S2’s PCD overnight. |

S3 can be the **lowest Shopify PCD** option (CSV spend + ShopifyQL totals, no LTV) and the **highest Meta isolation** option. Wave B scored S3 Love 2 because agencies do not leave 899 reviews — they also do not trigger Magic-summary-scale data reviews **until** you warehouse their clients’ customers.

**Kill-shaped event:** one agency user exports another client’s Meta spend. That is not a 1-star. That is a contract + Meta Platform ban.

---

## 6. S4 — Suite overlay

Compliance looks like S1 **definitions** without needing Advanced Access if spend stays CSV (the suite already OAuth’d).

| Landmine | Heat |
| --- | --- |
| Dual clock / “finance-grade” copy | 1 as product · **3** if we imply we are their accountant or we “certify” a number for tax |
| Export for A2X / bookkeeper | 1 — do not become a GL; liability |
| MCP read-only | 2 — same token/leak story, smaller if no order PII |
| Sitting on top of TW/NB | 1 — do not scrape their UI; no ToS war |

**Kill-shaped event:** a finance lead treats Mcfly as audited P&L. Our footer must say **not a substitute for books**. This is the option where **over-claiming definitions** is the legal risk, not OAuth.

---

## 7. S5 — Pixel company · S5b — partner pixel

### 7.1 S5 (own pixel / CAPI)

This is the **heat-4** option. MASTER_PLAN kill-on-contact is also a compliance opinion.

| Regime | Landmine |
| --- | --- |
| **PCD Level 2** | Browser ids, emails, phone for EMQ. Name/address if you enrich. Data-protection review likely as you scale. |
| **Consent** | GDPR/ePrivacy + Shopify Customer Privacy API / consent pixel. US state opt-out of “sale/share.” PCD Level 1 already says honor these **where applicable**. A pixel that fires before consent is the Parkour/Elevar support hell **and** a regulator story. |
| **Meta Business Tools / CAPI** | Separate terms from Marketing API `ads_read`. Advanced Matching, hashed PII, event quality. WeTracked 1★: cannot evidence accuracy. |
| **Meta §10.c / e** | Don’t retarget with data you shouldn’t; don’t build profiles. A “Mcfly audience” is how you die. |
| **Google** | Enhanced conversions / gtag consent mode — another policy stack. |
| **Shopify** | Pixel sandbox, App Store “works with pixels” claims must be true. |
| **Security** | Event stream is a **PII firehose**. Retention “for debugging EMQ” is how you fail purpose limitation. |

**Kill-shaped event:** iOS / consent change + 1-stars that the pixel “broke ROAS.” Capital + brand. Wave B scored S5 Religion-flex **1** for this reason.

### 7.2 S5b (Works-with Parkour / Elevar / WeTracked)

| Heat | Notes |
| --- | --- |
| 1 if **logo + URL only** | Listing “Works with.” No PII to us. |
| 2 if we **ingest** their event stream | We just bought S5’s PCD. |
| Partner quality | WeTracked 1★ evidence failure is **our** listing if we imply we vouch. |

**Research call remains RELIGION_FLEX R1-B:** logos, not pipes.

---

## 8. S7 — Free / 14-day bolt-on

Mostly **billing and review policy**, not PCD.

| Landmine | Heat |
| --- | --- |
| 14-day full trial | 0–1 — category default; 180-day anti-abuse |
| Forever-free | 1 — still need webhooks, PCD if orders flow on free shops; **support** is the real cost |
| Review modal | **2** if at install or “leave 5 stars for unlock” — official violate |
| Free SKU that still OAuth’s Meta | Same S1 Meta heat, **more** tokens to lose |

S7 does not reduce S1’s ads-policy heat. It multiplies the number of tokens you hold.

---

## 9. Matrix (options × regimes)

| Option | Shopify PCD | GDPR webhooks | Meta ads policy | Google Ads API | Extra |
| --- | --- | --- | --- | --- | --- |
| Live / S6 | L1 orders (already) | Stub risk | None | None | Listing over-claims LTV |
| **S1** spend-only + QL till | L1 minimize | Real `shop/redact` for tokens | `ads_read` + isolation | Token + Reporting use | 60-day Meta reconnect |
| **S1** API claim card | same | same | **§10.d mix** | Conversion value isolation | Counsel gate |
| **S2** | **L1–L2 warehouse** | Redact must work | same as S1 | same | Subprocessors, VAT honesty |
| **S3** | Can stay L1 | Per-shop redact | **g isolation** | MCC / Standard demo | Agency RBAC |
| **S4** | L1 | Easy | Maybe none (CSV) | Maybe none | Don’t play accountant |
| **S5** | **L2 firehose** | Heavy | Business Tools + §10 | Consent mode | Consent, EMQ |
| **S5b** | L1 if logos only | Easy | None | None | Partner 1-stars |
| **S7** | Same as core | Same | Same × N | Same × N | Review-policy temptation |

---

## 10. Founder checklist (research — still not a ship order)

Before any RESEARCH_OPTION leaves this folder:

1. **Inventory what we actually persist today** (Session email fields, Sentry, logs). Align listing “Customers” with reality.  
2. Write the **three webhook runbooks** including “we hold nothing” receipts.  
3. If S1: Meta use-case text = **“read spend to show next to Shopify sales for that merchant. No write. No pixel. No cross-shop. No profiles.”** Do not mention “mix with Google ROAS” in the App Review essay.  
4. If S1 claim card: **paste first** or Meta-only; get a human to read §10.d.  
5. If S2: stop and buy the Level 2 controls **before** the first email field.  
6. If S3: draw the isolation diagram first.  
7. If S5: do not. If S5b: URLs only.  
8. Never put “GDPR compliant” or invented security badges on apps.shopify.com.

---

## 11. One paragraph

Mcfly is already a PCD Level 1 app the moment it pages orders; the GDPR webhooks are subscribed and only half-implemented. S1 adds two ad platforms whose worst clause is Meta’s **do-not-mix** rule — which is uncomfortably close to the **claims-vs-cash** card Wave B used to justify Love 4. S2 turns the shop into a warehouse and fails unless Level 2 paperwork is real. S3 is an isolation problem wearing a pricing problem. S5 is a consent-and-PII company. The cheapest compliance win in this folder is the same as the product win: **ShopifyQL aggregates, spend-only OAuth, paste the lie, delete everything on uninstall.** That is still not legal advice. It is the shape that keeps the option in “App Review calendar” instead of “counsel + incident policy + pixel.”
