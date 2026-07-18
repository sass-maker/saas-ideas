---
title: StoryTunes — Spec
description: Product spec for the multiplayer story engine with canon voting and AI co-authors. The one spec the deep-dive endorses shipping.
---

# StoryTunes `[F8 M4 T7]`

_Scores out of 10 — fun to build, money potential, technically challenging._

Collaborative storytelling with voting, branching canon, and optional AI co-authors.

## Product

People write a story together in real time. At each step, contributors submit the next sentence, paragraph, scene, or branch option. The community votes, and the winning contribution becomes canon. AI characters can also participate as visible collaborators.

## Positioning

Not a generic writing tool.

It is a multiplayer story engine:
- part writers' room
- part game
- part social collaboration

## Core Loop

1. A story room starts with a premise.
2. Users submit possible next parts.
3. Users and AI collaborators vote or react.
4. The winning part becomes part of the main story.
5. New branches can open when there are strong alternative paths.

## MVP

- story rooms
- live editor + realtime presence
- submit next paragraph / next option
- timed voting rounds
- winning entry becomes canon
- visible branching story tree
- optional AI collaborator with a named persona

## Target Users

- hobby fiction writers
- fan-fiction communities
- RP / improv / worldbuilding groups
- classrooms or writing clubs

## Why It Could Be Interesting

- the fun is in the process, not just the final text
- voting creates game tension and social feedback
- branching structure makes the story feel alive
- AI collaborators can add surprise without replacing humans

## Key Constraint

The product should feel playful first. If it feels like a normal docs editor with votes bolted on, it loses the point.

## Research Snapshot

As of 2026-04-04, this category exists, but it is fragmented across several different product shapes:
- collaborative story games
- branching fiction platforms
- social fiction communities
- AI writing tools
- worldbuilding and authoring software

There is still room for a sharper multiplayer story engine with canon voting and visible AI collaborators.

## Similar Products

Direct and close products already built:
- Storium: online storytelling game where people write stories together by playing a game
- PlotVote: community votes on plot direction and AI writes the next chapter
- WriteJam: collaborative storytelling platform with shared writing and AI suggestions
- Role Playing Story: branching fiction app where users create new branches for everyone
- Storyfall: interactive fiction platform with publishing, multiplayer play, and monetization

Being built or early:
- Mycelore: collaborative branching fiction and shared world-building, currently in private preview
- Role Playing Story: still in beta as a solo-developer product
- Storyfall: live, but still in early expansion mode and adding platform capabilities

Adjacent products:
- Twine: nonlinear story authoring tool
- Episode: large interactive story network and creator platform
- Campfire: planning, drafting, and co-writing tool for authors
- World Anvil: worldbuilding, maps, timelines, and co-author support
- Sudowrite: AI writing partner for fiction
- NovelAI: AI story and fiction generation

## Funding / Revenue Status

As of 2026-04-04:

- Storium: crowdfunded on Kickstarter in 2014 at $251,362 and later described itself as community-funded.
- PlotVote: free to use for reading and voting. No public funding or revenue disclosure found.
- WriteJam: freemium / subscription product with listed paid tiers. No public funding or revenue disclosure found.
- Role Playing Story: beta solo-developer project with premium contribution features. No public funding or revenue disclosure found.
- Storyfall: early indie platform with creator monetization features. No public funding or revenue disclosure found.
- Mycelore: private preview. No public funding or revenue disclosure found.
- Twine: open-source and donation-supported through Patreon and the Interactive Fiction Technology Foundation.
- Episode: product inside Pocket Gems. Pocket Gems raised $5M in 2010 and $90M from Tencent in 2017. Historic reporting showed strong Episode revenue growth, but I did not verify a current standalone revenue number for Episode.
- Campfire: subscription / lifetime-license product. I could not verify public venture funding or a public revenue number.
- World Anvil: subscription / lifetime membership product with Patreon and community support. No public venture funding or public revenue number found.
- Sudowrite: seed-funded. TechCrunch reported a $3M round in 2021, mostly from angel investors. No public revenue number found.
- NovelAI: subscription-funded SaaS. The team has said it intends to rely on subscription revenue to cover operating costs. No public venture funding found.

## Research Takeaways

- There is no dominant modern product that cleanly combines:
  collaborative writing + voting + branching canon + AI collaborators.
- Existing tools usually own only one slice:
  solo authoring, branching, publishing, roleplay, AI assistance, or community.
- That makes the multiplayer writers' room angle more interesting than a generic writing app.
- The most distinctive part is not "AI helps write stories." It is:
  people propose branches, people vote, the story canon evolves, and AI shows up as a named participant.

## Best Buildable Direction

The strongest first cut is:
- public or private story rooms
- timed rounds
- submit next paragraph or branch option
- vote to decide canon
- preserve rejected paths as visible alternate branches
- optional AI personas that also submit entries

## Main Risks

- quality control and moderation
- ownership and canon rules
- cold-start network effects
- keeping the product playful instead of turning it into a generic editor
