#!/usr/bin/env python3
"""Source of truth for the master idea list. Rebuilds README + docs/ideas.json.

Run: python3 scripts/build.py

Scoring:
- F/M/T/C each /10
- C = competition pressure (1 open field, 10 brutal)
- M_eff = max(M - max(C-3, 0), 0)
- Adj  = F + M_eff + T
- Active iff max(F, M_eff, T) >= 8
"""

import json, re, csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Hand-curated AI ideas (fleshed-out detail + scores incl. competition)
# ---------------------------------------------------------------------------

AI_IDEAS = [
    # (F, M, T, C, title, body)
    (7, 9, 10, 9, "Trustworthy automation infra (theme)",
     "Reliable agent execution in messy real-world systems: permissions, retries, idempotency, rollback, audits. Eval harnesses, provenance, real guardrails. **Comp:** LangSmith, LangFuse, Braintrust, Helicone, Galileo, Arize — well-funded and crowded. **Wedge:** focus on a single vertical (e.g. revenue ops or back-office finance) where guardrails are mandatory."),
    (5, 9, 8, 9, "Interoperability / data plumbing (theme)",
     "Moving data across SaaS tools, warehouses, CRMs; schema mapping, identity resolution, lineage, business-logic glue. **Comp:** Fivetran, Airbyte, Hightouch, Census, Stitch, Segment, Workato — brutal. **Wedge:** AI-native config (point at a source, it infers the schema and the joins) targeted at solo PMs not data teams."),
    (6, 5, 7, 8, "Personal knowledge assistant",
     "Personal RAG that flags whether a new input is genuinely new vs. already known to you. Primitive that powers \"is this novel?\" elsewhere. **Comp:** Mem, Notion AI, Reflect, Obsidian + Smart Connections, Glasp. **Wedge:** API-first; let other apps consume the \"novelty\" signal."),
    (7, 5, 7, 7, "AI social media with named personas",
     "Social network populated by AI influencer personas that post, comment, like, and cross-platform. Users can hire them. **Comp:** Character.ai, Hedra, Botify, OnlyFans-AI clones. **Wedge:** social/feed dynamics (algorithmic timeline, personas with consistent voice across long arcs)."),
    (6, 5, 6, 5, "AI cacher",
     "Cached-Q&A SaaS for knowledge bases that don't change often (regulations, medical, education). Per-topic TTL, vector-stored questions + answers, link related Qs. **Comp:** GPTCache, langfuse cache — infra primitives, not products. **Wedge:** the *product* layer (browseable cached answer pages + SEO)."),
    (5, 5, 5, 7, "Build a vector DB from a website",
     "Point at a sitemap, get a queryable embedding store + embed snippet. **Comp:** SiteGPT, Mendable, custom-GPTs, Fini. **Wedge:** white-label / API-first."),
    (6, 5, 6, 9, "Chat with content (books / podcasts / hoarded stuff)",
     "Chat-with-PDF / podcast / starred-repos. **Comp:** ChatPDF, Glasp, MyMind, Recall, hundreds of variants. **Wedge:** very few — this category is basically commodity unless you own a unique corpus."),
    (5, 3, 6, 4, "Find similar git commits",
     "Search commit history semantically. Find prior changes that touched related code, similar bug fixes, etc. **Comp:** Sourcegraph (broad), nothing dedicated. **Wedge:** zero-config dev tool, $5/mo per dev."),
    (6, 5, 6, 7, "Search across browser history",
     "Semantic search over your tabs, auth'd pages handled gracefully (store metadata not content). **Comp:** Rewind, Arc, History.app, raycast-history. **Wedge:** privacy-first local-only mode."),
    (5, 3, 5, 5, "Multi-LLM Q&A with voting",
     "10 LLMs answer common questions; users vote best answer. **Comp:** Chatbot Arena, Poe, You.com Smart. **Wedge:** SEO play (cached canonical answers indexed for long-tail queries)."),
    (5, 5, 6, 7, "Research paper recommender",
     "Embeddings per paper, graph-based prereq view, cited-by hierarchy. **Comp:** Elicit, Semantic Scholar, Scite, Undermind, Consensus. **Wedge:** none obvious unless vertical-specific."),
    (6, 5, 5, 6, "Subreddit / community digester",
     "Every ~8h, distill trending posts of a subreddit into a Slack/email digest. Cache results, SEO pages per subreddit. **Comp:** various Substack newsletters, Pushshift-derived tools. **Wedge:** broad coverage + custom prompts per user."),
    (4, 4, 5, 6, "Celebrity / fictional-character SEO site builder",
     "Auto-generated sites about celebrities or franchise characters; community-edited; appearance tracking. **Comp:** Fandom, Wikipedia, IMDb. **Wedge:** AI-generated long-tail."),
    (4, 5, 5, 4, "AI Ayurveda / wellness store",
     "Problem → herb/mineral lookup with disclaimers, integrated store. JAMStack with auto-blog-from-query. **Comp:** Practo, Cure.fit, various Ayurveda sites. **Wedge:** product-first not content-first; commerce angle."),
    (6, 3, 5, 5, "Memenza — AI meme generator",
     "Best-template-finder from user text; tiered uploaders; AI personas riff on news headlines. **Comp:** Imgflip + AI, Supermeme.ai. **Wedge:** persona/feed angle."),
    (4, 8, 6, 8, "B3 — Recruiter / candidate intelligence",
     "Enrich candidates from public signals (GitHub, talks, posts); score fit vs. JD; surface passives. **Comp:** Gem, Findem, Loxo, LinkedIn Recruiter, Eightfold. **Wedge:** target solo recruiters and 1–5-person agencies priced at $50–200/mo (the enterprise tools are $1K+/seat)."),
    (6, 7, 7, 7, "A1 — Synthetic user QA tester",
     "AI agent walks through user flows from a natural-language spec; reports regressions. **Comp:** QA Wolf, Mabl, Reflect, Octomind, Devin. **Wedge:** persona-based synthetic users that retain memory across sessions, not just script replay."),
    (5, 7, 6, 5, "B2 — AI postmortem / RCA generator",
     "Ingest incident timeline (logs, alerts, Slack, PRs); draft postmortem. **Comp:** Jeli, Rootly, FireHydrant — all bundle this inside incident-mgmt suites. **Wedge:** standalone, BYO-IM, $50/mo."),
    (5, 7, 7, 9, "B1 — AI log / incident copilot",
     "NL queries on logs, anomaly explanations, cross-service correlation. **Comp:** Datadog AI, New Relic AI, Honeycomb Query Assistant, Splunk. **Wedge:** vendor-agnostic ingest; useful even if you're already on Datadog."),
    (4, 6, 6, 5, "A4 — Negotiation / sales roleplay partner",
     "Voice AI roleplays prospects for SDR/AE training. **Comp:** Hyperbound, BoldlyDo. **Wedge:** vertical-specific scenarios + import customer transcripts as training data."),
    (4, 6, 5, 8, "B5 — Customer interview digest",
     "Cluster themes across recorded calls (Gong/Otter/Fireflies); extract quotes per theme. **Comp:** Gong, Chorus, tl;dv, Fathom — incumbents already do AI summaries. **Wedge:** BYO-recordings; no integration; PM-tool-first not sales-tool-first."),
    (4, 5, 6, 8, "B6 — AI knowledge ops",
     "Internal-doc search with staleness flagging and ownership inference. **Comp:** Glean ($$$), Microsoft Copilot for Work, Notion AI, Atlassian Rovo. **Wedge:** small teams (10–50 people) priced at $5/seat."),
    (7, 5, 7, 7, "C2 — Screen / browser copilot",
     "Always-on copilot that watches your screen and proactively offers context. **Comp:** Cursor, OpenInterpreter, Self-Operating Computer, Highlight, Cluely. **Wedge:** cross-app focus + privacy (local LLM option)."),
    (8, 4, 9, 5, "B4 — AI step-through debugger",
     "AI explains \"why is this variable that value?\" by tracing prior steps. Production traces via log replay. **Comp:** existing IDE debuggers + Cursor. **Wedge:** post-mortem replay debugging on production traces."),
    (4, 7, 7, 8, "A3 — Deep-dive investment analyst",
     "Ingest 10-Ks, transcripts, news, expert calls; produce structured company deep-dives. **Comp:** AlphaSense, Hebbia, Daloopa, BamSEC. **Wedge:** solo investor / family office tier at $500/mo (incumbents are $25K+/year)."),
    (4, 8, 8, 3, "A2 — Legacy code resurrection",
     "AI-assisted COBOL/old-Java/Perl-monolith → modern stack migration with test harness generation. **Comp:** specialized consultancies (Wipro, Accenture); no real product. **Wedge:** the absence of a product is the wedge — if you can deliver, enterprises pay 6 figures."),
    (6, 4, 7, 7, "C1 — LLM experiment / routing hub",
     "Best-model-per-call routing, A/B, fallback chains, cost tracking. **Comp:** OpenRouter, LiteLLM, Portkey, Helicone. **Wedge:** opinionated for product teams (not infra teams) with experiment templates."),
    (4, 4, 5, 7, "B7 — LLM benchmarks & cost optimizer",
     "Continuous prompt eval across models + cost forecasting + opt recommendations. **Comp:** Helicone, PromptLayer, LangSmith. **Wedge:** focus on the *recommendation*, not just the dashboards."),
    (6, 3, 6, 4, "C3 — Builder brain",
     "Personal AI that remembers what you've built, tried, abandoned; surfaces patterns. **Comp:** none directly. **Wedge:** for indie hackers / solo founders; B2C-priced ($10/mo)."),
    (5, 6, 5, 7, "Idea #1 — Competitor listener",
     "Enter your company URL → monthly report on industry chatter; scan Twitter/LinkedIn for employee movement and hiring. **Comp:** Crayon, Klue, Kompyte (enterprise); newer Apollo/Clay variants. **Wedge:** solo-founder pricing + auto-generated reports."),
    (3, 7, 2, 5, "Idea #2 — Society of VERY Interesting People",
     "Application-only paid community (100–200 members at $2.5–5K/yr). 3 interviews per member per year, custom questions. **Comp:** Trends.co, Hampton, Pavilion, Sidebar. **Wedge:** the *content* (interview corpus) as a moat."),
    (5, 5, 4, 8, "Idea #3 — DateMyFriends",
     "Dating app where your friends build/promote your profile and approve introductions. **Comp:** Hinge, Bumble, Wingman (the friend-managed app), Coffee Meets Bagel. **Wedge:** vertical (e.g. dating-for-30+-with-kids); but consumer dating is brutal."),
    (4, 7, 5, 7, "Idea #4 — Granola for Salespeople",
     "Call recording + automated personalized sales-style follow-ups. **Comp:** Granola (already exists), Fathom, Otter, Gong, Apollo's call recorder. **Wedge:** sales-rep-specific (writes follow-up in your tone, drafts CRM updates)."),
    (3, 5, 2, 3, "Idea #5 — Undercover customer as a service",
     "Real humans walk through your sales funnel and report what's broken. Service business. **Comp:** UserTesting (script-based), TryMyUI, FullStory recordings (not human). **Wedge:** humans + structured report. Service margins are low."),
    (5, 4, 4, 5, "Idea #6 — Memories for your email",
     "\"On this day\" feature for email; nostalgia + nudge to reconnect with old contacts. **Comp:** Superhuman has some of this, Reclaim.ai. **Wedge:** standalone, works with Gmail."),
    (3, 5, 3, 3, "Idea #7 — 360 life audit",
     "Service auditing your wardrobe, diet, skincare, hobbies, spending; gives well-researched suggestions. Service business. **Comp:** various luxury concierge services. **Wedge:** AI-automated tier + premium human tier."),
    (3, 5, 2, 3, "Idea #8 — Productivity retreats",
     "Anti-yoga retreat. Sign up to be extremely productive for 30/90 days. **Comp:** Builders & Backers, Edyn, On Deck (sort of). **Wedge:** focus + accountability, not networking."),
    (4, 2, 5, 4, "C4 — Small incident / log explainer",
     "Single-feature standalone — likely better as part of B1, not its own business."),
]

