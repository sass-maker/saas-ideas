# AI Knowledge base Dump


Ai chatbot for fitness. Can just feed all possible exercises with tutorial. User can come in ask about what they have and what they need and get super personalised plan.

## Ayurveda
Problems to herbs, minerals. Along with product link
Should be able read prescriptions and tests results

Ayurveda website linked to our online store.
A website which lets you choose a body part and tells you relevant herbs required to cure it.
Can have both figure (actual internalized human body) and list view,

People can come and rate the herbs and vote for the best herb for particular illness.

Can be extended for all natural substances along with their places to buy.

Can use redwoodJS as CMS. Vercel Store as frontend.


Can also integrate foodstore and skin care
Where we break myths of various food items.
Also let’s you choose foods as per your requirements

For each generic query, auto create a blog via db insertions
Can redeploy the web everyday to make it work with SSG
Something like dukaan but more specific to advice and show products
Also should always give proper disclaimer and inform doctors need

## Random
AI cacher. a #saas that stores list of all queries asked with their cached response and TTLs. User can see list of questions asked, also when starts typing they can see the questions related to what they want and chose whether they want to create a new query.
Response can be fetched from DB and based on TTL they can either be returned or re-asked.
Should have
- topic, subtopic level filtering
- ⁠mass ttl cleanup based on topic/subtopic (can store valid till field per answer and topic)
- ⁠should be able to work for a particular set of data
For each response should also have linked questions.
Then this project can be extended to medicine knowledge base and Front.page education bot
Should work very well every knowledge base that is not very frequently updated.
With help of date answered and valid till we should be able to handle it
Will store 2 things in vector DB.
First the knowledge base
And second all existing questions
Won’t be good where too many personalizations and subsequent questions
An app that’s lets you build a vector database out of scrapping a website
Can use site map or shit

Can build a chemist assistant after dumping all known chemicals known to mankind

An quotes handbook, which will give you quote based on what you want.

App should also able to take subtitles and find the point of dialogue. Instead of indexing on timestamps, index on complete lines.

Can end up making copilots for all jobs - lawyers, doctors etc

Can base it on some person’s content as well

Chat with any book to try it out

An app to search across commit history

An app to search across mine hoarded stuff - books, starred repo (can use that extension)(hoarder.com)
Can transform this into an embeddable extension of various apps. People can come and hoard some stuff there and let everyone query on that. Can embed this anywhere with search ig. See sitegpt.com

Should be able to search in podcasts (also across)

Similar app can act as a personal knowledge base and helps you understand whether you have learned something new or not based on daily input. Gives user most similar stuff and asks whether they have learnt new or not.
Figuring out whether something is new or not can be dominantly used at multiple places, for example letting user enter product, making agent etc. What happens a SM adopts it to improve content quality, by not letting user post same but embedding original content. This will be gamed by users and counter intuitive to what SM stands right now.

can try to find similar git commits

https://pmfm.ai

An app that keeps you posted on everything new happening in the subreddit. Just check out the few trending posts every 8hr or so from the selected repos. Collects all the interesting info, uses gpt to distill it and then slacks you. To get SEO, can include Reddit hot posts summary. People can come and enter their favourite subReddit and see info about it. If it exists just return it, if it doesn’t make it and store in db for refreshing in future.
Allow user to immediate refresh if they have premium or it’s been a while that subReddit is refreshed. This way cron isn’t needed to be settled up and people can see my cool server side push events implementation.
Can everyone a new page is added or updated, can I debounce and send Google a reindex request. Can have weekly and monthly pages for the subreddit, along with history. Can also chat with subreddits.

To get info about any reddit page just add ".json" at end

Can also cache questions people ask like slug.  /q/What-about-this?

- An app that builds website for celebrities and movies very quickly. Can use it to generate SEO, articles can be of course community driven (consensus). Everyone can also see all the new information regarding the actor scrapped. Maybe combine with story tunes. Something similar to directories. Can also be used to track their public/social appearances. Can also try to read between the lines and generate a feed for it. How about just a SM which has celebrities tracker accounts and posts alot of stuff. Maybe has their AI profiles interact in public.

- an app that search across your browser history - need to handle websites whose content depending mostly on auth (maybe just take base and info about this only)

- the app should be able to answer questions prev asked for free/instant with 10 diff LLMs, users can come vote about which answer is best. User can refresh, can see related questions. No personalizations, just general niche questions answered well and opened for everyone. Kinda like stackoverflow, but answered by LLMs
- Research app which recommends papers based on what the user searches, has detailed, broken-down embeddings for each research paper. Similar well cited research papers can be recommended. Can have ad blocks in between research papers depending upon user query. Can show graph based hierarchy to show pre-requisites properly

- The AI social media can have bunch of social media influencers. Which can also make bunch of reels and those AI personas are also hireable and cross post across different platforms.
Can also integrate my logic of vector hot feed there as well to showcase skillet.

## Memenza
An app that gives you multiple meme templates based on your entered text, we can give users multiple options to choose and get feedback to further improve the algorithm.

Website with all the latest memes in different categories.

2 kinds of uploader - verified and not verified. Top memer awards will be given. Leagues will be awarded to memers. Memers can even add their own categories once they are verified and after the category is checked by moderators. There can be an AI which can make memes in real time by taking inputs from user. Also should be the best meme format finder.

Different AI personalities create memes on different news headlines to create a nice feed. Also AI personalities can like/dislike the memes. Will start off as simple meme generator, maybe can create embedding of text expaination of all meme images. Then people can input the text and will try to determine best suited

For SEO purposes, user’s queries can be cached, gives less resource intensive search results as well.











