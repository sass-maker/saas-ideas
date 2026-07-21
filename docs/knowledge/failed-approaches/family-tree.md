---
title: FamilyTree — failed approach
description: Why the FamilyTree spec is unshippable solo and what (if anything) survives.
---

# FamilyTree — failed approach

- **Spec:** [docs/product/specs/family-tree.md](../../product/specs/family-tree.md)
- **Scores:** `F7 M5 T8 C9` → `money = 5 + 2 - 9 = -2`
- **Deep-dive:** [spec-deep-dives.md](../learnings/spec-deep-dives.md)

## Verdict: niche-pivot or dead

The spec is **everything**: tree + "About Me" auth + GiftMe + matrimonial +
ecommerce stores + genetic prediction + hiring-trees + chat + a family Discord
clone. A solo dev cannot ship this; even shipping any one component competes
with a funded incumbent.

## Why it fails

- **Records + DNA** are owned by Ancestry ($1.3B rev, Blackstone seeking ~$10B
  exit) and MyHeritage. 23andMe filed bankruptcy March 2025 and was sold to
  TTAM (nonprofit) July 2025 — DNA-as-consumer-product proved fragile.
- **Free / social tree** is owned by FamilySearch (LDS-funded, free) and
  WikiTree (free, volunteer). Geni (200M profiles) added an interactive fan
  chart in 2025 — they are not stagnant.
- **The "social family network" graveyard is real.** Ancestry's MyFamily.com
  shut down in 2014. Nobody wants another family social network; they want
  records and DNA matches.

## What survives (maybe)

The matrimonial-meets-tree angle for the Indian diaspora (Shaadi.com market,
~$400M) is the only sliver that is not directly owned by a funded incumbent.
The "About Me" profile-as-API portion is a separate, unrelated idea — strip it
out and evaluate on its own.

## Why C = 9

Every component of the spec has a $100M+ incumbent. The market is not open at
any layer the spec targets.

## Do not re-investigate without

- A specific niche (e.g. diaspora-Indian matrimonial) and a distribution plan
  for that niche, or
- A records/DNA partnership that breaks the incumbent data moat — unlikely for
  a solo dev.
