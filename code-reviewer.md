# Code Reviewer

Will start off a simple code reviewer. (have already created repo with initial flow)

In future will expand to:
- Code View Generator (something like deepwiki), index and understand incremental changes
- Documentor (document everything) in slack, linear etc. Auto capture knowledge base
- connect with Analytics to answer questions there regarding what could lead to what
- analyse application logs to find bugs, happenings. Also has understanding of new releases.
- have conversation with app owners regaridng new features and their impacts. AI will also ask questions to fill all the gaps it needs to fill
- figure out issues -> commits -> tickets/owners

Core components:
- code index and understanding - something like cursor/claude-code. How they understand the codebase recuresively. Then I need to do this historically and get meaning out of individual commits.
  - can also do changelogs across releases and discover outputs by devs
- logs understanding - first need to create my own logging system, then how to plug it everywhere. then handle the storage and understanding of events/bugs with those logs
- integration of analytic tools, linear and slack. User should be able to understand what ticket moved the needle. Slack answers are remembered.
- saas tester - maybe the thing to test whether an app is useful (able) or not. And possible merger w sass maker.
