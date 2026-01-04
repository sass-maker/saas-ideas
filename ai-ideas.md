# AI Ideas

1) trustworthy automation (ai made this the bottleneck)

we are moving from "software = tools you operate" to "software = agents that act". brutal requirement: trust.

- reliable agent execution in messy real-world systems (permissions, retries, state, idempotency, rollback, audits)
- evaluation harnesses for ai behavior (tests for "does it do the right thing?" not just "does it compile?")
- provenance: what data/model/tool produced this output; can it be traced and reproduced?
- guardrails that arent theater: policy, monitoring, incident response for ai

if you build anything ai-adjacent and dont solve trust, you're building a demo.

2) interoperability and data plumbing (still painfully unsolved)

world runs on broken pipes:

- moving data across saas tools, warehouses, event streams, crms, internal systems
- mapping schemas, resolving identities, deduping entities, lineage
- "business logic glue" that currently lives in tribal knowledge and brittle scripts

the opportunity isnt a new db. its making data movement + meaning cheap.
