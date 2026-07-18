import { defineConfig } from "blume";

/**
 * Blume is the presentation/search layer for the docs/ knowledge system.
 * The committed Markdown in docs/ is the source of truth; this config only
 * controls how it is rendered. See AGENTS.md and
 * docs/architecture/decisions/adr-007-relocate-site-reclaim-docs.md.
 *
 * The published SaaS-ideas catalog lives in site/ and is unrelated to Blume.
 */
export default defineConfig({
  title: "SaaS Ideas",
  description:
    "Knowledge system for the saas-ideas catalog: product, architecture, decisions, operations, and durable learnings.",

  content: {
    // Blume reads the knowledge system from docs/. The published catalog
    // (site/) is a separate Cloudflare Pages project and is not rendered here.
    root: "docs",
  },

  search: {
    provider: "orama",
  },

  markdown: {
    imageZoom: true,
  },

  ai: {
    // Blume manages its own llms.txt / markdown negotiation for the docs site.
    // The catalog's agent surfaces in site/ are separate (see docs/operations/agent-surfaces.md).
    llmsTxt: true,
  },

  seo: {
    sitemap: true,
    robots: true,
  },

  deployment: {
    output: "static",
    // Docs site deploy target is not yet fixed — see STATUS.md.
    site: "https://docs.saas-ideas.pages.dev",
  },
});
