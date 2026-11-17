---
name: parpi
description: One still public page on a graphite sheet, with sodium amber only on the stamp and the claim slip.
colors:
  amber: "#e2a23a"
  stamp-ink: "#1a1408"
  sheet: "#1c2328"
  ink: "#e7e2d6"
  secondary: "#c5d0d6"
  rule: "#8aa4b5"
typography:
  display:
    fontFamily: "Familjen Grotesk, sans-serif"
    fontSize: "clamp(3rem, 12vw, 6rem)"
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Familjen Grotesk, sans-serif"
    fontSize: "clamp(1.7rem, 4vw, 2.4rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Familjen Grotesk, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
  body:
    fontFamily: "Familjen Grotesk, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
  label:
    fontFamily: "Martian Mono, ui-monospace, monospace"
    fontSize: "0.72rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.06em"
spacing:
  page-gutter: "1rem"
  sheet-pad-x: "1.25rem"
  sheet-pad-y: "1.35rem"
  field-key: "9rem"
  column-gap: "1rem"
  stack-end: "3rem"
components:
  stamp:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.stamp-ink}"
    typography: "{typography.label}"
    padding: "0.32rem 0.5rem"
  claim-slip:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.stamp-ink}"
    padding: "0.65rem 1.25rem"
    height: "44px"
  nav-link:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    height: "44px"
---

# Design System: parpi

## Overview

**Creative North Star: "The Carbon Job Ticket"**

The page is one carbon work ticket printed on a graphite sheet. The sheet is the ground. A single carbon-blue rule separates the ticket from the sections under it and draws every field. Sodium amber is the ink of the status stamp and the perforated claim slip, and it appears nowhere else. Prose and the display word are a grotesque; keys, the stamp, the navigation, and the slip are a mono.

Density is a form, not a dashboard. One column, short sections, and empty facts drawn as blank rules. The page does not move. Focus is a 2px amber outline. There is no radius and no shadow.

The direction asked for the sheet to sit on a darker ground. The shipped page makes the sheet the background. A darker track color exists only on the scrollbar and is not part of this system.

**Key Characteristics:**

- Graphite sheet as the page ground
- Sodium amber only on the stamp and the claim slip
- One 1px carbon-blue rule
- Grotesque for prose and display, mono for keys, stamp, navigation, and the slip
- Empty facts drawn as a blank rule
- No radius, no shadow, no motion

## Colors

A dark graphite field, warm paper ink, one cool rule, and a rare amber.

### Primary

- **Sodium amber** (`#e2a23a`): The status stamp and the claim slip. Also the caret, the text selection, and the keyboard focus outline.

### Neutral

- **Graphite sheet** (`#1c2328`): Page, sheet, and navigation ground.
- **Paper ink** (`#e7e2d6`): Display type, field values, and navigation.
- **Secondary ink** (`#c5d0d6`): The name line, lede, section prose, and field keys.
- **Carbon rule** (`#8aa4b5`): Every 1px divider, the blank underline, and the scrollbar thumb.
- **Stamp ink** (`#1a1408`): Type and the dashed perforation on amber.

### Named Rules

**The Amber Rarity Rule.** Amber is the stamp, the claim slip, selection, caret, and focus. It is not a fill for sections, links, or body type.

**The One Stroke Rule.** Dividers, field rules, and the blank underline are a 1px solid carbon rule. The claim slip is the only dashed stroke, and that dash is stamp ink.

## Typography

**Display Font:** Familjen Grotesk (with sans-serif)
**Body Font:** Familjen Grotesk (with sans-serif)
**Label/Mono Font:** Martian Mono (with ui-monospace, monospace)

**Character:** A plain grotesque carries the name and the sentences. The mono is the ticket's machinery: keys, stamp, navigation, blank marks, and the slip.

Both families are self-hosted at weights 400 and 700. `font-display` is `swap`.

### Hierarchy

