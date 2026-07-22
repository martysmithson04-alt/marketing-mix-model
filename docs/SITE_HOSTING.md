# Marketing site hosting — GitHub Pages

**Canonical host for mcflyads.com:** GitHub Pages (Actions), not Cloudflare Pages / Wrangler.

The Shopify app stays on **Fly** (`mcfly-analytics.fly.dev`). Do not set App URL to mcflyads.com.

## Why GitHub Pages

- `/site` is static HTML — perfect for Pages
- Deploy is already in CI (`.github/workflows/pages.yml`)
- Cloud agents can ship site changes via git push; no `CLOUDFLARE_API_TOKEN` needed
- Cloudflare stays useful as **free DNS** (optional orange-cloud proxy), not as the origin

## One-time setup (human, ~2 minutes)

### 1. Enable Pages (Actions source)

Repo → **Settings → Pages**:

- **Source:** GitHub Actions  
- Save

If the setting is missing, merge this branch to `main` and re-run **Deploy site to GitHub Pages** (workflow includes `enablement: true`).

### 2. Point DNS at GitHub

In Cloudflare DNS for `mcflyads.com` (DNS-only or proxied):

| Type | Name | Target |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `martysmithson04-alt.github.io` |

Then in repo Settings → Pages → Custom domain: `mcflyads.com` → enable **Enforce HTTPS** once DNS checks pass.

`site/CNAME` already contains `mcflyads.com`.

### 3. Stop Cloudflare Pages origin (if still live)

If an old Cloudflare Pages project still owns the domain, remove that custom domain / Pages route so GitHub is the origin. Keep Cloudflare as DNS registrar/proxy only.

## Deploy loop (ongoing)

| Event | What happens |
| --- | --- |
| Push to `cursor/**` touching `site/**` | `validate` job only (PR-safe) |
| Push / merge to `main` touching `site/**` | `validate` + **deploy** to GitHub Pages |
| Manual | Actions → **Deploy site to GitHub Pages** → Run workflow |

No Wrangler. No CF API token.

## Preview without custom domain

Until DNS is pointed: `https://martysmithson04-alt.github.io/marketing-mix-model/`  
Absolute paths (`/assets/...`) work correctly once the custom domain is attached; prefer testing on `https://mcflyads.com` after DNS.
