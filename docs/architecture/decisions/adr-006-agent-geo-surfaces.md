---
title: ADR-006 — Agent/GEO surfaces (llms.txt, /api/ai, index.md)
description: Publish machine-readable surfaces alongside the human catalog so agents and search can read the site.
---

# ADR-006 — Agent/GEO surfaces (llms.txt, /api/ai, index.md)

- **Status:** Accepted
- **Date:** 2026-07 (commit `33dd667`)

## Context

The published catalog is a client-rendered HTML table (`site/index.html` fetches
`site/ideas.json` at runtime). That is good for humans but invisible to AI
crawlers, search engines that execute limited JS, and agents that want a
machine-readable inventory. As agent discovery ("GEO") became relevant in 2025,
the site had no surface an agent could read without executing JavaScript.

## Decision

Publish four machine-readable surfaces from `site/` (served as static files by
Cloudflare Pages):

- `site/llms.txt` — the agent index (per the llms.txt convention): one-line
  product description plus links to the other surfaces.
- `site/llms-full.txt` — the full agent brief: product description, machine
  surface URLs, sitemap, robots, and fleet/contact pointers.
- `site/index.md` — a markdown version of the homepage (markdown negotiation:
  agents can fetch `.md` to get the brief without JS).
- `site/api-ai.json` — a JSON inventory of public surfaces, the `markdown`
  negotiation flag, and the `auth.public: true` declaration.
- `site/robots.txt` — explicitly allows `/llms.txt`, `/llms-full.txt`,
  `/index.md`, `/api/ai` for all user agents, and points to the sitemap.

## Consequences

- **Pro:** agents and AI crawlers can read the product without executing JS.
- **Pro:** `api-ai.json` follows a small convention (`name`, `version`, `url`,
  `surfaces`, `auth`) that other fleet projects also use, so a fleet-wide
  agent index is possible.
- **Con:** the surfaces reference `https://ideas.sassmaker.com/...` while the
  README references `https://saas-ideas.pages.dev/`. Both resolve to the same
  Cloudflare Pages project (custom domain + pages.dev), but the inconsistency
  is a documentation smell — see [operations](../../operations/).
- **Con:** `index.md` is a 2-line stub ("# SaaS Ideas / Scored catalog of SaaS
  product ideas."). It is intentionally minimal because the real data is in
  `ideas.json`; the markdown surface is a pointer, not a second data home.

## Non-goal

These surfaces describe the **catalog product**, not the knowledge system. The
knowledge system (`docs/`) is rendered by Blume and has its own (Blume-managed)
`llms.txt` / markdown negotiation. Do not duplicate knowledge-system content
into `site/`.
