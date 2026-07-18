---
title: Development
description: How to add, rescore, and build ideas in the saas-ideas catalog.
---

# Development

## Add or rescore an idea

All ideas and scores live in `scripts/build.py`. There is no other input. Pick
the right list for your idea (see [idea sources](../product/idea-sources.md)):

- New AI/ML idea → append a tuple to `AI_IDEAS`.
- New idea generated to fit the solo/$5K-MRR brief → append to `FRESH_IDEAS`
  (the only list that takes `F_feas` and `customer` inline).
- A flushed-out spec → append to `SPEC_IDEAS` and add the spec doc under
  `docs/product/specs/`.

Each tuple is `(F, M, T, C, ...)` (and `F_feas`, `customer` for `FRESH_IDEAS`).
The body **must** include a `**Comp:**` line (incumbents + funding) and a
`**Wedge:**` line (the defensible angle, or "none"). For fresh ideas, also
include a `$X/mo × N users = $5K MRR` math sketch and a `Tech:` line.

If your idea is not matched by the `FEAS` or `CUSTOMER` substring tables, add a
substring entry so `F_feas` and `customer` are stamped correctly rather than
left at the default (`F_feas=4`, `customer=non-dev`).

## Build

```
python3 scripts/build.py
```

Stdlib-only, offline. Writes `README.md` and `site/ideas.json`. The script
prints a summary: total ideas, best-bet count, max fun, max money, and the
Starterstory keep/drop counts.

## Validate docs

```
python3 scripts/check-docs.py
```

Checks every Markdown link in `docs/` resolves (internal links relative to the
repo, external links via HEAD), and that every `docs/**/*.md` has frontmatter
`title`/`description`. Exits non-zero on any failure. Run before committing
doc changes; CI runs it on push (see `.github/workflows/docs-check.yml`).

## Preview the docs site (Blume)

```
npm install        # first time only — installs blume (pinned in package.json)
npx blume dev      # hot-reload preview of docs/
npx blume build    # static HTML into dist/
npx blume validate # link validation through Blume itself
```

Blume is the presentation layer only — the Markdown in `docs/` is the source of
truth. See [blume.config.ts](../../blume.config.ts).

## Preview the published catalog

Open `site/index.html` in a browser, or serve the folder:

```
python3 -m http.server -d site 8000
# visit http://localhost:8000
```

The table fetches `site/ideas.json` at runtime, so always run `build.py` first.

## Do not

- Do not hand-edit `README.md` or `site/ideas.json` — both are generated.
- Do not hand-edit `site/index.html`'s data — it reads `ideas.json`. (The HTML
  shell itself is hand-maintained; edit it for layout/style only.)
- Do not add a new scoring axis without updating [scoring.md](../product/scoring.md)
  and adding an ADR.
- Do not commit `dist/`, `.blume/`, or `node_modules/` (see `.gitignore`).
