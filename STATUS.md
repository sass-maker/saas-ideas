# STATUS.md

Short view of the current objective, active work, blockers, and next steps.
Last updated: 2026-07-18.

## Current objective

Build a maintainable, local-first knowledge system for `saas-ideas` and
consolidate the scattered docs (specs, strategy, market research) into one
canonical `docs/` tree rendered by Blume. Markdown stays the source of truth;
Blume is presentation only.

## Just completed (this change)

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

- None in flight. Awaiting human review of this consolidation before any
  deploy or push.

## Blockers / unresolved questions

1. **Cloudflare Pages build output directory** was `docs/`, now needs to be
   `site/` on the dashboard (or always pass `./site` to
   `wrangler pages deploy`). **Human action required** — see
   [deploy runbook](docs/operations/deploy.md).
2. **Canonical URL inconsistency:** `README.md` says
   `saas-ideas.pages.dev`; agent surfaces in `site/` say
   `ideas.sassmaker.com`. Pick one and align both.
3. **Missing `sitemap.xml`:** `site/robots.txt` references
   `https://ideas.sassmaker.com/sitemap.xml` but no sitemap is committed.
   Either generate one or drop the reference.
4. **Docs site deploy target not fixed:** Blume `dist/` needs a separate
   Cloudflare Pages project (e.g. `saas-ideas-docs`) and a canonical URL.
5. **Blume version:** pinned to `1.0.2` in `package.json` (1.0.3 is 5 days old
   at the time of writing, below the 7-day vetting threshold). Bump to a newer
   stable version once it has aged.

## Next steps

1. Human reviews this diff; address feedback.
2. Update Cloudflare Pages project build output to `site/` (or confirm the
   explicit-`./site` deploy command is the workflow).
3. Resolve the canonical-URL and sitemap gaps above.
4. `npm install` + `npx blume build` to verify the docs site renders; pick a
   docs deploy target.
5. Wire a docs-deploy step into `.github/workflows/docs-check.yml` once the
   target is decided.
