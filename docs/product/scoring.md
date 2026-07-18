---
title: Scoring Model
description: The exact scoring formulas, axes, and best_bet criterion used to rank ideas.
---

# Scoring Model

The scoring logic lives in `scripts/build.py`. This page is the human-readable
reference; if they ever disagree, **the code wins** — fix this page.

## Raw axes (each /10)

| Axis | Meaning | 1 | 10 |
| --- | --- | --- | --- |
| `F` | Fun to build | chore | genuinely exciting |
| `M` | Money potential (raw, pre-competition) | no revenue path | large market |
| `T` | Tech challenge | trivial | hard engineering |
| `C` | Competition pressure | open field | brutal, well-funded incumbents |
| `F_feas` | Solo-dev feasibility | needs $10M + sales team | solo ships V1 in a weekend |

`F_feas` is stamped per-idea from a substring lookup table (`FEAS` in
`build.py`), or hand-set on fresh ideas. It encodes capital required,
distribution motion, cold-start network effects, time-to-MVP, sales cycle, and
incumbent moats — i.e. "can one person actually get this to revenue", which is
orthogonal to how fun or large the market is.

## Customer type

`customer` ∈ {`dev`, `b2b-tech`, `non-dev`}:

- `dev` — individual developers (hardest to monetize; they believe they can
  build it themselves).
- `b2b-tech` — companies buy for their technical teams (real motion, slower).
- `non-dev` — everyone else: prosumers, vertical ops, students, writers,
  recruiters (usually easiest to extract $).

Stamped from the `CUSTOMER` substring table in `build.py`, or hand-set on fresh
ideas. Defaults to `non-dev`.

## Derived scores

```
m_eff  = max(M - max(C - 3, 0), 0)        # legacy, kept for tooltip/debug
adj    = F + m_eff + T                     # legacy default sort
fun    = F + T                             # range 2..20
money  = M + F_feas - C                    # range ~-8..19, practical -3..17
```

`fun` and `money` are the two collapsed axes the catalog actually sorts on.
They replaced the older single `adj` sort — see
[ADR-002](../architecture/decisions/adr-002-derived-fun-money-scores.md).

## best_bet criterion

```
best_bet = (customer != "dev") AND (fun >= 14 OR money >= 5)
```

Rationale: a best bet must be (a) not sold to individual devs, and (b) strong
on at least one of the two collapsed axes — either genuinely fun+technical
(`fun >= 14`, e.g. F7 T7 or F8 T6) or clearly positive after the competition
penalty (`money >= 5`). See
[ADR-004](../architecture/decisions/adr-004-best-bet-criterion.md).

## Default sort

`best_bet` desc → `money` desc → `fun` desc. The published table lets the user
re-sort by any column.

## Hard filter

Ideas with `T < 7` are dropped from the dataset entirely (not just hidden).
See [ADR-003](../architecture/decisions/adr-003-tech-heavy-filter.md).

## Why these axes and not others

The model is deliberately small (5 axes + 1 type) because every axis is
hand-scored. Adding axes multiplies the scoring effort without improving
discrimination once `C` and `F_feas` are both present — together they already
encode "is the market defensible" and "can a solo dev reach it". The
[learnings](../knowledge/learnings/) capture the market research that feeds
`C` and the feasibility reasoning that feeds `F_feas`.