# ---------------------------------------------------------------------------
# README items: keep existing prose, add C scores by lookup
# Key = first ~50 chars of the title (stable enough to match)
# ---------------------------------------------------------------------------

# Hand-curated C (and F/M/T) per README idea
# Format: (F, M, T, C, full description). Source = "README".
README_IDEAS = [
    (9, 6, 10, 7, "An app that animates manga and comics. Ensure voice for a particular character remains the same, identify dialogue owners, assign a consistent voice/tone; fill scene gaps, add BGM, optionally extend novels by generating character designs. Training data: manga → anime conversions. **Comp:** Runway, Pika, Wonder Dynamics, aspara.ai. **Wedge:** manga-specific (voice consistency across many chapters)."),
    (8, 8, 8, 9, "AI analytics company: auto-generates user reports from instrumentation; flow diagrams; identifies pain points and self-labels gaps. Browser-extension mode for users to see how they interact. Can predict the user's next move. State-machine view of user lifecycle. **Comp:** PostHog, Heap, FullStory, June, Mixpanel, Amplitude, Datadog RUM — and PostHog already does most of this. **Wedge:** brutal market; only a sharp vertical (e.g. e-commerce-only with conversion-focused reports) has a shot."),
    (8, 6, 9, 7, "DB → sheet/notion app with git-style data merge, virtual grid for high-capacity, AI copilot, shareable subData. **Comp:** Airtable, Outerbase, Rowy, Glide, Baserow, NocoDB. **Wedge:** the git-style merge (true branchable/mergeable data) is the unique angle."),
    (8, 5, 9, 5, "Bizarre idea: fluid apps — apps that let users prompt and modify the app to their liking. **Comp:** Bolt.new, v0, Lovable, Replit Agent (build-time); this is closer to runtime prompt-driven UI. **Wedge:** runtime malleability, not just one-shot generation."),
    (8, 5, 9, 5, "Time-series geographical heatmap from many sources (Swiggy-style demand). Approximate future demand from history; IP-as-input. Timeseries DB or CH. Kalman/Viterbi for smoothing. **Comp:** Mapbox, Kepler.gl, Carto, Datawrapper. **Wedge:** real-time multi-source forecasting (not just visualization)."),
    (7, 7, 8, 7, "Pluggable recommendation system anyone can plug in: custom fields, custom interactions, weightages. Vector-search backbone, beta mode, test env. **Comp:** Algolia Recommend, AWS Personalize, Recombee, Aporia. **Wedge:** focus on indie/small SaaS (the incumbents target enterprise) with one-line install."),
    (6, 7, 8, 8, "Scalable n8n alternative — automation builder that doesn't fall over above N workflows. **Comp:** n8n, Zapier, Make, Pipedream, Workato. **Wedge:** scaling/perf focus alone is thin; pair with a specific vertical (e.g. RevOps automation)."),
    (8, 5, 7, 7, "A SM with personality bots that interact with all posts and each other. Users create agents with their own API keys (for a price). Agents discuss and reach consensus. Could power StoryTunes-style collab. **Comp:** Character.ai, Hedra, persona-AI. **Wedge:** multi-agent dynamics, not just 1:1 chat."),
    (8, 4, 8, 6, "Build a minimalist graph library for fun. Canvas, WebGL, SVG. Useful for: knowledge graphs, family-tree managers, agent decision diagrams, learning-tool annotations (click → make an anki card). **Comp:** D3, Sigma.js, react-flow, Cytoscape. **Wedge:** ergonomic API + opinionated layouts for specific use cases."),
    (8, 4, 7, 8, "Tree Visualizer — visualise tree algorithms; let users build trees and write algo there. Extend with an IDE for collaborative leetcode (test + submit for all). **Comp:** leetcode itself, Coderpad, HackerRank, VisuAlgo. **Wedge:** real-time collaboration on the *algorithm canvas*, not just code."),
    (7, 3, 9, 5, "A website that tells you the time complexity of code you paste. Tests for edge cases when given expected input size. Class to detect infinite loops, misc errors. Reports execution time on various inputs. **Comp:** Big-O calculators (academic), Codility-style runners. **Wedge:** AI-assisted (\"why is this O(n²)\")."),
    (7, 4, 7, 3, "Let old machines be used as a server. Next step Dukaan-style hosting. Full CI/CD, metrics, log management. Auto scale/descale. **Comp:** Hetzner/OVH self-host, Coolify, Caprover. **Wedge:** repurposing-old-hardware angle for indie/hobby use."),
    (7, 5, 6, 8, "The family tree app — https://github.com/sarthakagrawal927/Tree. **Comp:** Ancestry, MyHeritage, FamilySearch, 23andMe, Geni. (full spec in `family-tree.md`)"),
    (8, 4, 7, 5, "Storytunes. Multi-author collab story writing with line-by-line voting; can include AI contributors. Each on-site event = a story; auto-summarised. Spec: `storytunes.md`. **Comp:** Storium, PlotVote, WriteJam, Storyfall, Mycelore. **Wedge:** AI persona contributors voted alongside humans."),
    (6, 7, 6, 7, "Meeting helper a la shadow.do / cluely.com. **Comp:** Granola, Fathom, Otter, Cluely, Tactiq. **Wedge:** specific vertical (e.g. interview-only, or therapy-only)."),
    (5, 6, 7, 5, "CCTV app customisable for special queries (\"how long did the doctor sit?\", \"is the bin in position?\"). **Comp:** Verkada, Camera.ai, custom CV. **Wedge:** prompt-based query interface vs. preset analytics."),
    (8, 3, 8, 5, "Open world game with AI characters."),
    (7, 3, 8, 5, "An app that lets you build walkable 3D worlds; choose to design each building. **Comp:** Roblox Studio, Decentraland, Spatial. **Wedge:** AI-assisted building."),
    (6, 5, 7, 8, "Lightweight observability + logs framework you can attach to all your products with one click. **Comp:** Datadog, New Relic, Sentry, Axiom, Highlight. **Wedge:** indie-priced + dead-simple."),
    (6, 5, 7, 7, "Analyses GitHub repository history; explains how the codebase works and behaves. Determines importance by change-frequency; explains each commit, effort, contribution patterns. **Comp:** Sourcegraph, Greptile, CodeRabbit. **Wedge:** historical/archaeological focus vs. real-time code review."),
    (7, 6, 5, 6, "An app that quickly creates mock APIs using AI and deploys them. Redis for sample data, random query-param generation. **Comp:** Mockoon, Beeceptor, Mockend, Postman mock. **Wedge:** AI-spec-from-prose."),
    (7, 6, 7, 7, "A browser that remembers everything you have searched and lets you handle things accordingly. **Comp:** Rewind, Mem.ai, Arc, Spotlight history. **Wedge:** browser-only (not screen-recording) — lighter, more privacy-friendly."),
    (6, 5, 8, 5, "An agent that deep-dives on a person and finds out almost everything. Once it has full info it trades info from others and verifies from multiple sources, building a source-authenticity framework. **Comp:** Clay, Apollo, OSINT tools, BeenVerified. **Wedge:** the source-authenticity-from-trades primitive."),
    (7, 5, 5, 7, "A vscode extension that checks your commits before allowing push, via AI. Runs after lint/beautify/build. **Comp:** CodeRabbit, Greptile, GitButler review, Codium PR-Agent. **Wedge:** pre-push (not post-PR) timing."),
    (7, 3, 7, 6, "A chatbot arena where LLMs argue and reach consensus. Multi-agent decomposition of complex reasoning vs. single-model. **Comp:** Chatbot Arena, Poe, debate-style multi-agent demos. **Wedge:** consensus-protocol angle (vote/blockchain-style) for harder tasks."),
    (7, 4, 6, 5, "An app that can teach any concept in an interactive story with cartoons. **Comp:** Khan, Brilliant, custom GPTs, Synthesis. **Wedge:** the cartoon/animation generation pipeline."),
    (6, 4, 7, 4, "Build something like wikiboard.org but for the entire net. Click-to-zoom on tab, parallel threads, AI summary, full-page-embed, side-comments on highlights, PDFs too. **Comp:** Glasp, Hypothesis, Recall, Heptabase. **Wedge:** the spatial canvas (zoom + parallel) + AI summary."),
    (7, 3, 9, 3, "How to make AI work with a new programming language. Given all syntax + a compiler/test suite, AI iteratively writes code. **Comp:** research-only, no product. **Wedge:** academic angle + tooling for language designers."),
    (8, 2, 9, 3, "An on-disk trie of 1M sentences for fast next-word prediction. Disk-resident, child nodes per common prefix. Could find grammar mistakes (no matching path) or be a great suggester. **Comp:** none — niche. **Wedge:** the *engineering*, not the product."),
    (6, 6, 5, 6, "DB to sheet/notion app — see top entry (duplicate of fluid apps territory). Skip."),
    (6, 6, 5, 7, "An extension that can read everything on the web and lets you query on it. **Comp:** Glasp, Readwise Reader, Notion Web Clipper + AI, Recall. **Wedge:** query-first (not save-first)."),
    (6, 6, 5, 5, "An app that scrapes websites to decipher current mood about fundraises, hiring, scandals. **Comp:** Crayon, Apollo, broad scrapers. **Wedge:** mood/sentiment extraction is the differentiator."),
    (6, 6, 5, 6, "A simple web-based SQL table viewer with AI built in. **Comp:** Outerbase, Beekeeper Studio, TablePlus + AI plugins, DBeaver. **Wedge:** browser-native, zero-install, shareable links."),
    (4, 7, 6, 6, "Performance marketing agents — AI agents that run/optimize paid ads end-to-end (creative gen, bid management, audience iteration). **Comp:** AdCreative.ai, Smartly.io, Mutiny, Madgicx. **Wedge:** end-to-end automation for solo founders (not big marketing teams)."),
    (5, 6, 5, 5, "Linkedtree-like that shares ad revenue with users. 3 user-company relationship stages (visited/tried/paid). Users earn coins for e-commerce. Built-in analytics like Datafast. Vibe-design pages; import other linkedtree URLs; template marketplace. **Comp:** Linktree, Beacons, Bento, Stan. **Wedge:** the ad-revenue-share dynamic."),
    (5, 6, 7, 5, "An app like pager-duty but for live orders. **Comp:** PagerDuty, Opsgenie, custom. **Wedge:** order-flow-specific (sub-minute SLA monitoring for fulfilment teams)."),
    (5, 5, 5, 7, "Website recommender — share history/bookmarks; get sample sites you'd like. Plus a URL shortener with super analytics. Every click shows a recommended-sites loader. **Comp:** Bitly, Dub.co, Datafast, Stumbleupon vibe. **Wedge:** rec-engine inside the shortener."),
    (5, 5, 5, 6, "A tool that feeds an entire repo to an LLM in a readable way. Just give a github link and get a review. **Comp:** Greptile, CodeRabbit, Repomix, ingest-cli. **Wedge:** zero-config, public-link-only mode."),
    (4, 4, 5, 4, "Create a directory maker for fun. Release a bunch of directories (AI Wrapper directory etc). Same DB; collaborative voting; vote-based visibility. **Comp:** ProductHunt, There's an AI for that, Beautiful Public Data. **Wedge:** vote-driven curation + many sub-directories."),
    (4, 5, 5, 5, "Directory as a marketplace for domain selling. DNS verification, auction system, backlinks. **Comp:** GoDaddy Auctions, Sedo, Dan.com. **Wedge:** vertical (e.g. only AI domain auctions)."),
    (4, 4, 4, 4, "Why don't people selling SaaS have a bid system? Bidders profile (social verification). Gamify: bids placed, bids won, payment count. **Comp:** MicroAcquire, Acquire.com — but those are acquisitions, not bidding for the product. **Wedge:** live-bid-and-buy model."),
    (5, 5, 4, 4, "Summarise threads — twitter, reddit etc. **Comp:** ThreadReaderApp, TweetHunter, native Twitter Summary. **Wedge:** cross-platform + topic clusters."),
    (5, 6, 5, 8, "A super app to help you prepare for tests, integrate AI questioning, anki notes, extremely personalised. **Comp:** Quizlet, Anki + plugins, RemNote, Brainscape. **Wedge:** AI-personalisation alone is no longer differentiated."),
    (5, 6, 5, 5, "A browser extension that fills all forms for you (regular forms, post/comment creation). Beyond what browsers already do. **Comp:** browsers themselves, Magical, 1Password, autofill plugins. **Wedge:** generative — drafts posts/comments contextually, not just stored fields."),
    (4, 6, 6, 8, "RAG is mostly data prep. Maybe buy something like Memoryrag.com. Post-training studying + inference optimisation. **Comp:** LlamaIndex, LangChain, Unstructured.io. **Wedge:** as a vertical RAG-as-a-service."),
    (5, 4, 4, 4, "Verified-tweet screenshot tool. Use a tool like tweethunter.io/tweetpik to generate screenshot + share. Or browser ext that lets you tweet-as-image directly. **Comp:** TweetHunter, Tweetpik, Poet.so. **Wedge:** verification angle (cryptographic proof + ledger of the original tweet)."),
    (4, 3, 4, 7, "An app integrated in SH for book/movie recommendations within groups. **Comp:** Letterboxd, Goodreads, Hardcover. **Wedge:** group/friends-only recs."),
    (6, 4, 5, 8, "EverythingRated.com — rate anything on any aspect. Users create aspects, categories, things. **Comp:** Reddit itself, dedicated rating sites per vertical. **Wedge:** mostly content quality / community."),
    (3, 6, 4, 8, "A dedicated app for lawyers / CA / professionals — like Practo for health. Plumber, carpenter etc. Voice prompts to reduce friction. **Comp:** Practo, JustDial, UrbanCompany, Sulekha. **Wedge:** voice-prompt onboarding for tradespeople."),
    (3, 5, 4, 7, "An app to book transport for local tourism. Many packages, tourist target audience, partner with agencies. MMT-but-taxis. **Comp:** MMT, GoIbibo, Yatra, Booking. **Wedge:** taxi-vertical only + AI-generated itineraries."),
    (4, 3, 4, 4, "An app for panic — provides less options, learns what suits the user, personalised care. Can extend for old people. **Comp:** Headspace, Calm, Wysa, Woebot. **Wedge:** crisis-moment-only mode."),
    (4, 3, 4, 6, "Tier-list app where people can vote. Consider merging with storytunes / everythingRated. **Comp:** tiermaker.com. **Wedge:** real-time collaborative voting (storytunes-style)."),
    (5, 3, 4, 5, "Temp splitwise (can also host lists and shit) — https://github.com/sarthakagrawal927/temp-splitwise. _(shipped)_ **Comp:** Splitwise, Settle Up. **Wedge:** no-account/temp-room angle."),
    (6, 2, 5, 7, "Shareable music list with realtime DnD editing across sources — https://github.com/sarthakagrawal927/musicDnD. _(shipped)_ **Comp:** Spotify collaborative playlists, Apple Music shared, Songbird. **Wedge:** cross-platform (Spotify+YouTube+Apple) merging."),
    (4, 3, 4, 7, "Location tracking app — https://github.com/sarthakagrawal927/location-tracker-app. _(shipped)_ **Comp:** Life360, Find My, Google Family Link. **Wedge:** zero-account, link-share-only."),
    (6, 5, 4, 6, "An app to find relevant places based on user feedback — nomad-list-style for other things — https://github.com/sarthakagrawal927/maps-server. _(shipped)_ **Comp:** Nomad List itself, Wanderlog. **Wedge:** vertical-specific (e.g. \"best cafes to work from\")."),
    (3, 5, 4, 5, "An app to understand users' needs — can be used to sell software/medicine/cosmetics/clothes/food. **Comp:** UserInterviews, Maze, Lookback. **Wedge:** AI-conducted interviews + analysis pipeline."),
    (5, 3, 4, 4, "An app that summarises git commits and posts to Twitter (also a tweet scheduler bot). https://github.com/jnsahaj/lumen — exists. **Wedge:** none if you don't build a community around it."),
    (4, 6, 6, 7, "An app that analyses stock data to determine purchases by health (short/long term). **Comp:** Koyfin, Simply Wall St, Stock Rover, TradingView. **Wedge:** AI-driven (\"explain this stock in plain English\")."),
    (4, 4, 4, 7, "An app to have maps for everything — start with rental properties; users add scenery/food/sunset/lit-area pins. **Comp:** Google Maps, MapMyIndia, OSM-based apps. **Wedge:** community-curated pins per vertical."),
    (3, 5, 4, 5, "Application to help companies track employee location and assign tasks. **Comp:** Hubstaff, Time Doctor, Skedulo. **Wedge:** specifically for field-service teams (delivery/utilities)."),
    (3, 5, 5, 7, "Start a business with payment integration. Provide people with no business a way to collect money. Send earned amount as contractual pay. **Comp:** Stripe Atlas, Razorpay, Cashfree, UPI apps. **Wedge:** none in markets with mature UPI."),
    # Games
    (5, 5, 5, 6, "Tambola with real money — custom rooms with/without. Like the IPL betting game. **Comp:** Indian gaming apps (MPL, Dream11, Winzo). **Wedge:** regulatory/legal challenge in India."),
    (5, 3, 4, 5, "Phone-time control: answer questions to unlock, difficulty rises with usage count; sets daily time and decreases contrast over the day. **Comp:** Opal, OneSec, ScreenZen. **Wedge:** the question-answering ritual is novel."),
    (4, 2, 4, 6, "Anti Chess App. **Comp:** chess.com Anti-Chess, lichess. **Wedge:** none."),
    (4, 2, 4, 7, "Monopoly Game. **Comp:** existing digital versions."),
    (5, 3, 5, 6, "Catan at larger scale online for companies — more bricks, dice numbers can repeat. **Comp:** Catan Universe. **Wedge:** company/team-building format."),
    (4, 3, 4, 5, "A dashboard filled with mini-games. **Comp:** Poki, CrazyGames."),
    (7, 3, 5, 5, "Poker with stakes of tasks instead of money. Others assign you tasks, value set by consensus. Like truth-and-dare for poker. **Comp:** none direct. **Wedge:** social-stakes mechanic."),
    (4, 1, 4, 3, "JS implementation of the glasses-matching game. **Comp:** none."),
    (4, 3, 4, 5, "Small web-games directory. **Comp:** Poki, CrazyGames, itch.io."),
    (5, 1, 5, 3, "Build a project using t3-app and party-kit. _(tech demo, not a product)_"),
    (5, 4, 5, 5, "Reels + games combo — swipe to play a new game or next level. Reels on the side. Submit-your-own games. **Comp:** Roblox, Tappy. **Wedge:** TikTok-format game discovery."),
    (6, 3, 5, 5, "Chrome extension to download blogs as PDF. Use AI to add tailwind classes for prettier rendering. **Comp:** SingleFile, Pocket, save-as-PDF, Reader-mode tools. **Wedge:** the AI re-styling is the unique angle."),
]

