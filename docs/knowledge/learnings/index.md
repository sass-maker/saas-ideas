---
title: Learnings
description: Durable market research and scoring methodology notes.
---

# Learnings

- [Spec deep-dives](spec-deep-dives.md) — honest market analyses for the four
  flushed-out specs (FamilyTree, magicform, Productivity App, StoryTunes),
  produced via web research. This is the source for the `C` bumps in
  `scripts/build.py` and for the failed-approach verdicts.

## How competition scores are sourced

The `C` (competition) axis is the most research-heavy score. For each idea, the
`**Comp:**` line in the idea body records the named incumbents and, where
known, their funding/ARR. The scoring convention:

- `C = 3` — open field, no funded incumbent.
- `C = 5-6` — incumbents exist but are small, slow, or bootstrapped.
- `C = 7-8` — well-funded incumbents actively shipping the wedge.
- `C = 9` — the wedge is already gone (incumbents shipped it) or the market is
  locked by a moat (records, DNA, data licensing).
- `C = 10` — brutally consolidated horizontal category (e.g. LLM routing,
  observability) where a solo entry has no angle.

These numbers are judgement calls backed by the research in
[spec-deep-dives.md](spec-deep-dives.md) and the per-idea `**Comp:**` notes.
Re-research an incumbent landscape before bumping a `C` score down (i.e. before
claiming a market has opened up).
