# Marty Smithson — portfolio

Static personal site for **Marty Smithson** (American Fork, Utah). Marketing analytics and measurement: MMM, attribution, incrementality.

This folder is standalone. It does not join the repo root npm workspaces and does not change the Mcfly Analytics app or `site/` marketing pages.

**Side project (not the portfolio’s employer story):** [Mcfly Analytics](https://mcflyads.com) — Shopify app.

## Local

```bash
cd marty-portfolio
npm install
npm run dev      # http://localhost:4321
npm run build    # writes ./dist
npm run preview  # serve ./dist
```

Requires Node 18+.

## Deploy on Cloudflare Pages

Fully static. No server functions, no Astro adapter.

### Git integration

1. In Cloudflare Pages, create a project from this repository.
2. Set **Root directory** to `marty-portfolio`.
3. Build command: `npm run build`
4. Build output directory: `dist`
5. Framework preset: none (or Astro). Node 18+ / 22 is fine.

After the first production hostname exists, set `site` in `astro.config.mjs` to that origin so canonical and Open Graph URLs are absolute. Then add the same origin as `Sitemap:` in `public/robots.txt`.

### Direct upload (`wrangler`)

From this folder, after a local build:

```bash
cd marty-portfolio
npm install
npm run build
npx wrangler pages deploy dist
```

`wrangler` will ask for a project name on first deploy (for example `marty-portfolio`). Subsequent deploys reuse it.

### Headers

`public/_headers` ships with the build (`nosniff`, referrer policy, frame deny). Cloudflare Pages applies it automatically.

## Content source

Experience titles and dates follow [LinkedIn](https://www.linkedin.com/in/marty-smithson). Metrics on the Work section are the figures already associated with those roles — nothing extra is invented here.
