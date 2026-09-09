# Partner Program / Built for Shopify / review policy — WAVE C

**Fetched:** 2026-09-09 · official Shopify developer + Help + Partner pages only.  
**Rule:** This file changes strategy. It does not invent install counts or rating thresholds Shopify did not print.

WAVE A (`APP_STORE_MARKET.md`, `RESEARCH_LOG.md`) said Built for Shopify numeric gates were **unpublished**. WAVE C correction: the **install and review gates are now on the official requirements page**. The **rating number is still unpublished**.

---

## 1. App Store money (developer)

Source: https://shopify.dev/docs/apps/launch/distribution/revenue-share (LIVE 2026-09-09)

| Rule | Official text |
| --- | --- |
| First $1,000,000 USD gross app revenue (from **January 1, 2025**) | **0%** revenue share — you keep 100% |
| Above $1,000,000 | **15%** (you keep 85%) |
| Processing | **2.9%** + applicable sales tax, charged **separately** from revenue share |
| Registration | **$19 USD** one-time per Partner account to sell on the App Store |
| Refunds | Revenue share is on **gross**, not net. Refunds are **not** deducted |
| Multi-app / multi-account | Gross is summed across **Associated Developer Accounts** |
| High-earner carve-out | If prior-year App Store earnings ≥ **$20,000,000** **or** company revenue ≥ **$100,000,000**, the $1M 0% band **does not apply**. 15% on all app revenue. Reassessed annually |

Help Center still describes the older “reduced 15% from 20% + 0% on first $1M” framing: https://help.shopify.com/en/partners/build-integrate/making-apps

`CURRENT_RELIGION` implication for Mcfly at $39: until $1M App Store gross, Shopify’s cut is the **2.9% processing fee**, not 15–20%. WAVE A’s “20% (or 15%) on $39 ≈ $31–$33 net” is **stale for a sub-$1M developer**. Recalc: $39 − 2.9% ≈ **$37.87** before tax. Do not publish that as a forecast; it is arithmetic on the official fee, not a Mcfly metric.

`RESEARCH_OPTION`: treat the $1M holiday as a **reason to stay on Shopify billing** rather than fight for off-platform.  
`EVIDENCE`: requirement 1.2 — off-platform billing cannot be distributed on the App Store (https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements).  
`RISK`: Associated Developer Account rules; hiding revenue across accounts is a Partner Program Agreement violation (same revenue-share page).

**Do not confuse** app-developer share with the **August 10, 2026 referral-partner earning model** (20% of merchant subscription + 0.1% eligible online GMV for 4 years). That is for partners who *refer stores to Shopify*, not for app SKUs. Sources: https://www.shopify.com/partners/blog/a-new-partner-earning-model · https://help.shopify.com/en/partners/help-support/faq/earnings

Partner Program Agreement still contains a 15% App Revenues clause: https://www.shopify.com/partners/terms — the **developer docs page above is the operational rate card** as of this fetch.

---

## 2. Built for Shopify — what it actually buys

Source: https://shopify.dev/docs/apps/launch/built-for-shopify (LIVE)

Promotional benefits once granted:

| Benefit | Exclusive to BFS? |
| --- | --- |
| Listing highlight at top of highlights list | BFS |
| Badge on app card (search, category, listing) | BFS |
| Search filter “Built for Shopify” | BFS |
| Priority App Store review queue for *future* apps | BFS developers |
| App Store **ads plan-based targeting** | BFS |
| Search ranking boost | **Not exclusive** — BFS ranks above other boosted apps |
| Homepage / category first collection eligibility | Not exclusive; personalized; **not guaranteed** |
| Admin “Picked for you” | Not exclusive; not guaranteed |
| Story pages | Eligibility needs min installs / reviews / rating (same unpublished rating number) |
| Sidekick / increased visibility achievement | Separate achievement; same usefulness trio |

Process facts that change calendar:

- You **must apply**. Prerequisites auto-evaluate; apply from Partner Dashboard → App → Distribution.
- Fail the **same criterion three times** → application **suspended 3 months**.
- Annual recertification. Failures: email + **60 days** to fix.
- Merchant Help Center: Shopify “reviews certifications annually”; badge can be **lost**. https://help.shopify.com/en/manual/apps/about-apps

---

## 3. BFS numeric gates (WAVE C correction)

Source: https://shopify.dev/docs/apps/launch/built-for-shopify/requirements §1.2 (LIVE 2026-09-09)

| ID | Gate | Published number? |
| --- | --- | --- |
| 1.2.1 | Minimum **50 net installs from active shops on paid plans** | **Yes** |
| 1.2.2 | Minimum **five reviews** | **Yes** |
| 1.2.3 | Minimum **recent** app rating | **No number printed** |

Repo `APP_STORE_LISTING.md` heuristic (“~50 paid-plan installs + 5 reviews”) now **matches official 1.2.1 / 1.2.2**. WAVE A was wrong to call those unpublished. The **rating** gate remains unpublished — do not invent 4.0 or 4.5.

Other BFS requirements that bite Mcfly’s current shape:

