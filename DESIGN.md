---
name: SaaS Ideas
description: Dense, inspectable product-idea ranking for one decisive operator.
colors:
  canvas-dark: "#0d1117"
  text-dark: "#e6edf3"
  muted-dark: "#8b949e"
  border-dark: "#30363d"
  accent-dark: "#58a6ff"
  success-dark: "#3fb950"
  best-bet: "#d29922"
typography:
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 600
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "14px"
    lineHeight: 1.5
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: ".8rem"
    fontWeight: 600
rounded:
  sm: "3px"
  md: "6px"
spacing:
  xs: ".25rem"
  sm: ".5rem"
  md: ".75rem"
  lg: "1.25rem"
components:
  input:
    backgroundColor: "transparent"
    textColor: "{colors.text-dark}"
    rounded: "{rounded.md}"
    padding: ".4rem .6rem"
  badge:
    textColor: "{colors.muted-dark}"
    rounded: "10px"
    padding: ".05rem .4rem"
---

# Design System: SaaS Ideas

## Overview

**Creative North Star: "The Operator's Ledger"**

This is a compact decision surface, closer to a well-kept engineering ledger than a marketing dashboard. Density, direct comparison, and honest source context lead. The incumbent GitHub-like neutral palette and system type remain the visual authority.

**Key Characteristics:** dense, flat, scan-first, data-led, restrained.

## Colors

Dark and light schemes use neutral canvases, quiet borders, one link accent, green for strong scores, and amber only for best-bet emphasis.

## Typography

System sans-serif keeps the static page fast and familiar. Numeric columns use tabular figures; idea prose remains the dominant reading content.

## Layout

Desktop uses the full-width comparison table. Phone layouts recompose each row into a single card-like ledger entry: idea first, three decision scores second, source and customer last. Controls stack without changing their labels or behavior. The breakpoint is content-driven below 680px; 768px retains the table.

## Elevation & Depth

The system is flat. Borders, tonal row hover, and strong-score cell fills provide separation; shadows are not part of the language.

## Shapes

Inputs use 6px corners, inline badges use compact pills, and mobile rows use the same 6px geometry. Avoid soft oversized cards.

## Components

Inputs and filters are transparent with a single neutral stroke. Badges remain quiet outlined metadata. Strong score cells use a muted green fill; the best-bet star remains amber.

## Do's and Don'ts

### Do:

- **Do** keep idea text first in the mobile reading order.
- **Do** retain visible Money, Fun, best-bet, source, and customer context.
- **Do** keep desktop density and sorting unchanged.

### Don't:

- **Don't** make horizontal scrolling the primary phone interaction.
- **Don't** hide decision-critical fields on mobile.
- **Don't** introduce decorative dashboard cards, gradients, or dependencies.
