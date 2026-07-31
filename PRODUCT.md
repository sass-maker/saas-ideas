# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

The maintainer uses the public catalog at a desk or on a phone to compare tech-heavy SaaS ideas and choose a plausible solo path to $5K MRR. Public visitors may inspect the reasoning, but the product is personal decision support rather than a marketplace.

## Product Purpose

Make idea ranking reproducible: filter, sort, and compare each idea's money potential, fun, feasibility, competition, source, and customer context without relying on memory or vibes.

## Positioning

The catalog combines explicit score derivation with the underlying wedge, competitor notes, and revenue math. Its value is transparent ranking logic, not crowd voting or backlog management.

## Operating Context

Ideas and scoring live in `scripts/build.py`; `site/ideas.json` and the README are generated. The published product is one static, sortable, filterable HTML catalog under `site/`.

## Capabilities and Constraints

- Preserve all filters, sorting dimensions, scores, best-bet status, source, customer type, and idea copy.
- Keep the site dependency-free and usable as a static Cloudflare Pages artifact.
- Never hand-edit generated catalog data.
- Desktop favors dense comparison; narrow screens must preserve the same decision information in a readable order.

## Evidence on Hand

The scored catalog and its real idea content are in `site/ideas.json`; scoring rationale and product constraints are documented under `docs/product/`.

## Product Principles

- Ranking logic stays visible and reproducible.
- Idea substance outranks decorative presentation.
- Mobile adaptation preserves decisions rather than hiding core facts.
- Static, local-first operation remains simple.
