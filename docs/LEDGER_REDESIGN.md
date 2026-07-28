# Ledger redesign (Plan 2 merge)

Merged with the enterprise teardown on branch `cursor/enterprise-site-redesign-4593`.

| Gate | Target | Notes |
| --- | --- | --- |
| Raw hex outside `tokens.css` | 0 | Enforced in site.css / demo-desk / waitlist-dock |
| Body face | Public Sans | Replaces Instrument Sans / Figtree |
| Paper | `#F1F2EE` cool accounting stock | Not warm cream |
| Accents | `--black-ink` / `--red-ink` only | Semantic above/below |
| Hero | Typeset fraction + margin slider | Paints without JS; JS enhances BE line |
| Monogram | `mcfly-m.svg` (~346 B) | PNG retained as fallback asset |
| Decor layers | mesh/grain/gridline/atmosphere hidden | |

Rule file: `.cursor/rules/design-system.mdc`
Baseline sizes: `docs/audit/baseline/SIZES.txt`
