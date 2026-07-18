---
title: Architecture
description: Build pipeline, data flow, and deploy topology for saas-ideas.
---

# Architecture

The system has three layers, deliberately separated so the source of truth
(code) is never confused with the presentation (published site or docs site).

## Layers

1. **Source of truth** — `scripts/build.py` (idea lists, scores, scoring logic)
   and `data/starterstory_descriptions.json` (researched descriptions).
2. **Generated artifacts** — `README.md` and `site/ideas.json`, both written by
   `build.py`. Never hand-edited.
3. **Presentation** — two independent consumers of the generated artifacts:
   - **Published catalog** (`site/`) — static HTML table (`site/index.html`)
     that fetches `site/ideas.json` at runtime, plus agent/GEO surfaces. Deployed
     to Cloudflare Pages. See [operations](../operations/).
   - **Docs site** (`docs/` via Blume) — this knowledge system, rendered to
     static HTML by Blume. Markdown is the source of truth; Blume is only the
     presentation/search layer. See [development](../development/).

## Data flow

```
scripts/build.py  ── writes ──>  README.md            (generated stub)
                 ── writes ──>  site/ideas.json       (generated data)
                                                │
                                                ▼
                          site/index.html  (static, reads ideas.json at runtime)
                                                │
                                                ▼
                          Cloudflare Pages  ──>  saas-ideas.pages.dev

data/starterstory_descriptions.json  ── read by ──>  build.py
solopreneur_ideas.json (git history) ── read by ──>  build.py  (via fetch_sol())
```

`build.py` is a single self-contained Python script with no dependencies beyond
the stdlib (`json`, `re`, `csv`, `subprocess`, `pathlib`). It runs offline.

## Why a single script

The whole catalog is rebuilt from one script so that any score change is a
single, reviewable diff and the output is always reproducible. There is no
database, no partial state, no "migrate" step — `build.py` is idempotent and
fully rebuilds `README.md` + `site/ideas.json` on every run. See
[ADR-001](decisions/adr-001-single-source-of-truth.md).

## Deploy topology

- **Catalog** — `npx wrangler pages deploy ./site --project-name saas-ideas`
  → `saas-ideas.pages.dev` (also `ideas.sassmaker.com`). Static, no server.
- **Docs site** (planned) — `blume build` → `dist/`, deployable to a separate
  Cloudflare Pages project or path. Not yet wired into CI; see
  [operations runbook](../operations/deploy.md).

## Decisions

Architectural decisions are recorded as ADRs in [decisions/](decisions/). Each
ADR captures the context, decision, and consequences of a non-obvious choice.
Start with [ADR-001](decisions/adr-001-single-source-of-truth.md).
