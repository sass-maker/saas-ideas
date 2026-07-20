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

Temp dump:
Yes — **Messi plot armour thickened to illegal levels**. Argentina were **2–0 down to Egypt with 11 minutes left**, then Romero scored, Messi equalized, and Enzo Fernández won it in stoppage time. Messi also missed a first-half penalty, which somehow makes the plot armour worse, not weaker. ([Reuters][1])

# PRD: **World Eleven Mythos**

## 1. Product Summary

**World Eleven Mythos** is a serialized shonen-style football universe inspired by real football history, player archetypes, club empires, national pipelines, and tactical philosophies.

It does **not** use real player names, club names, logos, or competitions. It turns football into a mythic power-system world: nations have inherited styles, clubs are empires, and elite players are “captain-class” monsters.

## 2. Core Idea

Football is globally played, but elite power is concentrated in a few countries, clubs, systems, and once-in-a-generation players.

The product dramatizes that as:

> **A world where football styles are inherited like magic systems, superclubs hoard prodigies, and the World Cup becomes the final tournament arc for deciding which philosophy rules the next era.**

## 3. Target Audience

Primary users:

* Football fans who enjoy tactics, history, player debates, and GOAT narratives.
* Anime/manga fans who like shonen power systems, captains, squads, awakenings, and tournament arcs.
* AI-native creators/builders interested in new IP formats.

Secondary users:

* Casual sports fans.
* Webtoon readers.
* Short-form video audiences.
* Fantasy sports / card-collector audiences.

## 4. Problem

Football already has shonen-level mythology, but it is scattered across real matches, fan debates, YouTube clips, and player legacies.

There is no serious fictional universe that combines:

* football history,
* modern superclub concentration,
* national playing styles,
* tactical systems,
* player archetypes,
* and shonen-style escalation.

## 5. Proposed Solution

Create an AI-assisted serialized IP with three initial content formats:

1. **Character Cards**

   * player analogue
   * nation
   * club empire
   * style lineage
   * signature ability
   * weakness
   * rivalry

2. **Short Manga/Webtoon Scenes**

   * 6–12 panels
   * focused on one duel, one goal, one awakening, or one tactical reveal

3. **Fake Match Reports**

   * written like sports journalism
   * includes score, tactical analysis, dramatic moments, and lore implications

## 6. MVP

The MVP should **not** be a full anime.

Start with:

> **30 character cards + 10 lore articles + 5 short manga scenes + 3 fake match reports.**

The goal is to test whether people care about the universe before building animation, game mechanics, or a full story.

## 7. Product Pillars

### A. Player Mythology

Players are not direct copies. They are archetypes.

Examples:

| Real-world archetype | Fictional treatment                               |
| -------------------- | ------------------------------------------------- |
| Messi-type           | aging god of vision, tempo, and impossible angles |
| Ronaldo-type         | fallen emperor fighting time itself               |
| Mbappé-type          | speed prince of the modern era                    |
| Haaland-type         | goal-devouring northern monster                   |
| Yamal-type           | child prodigy who sees impossible geometry        |
| Neymar-type          | cursed dancer whose body betrayed his magic       |

### B. Nation Styles

Countries become football civilizations.

| Real idea   | Fictional version    |
| ----------- | -------------------- |
| Brazil      | Sun Kingdom          |
| Argentina   | Fate-Touched Nation  |
| Spain       | Possession Church    |
| France      | Monster Republic     |
| England     | Golden League Empire |
| Portugal    | Broken Crown         |
| Germany     | Machine State        |
| Netherlands | Geometry School      |

### C. Club Empires

Clubs are guilds/empires that collect elite talent.

| Real idea   | Fictional version  |
| ----------- | ------------------ |
| Real Madrid | Royal Astral CF    |
| Barcelona   | Catalan Loom       |
| Man City    | Blue Engine        |
| PSG         | Paris Saint-Grail  |
| Bayern      | Iron Munich        |
| Liverpool   | Red Anfield Order  |
| Arsenal     | North London Forge |

### D. Tactical Power System

Football abilities are grounded in actual tactics.

Examples:

| Tactical concept  | Shonen ability      |
| ----------------- | ------------------- |
| pressing          | pressure domain     |
| passing triangles | geometry chains     |
| counterattack     | rupture sprint      |
| low block         | iron shell          |
| false nine        | ghost striker       |
| inverted fullback | hidden axis         |
| vertical runs     | line-breaking blade |
| set-pieces        | ritual formations   |

