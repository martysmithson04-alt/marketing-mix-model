# Onboarding battle — first 10 minutes, winners vs losers

**Date:** 2026-09-09 (Wave B)  
**Mode:** RESEARCH ONLY.  
**Question:** In the first ten minutes after Install, who wins the merchant — and why Mcfly, as shipped, loses before the trial clock is interesting.

Sibling PR #6 (`MONETIZATION_PATTERNS.md` §5) already mapped official Shopify setup-guide rules. This file is the **battle record**: live products, live 1-stars, and a minute-by-minute of Mcfly’s actual Admin path.

---

## 0. What “first 10 minutes” means

Official Shopify ([Onboarding](https://shopify.dev/docs/apps/design/user-experience/onboarding)):

- Brief, direct. **Avoid more than five steps** (additional steps → drop-off).
- Request information **only if necessary**.
- Non-essential onboarding is **dismissible**.
- Discrete steps **auto-complete**; show **progress**.
- After completion, **remove** the onboarding UI.
- Merchants should know what to do next. That “leads to higher usage retention.”

Official homepage / BFS (cited in PR #6): the app home must show the app is **working** and, if possible, **how well** — not a static welcome. Primary workflows stay **in Admin**. Do not require installing **another** app as a setup step.

TSC MARKET_REPORT (May 2026, [onboarding-benchmarks](https://taylorsicard.com/blog/shopify-app-onboarding-benchmarks)) — **not Mcfly metrics**:

| Claim | Number | Use |
| --- | --- | --- |
| Median trial→paid | 15–20% | Planning stress test |
| Top-quartile trial→paid | 35–50% | Same |
| Median activation (first value in 7 days) | 35–40% | Same |
| Top-quartile activation | 60–70% | Same |
| 60-day retention after first paid month | median 50–60%; top 75–85% | Same |
| Abandonment texture | blank first screen → back to Admin in **20 minutes** → uninstall at next app audit | Descriptive |
| 72-hour rule | no activation → very high churn risk | Descriptive |
| Day-7 rule | without activation, recovery “statistically unlikely” | Descriptive |

Kompassify Aug 2026 (MARKET_REPORT): merchants **trial several apps the same afternoon**; they keep whoever shows a result first. Reviews are written disproportionately in week one — delight or rage.

**Mcfly constraint:** 7-day trial. If TSC’s day-7 recovery line is even directionally true, **the entire paid life of a Mcfly trial is the recovery window.** There is no week two of unpaid use.

---

## 1. Mcfly, minute by minute (as it exists)

Sources: live listing; `site/product.html` / `site/support.html`; shipped `app/app/routes/app._index.tsx` + `/app/spend` + `/app/connections` (OAuth stubs); `docs/APP_FEATURES.md`.

| Minute | What the merchant does | What they see | Verdict |
| --- | --- | --- | --- |
| 0:00 | Clicks Install on a **$39** card next to Clarity / Parkour **Free** | Permission: customers, orders, device/activity, store owner | Already a worse deal than the rail they came from |
| 0:30 | Lands in embedded app | **“MER Dashboard”** (repo name). Listing said **Total ROAS**. Period chips MTD/QTD/YTD | Integrity leak in the first screen |
| 1:00 | Reads four cards | Shopify sales (real, or $0 + error banner). **Ad spend (manual) $0**. MER blank. Break-even from whatever default margin | Official fail: homepage does not show the app **working well**. It shows Analytics they already have + an empty spend hole |
| 1:30 | Empty channel mix | “No spend recorded… Add spend entries” | The product is a **link to homework** |
| 2:00 | Opens Spend | Manual Meta / Google / Other. CSV is **Planned** in `APP_FEATURES.md`, while the **listing** already sells “Spend CSV” | Integrity leak #2. Site describes download-blank-template → Sheets Import → fill → download → paste |
| 2:00–20:00+ | Leaves Admin for Ads Manager / Sheets | This is **not** onboarding. This is the weekly job they already skip (Community 657805: sheet is a week behind) | Clock is dead. TSC’s 20-minute “back in Admin doing something else” is the designed path |
| If they return | Type a number or paste | MER appears. Allocation card may advise from sales∝spend if no channel sales | First value is **self-served fiction quality** unless they pasted real totals |
| Connections | “Connect Meta / Google” | **Stubs.** Live site: “No ad-account OAuth.” MASTER_PLAN Phase 2: OAuth | Third religion. Merchant who clicks Connect is trained that Mcfly is broken |
| Minute 10 | — | No checklist, no progress, no SAMPLE-to-live toggle in the Admin app (SAMPLE lives on the **marketing** demo, not the install) | Official: no setup guide, no 5-step cap, because there is no guide — only an empty desk |

`site/support.html` “live desk” order: *turn Sample desk OFF → Confirm margin → Paste spend → optional 4.0× goal → open Total ROAS.* That is a **website** ritual. The shipped Admin route does not mention Sample desk. Design-partner SAMPLE and production blank are different products.

**Listing vs app (first 10 minutes lies):**

| Listing / site claim | App in repo | First-session effect |
| --- | --- | --- |
| Total ROAS | Heading **MER** | Confused religion |
| Spend CSV | CSV **Planned** | Merchant hunts a button |
| LTV / Goals / full-year board | Not in route map | “Paid plan adds…” on a **single** $39 plan |
| 10 minutes | Requires leaving Admin | 7-day trial evaporates |
| mailto in listing bullet | Not a feature | Looks unfinished (Wave A teardown) |

This is not a polish issue. This is **onboarding as false advertising**. Shopify listing requirements: pricing and claims must be accurate. LTV/Goals/CSV as “now” is an App Review / 1-star seed.

---

## 2. Winners (first 10 minutes) — with evidence

A winner gets the merchant to a **confirmable outcome** without a second product and without a sales call.

### W1 — Parkour: “2 minutes, no coding”

- Listing hero: setup in **2 minutes**. Free. 4.9 / 191.
- Visible reviews: Kismet Glow (9 days) switched from native FB/IG; AROMATICA cites EMQ 9.2 (reviewer claim).
- Outcome: pixel/CAPI **working**. Verification lives in Events Manager — merchant can **see** it.
- Why they win: activation = “events fire.” Matches official “show it’s working.”
- Why Mcfly cannot copy the *mechanism* without breaking religion. Mcfly can copy the **timebox**.

### W2 — Clarity: one-click, Free, Microsoft

- 4.6 / 2,125. Launched 2025-07-17. Heatmaps/replays appear as traffic exists; empty-store path is still a working shell.
- Outcome: recordings exist or a clear empty state that is **the product** (watch sessions), not a hole where the product should be.
- Why they win: zero price + instant surface + brand. Mcfly has none of three.

### W3 — TrueProfit / Lifetimely / Kleio: connect ads, number appears

- TrueProfit listing: “Real-time sync ad spends from Facebook, Google, TikTok…” 14-day. First value = **profit tile with spend in it** after OAuth + Cost per item (partial). Named CS (Vani, Durra) if it fails.
- Lifetimely: Free ≤50 orders; 14-day on paid. ATTN 2026: build dashboard + **automated daily email** as a late onboarding step — but **P&L is visible first**.
- Kleio: 14-day, $29, “connect ad channels… real-time,” founder replies to reviews. 5-stars at 2–8 months of use (not 2-day dopamine only). Trek Light / EMME: left TW.
- Why they win: **OAuth is the onboarding.** Homework is COGS, which they can defer (progressive disclosure — TSC). Official: don’t ask what you don’t need for first value.

### W4 — Better Reports: support *is* minute 10

- Becky's Boutique (2026-07-01): ~20 hours using, 5★ because support **built the report**. ShopCOTW (2026-09-03): stock-movement filter delivered **in hours**.
- Why they win: first value can be **a human artifact**. 5.0 / 1,198. This is not scalable at $19.90 without a team — they have a team. Mcfly’s “human inbox” is the right *shape* and the wrong *capacity*.

### W5 — Elevar: named onboarder in first 11 days

- APM Monaco (2026-09-04), LÜME, Old Bones. $225+. Outcome: tracking punch list, not a dashboard selfie.
- Why they win: **enterprise first 10 minutes is a calendar invite**, not a wizard. Polar 5-stars say the same. Polar 1-stars are people who wanted W1 and got a **sales-call gate**.

### W6 — Official-compliant setup guide (category-agnostic)

Shopify App Founders / May 2026 activation playbook (MARKET_REPORT): define one activation; ≤5 checklist items; start with install already ticked; live verification; 24h one-ask email; 72h founder-signed rescue. TSC: checklists **longer than five** get treated as optional.

Winners in this aisle either **skip the checklist** (Parkour) or **make step 3 the value** (connect ads → see profit).

---

## 3. Losers (first 10 minutes) — with evidence

### L1 — Blank desk + homework (Mcfly’s designed path)

TSC first-person: *first screen after install showed me a blank dashboard… within twenty minutes I was back in my Shopify admin.* That is Mcfly’s `/app` with $0 spend.

Kompassify: if first result needs a scheduled hour (export three ad accounts), merchants abandon and **do not resume**.

### L2 — Polar sales-call / email-verify gate

Visible 1-stars are **pre-value**:

| Reviewer | Time-to-rage | Cite |
| --- | --- | --- |
| dryoasisplants, 2024-10-01 | **6 minutes** | “before you can try — it requires a sales call” |
| Skechers.dk, 2023-05-12 | 6 minutes | Email verify never arrives |
| Minseart, 2025-04-25 | immediate | “private emails not allowed” |

Polar can afford this at $750 + CS. Mcfly cannot. **Do not copy Polar’s gate.** Copy Polar’s *post-gate* human.

### L3 — TW enterprise UI on a small shop

BioPower Pet (2026-04-02): overload, would leave if not for **historical data lock-in**. Noirblanc 2★: cannot even launch; no CS. Zamage: polished **sales** onboarding, then CSM void.

First 10 minutes as a **demo theater** that dumps you into an OS = 16% 1-star texture (not only onboarding, but onboarding is the start).

### L4 — 12-step configure-everything wizard

TSC: “the worst-performing pattern in Shopify app onboarding, and also the most common.” Features-before-activation. Mcfly does not have this wizard. Mcfly has the **other** failure: **zero guidance, zero value**. Opposite costume, same outcome.

### L5 — “Install our other app” / connector tax

Official: do not require installing another app. Mcfly site tells merchants they **may** pay SyncWith / Coupler / Supermetrics to fill a CSV. That is honest and **onboarding-lethal**. First 10 minutes now includes a **second** vendor. Winners hide pipes (TrueProfit OAuth). Losers send you shopping.

### L6 — Trial shorter than time-to-homework

Shopivibe MARKET_REPORT (Wave A): 7-day only if TTV is **immediate**. Profit cluster live trials: TrueProfit / Lifetimely / BeProfit / Better Reports / Kleio / SyncWith = **14**; Elevar **15**; Metorik / A2X **30**. Mcfly **7**. The 7 is a loser configuration for a paste product. It would be a winner configuration for Parkour.

### L7 — Implementation product that misses the SLA

Analyzify Raregen (2025-09-11): $295 professional implementation, listed 1–2 business days, **nothing**, self-installed from docs. Tameson: six stores, five months to first prod beta. First 10 minutes were a **ticket**. Then a 1-star months later. White-glove that misses its own clock is worse than no white-glove.

---

## 4. Battle table (same merchant, same afternoon)

Imagine P1 founder who searched “ROAS” or clicked “more like this” from a pixel app. They install two things. Who keeps them?

| Pair | Minute 10 winner | Why |
| --- | --- | --- |
| Parkour vs Mcfly | **Parkour** | Free, 2 min, EMQ. Mcfly still empty. |
| Clarity vs Mcfly | **Clarity** | Free, working shell. |
| TrueProfit vs Mcfly | **TrueProfit** | 14-day, spend sync, profit tile. Same ~$35–39 wallet. |
| Kleio vs Mcfly | **Kleio** | $29, 14-day, ads connect, P&L. Same rail. |
| Lifetimely Free vs Mcfly | **Lifetimely** | $0 ≤50 orders, daily P&L. |
| SyncWith vs Mcfly | **SyncWith** if they live in Sheets | $4.99, they already have the ritual. |
| Better Reports vs Mcfly | **Better Reports** if they wanted a report | Email/Sheets out. Mcfly is spend *in*. |
| Polar vs Mcfly | **Neither**, or Polar if they book the call | Polar 1-stars in 6 min; Mcfly blank in 6 min. Polar wins only the merchant who wanted a warehouse. |
| Mcfly vs Sheet they already have | **Sheet** | $0, no new permission surface. |

There is **no public pairing** in which paste-only Mcfly wins minute 10 against a current alternative for the same job. The only win condition is **no alternative installed** and a founder who already has this week’s CSV on the clipboard. That person is a design partner, not an App Store shopper.

---

## 5. What “winning” would look like without becoming Parkour

Religion-flexible, still cash:

| Minute | RESEARCH_OPTION path | Official / evidence |
| --- | --- | --- |
| 0:30 | Checklist of **4**: Installed ✓ · Sales live ✓ · Spend connected **or** SAMPLE spend loaded · See Total ROAS | Shopify ≤5; install pre-ticked (Kompassify) |
| 1:00 | Home shows **live sales** + **last-7-days spend** (OAuth) or clearly labeled **SAMPLE spend vs live sales** | Homepage “working + how well” |
| 3:00 | One definition line: “Shopify Total Sales after returns, tax ___” | Kove / VocaSpark 1-stars |
| 5:00 | Claims-vs-cash only if platform number exists; else hide | Don’t ask what you don’t need |
| 8:00 | “Email me this every Monday” toggle — default **on** | Better Reports loop |
| 10:00 | Progress complete; onboarding UI **removed** | Official |

CSV / billboard paste becomes **step 6**, after first value — progressive disclosure (TSC). Official: don’t require SyncWith.

**Activation metric to instrument** (hypothesis, not measured): `first_computed_mer_with_spend_gt_0` inside 24 hours. Secondary: `monday_email_opened` inside 14 days. If the founder will not OAuth, the activation metric is **structurally** >10 minutes for almost all App Store shoppers. Then the honest trial is **14–30 days**, not 7.

---

## 6. Email as onboarding (Mcfly has none)

TSC: Shopify-app welcome emails **51–64%** open (MARKET_REPORT) — highest engagement besides the install. One ask, not a feature tour. 72-hour rescue **from a named human**.

Mcfly today: no lifecycle email. The highest-leverage onboarding change that does **not** require Meta App Review is a **founder-signed** “paste these three cells or reply with your CSV” message at +24h and +72h. That is still a loser vs TrueProfit OAuth. It is a winner vs silence.

Do **not** ask for a review at install (official: no install-time nag; no “leave a positive review”).

---

## 7. Empty-store and zero-ad-spend paths

Kompassify: design **zero orders** as onboarding, not an error. Mcfly’s honest empty-store state is “you have no sales; Total ROAS is undefined.” That can still be a **working** explanation + SAMPLE. Today, a store with sales and no spend sees a **half-working** lie (sales yes, MER no). Worse than empty: it looks broken.

A store with no ads should not be in the ICP (TSC mismatch). The listing hero (“including billboards”) invites them anyway. First 10 minutes for a non-advertiser: they confirm Mcfly is not for them and uninstall. That uninstall still counts in TSC’s ranking gossip.

---

## 8. Verdict

**Winners** compress TTV to a **verified number or a verified fire**, inside Admin, in ≤10 minutes, with ≤5 steps, and a 14-day clock if the number needs a day of data.

**Losers** show a blank, a sales call, a second vendor, a 12-step wizard, or a 7-day clock on a homework product.

Mcfly is a **textbook loser** of the first 10 minutes: blank spend, name mismatch, listing claims not shipped, OAuth stub, 7-day trial, pixel-rail ICP, no checklist, no email, no SAMPLE in Admin. Religion did not force this. **Incompletion** did. Phase 2 OAuth is already in MASTER_PLAN. Live site forbids it. The first 10 minutes are that contradiction, rendered as a $0 spend card.

---

## Sources

- https://shopify.dev/docs/apps/design/user-experience/onboarding
- https://shopify.dev/docs/apps/launch/marketing/manage-app-reviews
- https://taylorsicard.com/blog/shopify-app-onboarding-benchmarks (MARKET_REPORT)
- https://kompassify.com/blog/shopify-app-onboarding-guide (MARKET_REPORT)
- Live listings 2026-09-09 (Mcfly, Kleio, Parkour, Clarity, TrueProfit, Polar)
- Repo: `app/app/routes/app._index.tsx`, `docs/APP_FEATURES.md`, `site/product.html`
- Wave A: `REVIEW_THEMES.md` Theme F; `APP_STORE_MARKET.md` §7
- PR #6 §5 (sibling)
