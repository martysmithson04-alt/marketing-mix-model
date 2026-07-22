# Mcfly site craft — anti-slop design system

Use this before changing mcflyads.com. Agents that ignore it produce generic AI landing pages.

## Skeleton (locked)

**Name:** Cash Ledger  
**Metaphor:** Operator cash desk — spend out vs Shopify in. Not “AI platform,” not purple SaaS OS.

| Rule | Do | Don’t |
| --- | --- | --- |
| First viewport | Brand + one thesis + one lede + CTA + **live desk** | Centered pill stack, badge chips, logo wall, stats strip |
| Brand | `Mcfly Analytics` is the largest type in the hero | Tiny eyebrow brand |
| Product visual | Coded interactive desk (SVG/CSS), full-bleed plane | Stock photo, abstract blobs, glow orbs |
| Section rhythm | Asymmetric / editorial / definition stacks | Identical 3-card grids every band |
| Motion | ≤3 intentional pieces that teach the product | Fade-in-up on every block |
| Color | Cool paper + ink + forest truth + ledger red | Purple→indigo, neon glow, cream+terracotta |

## Tokens

```text
--ink        #12151a
--paper      #e8ecef
--paper-2    #f3f5f7
--chalk      #fbfcfd
--truth      #0d6b52
--truth-2    #149a72
--lie        #b83a2a
--steel      #161c24
--display    Bricolage Grotesque
--body       Figtree
--mono       IBM Plex Mono (numbers / labels only)
```

Hue band **200–290° (blue-purple) is banned** for accents. Default hero is **light ledger paper**, not dark-mode SaaS.

## Motion allow-list (only these)

1. **Hero MER count-up** — once on load (`[data-mer-count]`)
2. **Spark stroke draw** — once when sparkline paints (`.spark-path.is-draw`)
3. **Desk pointer parallax** — mouse/tilt on `[data-desk]`, subtle (~4.5°)
4. Optional: live demo sliders (already product, not decoration)

No IntersectionObserver stagger on every `.band`. Prefer no entry animation.

## Section patterns (anti 3-card)

- **Proof rail** — continuous bordered strip (`.lie-grid`), not floating cards
- **Wedge** — 2-column they/us (`.better-grid`), not equal trio cards
- **Formula** — ink steel band, typography only
- **How** — numbered vertical rail (`.how-rail`)
- **Live** — stacked instruments, not card mosaic

## Copy voice

- Short, operator English  
- Name the enemy (platform ROAS theater) once; then sell cash MER  
- No “unlock,” “supercharge,” “seamless,” “next-gen,” “AI-powered”

## Reference research (why)

Distinctive sites win on **structure** (skeleton), not parameter swaps (different purple). Prefer interactive product demos above the fold over cinematic canvas gimmicks. Sources informing this file: Sailop anti-slop hero compositions / motion guidance; SaaS “show don’t tell” hero demos.

## Deploy note

**Host:** GitHub Pages (see [`SITE_HOSTING.md`](./SITE_HOSTING.md)).  
Site changes ship by merging to `main` — CI deploys `/site`. Do not use Wrangler / Cloudflare Pages for the brochure.
