# AI Ideas

Consolidated from earlier `ai-ideas.md`, `ai-knowledge-app.md`, and `by-ai.md`.

Scores: `[F? M? T?]` per idea, each out of 10. **F**un to build, **M**oney potential (direct or indirect), **T**echnically challenging.

**Active** = at least one score is ≥ 7. **Archive** = everything below the bar, kept for reference.

---

## Active

### Themes worth building around

#### 1. Trustworthy automation (AI made this the bottleneck) `[F7 M9 T10]`

We are moving from "software = tools you operate" to "software = agents that act". Brutal requirement: trust.

- reliable agent execution in messy real-world systems (permissions, retries, state, idempotency, rollback, audits)
- evaluation harnesses for AI behavior (tests for "does it do the right thing?" not just "does it compile?")
- provenance: what data/model/tool produced this output; can it be traced and reproduced?
- guardrails that aren't theater: policy, monitoring, incident response for AI

If you build anything AI-adjacent and don't solve trust, you're building a demo.

#### 2. Interoperability and data plumbing (still painfully unsolved) `[F5 M9 T8]`

World runs on broken pipes:

- moving data across SaaS tools, warehouses, event streams, CRMs, internal systems
- mapping schemas, resolving identities, deduping entities, lineage
- "business logic glue" that currently lives in tribal knowledge and brittle scripts

The opportunity isn't a new DB. It's making data movement + meaning cheap.

### Knowledge-base / search / RAG product ideas

#### Personal knowledge assistant `[F6 M5 T7]`
Acts as a personal knowledge base; helps you understand whether you've learned something new based on daily input. Gives most-similar stuff and asks whether you've learned new or not. The "is this new?" primitive can be used in many places — letting users enter products, building agents, etc. If a social network adopts it to improve content quality (by embedding original content and refusing duplicates), it would be gamed by users and counter-intuitive to what SM stands for today.

#### AI social media with personas `[F7 M5 T7]`
A social media with AI influencers. They make reels and cross-post. AI personas hireable. Integrate vector-hot-feed logic. AI personalities create memes on news headlines; like/dislike each other's memes.

### AI-generated suggestions (external)

#### Tier A — easy to price, easy to demo ROI
- **B3 — Recruiter / Candidate Intelligence.** `[F4 M8 T6]` You already think about resumes/jobs. Small recruiters and in-house HR have clear pain and budgets.
- **A1 — Synthetic User QA Tester.** `[F6 M7 T7]` QA is a real line item. Self-serve $50–$200/mo per team is believable. Competition exists; value story is simple.
- **B2 — AI Postmortem & RCA Generator.** `[F5 M7 T6]` Narrow, painful, mandated in any semi-serious org. Turns hated work into editing. Good wedge into SRE/infra budgets.

#### Tier B — strong but harder
- **B1 — AI Log & Incident Copilot.** `[F5 M7 T7]` Outage cost huge → value clear. But space is noisy and expectations high.

#### Tier C — interesting but slow / unclear monetization
- **C2 — Screen/Browser Copilot.** `[F7 M5 T7]` Could get B2C subs from devs/researchers. Real but not obviously huge; needs UX polish + growth loops.
- **B4 — AI Step-Through Debugger.** `[F8 M4 T9]` Strong devtool, but devtools hard to monetize early without distribution. More strategic than quick cash.
- **A3 — Deep Dive Investment Analyst.** `[F4 M7 T7]` Very high ARPU if it works, but no VC/M&A network yet. Long sales cycles, trust barrier.
- **A2 — Legacy Resurrection.** `[F4 M8 T8]` Enterprises could pay 5–6 figures, but won't trust a random new tool with their core systems. Multi-year credibility play.
- **C1 — LLM Experiment & Routing Hub.** `[F6 M4 T7]` Devs love it; devs also love not paying. Many will self-host. Monetizable, but you'll fight "I can just script this".

#### Other framed pitches (active)
- **Idea #2 — The Society of VERY Interesting People.** `[F3 M7 T2]` Application-only community of 100–200 members. High-end service ($2.5K–$5K/year). Interview each member 3x/year with a set of life questions.
- **Idea #4 — Granola for Salespeople.** `[F4 M7 T5]` Video-call recording + automated personalized follow-up tailored to sales motion.

---

## Archive (no single score ≥ 7)

### Knowledge-base / search / RAG (archive)

#### AI cacher `[F6 M5 T6]`
A SaaS that stores all queries asked with their cached response and TTLs. User can see list of questions asked; when they start typing they see related questions and choose whether to create a new query. Response is fetched from DB and, based on TTL, either returned or re-asked.

Features:
- topic / subtopic level filtering
- mass TTL cleanup based on topic/subtopic (store valid-till field per answer and topic)
- works for a particular set of data
- linked questions per response

Extends to medicine knowledge base, education bots, etc. Works very well for knowledge bases that are not frequently updated. Won't be good where many personalizations / subsequent questions are needed. Stores two things in vector DB: the knowledge base, and all existing questions.

#### Build-a-vector-DB-from-a-website `[F5 M5 T5]`
An app that builds a vector database by scraping a site (use sitemap). Embeddable as an extension of various apps. People can hoard stuff and let everyone query on it. See sitegpt.com.

#### Chat with content `[F6 M5 T6]`
- Chat with any book
- Search across podcasts (also across multiple)
- Search across mine-hoarded stuff — books, starred repos (hoarder.com extension)
- App should be able to take subtitles and find the point of a dialogue — index on complete lines, not timestamps

