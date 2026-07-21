---
title: Deploy Runbook
description: Step-by-step publish flow for the saas-ideas catalog and the docs site.
---

# Deploy Runbook

## Catalog (Cloudflare Pages)

Prerequisites: Python 3, `npx`/Node, and `wrangler` authenticated to the
`sass-maker` Cloudflare account.

```
# 1. Rebuild from source of truth
python3 scripts/build.py

# 2. Sanity-check the output
python3 scripts/check-docs.py
python3 -c "import json;d=json.load(open('site/ideas.json'));print('rows:',len(d),'best_bets:',sum(x['best_bet'] for x in d))"

# 3. Preview locally (optional)
python3 -m http.server -d site 8000

# 4. Deploy
npx wrangler pages deploy ./site --project-name saas-ideas
```

### Git-connected production builds

`wrangler.jsonc` is the tracked source of truth for the Pages output directory
and points production builds at `site/`. Cloudflare's Git integration publishes
`main`; do not add a second Actions deployment pipeline.

The explicit Wrangler command above remains the recovery path when a clean,
validated `main` deployment must be republished manually.

## Docs site (Blume → static)

Not yet wired to CI. Manual publish:

```
npm install
npx blume build        # writes dist/
npx blume validate     # link check
npx wrangler pages deploy ./dist --project-name saas-ideas-docs
```

The docs site is a separate Pages project from the catalog. Its URL is not yet
fixed — see
[STATUS.md](https://github.com/sass-maker/saas-ideas/blob/main/STATUS.md).

## Rollback

Both Pages projects keep per-deploy aliases. To roll back, open the project in
the Cloudflare dashboard → Deployments → promote a previous deployment. No
code rollback is needed because the source of truth (`build.py`, `docs/`) is
versioned in git.

## What not to do

- Do not deploy `docs/` as the catalog — it is the documentation source, not
  the published site. The catalog lives in `site/`.
- Do not deploy without running `build.py` first — `site/ideas.json` may be
  stale relative to `build.py`.
- Do not commit `dist/` or `.blume/` — they are build outputs.
