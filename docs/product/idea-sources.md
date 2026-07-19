---
title: Idea Sources
description: Where the ideas in the catalog come from and how each source is scored.
---

# Idea Sources

Every idea in `site/ideas.json` carries a `source` field. The build pipeline
treats each source differently. The five sources, in `scripts/build.py`:

## `ai-ideas` — `AI_IDEAS`

Hand-curated AI/ML-flavored ideas. Each tuple is
`(F, M, T, C, title, body)`. The body always contains a `**Comp:**` line
(incumbents + funding) and a `**Wedge:**` line (the defensible angle, or "none").
This is the most opinionated source — scores are set directly, not derived.

## `README` — `README_IDEAS`

The original backlog that lived in earlier README revisions. Each tuple is
`(F, M, T, C, body)`. Same Comp/Wedge convention as `ai-ideas`. These are
older ideas kept for history; many are now flagged as weak or dead.

## `spec` — `SPEC_IDEAS`

The four ideas that were flushed out into full product specs (see
[specs](specs/)). Each tuple is `(F, M, T, C, body)` and the body links to the
spec doc. Scores here incorporate the
[spec deep-dive](../knowledge/learnings/spec-deep-dives.md) market research —
`C` is bumped to 9 where incumbents are locked in.

## `fresh` — `FRESH_IDEAS`

Ideas generated outside the original backlog to fit a specific brief: tech-heavy
(`T >= 7`), non-dev customer, $5K MRR achievable by a solo dev, with a real
wedge against incumbents. Each tuple is
`(F, M, T, C, F_feas, customer, title, body)` — the only source that pre-stamps
`F_feas` and `customer` inline, because the brief was explicit about them. The
body includes a rough `$X/mo × N users = $5K MRR` math sketch and a `Tech:` line.

## `starterstory` — fetched from git history

The only non-hand-curated source. Starterstory founder interviews were scraped
into `solopreneur_ideas.json` (now deleted from the tree; `build.py` recovers
it from git history via `fetch_sol()`). Inclusion criteria, applied in
`build.py`:

- Category is **tech-first** (`T_baseline >= 7` in the `CAT` table).
- Revenue **>= $5K/month** (`MIN_REVENUE = 5000`).
- Category not in `SOL_DROP` (sitemap, travel, niche blogs, etc.).

Scores are derived from category baselines (`CAT`) and parsed revenue
(`m_from_revenue`), not hand-set per entry. Descriptions come from
`data/starterstory_descriptions.json` (pre-researched clean summaries keyed by
story URL), falling back to `extract_description()` which strips the
Starterstory interview boilerplate.

See [ADR-005](../architecture/decisions/adr-005-starterstory-inclusion.md) for
the history of dropping then re-adding this source.

## Why no automated scraping at build time

`fetch_sol()` reads from git history, not the network, so the build is
reproducible and offline. The scrape was a one-time operation; its output is
frozen in history. Re-scraping would re-introduce licensing/ToS and
reproducibility problems for no scoring benefit.