#### Find similar git commits `[F5 M3 T6]`
An app to search across commit history. Also a primitive for finding similar git commits.

#### Search across browser history `[F6 M5 T6]`
Need to handle sites whose content depends mostly on auth — just take base and info.

#### Multi-LLM Q&A with voting `[F5 M3 T5]`
Answers previously-asked questions for free/instant with 10 different LLMs. Users vote which answer is best. Refresh, see related questions. No personalization — just general niche questions answered well and open for everyone. Like Stack Overflow, but answered by LLMs.

#### Research paper recommender `[F5 M5 T6]`
Recommends papers based on what the user searches. Detailed, broken-down embeddings per paper. Similar well-cited papers recommended. Ad blocks between papers based on query. Graph-based hierarchy to show prerequisites.

#### Subreddit digester `[F6 M5 T5]`
Stays posted on everything new in the subreddit. Checks trending posts every 8h; distills with LLM and Slacks you. For SEO, include Reddit hot-posts summary. Users enter their favorite subreddit — return cached version if exists, else build and store. Premium = immediate refresh. Custom prompts. Charge for latest data, faster refreshes, dynamic prompts, ability to export.

- Tip: append `.json` to any reddit URL for the JSON
- Cache user questions like `/q/What-about-this?`
- Weekly / monthly summary pages with history

#### Celebrity / fictional-character site builder `[F4 M4 T5]`
Generates SEO sites very fast. Community-driven articles (consensus). Track public/social appearances. Could combine with story-tunes. Could be a social network with celebrity-tracker AI personas that interact in public.

### AI Ayurveda / wellness store `[F4 M5 T5]`

Problems → herbs → minerals, plus product links. Read prescriptions and test results.

- Ayurveda website linked to an online store.
- Pick a body part → relevant herbs to cure it. Figure (internalized human body) + list view.
- People rate herbs and vote for the best herb for an illness.
- Extend to all natural substances and where to buy.
- RedwoodJS as CMS, Vercel Store as frontend.
- Integrate food store and skincare. Break myths of food items. Choose foods per requirements.
- For each generic query, auto-create a blog via DB insertion. Redeploy daily for SSG (JAMStack — like superblog). Something like Dukaan but more specific to advice + showing products.
- Always include disclaimer and inform when a doctor is needed.

Adjacent: chemist assistant after dumping all known chemicals. AI fitness chatbot (feed all exercises with tutorials; personalized plan based on what user has and needs). Quotes handbook.

Can end up making copilots for all jobs — lawyers, doctors, etc. Can base any of them on a specific person's content.

### Memenza `[F6 M3 T5]`

Multiple meme templates based on entered text. Give users multiple options and capture feedback to improve the algorithm. Website with latest memes in different categories.

- Two uploader tiers: verified and not verified.
- Top-memer awards. Leagues. Verified memers add their own categories (after moderator check).
- Real-time AI meme generator from user input.
- Best meme-format finder.
- Different AI personalities create memes on news headlines for a feed. AI personas like/dislike memes.
- Start as a simple meme generator; create embeddings of text explanations of all meme images; given a user prompt, find best-suited template.
- For SEO: cache user queries.

### AI-generated suggestions (archive)

- **A4 — Negotiation/Sales Roleplay Partner.** `[F4 M6 T6]` Corporate L&D spends a lot. Need sales motion and proof. Even a few teams at $200–$500/mo each matters.
- **B5 — Customer Interview Digest.** `[F4 M6 T5]` PMs/founders already pay for Gong/Chorus/tl;dv. If you're "cheaper and simpler", you can carve out a niche.
- **B6 — AI Knowledge Ops.** `[F4 M5 T6]` Big TAM, swamped with competitors, requires selling into mid-sized companies. Higher friction.
- **B7 — LLM Benchmarks & Cost Optimizer.** `[F4 M4 T5]` Nice-to-have. Budgets tiny unless you evolve into a full "LLM ops" platform (crowded).
- **C3 — Builder Brain.** `[F6 M3 T6]` Emotionally compelling, but users don't pay reliably. Cool toy unless turned into a team product.
- **C4 — Small Incident/Log Explainer.** `[F4 M2 T5]` Standalone is just a feature of B1, not a business.
- **Idea #1 — Competitor listener.** `[F5 M6 T5]` Enter your company URL → monthly report on what's happening in your industry. Scan Twitter and LinkedIn for competitor info. Track employee movement and hiring.
- **Idea #3 — DateMyFriends.com.** `[F5 M5 T4]` Friends build/promote your dating profile and act as middlemen who must approve introductions.
- **Idea #5 — Undercover boss/customer as a service.** `[F3 M5 T2]` Send a real person through your sales funnel and report back what's broken.
- **Idea #6 — Memories for your email.** `[F5 M4 T4]` Photos-style memories feature for old emails. Nostalgia + nudge to reconnect with long-forgotten contacts.
- **Idea #7 — 360 life audit.** `[F3 M5 T3]` Service that audits your entire life (wardrobe, diet, skincare, hobbies, spending) and gives well-researched suggestions. Manual at first, automated over time.
- **Idea #8 — Productivity palace (retreats).** `[F3 M5 T2]` Opposite of yoga retreat — sign up to be extremely productive for 30 or 90 days.
