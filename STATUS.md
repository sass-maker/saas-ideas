# STATUS.md

Short view of the current objective, active work, blockers, and next steps.
Last updated: 2026-08-01.

## Current objective

Build a maintainable, local-first knowledge system for `saas-ideas` and
consolidate the scattered docs (specs, strategy, market research) into one
canonical `docs/` tree rendered by Blume. Markdown stays the source of truth;
Blume is presentation only.

## Just completed

- Added an intentional 390px catalog layout that presents each idea first,
  keeps Best/Money/Fun plus source/customer context visible, and exposes mobile
  sorting without changing desktop table, filter, or score behavior.
- Made `ideas.sassmaker.com` the single canonical public URL.
- Added tracked Cloudflare Pages configuration for the `site/` output directory
  so Git-connected builds cannot publish the Blume docs tree by mistake.
- Removed the redundant Actions deployment lane; Cloudflare Git integration is
  the sole automatic catalog deploy path.
- Added the sitemap referenced by robots and agent surfaces.

## Knowledge-system consolidation

- Relocated the published catalog `docs/` → `site/` (git-mv, history
  preserved) and reclaimed `docs/` for the knowledge system
  ([ADR-007](docs/architecture/decisions/adr-007-relocate-site-reclaim-docs.md)).
- Moved root specs/strategy into `docs/`:
  `family-tree.md`, `magic-form.md`, `productivity.md`, `storytunes.md` →
  `docs/product/specs/`; `spec-deep-dives.md` →
  `docs/knowledge/learnings/`; `PROJECT-STRATEGY.md` →
  `docs/product/portfolio-strategy.md`.
- Updated `scripts/build.py` to write `site/ideas.json`, emit the new deploy
  command, and point spec links at GitHub blob URLs.
- Wrote `AGENTS.md`, `docs/` knowledge tree (product, architecture, 7 ADRs,
  development, operations, knowledge/learnings, knowledge/failed-approaches),
  `blume.config.ts`, `package.json`, `scripts/check-docs.py`, CI workflow.
- Updated `.gitignore` for Blume outputs and agent logs.

## Active work

- Verify the first Git-connected production deployment using `wrangler.jsonc`.

## Blockers / unresolved questions

1. **Docs site deploy target not fixed:** Blume `dist/` needs a separate
   Cloudflare Pages project (e.g. `saas-ideas-docs`) and a canonical URL.
2. **Blume version:** pinned to `1.0.2` in `package.json` (1.0.3 is 5 days old
   at the time of writing, below the 7-day vetting threshold). Bump to a newer
   stable version once it has aged.

## Next steps

1. Verify `ideas.sassmaker.com`, `sitemap.xml`, and agent surfaces after the
   Git-connected deployment.
2. `npm install` + `npx blume build` to verify the docs site renders; pick a
   docs deploy target.
3. Wire a docs-deploy step into `.github/workflows/docs-check.yml` once the
   target is decided.
