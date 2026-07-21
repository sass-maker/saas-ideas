---
title: Operations
description: Deploy runbook and the agent/GEO surfaces served by the published catalog.
---

# Operations

The published catalog is a static site on Cloudflare Pages. There is no server,
no database, no scheduled jobs, no migrations. Operations is essentially "build
and deploy".

- [Deploy runbook](deploy.md) — how to publish a catalog update.
- [Agent/GEO surfaces](agent-surfaces.md) — the machine-readable files served
  from `site/`.

## Scheduled jobs

None. `build.py` is run manually when scores change. There is no cron, no
GitHub Actions workflow that rebuilds the catalog, and intentionally no
automated scraping (see
[ADR-005](../architecture/decisions/adr-005-starterstory-inclusion.md)).

## Domains

The catalog is published through one Cloudflare Pages project:

- `https://ideas.sassmaker.com/` — the canonical public URL used by the
  generated README and agent/GEO surfaces.
- `https://saas-ideas.pages.dev/` — the provider-managed origin alias, useful
  only for deployment diagnostics.

The branded custom domain is canonical; do not present the provider alias as a
second public product URL.
