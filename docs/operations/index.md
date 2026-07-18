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

The catalog is reachable at two URLs that resolve to the same Cloudflare Pages
project:

- `https://saas-ideas.pages.dev/` — the Pages default domain (referenced in
  the generated `README.md`).
- `https://ideas.sassmaker.com/` — custom domain (referenced in the agent/GEO
  surfaces in `site/`).

**Open inconsistency:** the two surfaces use different canonical URLs. Pick one
(`ideas.sassmaker.com` is the friendlier, branded one) and align both before
the next deploy. Tracked in [STATUS.md](../../STATUS.md).
