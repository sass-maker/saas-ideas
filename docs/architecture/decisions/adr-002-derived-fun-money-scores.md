---
title: ADR-002 — Derived fun / money scores replace single adj sort
description: Collapse the raw axes into two derived scores (fun, money) and sort on those.
---

# ADR-002 — Derived `fun` / `money` scores replace single `adj` sort

- **Status:** Accepted
- **Date:** 2026-03 (commits `6fe99b7`, `9542b2f`, `a58a35d`)

## Context

The original sort was a single `adj = F + m_eff + T` number. This collapsed
fun, money, and tech into one figure, which hid **why** an idea ranked where it
did: a high-`adj` idea could be there because it is fun to build and
technically interesting but has no viable money path, or because it is a real
revenue opportunity but boring. Those are very different bets and should not
share a single rank.

The model also lacked a solo-feasibility axis: an idea can score well on
`F/M/T` and still be unshippable by one person (e.g. needs enterprise sales,
data licensing, or $10M compute).

## Decision

1. Add a `F_feas` (/10) solo-dev feasibility axis, stamped per-idea.
2. Add a `customer` type (`dev` / `b2b-tech` / `non-dev`).
3. Collapse to two derived scores:
   - `fun = F + T` (range 2..20)
   - `money = M + F_feas − C` (range ~-8..19)
4. Sort on `best_bet` → `money` → `fun` (see
   [ADR-004](adr-004-best-bet-criterion.md)), not on a single number.
5. Keep `m_eff` and `adj` in the data for tooltip/debug only — do not sort on
   them.

## Consequences

- **Pro:** the two-axis view makes the fun-vs-money tradeoff explicit. An idea
  that is high-`fun` / low-`money` is visibly a "build for joy" bet, not a
  revenue bet.
- **Pro:** `F_feas` independently encodes "can a solo dev reach revenue", which
  `M` (raw market size) does not.
- **Con:** two numbers to reason about instead of one — but the `best_bet`
  flag (ADR-004) restores a single yes/no for "should I pursue this".
- **Con:** `money` can go negative for high-competition ideas, which is
  intentional (it signals "the market penalty eats the opportunity") but
  requires the sort to clamp via `max(money, 0)` only inside the legacy `adj`,
  not in the primary sort.

## Implementation notes

`fun` and `money` must be computed **after** `F_feas` and `customer` are
stamped. An earlier version computed them too early and produced wrong values;
commit `a58a35d` fixed the ordering. This ordering constraint is now encoded in
the script's structure (stamp loop precedes derive loop).
