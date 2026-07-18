---
title: ADR-007 — Relocate published site to site/, reclaim docs/ for the knowledge system
description: Move the Cloudflare Pages deploy directory from docs/ to site/ so docs/ can hold the documentation source of truth.
---

# ADR-007 — Relocate published site to `site/`, reclaim `docs/` for the knowledge system

- **Status:** Accepted
- **Date:** 2026-07-18

## Context

The `docs/` directory historically served as the Cloudflare Pages deploy
directory: it held `index.html`, `ideas.json`, and the agent/GEO surfaces
(`llms.txt`, `api-ai.json`, etc.) — all generated or static artifacts, no
hand-written documentation. The hand-written docs (specs, portfolio strategy)
lived at the **repo root**.

This conflicted with two goals:

1. Building a structured `docs/` knowledge system (the conventional home for
   repository documentation) — impossible because `docs/` was already the
   deploy target.
2. Rendering that knowledge system with Blume, which reads a content folder
   (conventionally `docs/`) of Markdown.

Putting the knowledge system in `docs/` alongside `index.html`/`ideas.json`
would mix hand-written documentation with deploy artifacts and cause Blume to
try rendering `ideas.json` and the agent surfaces.

## Decision

1. **Relocate** the published site from `docs/` to `site/` (git-mv, preserving
   history): `index.html`, `ideas.json`, `llms.txt`, `llms-full.txt`,
   `index.md`, `api-ai.json`, `robots.txt`.
2. **Reclaim** `docs/` for the knowledge system: product, architecture,
   decisions, development, operations, knowledge.
3. **Update** `scripts/build.py` to write `site/ideas.json` (not
   `docs/ideas.json`) and to emit the new deploy command
   (`wrangler pages deploy ./site`) and new doc paths in the generated README.
4. **Move** the root spec/strategy markdown into `docs/` (git-mv):
   `family-tree.md`, `magic-form.md`, `productivity.md`, `storytunes.md` →
   `docs/product/specs/`; `spec-deep-dives.md` →
   `docs/knowledge/learnings/`; `PROJECT-STRATEGY.md` →
   `docs/product/portfolio-strategy.md`.
5. Blume reads `docs/` (`content.root: "docs"`); the published catalog stays at
   `site/`. The two presentation layers are fully independent.

## Consequences

- **Pro:** `docs/` now unambiguously means documentation, matching
  repo-wide convention.
- **Pro:** Blume can render the knowledge system without touching deploy
  artifacts.
- **Pro:** one home for each fact — specs no longer split between repo root
  and the catalog.
- **Con (operational):** the deploy command changes from
  `wrangler pages deploy ./docs` to `wrangler pages deploy ./site`. The
  Cloudflare Pages project (`saas-ideas`) build output directory must be
  updated to `site/` on the Cloudflare dashboard, or the deploy must pass
  `./site` explicitly (the README and runbook now do). **This is the one
  external action required to complete this ADR** — see
  [operations/deploy](../../operations/deploy.md).
- **Con:** the spec links inside `build.py` idea text (rendered in the
  published table) previously pointed to relative `family-tree.md` etc.,
  which were already 404 on the Pages site (specs were at repo root, never
  deployed). They now point to GitHub blob URLs so they resolve everywhere.

## Verification

After this change, `python3 scripts/build.py` must still succeed and produce
`site/ideas.json` with the same row count as before (the move is purely
relocation, no scoring change). The doc validator
(`scripts/check-docs.py`) must pass with no broken internal links.