| ID | Requirement | Mcfly research read |
| --- | --- | --- |
| 2.1.1–2.1.3 | Admin Web Vitals at p75: LCP ≤2.5s, CLS ≤0.1, INP ≤200ms; **≥100 calls / 28 days** to be assessed | New apps cannot even *be measured* until traffic exists |
| 2.2.1 | Storefront Lighthouse drop ≤10 points | Paste-CSV desk should be fine if no theme inject |
| 3.1.1–3.1.2 | Embedded App Bridge; primary workflows **inside admin**; do not embed the marketing site | `CURRENT_RELIGION` site-as-product is a BFS reject if the admin iframe is a brochure |
| 3.1.3 | Seamless signup on Shopify credentials; extra login only for B2B exceptions | Fine if install = account |
| 3.1.4 | **Simplified monitoring/reporting on app home** even if the real reports live elsewhere | This is the cash desk’s actual BFS job |
| 3.1.5 | Third-party connection settings inside admin | Future OAuth spend (`RESEARCH_OPTION` R3) must live in the embedded app |
| 4.1.1 | Look like admin. **Rejection examples include black background, non-Polaris primary buttons, serif/script body, green/purple primaries** | Ledger black canvas is a **documented BFS reject reason** if it is the admin UI. Marketing site is out of scope; **embedded app is not**. |
| 4.1.2 | Mobile: no unreachable content, no forced two-column |
| 4.1.4 | Use App Bridge nav, not a second nav |
| 4.1.5 | Contextual Save Bar for forms |

`CURRENT_RELIGION`: “Do not chase BFS until ~50 paid + 5 reviews.” Still correct as a **sequence**.  
`RESEARCH_OPTION`: design the **embedded** app to Polaris *now*, because 4.1.1 will block the badge even after the 50/5 gate.  
`EVIDENCE`: requirements 4.1.1 rejection list (same page).  
`RISK`: rewriting the marketing site to Polaris does **nothing** for BFS; only the admin app is scored.

---

## 4. Review policy (the ranking object)

Source: https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews (LIVE)

| Rule | Official |
| --- | --- |
| Who | Installed merchants, or within **45 days of uninstall** |
| Overall rating | **Not a simple average.** Weighted for recent / useful / trustworthy |
| Search | “positive reviews make your app appear higher in … search results and category pages” |
| AI Magic summary | ≥**100 reviews with body text** and ≥**4.0**; up to **14 days** to appear |
| Neutral ask only | Example they bless: “We value feedback! …” |
| Forbidden | “Leave us a **positive** review”; incentives; unsolicited review email; ask at **onboarding/install**; fake reviews; compelling edits |
| Consequences | Review removal; **ranking demotion**; removal from promotional surfaces; **unpublish**; Partner account termination (requirements 1.3) |
| Unpublished reviews | Do not count toward total or rating. Appeal exists |
| Trust delay | A review “may not appear immediately”; Shopify establishes trust first |

App Store requirements 1.3.1 (same requirements page): incentives forbidden **in-app and off-platform**.

`CURRENT_RELIGION`: no paid reviews, no “positive” CTA. Keep.  
`RESEARCH_OPTION`: App Bridge review modal **after** first week with spend>0 and a rendered Total ROAS — official “don’t ask at onboarding.”  
`EVIDENCE`: “How not to ask” table on the manage-reviews page.  
`RISK`: 0 reviews forever if merchants never add spend in 7 days (TTV mismatch; see `PRICING_LADDERS.md`).

---

## 5. Listing + billing constraints that change packaging

Source: https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements (LIVE)

- **1.2** Bill through Shopify App Pricing / Billing API. Off-platform billing = not distributable.
- **1.2.3** Merchants must **upgrade/downgrade without support tickets or reinstall**.
- **1.1.4 / 1.1.5** Factual listing only; no duplicate apps.
- WAVE A already logged: **no testimonials in listing copy or images** (4.3.x). Social proof = Shopify’s review module only.
- Trials: Shopify tracks trial days over **180 days** to stop reinstall-reset. https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials

`RESEARCH_OPTION` vs `CURRENT_RELIGION` on price: a $39 → $79 jump is legal if Billing API can change plans in-app. It is still commercially stupid at 0 reviews (`RELIGION_FLEX.md` R5).

---

## 6. Strategy menu this file actually supports

| Move | Tag | Why this file |
| --- | --- | --- |
| Stay on Shopify billing | `CURRENT_RELIGION` + evidence | $1M 0% share + 1.2 ban on off-platform |
| Do not apply for BFS this week | `CURRENT_RELIGION` | 0 installs, 0 reviews; 1.2.1 / 1.2.2 fail |
| Design embedded UI for Polaris, not Ledger-black | `RESEARCH_OPTION` | 4.1.1 reject list |
| Neutral review modal after first computed week | `RESEARCH_OPTION` | Official ask rules |
| 14-day trial (not 7) | `RESEARCH_OPTION` (R4-B) | 180-day window still applies; 7 days is shorter than every loved profit peer we fetched |
| Treat BFS ads plan-targeting as a **later** weapon | `RESEARCH_OPTION` | Exclusive BFS benefit; useless before 50/5 |
| Do not pay for reviews / “positive” copy | `CURRENT_RELIGION` | Demotion / unpublish |

The Partner Program does not reward “anti-attribution” theology. It rewards **installs on paid shops, five written reviews, a recent rating Shopify will not name, an embedded Polaris app, and a listing that is not a pixel.**
