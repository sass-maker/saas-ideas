---
title: Portfolio Strategy
description: Fleet-wide portfolio operating model — Commercial / Personal / Infra / Playground buckets, current commercial focus, and promotion criteria. Fleet-level doc that lives in this repo.
---

# Project Strategy — April 2026

This doc is the portfolio operating model.

Not every repo is a startup. Not every useful project needs monetization pressure.

The portfolio is split into 4 buckets:

- **Commercial** — products we are intentionally trying to sell
- **Personal** — tools that are useful to me directly
- **Infra** — reusable systems that support other projects
- **Playground** — experiments, portfolio pieces, and fun builds

---

## Core Rules

1. Only the `Commercial` bucket is constrained.
2. Keep at most 2 active commercial bets at a time.
3. New projects are allowed.
4. New `Commercial` projects are not allowed unless an existing commercial bet is paused, dropped, or shipped enough to free attention.
5. `Personal` projects are allowed to exist even if they never monetize.
6. `Infra` projects are judged by reuse and leverage, not direct revenue.
7. `Playground` projects are judged by speed, learning, novelty, and portfolio value, not maintenance or monetization.
8. Projects can move between buckets later.
9. Security fixes, credential rotation, and obvious bug fixes still matter regardless of bucket.

---

## Current Commercial Focus

### 1. Resume Tailor
- **Repo:** `resume-tailor`
- **Role:** Active commercial bet
- **Why:** Closest to a real sellable product. Already has a landing page, pricing, and checkout flow.
- **Current focus:** distribution, conversion, and first paying users

### 2. MentionPilot
- **Repo:** `mentionpilot`
- **Role:** Active commercial bet
- **Why:** Strong category potential, but still needs sharper positioning and distribution.
- **Current focus:** clarify paid vs free/BYOK positioning, then push distribution

---

## Bucket Assignments

### Commercial
- `resume-tailor`
- `mentionpilot`

### Personal
- `reader`
- `email-manager`
- `today-little-log`
- `agentMode`
- `chess`
- `port-whisperer`
- `agent-resume`

### Infra
- `saas-maker`
- `free-ai`

### Playground
- `CodeVetter`
- `swe-interview-prep`
- `linkchat`
- `looptv`
- `reel-maker`
- `open-historia`
- `anime_list`
- `starboard`
- `significanthobbies`
- `assistant`

### Outside This Sorting
- `vaulthealth`
- `stripe-integration`
- `bug-bash`
- `experiment`
- `reference`
- `_archived`

---

## Notes On Borderline Projects

### LinkChat
- `Roast` and `Newspaper` are not separate products.
- They are features/pages inside `linkchat`.
- Keep bucket decisions at the repo level unless they are spun out into their own project later.

### Personal vs Playground
- **Personal** means utility.
- **Playground** means exploration.
- If a project disappears tomorrow and that breaks a real workflow, it is probably `Personal`.
- If a project mostly exists because it was interesting, impressive, fun, or worth learning from, it is probably `Playground`.

### Future Promotion Candidates
- `CodeVetter`
- `swe-interview-prep`
- possibly `linkchat`

These are not active commercial bets right now. Revisit only when there is real pull.

### Worth Keeping From Older Notes

These are useful future directions, not current priorities:

- `saas-maker`: AI feedback summarizer, side-project marketplace, and other reusable product modules are still good extension ideas.
- `reel-maker`: wrapping the current generation stack into a usable product for AI video marketing / content ops is still a valid direction.
- `agentMode`: a "personal reporter" style digest across sources is still a strong personal or future productized layer.
- `significanthobbies`: "StumbleUpon for People" remains a good extension of the existing hobby graph and social discovery direction.
- `swe-interview-prep`: can later generalize into a broader learning app if there is real pull beyond interview prep.
- `reader`: browser-extension distribution / capture remains a sensible direction if the product is ever pushed harder.
- `anime_list`, `open-historia`, and `starboard`: still make sense as polished niche or portfolio projects even if they are not major monetization bets.

---

## Promotion Criteria

A `Personal` or `Playground` project can move to `Commercial` later if at least one of these becomes true in a meaningful way:

- I use it constantly and would genuinely miss it
- other people keep asking for it
- distribution starts to work naturally
- the monetization path becomes obvious enough to test
- I am willing to support it as a real product, not just a fun build

---

## Operating Guidance By Bucket

### Commercial
- optimize for users, distribution, onboarding, pricing, billing, retention
- deadlines and focus matter
- avoid splitting attention across too many products

### Personal
- optimize for usefulness, speed, and fit with my own workflow
- ship what makes my life easier
- no pressure to justify via market size

### Infra
- optimize for reuse across multiple projects
- build only what compounds or removes repeated work
- do not force monetization unless real demand shows up

### Playground
- optimize for curiosity, novelty, visual ambition, and learning
- ship quickly
- keep maintenance expectations low

---

## Cross-Bucket Maintenance

- `today-little-log`: rotate exposed credentials
- keep obvious security problems from sitting forever
- commit and push often enough that repos do not drift into large invisible backlogs

---

*Last updated: 2026-04-04*
