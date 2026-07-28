# Enterprise-grade site redesign — execution log

Source brief: founder teardown of live mcflyads.com (2026-07-28).

| Phase | Scope | Status |
| --- | --- | --- |
| 0 | Sync live site into `site/` | Done |
| 1 | Design tokens & type (no layout) | Done |
| 2 | Hero rebuild + desk → `/demo` | Done |
| 3 | Copy rewrite (§2.4 laws) | Done |
| 4 | Trust layer | Done |
| 5 | Structural de-templating | Done |
| 6 | Motion & polish | Done |
| 7 | QA gates | Partial — see PR |

## Phase 1 notes

- Palette: paper / ink / ledger-green / loss-red / brass / slate-mute
- Fonts: Newsreader (display) + Instrument Sans (body) + IBM Plex Mono (data)
- `--cyan` aliased to brass/ledger for compat; hardcoded `#5ee7f0` retinted
- Demo desk tokens inverted to dark instrument on light page
- `<strong>` removed from inside `<p>` only (UI labels in lists/tables kept)


## Ledger Plan 2 merge

Cool accounting paper, Public Sans, `tokens.css`, fraction hero, SVG monogram. See `docs/LEDGER_REDESIGN.md`.
