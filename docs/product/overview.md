---
title: Product Overview
description: What the saas-ideas catalog is, who it's for, and what it outputs.
---

# Product Overview

`saas-ideas` is a personal decision-support tool: a scored, sortable catalog of
SaaS product ideas, filtered to the subset that is tech-heavy and plausibly
solo-shippable to a $5K MRR target. It is **not** a product for sale — it is the
upstream reasoning that picks which fleet project becomes the next commercial
bet (see [portfolio strategy](portfolio-strategy.md)).

## Output

A single static HTML page (`site/index.html`) that renders a sortable, filterable
table from `site/ideas.json`. Each row is one idea with:

- raw scores `F / M / T / C` (each /10)
- solo feasibility `F_feas` (/10) and a one-line reasoning
- customer type (`dev` / `b2b-tech` / `non-dev`)
- derived `fun = F + T` and `money = M + F_feas − C`
- a `best_bet` flag (see [scoring model](scoring.md))
- a free-text idea body containing the wedge, competitor notes, and a rough
  $5K-MRR math sketch for fresh ideas

The page is deployed to Cloudflare Pages at
<https://saas-ideas.pages.dev/> (also reachable as
<https://ideas.sassmaker.com/> — see [operations](../operations/)).

## Audience

One person: the maintainer. The catalog exists to enforce honest, reproducible
ranking rather than vibes-based prioritization. The published site is public so
the reasoning is inspectable, not because there is an external user base.

## What it is not

- Not a CRM, not a backlog tracker, not a project management tool.
- Not a marketplace of ideas for others to vote on.
- Not auto-updated by agents — every score is a deliberate human (or
  human-directed) judgement recorded in `scripts/build.py`.

## Related

- [Scoring model](scoring.md) — exact formulas and what each axis means.
- [Idea sources](idea-sources.md) — where the ideas come from.
- [Specs](specs/) — four ideas flushed out into full product specs.
- [Portfolio strategy](portfolio-strategy.md) — how catalog output feeds fleet
  commercial-bet decisions.