# ---------------------------------------------------------------------------
# Specs
# ---------------------------------------------------------------------------

SPEC_IDEAS = [
    (7, 5, 8, 8, "FamilyTree — [spec](family-tree.md). Social family-tree with auth/genetic angles. **Comp:** Ancestry, MyHeritage, FamilySearch, 23andMe, Geni."),
    (7, 7, 7, 8, "magicform — [spec](magic-form.md). AI-built forms with realtime/2-way comms and SDK embed. **Comp:** Typeform, Tally, Fillout, Google Forms, Jotform, SurveyJS."),
    (8, 5, 8, 8, "Productivity App — [spec](productivity.md). Life-OS combining habits, schedule, goals, journal, social mode. **Comp:** Notion, Todoist, Motion, Sunsama, Akiflow."),
    (8, 4, 7, 5, "StoryTunes — [spec](storytunes.md). Multiplayer story engine with canon voting and AI co-authors. **Comp:** Storium, PlotVote, Storyfall, Mycelore."),
]

# ---------------------------------------------------------------------------
# Solopreneur — category-based C baselines applied to scraped entries
# ---------------------------------------------------------------------------

CAT = {
    'greatest-hits':                                  (6, 4, 7, 'Greatest Hits'),
    'micro-saas-ideas':                               (6, 6, 7, 'Micro SaaS'),
    'solo-developer-ideas':                           (6, 6, 7, 'Solo Developer'),
    'solopreneur-ideas':                              (6, 4, 7, 'Solopreneur'),
    'gpt-wrapper-ideas':                              (7, 6, 8, 'GPT Wrappers'),
    'automation-ideas':                               (6, 6, 7, 'Automation'),
    'digital-product-ideas':                          (6, 5, 7, 'Digital Products'),
    'productized-services':                           (4, 3, 6, 'Productized Services'),
    'freemium-and-open-source-ideas':                 (6, 5, 7, 'Freemium / Open Source'),
    'weekend-projects':                               (7, 3, 5, 'Weekend Projects'),
    'm2m-by-makers-for-makers':                       (7, 4, 6, 'Makers for Makers'),
    'plugins':                                        (6, 5, 6, 'Plugins'),
    'apps-so-simple':                                 (6, 3, 6, 'Apps So Simple'),
    'one-page-websites':                              (4, 2, 7, 'One-Page Sites'),
    '1m-shovels':                                     (5, 3, 7, '$1M Shovels'),
    'no-audience-required':                           (7, 3, 5, 'No Audience Required'),
    'ideas-you-can-build-today-with-no-code-tools':   (4, 2, 7, 'No-Code Ideas'),
    'bubble-ideas':                                   (4, 2, 6, 'Bubble Ideas'),
    'no-code-ideas':                                  (4, 2, 6, 'No-Code'),
    'problems':                                       (5, 5, 5, 'Real Problems'),
    'marketplaces':                                   (4, 5, 7, 'Marketplaces'),
    'david-vs-goliath':                               (4, 3, 5, 'David vs Goliath'),
    'weird-but-profitable-ideas':                     (5, 3, 3, 'Weird but Profitable'),
}
SOL_DROP = {'sitemap','travel-and-digital-nomad-ideas','niche-blog-ideas','niche-sites','launched-with-website-builder'}

