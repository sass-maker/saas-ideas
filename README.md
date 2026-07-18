# Saas Ideas

Browse the full sorted list at **https://saas-ideas.pages.dev/**.

All ideas live in `site/ideas.json` (generated). The single source of truth is
`scripts/build.py`; edit it to change scores or add ideas, then:

```
python3 scripts/build.py
npx wrangler pages deploy ./site --project-name saas-ideas
```

Scoring: F/M/T/C each /10 — **F**un to build, **M**oney potential (raw),
**T**ech challenge, **C**ompetition pressure (1 open / 10 brutal).
M_eff = max(M − max(C − 3, 0), 0). Adj = F + M_eff + T (legacy sort).
Derived: `fun = F + T`, `money = M + F_feas − C`; `best_bet` iff customer ≠ dev
AND (fun ≥ 14 OR money ≥ 5). Default sort: best_bet, then money, then fun.

Knowledge system (architecture, decisions, specs, learnings): see [docs/](docs/)
and [AGENTS.md](AGENTS.md). Flushed-out specs:
[FamilyTree](docs/product/specs/family-tree.md),
[magicform](docs/product/specs/magic-form.md),
[Productivity App](docs/product/specs/productivity.md),
[StoryTunes](docs/product/specs/storytunes.md).
Portfolio doc: [portfolio strategy](docs/product/portfolio-strategy.md).
