# Saas Ideas

![AI Generated](https://ai-percentage-pin.vercel.app/api/ai-percentage?value=0)
![AI PRs Welcome](https://ai-percentage-pin.vercel.app/api/ai-prs?welcome=yes)

Scores: `[F? M? T?]` per idea, each out of 10. **F**un to build, **M**oney potential (direct or indirect), **T**echnically challenging.

**Active** = at least one score is ≥ 7. **Archive** = everything below the bar, kept for reference.

## Active

- A browser that remembers everything you have searched and lets you handle things accordingly `[F7 M6 T7]`
- An app that quickly creates mock APIs using AI and deploys it. Use redis to store sample data and generate random query params to make it work. `[F7 M6 T5]`
- An app to handle time-series geographical data from various sources and view them like a heat map. Can be used for Swiggy orders or similar. Handle multiple sources and approximate future demand. Can also take IP as input. Useful for all kinds of analytics and to see active people. Using timeseries DB or CH. https://en.wikipedia.org/wiki/Kalman_filter, https://en.wikipedia.org/wiki/Viterbi_algorithm `[F8 M5 T9]`

* A pluggable recommendation system that anyone can plug in with custom field inputs and custom interactions with weightages. Built one for feed; simple vector search, scaled and made much more configurable. Beta mode to let users test new developments and a test env to try various configs. Stores recommendation items and user interactions in my db. `[F7 M7 T8]`
* An app that can teach any concept in an interactive story with cartoons and stuff. `[F7 M4 T6]`
* A vscode extension that checks your commits before allowing to push via AI. Need to think on how this can be better after lint, beautify and build function post hooks. `[F7 M5 T5]`
* A SM with bunch of different personality bots, they interact with all posts and with each other. Can also act as a user's advisors. Let people create different agents with their own API keys for a price. Need to think of scaling when there are too many AI agents. Do we limit them to topics or subreddits? Can we use this system for StoryTunes (the realtime collaboration)? Agents should be able to discuss among themselves and reach a consensus. `[F8 M5 T7]`
* Build a minimalist graph library for fun. Canvas, webgl and svg. Useful for: `[F8 M4 T8]`
  - knowledge graph
  - family tree / relationship manager
  - agent decision diagram (for saas maker, with various components integrated)
  - learning tool, graphic of things. Click on something and make an anki card
* Bizarre idea: fluid apps — apps that let users prompt and modify the app to their liking. `[F8 M5 T9]`
* Tree Visualizer — visualise tree algorithms, let users build trees and write algo there. Extend with an IDE for collaborative leetcode problems, lets them test and submit for all collaborators. `[F8 M4 T7]`
* A website that tells you the complexity of your code if you write your code on it. Tests your code for possible edge cases when described with time of input expected. Exception handling class which can detect infinite loops, misc errors. Tells you execution time on various inputs to judge complexity. `[F7 M3 T9]`
* Let old machines be used as a server. Next step would be something like Dukaan; if local drops shift to cloud. A simple project with complete CI/CD, metrics and log management. Maybe scaling and descaling as well. #infra `[F7 M4 T7]`
* The family tree app — https://github.com/sarthakagrawal927/Tree `[F7 M5 T6]` (full spec in `family-tree.md`)
* Storytunes. An app where people can write stories with voted collaboration from peers or public. Each single line can be voted against other lines, can involve AI. Voted collaboration writing experience. Can move to spreadsheet and others later. Each on-site event is also like a story; people can collaborate ideas and have a nice event summary at the end. StoryTunes data feedback can be used to generate a really good dataset. Spec: `storytunes.md` `[F8 M4 T7]`
* https://www.ycombinator.com/rfs (reference)
* Scalable n8n or similar tool. `[F6 M7 T8]`
* Performance marketing agents. `[F4 M7 T6]`
* CCTV app that customizes for various special queries like for how long was the doctor sitting, how long the patient sat, the bin is in the position or not. `[F5 M6 T7]`
* A meeting helper (https://www.shadow.do/, https://cluely.com). `[F6 M7 T6]`
* DB to sheet/notion app with features like: git-style data merge, virtual grid for high capacity (cache all data and update on change, maybe cache via some compression mechanism, AI copilot, shareable subData, etc). `[F8 M6 T9]`
* Analytics: An AI analytics company that auto-generates user reports based on analytics. Can require manual plumbing or just SDK install (detects all user interactions). Makes flow diagrams, maps old website CTA to newer CTA. Lets clients fix mistakes. Auto-generates relevant flow diagrams based on asked queries (as it will have entire context of the app). Can identify pain points; self-labels where not plumbed. Can be advertised as a browser extension for users to check how they interact with websites. Identify where Agent/human would fail to understand. Merge context from Product Dev replacement, extension in which you can prompt and modify websites. Try to extract information on how users shop/behave. Integrate foresight — predict user's next move. Ends up creating a huge state-machine flow diagram (entire life cycle of user, time spent on screen/between events). Option to remove anomalies in avg (top10, bottom10). Convert each user's action into statements and generalise behaviour on platform. `[F8 M8 T8]`
* While I plan to build a lightweight analytics framework (something like datafast), I should also make my own observability+logs framework. A simplified tailored version. Something I can attach to all my products with one click. `[F6 M5 T7]`
- An agent that deep-dives into someone and finds out almost everything about them. Once they have full info, they use it to trade info from other people and verify it from other sources, eventually gaining more info. Will have to create a source authenticity framework where each source is rated based on past info (can be part of everythingIsRated). `[F6 M5 T8]`
- A chatbot arena where I put in some thought, where LLMs argue and come to a consensus (something is already built). Are results always better when the same question is asked to multiple models? Can we do it something like a consensus algorithm of blockchain? Or do they feel better for complex reasoning tasks, where a multi-agent approach breaks it into simpler pieces? `[F7 M3 T7]`
- An app that animates manga, comics. Ensure voice for a particular character remains the same and we properly identify the dialogue owner each time and create a profile for the character to assign suitable voice and tone. Fill scenes in middle, add proper BGM, expand wherever necessary. If this can be done, why not animate novels by giving initial character designs. By training on bunch of anime fights we can teach it how anime actions work and it can replicate. We have input-output for this as there are plenty of manga converted to anime. But it might end up messing with the story 😂. `[F9 M6 T10]`
- How to make AI work with a new language. Given all syntax and a compiler+test suite to continuously test, AI can iteratively write a lot of code as it can definitely create logic. `[F7 M3 T9]`
- An app that analyses GitHub repository history. Like codiem — also explains how the codebase works and behaves. Determine importance of codebase based on how frequently changes were made to the file/flow. What each commit meant? What was probable effort involved? What is the general contribution on this repo / across org? `[F6 M5 T7]`
- Build something like https://www.wikiboard.org, but for entire net. Click to zoom on tab, multiple parallel threads etc. AI summary and reasoning. A simple app that embeds the full page and is scrollable. Write comments on the side for each particular part by highlighting it. PDFs too. Can merge with interconnected browser thing. `[F6 M4 T7]`
- An on-disk trie made of 1M sentences that tries to predict next word quickly. Can't have all in memory, so it reads from disk. First node is start, with multiple child nodes as possible starts of sentences. Each new sentence with common path can increase the path nodes count. Can also be used to find grammatical mistakes if there is no existing mapping? Or it will just become a really good suggester. `[F8 M2 T9]`

### Games (active)
- A poker game with stakes of tasks instead of money. Everyone playing can add a few tasks on others; their value can be decided via consensus among other players. Solid stake without involving money. Like truth-and-dare for poker. Can be extended to different betting/gambling games. `[F7 M3 T5]`
- An app that lets you build walkable 3D worlds; choose to design each building. `[F7 M3 T8]`
- TD (https://github.com/maciej-trebacz/tower-of-time-game?tab=readme-ov-file) (reference)
- Open world game with AI characters. `[F8 M3 T8]`

---

## Archive (no single score ≥ 7)

- Create a directory maker for fun. And release a bunch of directories for fun, they all can use the same DB, ofc. E.g., the AI Wrapper directory. All lists (directories or such) in the market should be collaborative and modifiable via votes. The problem with this would be verifying accounts. They should be able to be visible and absent based on votes. Categorised, ranked. `[F6 M5 T4]`
- This directory can also act as a market place for domain selling. Will need to verify domain via DNS forwarding. Add a back link to my website there. Also need to know how to un-verify it (if someone sold it elsewhere). Can have auction system built in. `[F4 M5 T5]`
- Why don't people selling SaaS have a bid system? Bidders create a profile (with social profile connected for added verification). Gamify it: bids placed (and unique products bidded on), bids won and actual payment count. `[F4 M4 T4]`
- Summarise threads — twitter, reddit etc. `[F5 M5 T4]`
- A super app to help you prepare for tests, integrate AI-based questioning, anki notes and is extremely personalised. `[F5 M6 T5]`
- A browser extension that has your various info and just fills all the forms for you. Be it regular form, post/comment creation. How can it go beyond what browsers are already capable of doing? `[F5 M6 T5]`
- An extension that can read everything on web and lets you query on it. `[F6 M6 T5]`
- An app that scrapes websites to decipher the current mood about things like: fundraise, hiring, scandals etc. `[F6 M6 T5]`
- Linkedtree-like product that shares ad revenue. Start with Google ads but move to our product ideas. Three stages for a user-company relation based on which ad can be made: visited, tried and paid. Users paid in coins which can be used with e-commerce after tie-ups. Seed celebrities with their link to see if they love it. Maybe make it as a service, where you personally tailor each page. Why not have analytics like datafast. Let users vibe-design their page. Let them paste other linkedtree URLs and import data, maybe make a form and share. Marketplace where people share templates? Charge others for designing their page? `[F5 M6 T5]`
- RAG is mostly dependent on data prep. Maybe buy something like Memoryrag.com. Post-training studying can be useful. And inference optimisation. `[F4 M6 T6]`
- There is a plethora of fake tweet screenshots — how about something like verified tweet. Use a tool like https://tweethunter.io/tweetpik to generate screenshot and easy share button to share with link and image. Or maybe people want to be misinformed or manipulate others. There are ways to tweet text directly; if you can figure out how to tweet image just by clicking, can also turn it into browser extension. `[F5 M4 T4]`
- An app (maybe integrated in SH as list or something like feature list in saasmaker). People can recommend books/movies in groups. `[F4 M3 T4]`
- EverythingRated.com — a website where people can rate anything and everything on different aspects. People can create new aspects, new categories, new things to rate. `[F6 M4 T5]`
- An app like pager-duty but for orders live. Need to build a system that will be used everywhere (elixir sounds good). `[F5 M5 T6]`
- A dedicated app for lawyers, CA to highlight and provide their services — like practo for health. Plumber, carpenter, driver for rent. People can add voice prompts to decrease the overhead of understanding the requirements before the professional accepts. `[F3 M6 T4]`
- An app that lets you book transport for local tourism. Lots of travel packages, target audience tourists. Probably partner with agencies. Soon shift towards one-stop platform for tourism. Like MMT but for taxis. `[F3 M5 T4]`
- An app that people wanna use in case of panic. Provides less options, learns from user experience what suits them. Personalised care, less overwhelming, welcoming. Can be extended for old people. `[F4 M3 T4]`
- An app to make tier lists easily. People can vote, so consider merging with similar ideas like storytunes or everythingRated. `[F4 M3 T4]`
- Temp splitwise (can also be used to host lists and shit) — https://github.com/sarthakagrawal927/temp-splitwise `[F5 M3 T4]` _(shipped)_
- A shareable music list (with DnD realtime editing, different source handling) — https://github.com/sarthakagrawal927/musicDnD/ `[F6 M2 T5]` _(shipped)_
- A location tracking app — https://github.com/sarthakagrawal927/location-tracker-app `[F4 M3 T4]` _(shipped)_
- An app that lets you find relevant places based on user feedback, something like nomad list but for similar stuff — https://github.com/sarthakagrawal927/maps-server `[F6 M5 T4]` _(shipped)_
- Website recommender — share some of your history/bookmarks or manual enter, and it gives you samples you'd want. A URL shortener with super analytics like datafast. Every time you click on a short URL, you first see a screen with either recommended websites (cookies based on previously visited) or what people also visited. LinkedTree should also have super analytics built-in, with similar loader. `[F5 M5 T5]`
- An app to understand users' needs. Can be used to sell (software, medicine, cosmetics, clothes, food etc). `[F3 M5 T4]`
- A simple web-based SQL table viewer with AI capabilities built in. `[F6 M6 T5]`
- An app that summarises git commits and posts them on Twitter (also build the tweet scheduling bot) (https://github.com/jnsahaj/lumen). `[F5 M3 T4]`
- An app that analyses stock data to determine purchases by determining its health in short term, long term etc. `[F4 M6 T6]`
- An app to have maps for everything, starting off rental properties. Users can add entries for all sorts of stuff: where sceneries are great, where food is great (not all places are listed on Zomato), where to go to see the sunset, which area is lit. `[F4 M4 T4]`
- An application to help companies track the location of their employees, give them directions/tasks etc. `[F3 M5 T4]`
- A tool which feeds entire repo to LLM in readable way. Just give github link and to get a review. `[F5 M5 T5]`
- Start a business with payment integration. Provide to people with no business a way to collect money. Send the amount they made to them as contractual pay. `[F3 M5 T5]`
- A better ad experience based on where the users are going instead of where they want to go. For example in airports, the ads can be improved based on where the flight is being sent, you can add some ad for the destination. `[F2 M3 T2]`
- What about having a podcaster embedded? At ALL places. `[F3 M2 T3]`

### Games (archive)
- A tambola game which takes real money and sends back real money. Custom rooms with or without money. Like the IPL betting game. `[F5 M5 T5]`
- An app that requires you to answer some questions before opening up. Difficulty keeps on increasing with the count you opened the app already. Also lets you set the amount of time you use your phone when you start. Asks every time for how long, decreases contrast over time, eventually converting it to black-n-white. `[F5 M3 T4]`
- Anti Chess App. `[F4 M2 T4]`
- Monopoly Game. `[F4 M2 T4]`
- Game of catan at much larger scale, playable online for companies. Main features can be scaled: more bricks, dice roll numbers can repeat. `[F5 M3 T5]`
- A dashboard filled with mini-games. `[F4 M3 T4]`
- A JS implementation of the game in which people match glasses. People predict an initial order of glasses, then the computer tells you the number of correct glass positions. `[F4 M1 T4]`
- Small web-games directory. `[F4 M3 T4]`
- Build a project using t3-app and party-kit. `[F5 M1 T5]`
- Since people nowadays love reels and games, how about an app that combines both. Swipe and get to play a new game or next level of old game. Reels on the side. Will make revenue with ads. Even better if you can let people submit games (embed web apps). `[F5 M4 T5]`
- An app (chrome extension) to download a good amount of blogs as PDF. People index already; why can't I render what I index in a pretty way? Since most websites use SPA, we might need AI to add tailwind classes to it after cleaning the HTML. `[F6 M3 T5]`

### Archive (earlier cleanup pass — duplicates, covered-by-active-projects, jokes, orphan URLs)

_These were removed in an earlier cleanup commit; restoring as archive per request. Scores are rough since these had been pre-deemed weak._

- An app that tells you what anime character you are based on your tweets or you can write your bio. Might have to scrap anime characters from their own wiki pages, Reddit reviews etc. `[F3 M2 T3]`
- Adult School ? adults organizing fest, sport events etc. A place where they can spend working on building whatever they want. They can pick any job they want to do as well. `[F3 M2 T2]`
- Vodka vanilla Oreo drink. A website where cocktails across different places are rated and reviewed. Just directly make EverythingIsRated? `[F2 M3 T2]` _(self-noted as duplicate of EverythingRated)_
- An app to help practice different boxing moves with different modes. Can extend to various other sports and add vision model for giving better direction and scoring to the user. `[F4 M3 T5]`
- An app that tells you how much gay you are based on your data, can reel market this. Can make bunch of similar apps in this direction: just simple API to ask, get some data from user → process it → ask AI for some conclusion and add poppy images they can share. Maybe an app with full of surveys like this. Then people can hold bunch of badges. They can select their most likely character within a particular universe. Connect with people with most common groups? Seems like a good way to monetise, by some mid games and leaderboard or some city creation. If badges seem important maybe a serious version with tie-ups to real-world organizations. `[F4 M5 T3]`
- Product called Propoganda for AI short-video-form marketing. Should have discovering new ideas, generation, posting, analytics and optimisation. Fullstack product with analytics, automation, content generation and optimisation. Can be part of saas-maker. Cheap prices, direct AI integration into discussion with data and everything. Premium packages could include private data, otherwise we can sell the data to others building similar products. An app that helps you create social creds (images, videos), by suggesting what's popular, what's good etc. Can also tell how likely a particular item is to do, based on market analysis. You can have virtual friends with personality and they can be part of their social cred. _(covered by `reel-maker`)_
- Personal Reporter — Reddit daily update summary; mails I received summary; news I care about. A bunch of similar things which can be like watching tv for the user from their fav character/voice. _(covered by `agentMode`)_
- Learning App (purpose is active recall, anki, journal, mind maps & general notes), plus access to general wiki (aka AI, try Apple AI also). Focus on interportability. Should base my learning app off of tldraw sdk. _(future direction of `swe-interview-prep`)_
- Complete Movies, Anime, Manga App with watchlist and active recommendations. Already have manga, anime setup. Should work with my existing app (anime_list), with focus on informing users about their relevant content, followed series etc. _(covered by `anime_list`)_
- Storytunes (duplicate of active entry above).
- Use-and-throw splitwise (duplicate of Temp splitwise above).
- Orphan reference: https://docs.google.com/spreadsheets/d/1s_ZDKtOoGqi1FtTyPeeS0h_0d96jOFJ-TuzwjWnnCPo (Google Sheets)
- Orphan reference: https://octolens.com/
