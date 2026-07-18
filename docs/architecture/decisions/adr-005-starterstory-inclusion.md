---
title: ADR-005 — Starterstory inclusion: tech-first + >= $5K/mo
description: Include Starterstory case studies only if tech-first category and >= $5K/month revenue.
---

# ADR-005 — Starterstory inclusion: tech-first + >= $5K/mo

- **Status:** Accepted
- **Date:** 2026-03 (commits `43ec54b`, `24ca4bb`, `816ba2f`)

## Context

Starterstory founder interviews were scraped into `solopreneur_ideas.json` and
merged into the catalog. The raw scrape included hundreds of entries across
every category — no-code tools, content sites, service businesses, dropshipping
— most of which are not tech-heavy and many of which earn trivial revenue.
Including all of them drowned the hand-curated ideas and made the catalog noisy.

The scrape was then deleted entirely (`43ec54b`) to clean up, which threw away
genuinely useful tech-first case studies (e.g. Plausible at $258K/mo, Boot.dev
at $236K/mo) that serve as existence proofs for the $5K MRR target.

## Decision

Re-include Starterstory entries, but with two hard filters applied in
`build.py`:

1. **Tech-first category only** — the `CAT` table assigns each Starterstory
   category a `T_baseline`; only categories with `T_baseline >= 7` are kept
   (GPT Wrappers, Micro SaaS, Solo Developer, Automation, Digital Products,
   Freemium/OSS, Plugins, Makers for Makers). Non-tech categories
   (Solopreneur, Productized Services, Weekend Projects, No-Code, etc.) are
   dropped.
2. **Revenue >= $5K/month** (`MIN_REVENUE = 5000`) — parsed from the
   `$X/month` string in each entry.

Additionally, `SOL_DROP` excludes a few categories outright (sitemap,
travel/digital-nomad, niche blogs, niche sites, launched-with-website-builder)
that are not product ideas at all.

Scores for kept entries are **derived**, not hand-set: `F/T/C` from the
category baseline (`CAT`), `M` from parsed revenue (`m_from_revenue`).
Descriptions come from `data/starterstory_descriptions.json` (pre-researched
clean summaries), falling back to `extract_description()` which strips the
interview boilerplate.

## Consequences

- **Pro:** the catalog includes real revenue existence proofs without being
  drowned by non-tech or sub-$5K entries.
- **Pro:** derived scoring means no per-entry hand-scoring effort for
  ~30-40 kept entries.
- **Con:** the source data is frozen in git history (`fetch_sol()` reads it
  from there, not the network). New Starterstory stories are not picked up
  automatically. This is accepted — re-scraping would re-introduce ToS and
  reproducibility problems for no scoring benefit.
- **Con:** derived `F_feas` for Starterstory entries defaults to 4 (unmatched
  in the `FEAS` table), which is honest ("we haven't feasibility-scored this
  external case study") but means their `money` score is conservative.

## Why descriptions are pre-researched

`extract_description()` strips boilerplate but the raw interview intros are
rambling and off-topic. A parallel agent pass fetched each kept story URL and
wrote a clean 1-2 sentence product summary; those are stored in
`data/starterstory_descriptions.json` keyed by URL. `build.py` prefers the
pre-researched description and only falls back to extraction if a URL is
missing from the JSON.
