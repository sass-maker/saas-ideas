---
title: Architecture Decisions
description: ADR index — non-obvious architectural and scoring decisions for saas-ideas.
---

# Architecture Decisions (ADRs)

Each ADR records a non-obvious decision: the context, the decision, and the
consequences. ADRs are append-only — a superseded decision gets a new ADR that
references the old one; the old one is never rewritten.

| # | Decision | Status |
| --- | --- | --- |
| [001](adr-001-single-source-of-truth.md) | Single source of truth in `build.py` | Accepted |
| [002](adr-002-derived-fun-money-scores.md) | Derived `fun` / `money` scores replace single `adj` sort | Accepted |
| [003](adr-003-tech-heavy-filter.md) | Hard-filter to `T >= 7` (tech-heavy) | Accepted |
| [004](adr-004-best-bet-criterion.md) | `best_bet` criterion for the $5K MRR target | Accepted |
| [005](adr-005-starterstory-inclusion.md) | Starterstory inclusion: tech-first + >= $5K/mo | Accepted |
| [006](adr-006-agent-geo-surfaces.md) | Agent/GEO surfaces (llms.txt, /api/ai, index.md) | Accepted |
| [007](adr-007-relocate-site-reclaim-docs.md) | Relocate published site to `site/`, reclaim `docs/` for the knowledge system | Accepted |

## When to add an ADR

Add an ADR when you make a decision that a future reader (human or agent) would
not be able to reconstruct from the code alone — typically a scoring-formula
change, a filter change, an inclusion/exclusion rule, or a structural
reorganization. Trivial changes do not need an ADR.
