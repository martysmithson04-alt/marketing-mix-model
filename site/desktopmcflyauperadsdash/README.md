# desktopmcflyauperadsdash

**Separate static Cash Desk** for service businesses and non-Shopify operators.
Runs entirely in the browser on GitHub Pages. **Not** the Shopify app. **Not** Fly. **Not** Cloudflare Workers.

## Isolation guarantees

| Surface | This folder touches it? |
| --- | --- |
| `/app` Shopify embedded app | **No** |
| `fly.toml` / Fly deploy | **No** |
| Cloudflare Workers / Pages / Wrangler | **No** |
| Waitlist / lead-gen on `index.html` | **No** |
| `packages/*` connectors / overnight | **No** |
| Marketing chrome (`site.css`, waitlist-dock) | **No** — Desk has its own CSS/JS |

**Allowed shared read-only asset:** `/assets/tokens.css` (colors/spacing tokens only — Desk does not edit that file).

## URL (after merge to main + Pages deploy)

`https://mcflyads.com/desktopmcflyauperadsdash/`

## What it does

1. Upload or paste **revenue** + **channel spend** CSVs  
2. Compute Cash MER, break-even MER, verdict, assumed cash-share mix, allocation  
3. Persist ledger in **localStorage** only (this browser)  
4. Export CSV + print weekly summary  

No accounts. No server. No Meta/Google OAuth.

## Local preview

Open `index.html` via any static server from `site/`, e.g.:

```bash
npx --yes serve site
# then visit /desktopmcflyauperadsdash/
```

## CSV schemas

**Spend:** `date,channel,amount,currency,note`  
**Revenue:** `date,amount,currency,note`
