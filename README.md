# Saas Ideas

Browse the full sorted list at **https://saas-ideas.pages.dev/**.

All ideas live in `docs/ideas.json`. To edit scores or add new ideas, edit
`scripts/build.py` (single source of truth), then:

```
python3 scripts/build.py
npx wrangler pages deploy ./docs --project-name saas-ideas
```

Scoring: F/M/T/C each /10 — **F**un to build, **M**oney potential (raw),
**T**ech challenge, **C**ompetition pressure (1 open / 10 brutal).
M_eff = max(M − max(C − 3, 0), 0). Adj = F + M_eff + T (default sort).

Flushed-out specs (one doc each): [FamilyTree](family-tree.md),
[magicform](magic-form.md), [Productivity App](productivity.md),
[StoryTunes](storytunes.md). Portfolio doc: [PROJECT-STRATEGY.md](PROJECT-STRATEGY.md).