def m_from_revenue(rev):
    if not rev: return 2
    r = rev.strip()
    if not r or r=='?': return 2
    m = re.search(r'\$([\d.]+)\s*([KMB])?', r, re.I)
    if not m: return 2
    n = float(m.group(1))
    suf = (m.group(2) or '').upper()
    if suf == 'B': mo = n * 1e9
    elif suf == 'M': mo = n * 1e6
    elif suf == 'K': mo = n * 1e3
    else: mo = n
    if mo >= 100_000: return 9
    if mo >= 10_000:  return 7
    if mo >= 1_000:   return 5
    return 3

def m_eff(M, C):
    return max(M - max(C - 3, 0), 0)

def adj_sum(F, M, T, C):
    return F + m_eff(M, C) + T

def is_active(F, M, T, C):
    return max(F, m_eff(M, C), T) >= 8

# ---------------------------------------------------------------------------
# Pull solopreneur from git history (json was deleted)
# ---------------------------------------------------------------------------

import subprocess
def fetch_sol():
    # walk back history to find the json
    log = subprocess.check_output(['git','log','--all','--pretty=%H','--','solopreneur_ideas.json'], cwd=str(ROOT)).decode().split()
    for sha in log:
        try:
            raw = subprocess.check_output(['git','show',f'{sha}:solopreneur_ideas.json'], cwd=str(ROOT))
            return json.loads(raw)
        except subprocess.CalledProcessError:
            continue
    return []

