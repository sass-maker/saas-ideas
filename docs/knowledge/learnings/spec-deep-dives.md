---
title: Spec Deep-Dives
description: Honest market analyses for the four flushed-out specs (FamilyTree, magicform, Productivity App, StoryTunes). Source for the C-bumps in scripts/build.py and the failed-approach verdicts.
---

# Spec deep-dives

Honest market analyses for the four flushed-out specs, produced via web research (2026). Source for the C-bumps in `scripts/build.py`.

## FamilyTree — `[F7 M5 T8 C9]` → Adj 15

**Market:** Genealogy products & services is a $6.6B market (2024) growing 12% CAGR to ~$15–20B by 2032. Ancestry alone has $1.3B revenue and 3M+ paying subs (Blackstone reportedly seeking $10B exit). MyHeritage ~$183M (2022). 23andMe filed bankruptcy March 2025, sold to TTAM (nonprofit) July 2025 — DNA-as-consumer-product proved fragile.

**Dominant players:** Ancestry/MyHeritage own records + DNA. FamilySearch (free, LDS-funded) + WikiTree (free, volunteer) + Geni (200M profiles, free + premium) own the *collaborative free tree* niche the spec targets. Geni added an interactive fan chart in 2025 — they're not stagnant.

**Wedge analysis:** The spec is **everything**: tree + auth ("About Me") + giftme + matrimonial + ecommerce stores + genetic prediction + hiring-trees + chat + family Discord clone. A solo dev cannot ship this; even shipping any one of these competes with a funded incumbent. The "social family network" graveyard is real — Ancestry's MyFamily.com shut down in 2014. Nobody wants another family social network; they want records and DNA matches.

**Recommendation: niche-pivot or dead.** If anything survives, it's the matrimonial-meets-tree angle for Indian diaspora (Shaadi.com market, ~$400M). The "About Me" portion is a separate idea unrelated to family. Strip everything else. Honest C=9 because every component has a $100M+ incumbent.

---

## magicform — `[F7 M6 T7 C9]` → Adj 14

**Market:** Online survey/form market ~$13.8B by 2026. Real, growing, but **brutally saturated**.

**Dominant players & funding:** Typeform $141M ARR, $935M val, $186.9M raised. Jotform $145M revenue, bootstrapped, 35M users. Tally $4M ARR (up from $1.9M in 2024), bootstrapped, **aggressive free tier (unlimited forms+submissions free)** — they are eating the value-conscious end. Fillout $19/mo with AI built in, generous free tier. Google Forms holds 47% market share.

**Wedge holds up:**
- 2-way comms (form responders can be re-pinged with updates) — genuinely novel
- Embeddable SDK with formId — Fillout has Notion/Airtable embeds but a clean dev-SDK is differentiated

**Wedge does NOT hold up:**
- "AI builds your form from a prompt" — **every single incumbent shipped this in 2024-25.** Typeform, Tally, Fillout, Jotform all have AI form generators. This was the spec's core differentiator and it's gone.
- AI summarization of responses — Typeform and Jotform also do this now
- Pricing race: Tally bootstrapped to $4M ARR by undercutting everyone with free unlimited

**Recommendation: niche-pivot.** Don't compete on AI-form-gen — go SDK-first. Position as "Stripe for forms" — a true embeddable primitive other apps use. Target dev-tools market, not survey market. C=9 because the 2024-25 AI wave already played out here.

---

## Productivity App — `[F8 M5 T8 C9]` → Adj 16

**Market:** Productivity software ~$65B (2024) → $75B (2025), task-management subset ~$5.1B.

**Dominant players & funding:** Notion $400M ARR (60% YoY growth), well-funded with a $10B+ val. Todoist 50M users, ~$20M ARR. Motion $50M ARR per Sacra (~$10M ARR per Latka — discrepancy), $550M valuation, raised $75M in 2025 alone. Sunsama, Akiflow $16–34/mo. Habit space: Habitica, Productive, Streaks, Loop, Habitify, Way of Life — dozens of competitors. Superhuman got acquired by Grammarly July 2025 — not dead, but absorbed. Mem still active but quiet.

**Wedge analysis:** The spec is ~300 features deep — habits + schedule + goals + journal + food log + mood + social mode + AI assistant + WhatsApp integration + mana mode + blindfold matchmaking + mental health app + spaced repetition. **This is a 3-year solo build at minimum.** The history of "life OS" attempts is brutal: opinionated all-in-ones consistently lose to Notion templates because users want flexibility. Motion's $50M ARR proves the AI-scheduling lane works — but Motion focused narrowly on calendar+tasks, not life-OS.

**Reality check:** F=8 is honest because this IS fun to build. But M_eff = 0 because C is brutal AND the spec dilutes any single defensible feature. The dev will likely be the only serious user.

**Recommendation: build for self only.** This is a "scratch your own itch" daily driver, not a business. If anything ships commercially, pick one feature (e.g., "mana mode" gamified task RPG, or the PSI-pressure journal) and ship that as a $5/mo standalone.

---

## StoryTunes — `[F8 M3 T7 C4]` → Adj 17

**Market:** AI writing assistants ~$1.23B (2025), AI book writing projected $47B by 2034 at 32.6% CAGR — but those are AI-writing numbers, not collab-multiplayer-fiction. AI roleplay chatbot market ~$500M growing to $1.9B by 2031.

**Dominant players & funding:**
- **Wattpad: $895M rev, 90M+ users, 170M MAU combined with Webtoon** — but single-author serialized, not multiplayer-vote-canon.
- **NovelAI:** subscription-only, ~8M monthly visits, no VC.
- **Sudowrite: only $1.8M ARR after 5 years, bootstrapped, 16 employees**. This is the leading AI fiction writing tool and it's tiny.
- **AI Dungeon collapsing:** Steam concurrent players down ~46% Feb 2025 → Apr 2026 due to filtering, memory issues, mismanagement.
- Storium: 2014 Kickstarter, community-funded, tiny. Storyfall: solo indie. Mycelore: private preview.

**Wedge holds up:** Nobody — funded or not — owns "multiplayer + canon voting + branching + AI personas as participants." Wattpad doesn't do multiplayer. Sudowrite doesn't do multiplayer. AI Dungeon's collapse leaves demand unmet for a better multiplayer narrative experience. The voted-canon mechanic is genuinely novel.

**Wedge doesn't hold up:** **The category ceiling is low.** Sudowrite at $1.8M after 5 years tells you the entire AI-fiction tooling market is small. Cold-start network effects on multiplayer fiction are very hard (Storium proves you can be the best-designed system and still stay tiny).

**Recommendation: build.** Of the four, this is the most viable for a solo dev. C is genuinely low (no funded incumbent in this exact slot), F is high (delightful systems work — voting, branching, AI personas, realtime), T is real (live collab + AI persona consistency across rounds is non-trivial). M is honestly low (3) — even succeeding here means a Sudowrite-scale outcome ($1–5M ARR), not a unicorn. But for a solo dev, $1–5M ARR is life-changing. Monetization design is the open question — premium AI personas, premium rooms, world-IP licensing.
