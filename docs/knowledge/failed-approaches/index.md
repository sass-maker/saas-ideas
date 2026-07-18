---
title: Failed Approaches
description: Ideas investigated and rejected, with the specific reason. Read before re-investigating.
---

# Failed Approaches

Each entry here is an idea that was flushed out and then **deliberately not
pursued**, with the reason. They are recorded so the same idea is not
re-investigated from scratch. The full market analyses live in
[spec deep-dives](../learnings/spec-deep-dives.md); this page is the
verdict-only index.

| Idea | Spec | Verdict | Core reason |
| --- | --- | --- | --- |
| [FamilyTree](family-tree.md) | [spec](../../product/specs/family-tree.md) | niche-pivot or dead | Records + DNA moats locked by Ancestry/MyHeritage; free/social owned by FamilySearch+WikiTree; spec scope unshippable solo. |
| [magicform](magicform.md) | [spec](../../product/specs/magic-form.md) | niche-pivot | Every form incumbent shipped AI form-gen in 2024-25; Tally's free tier undercutting; the spec's core wedge is gone. |
| [Productivity App](productivity-app.md) | [spec](../../product/specs/productivity.md) | build for self only | Life-OS scope graveyard; opinionated all-in-ones lose to Notion templates; ~3yr solo build; dev will be the only user. |

StoryTunes is the one spec the deep-dive endorses shipping — it is **not** a
failed approach. See its [spec](../../product/specs/storytunes.md) and the
[deep-dive](../learnings/spec-deep-dives.md#storytunes-f8-m3-t7-c4-adj-17).

## Other dropped categories (not full specs)

These were dropped at the source level rather than investigated individually —
see [ADR-003](../../architecture/decisions/adr-003-tech-heavy-filter.md) and
[ADR-005](../../architecture/decisions/adr-005-starterstory-inclusion.md):

- **Non-tech-heavy ideas (`T < 7`)** — hard-deleted from the dataset. Not
  archived individually; recoverable from git history if ever needed.
- **Starterstory non-tech-first categories** (Solopreneur, Productized
  Services, Weekend Projects, No-Code, etc.) — dropped at merge time.
- **Starterstory entries < $5K/mo** — dropped at merge time.

These are source-level filters, not idea-level verdicts, so they do not get
individual failed-approach pages.
