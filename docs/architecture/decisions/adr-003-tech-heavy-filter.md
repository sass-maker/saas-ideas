---
title: ADR-003 — Hard-filter to T >= 7 (tech-heavy)
description: Drop non-tech-heavy ideas from the dataset entirely rather than hiding them.
---

# ADR-003 — Hard-filter to `T >= 7` (tech-heavy)

- **Status:** Accepted
- **Date:** 2026-03 (commits `e2cf153`, `b9575f7`, `6fe99b7`)

## Context

The catalog initially kept all ~404 ideas and moved the tech-level filter to a
UI slider (default 7) so users could relax it. This made the dataset large and
diluted the catalog's purpose: the maintainer is a solo dev, and ideas that are
not tech-heavy are not interesting builds regardless of their money potential.

## Decision

Hard-delete ideas with `T < 7` (`MIN_T = 7`) from the dataset in `build.py`,
rather than hiding them in the UI. The filter runs after all sources are merged
and after Starterstory category filtering, before scoring is finalized.

## Consequences

- **Pro:** the catalog is focused — every remaining idea is at least a
  non-trivial technical build, which is the only kind the maintainer will
  actually pursue.
- **Pro:** smaller dataset is easier to keep scored accurately.
- **Con:** the dropped ideas are gone from `site/ideas.json`, so the published
  table no longer shows them at all. This is intentional — the catalog is a
  decision tool, not an archive. The ideas still exist in git history if ever
  needed.
- **Con:** `MIN_T` is inlined as `7` in the filter expression rather than
  referencing the `MIN_T` constant, because `MIN_T` is defined later in the
  script (commit `a21320d` fixed a forward-reference bug). If you move the
  constant, update the filter too.

## Non-goal

This filter is about **build interestingness**, not market size. A high-`T`
idea can still have a tiny market; that is captured by `M` and `money`, not by
this filter.