# ---------------------------------------------------------------------------
# Build master list
# ---------------------------------------------------------------------------

all_items = []  # list of dicts

for F, M, T, C, title, body in AI_IDEAS:
    all_items.append({'f':F,'m':M,'t':T,'c':C,'idea':f"**{title}.** {body}",'source':'ai-ideas'})
for F, M, T, C, body in README_IDEAS:
    all_items.append({'f':F,'m':M,'t':T,'c':C,'idea':body,'source':'README'})
for F, M, T, C, body in SPEC_IDEAS:
    all_items.append({'f':F,'m':M,'t':T,'c':C,'idea':body,'source':'spec'})

sol = fetch_sol()
for x in sol:
    src = x.get('source')
    if src in SOL_DROP or src not in CAT: continue
    Fb, Tb, Cb, label = CAT[src]
    M = m_from_revenue(x.get('revenue'))
    title = (x.get('title') or '').strip() or '(untitled)'
    rev = (x.get('revenue') or '?').strip() or '?'
    co = (x.get('company_name') or '').strip()
    url = (x.get('url') or '').strip()
    co_part = f" — {co}" if co else ''
    link = f" — [story]({url})" if url else ''
    idea = f"**{rev}** — {title}{co_part} _({label})_{link}"
    all_items.append({'f':Fb,'m':M,'t':Tb,'c':Cb,'idea':idea,'source':'starterstory'})

# Add derived fields (no active/archive split — sorting in the site handles it)
STRONG = 7  # threshold for "strong on an axis"
for x in all_items:
    x['m_eff'] = m_eff(x['m'], x['c'])
    x['adj']   = x['f'] + x['m_eff'] + x['t']
    s = []
    if x['f']     >= STRONG: s.append('F')
    if x['m_eff'] >= STRONG: s.append('M')
    if x['t']     >= STRONG: s.append('T')
    x['strengths'] = ''.join(s) or '—'
    x['s_count']   = len(s)

all_items.sort(key=lambda x: (-x['s_count'], -x['adj'], -max(x['f'], x['m_eff'], x['t']), -x['f']))
from collections import Counter
print(f"Total {len(all_items)} ideas | strength distribution: {dict(Counter(x['s_count'] for x in all_items))}")

# ---------------------------------------------------------------------------
# Write minimal README stub
# ---------------------------------------------------------------------------

stub = """# Saas Ideas

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
"""
(ROOT/'README.md').write_text(stub)

# ---------------------------------------------------------------------------
# Write docs/ideas.json
# ---------------------------------------------------------------------------

(ROOT/'docs'/'ideas.json').write_text(json.dumps(all_items))
print("Wrote README.md (stub) and docs/ideas.json")
