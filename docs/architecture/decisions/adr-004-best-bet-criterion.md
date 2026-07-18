---
title: ADR-004 — best_bet criterion for the $5K MRR target
description: Define a single yes/no flag for ideas worth pursuing toward a $5K MRR solo target.
---

# ADR-004 — `best_bet` criterion for the $5K MRR target

- **Status:** Accepted
- **Date:** 2026-03 (commits `3d15f03`, `a58a35d`)

## Context

After [ADR-002](adr-002-derived-fun-money-scores.md) introduced two derived
scores, there was no single signal for "should I actually pursue this". The
maintainer's concrete target is **$5K MRR achievable by a solo dev**, so the
flag should encode that specifically, not just "high scores".

An earlier criterion required strong on both axes, which was too strict — it
excluded ideas that are genuinely fun + technical enough to be worth building
even if the money path is thin, and vice versa.

## Decision

```
best_bet = (customer != "dev") AND (fun >= 14 OR money >= 5)
```

A best bet must:

1. **Not be sold to individual devs** — `dev`-customer ideas are the hardest to
   monetize (devs believe they can build it themselves), so they fail the $5K
   MRR target disproportionately.
2. Be strong on **at least one** of the two collapsed axes:
   - `fun >= 14` (e.g. F7 T7, or F8 T6) — worth building for the
     fun+technical payoff, or
   - `money >= 5` — clearly positive after the competition penalty, i.e. a
     real revenue path.

## Consequences

- **Pro:** one yes/no column the maintainer can sort to the top — the default
  sort is `best_bet` desc first.
- **Pro:** the OR (not AND) keeps both "joy builds with a chance of money" and
  "real revenue builds" eligible, which matches how the maintainer actually
  picks.
- **Con:** `dev`-customer ideas can never be best bets even when they score
  well. This is deliberate — see [idea sources](../../product/idea-sources.md):
  the `dev` exclusion is the single biggest filter for the $5K MRR target.
- **Con:** the `14` and `5` thresholds are hand-tuned, not derived. They were
  calibrated against the existing dataset to flag a manageable number of bets.
  If the dataset grows substantially, recalibrate (commit `3d15f03` is the
  reference calibration).

## Why `best_bet_why` mirrors `f_feas_why`

For best bets, `best_bet_why` is set to the `f_feas_why` reasoning so the table
tooltip explains *why the idea is feasible*, which is the most useful
one-liner when triaging best bets.