## 8. Main User Journey

1. User sees a character card on social media.
2. User recognizes the real-world inspiration.
3. User reads the player’s lore, ability, and weakness.
4. User follows a duel or match scene.
5. User starts debating matchups: “Can the Speed Prince beat the Possession Church?”
6. User enters the broader universe through rankings, brackets, and fake tournament arcs.

## 9. Content Requirements

Each character must have:

* Name
* Country
* Club empire
* Position
* Archetype
* Signature ability
* Weakness
* Historical lineage
* Rival
* Current arc status
* Visual motif
* One quote

Example:

```markdown
Name: Kairo Mbaye
Country: Monster Republic
Club: Paris Saint-Grail / Royal Astral
Position: Forward
Archetype: Speed Prince
Ability: Horizon Break
Weakness: Low-block patience
Lineage: Engineered-speed era
Rival: Eirik Håkon
Quote: "The pitch is only big until I start running."
```

## 10. Legal / IP Guardrails

Hard rules:

* Do not use real names.
* Do not use real faces.
* Do not use real club logos.
* Do not use real kits.
* Do not recreate real matches too directly.
* Do not make characters one-to-one copies.
* Use archetypes, not impersonations.

The safe creative principle:

> Make the audience feel the inspiration, but give the character enough original identity to survive without the reference.

## 11. AI Workflow

Use AI for acceleration, not final taste.

Pipeline:

1. Human defines lore and character archetype.
2. AI generates visual directions.
3. AI generates draft character cards.
4. Human edits for taste, originality, and football logic.
5. AI generates panel roughs.
6. Human selects and rewrites.
7. Final assets are published as serialized drops.

AI should help with:

* character concepts,
* lore variants,
* visual motifs,
* match reports,
* bracket simulation,
* social captions,
* translation/localization.

AI should **not** own:

* canon decisions,
* final writing voice,
* character hierarchy,
* football logic,
* legal judgment.

## 12. Success Metrics

Early MVP metrics:

| Metric                                  |                        Target |
| --------------------------------------- | ----------------------------: |
| Character card save/share rate          | High relative to normal posts |
| Comments debating matchups              |                 Strong signal |
| Repeat viewers across drops             |                 Strong signal |
| Newsletter / Discord joins              |        Early community signal |
| Requests for specific player archetypes |                 Demand signal |
| Fan-made rankings/brackets              |                   Best signal |

The strongest validation is not likes.

The strongest validation is:

> People arguing about the universe as if it is real.

## 13. Risks

| Risk                                    | Mitigation                                   |
| --------------------------------------- | -------------------------------------------- |
| Feels like cheap player parody          | Build archetypes, not clones                 |
| Football fans call it tactically stupid | Ground powers in real tactics                |
| Anime fans find it too dry              | Use rivalries, awakenings, visual metaphors  |
| Legal/IP issues                         | Avoid names, faces, logos, kits              |
| AI slop aesthetic                       | Human curation and consistent art bible      |
| Scope explosion                         | Start with cards and short scenes, not anime |

## 14. MVP Roadmap

### Phase 1 — Lore Bible

Create:

* 8 nation styles
* 7 club empires
* 30 player archetypes
* 10 historical lineages
* core terminology

### Phase 2 — Public Drops

Publish:

* 3 character cards per week
* 1 short match report per week
* 1 manga/webtoon scene every two weeks

### Phase 3 — Tournament Arc

Launch a fictional tournament bracket:

* 16 nations
* 4 groups
* knockout rounds
* fan voting optional
* creator-controlled canon result

### Phase 4 — Expansion

Add:

* interactive player database
* power rankings
* club empire map
* animated shorts
* collectible cards
* game prototype

## 15. Product Positioning

Not:

> “AI anime about fake Messi and fake Ronaldo.”

Better:

> **A shonen football mythology where nations, clubs, tactics, and historical player archetypes become a power system.**

## 16. Brutal Execution Note

The idea is strong, but the execution bar is high.

The bad version is easy: fake Mbappé with lightning.

The good version needs:

* football knowledge,
* anime pacing,
* historical taste,
* legal discipline,
* consistent art direction,
* and restraint.

Start small. Make **10 characters people actually want to argue about** before pretending this is an anime.

[1]: https://www.reuters.com/sports/soccer/argentina-stage-stunning-late-comeback-see-off-egypt-2026-07-07/?utm_source=chatgpt.com "Tearful Messi inspires Argentina to stunning comeback win over Egypt"