- **Display** (700, `clamp(3rem, 12vw, 6rem)`, line-height 0.9, tracking `-0.04em`): The word on the ticket. Familjen Grotesk.
- **Headline** (700, `clamp(1.7rem, 4vw, 2.4rem)`, line-height 1.05, tracking `-0.03em`): Section titles. Familjen Grotesk.
- **Title** (400, `1.35rem`, line-height 1.5): The public name under the display word, in secondary ink.
- **Body** (400, `1.125rem`, line-height 1.5): Lede and section prose, secondary ink, max length 72ch. Field values are the same family at `1.15rem` in paper ink.
- **Label** (700, `0.72rem`, tracking `0.06em`, uppercase): Field keys in Martian Mono and secondary ink. Navigation is the same family at `0.75rem`, weight 400, tracking `0.04em`, paper ink, not uppercased. The stamp is `0.75rem`, weight 700, tracking `0.08em`, uppercase. The slip is `0.85rem`, weight 700, tracking `0.02em`. A blank value is `0.78rem`, weight 400, tracking `0.02em`.

### Named Rules

**The Split Voice Rule.** Familjen Grotesk sets display, headlines, prose, and filled values. Martian Mono sets keys, the stamp, navigation, blank values, and the claim slip.

## Layout

One column, `min(72rem, calc(100% - 2rem))`, centered. The sheet padding is `1.35rem` vertical and `1.25rem` horizontal. The stack ends with `3rem` of space.

The mast is two columns: the display word and the name take the first column; the stamp sits at the end of the first row. Fields are a two-column grid, a `9rem` key and the value, with `1rem` between them and `0.7rem` / `0.85rem` of vertical padding. Each field opens with a top rule.

At `40rem` and below, the sheet side padding becomes `0.9rem` and each field stacks the key above the value with a `0.28rem` gap. Navigation wraps. Targets in the navigation and the slip keep a `44px` minimum height.

## Elevation & Depth

The system is flat. Nothing casts a shadow. Depth is the rule between bands, the amber stamp sitting on the sheet, and the claim slip breaking out to the sheet edges with a dashed top. The sheet and the page are the same color, so the ticket does not float.

### Named Rules

**The Flat Ticket Rule.** No box-shadow. A new surface is a rule or an amber band, not a lift.

## Shapes

Corners are square. Nothing sets a radius. The recurring geometry is the horizontal rule and the full-bleed slip, which cancels the sheet's side padding and closes the ticket with a dashed perforation.

## Components

### Navigation

- **Style:** A wrapping row of text links on the sheet, under a 1px carbon rule. Martian Mono at `0.75rem`, paper ink, no underline. Gap `0.25rem` `1.25rem`. Minimum height `44px`.
- **Hover / Focus:** No hover change. Focus is the page outline, 2px solid amber, 2px offset.

### Stamp

- **Shape:** Square. Padding `0.32rem` `0.5rem`.
- **Color:** Amber ground, stamp ink, Martian Mono `0.75rem` weight 700, tracking `0.08em`, uppercase.
- **Placement:** End of the mast's first row, aligned to the start of the display word.

### Field row

- **Style:** A definition pair. Key in label mono and secondary ink; value in Familjen Grotesk and paper ink.
- **Border:** 1px solid carbon rule on top.
- **Blank value:** Martian Mono, and a 1px carbon underline. Absence is a drawn rule, not a missing row.

### Claim slip

- **Shape:** Full width of the sheet, including the side padding it cancels. Square. Minimum height `44px`. Padding `0.65rem` `1.25rem`.
- **Color:** Amber ground, stamp ink, Martian Mono `0.85rem` weight 700, tracking `0.02em`. No underline.
- **Edge:** Top border is 1px dashed stamp ink. No other border.
- **Hover / Focus:** No hover change. Focus uses the page's 2px amber outline.

## Do's and Don'ts

### Do:

- **Do** keep the sheet as the page ground and separate bands with one 1px carbon rule.
- **Do** reserve amber for the stamp, the claim slip, selection, caret, and focus.
- **Do** set keys, the stamp, navigation, blank values, and the slip in Martian Mono, and prose plus display in Familjen Grotesk.
- **Do** draw an empty fact as a mono mark on a carbon underline.
- **Do** keep keyboard focus as a 2px amber outline with 2px offset.
- **Do** keep the claim slip full-bleed to the sheet, with a dashed stamp-ink perforation.

### Don't:

- **Don't** add radius, shadow, transition, or animation.
- **Don't** use amber as a section fill, a link color, or body text.
- **Don't** invent a second rule weight. The dashed perforation is the only exception, and it stays 1px.
- **Don't** put filled values in the mono. The mono marks keys and blanks.
