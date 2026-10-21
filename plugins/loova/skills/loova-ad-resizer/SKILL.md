---
name: loova-ad-resizer
description: "Adapt an existing product or ad image to requested dimensions and aspect ratios with Loova-compatible editing or deterministic resizing. Preserve product proportions, copy, and required content through containment, cropping, extension, or reflow."
metadata:
  version: "2.1.4"
  brand: "Loova"
  category: "image-creation"
---

# Ad Resizer

Adapt one creative to different placements without stretching the product or sacrificing essential information.

## Choose a method

Require the source, target dimensions or ratios, and protected content. If only a destination is supplied, use a provided template or verify its current dimensions. Carry the same source and product constraints across all requested outputs.

| Method | Use when | Preserve |
|---|---|---|
| Contain | The complete image or copy must remain visible | Proportions, with deliberate margins if needed |
| Crop | All essential content fits within a safe crop | Product, price, logo, and required disclosures |
| Extend | Additional background is needed and generation is allowed | Product identity and existing copy |
| Reflow | Elements can be rearranged for a new layout | Meaning, hierarchy, and exact content |

Prefer reflow when editable source layers exist. Do not pretend flattened text can be moved losslessly. Explain any reconstruction needed to expose covered areas or rebuild text.

## Workflow

1. Mark product, logo, price, headings, disclosures, and non-croppable regions. Identify background that can be cropped or extended.
2. Calculate each target separately. For source W x H and target w x h, contain uses min(w/W, h/H); cover-and-crop uses max(w/W, h/H). These formulas do not make a centered crop safe automatically.
3. If important content cannot fit readably, use permitted margins or reflow. Extend only the background; do not invent hidden product faces, accessories, or new claims.
4. Read [Loova execution](references/execution.md). Use a supported deterministic resize/composite path or Loova generative extension. If exact export dimensions are unsupported, report actual dimensions rather than claiming an exact-size delivery.
5. Inspect every target independently. Check required text, real pixel dimensions, product geometry, texture continuity, and any UI-safe area.

## Delivery

Return a target-to-file map with actual dimensions and the chosen method. Preserve the source. Identify unmet targets separately; do not label one square file as several different exports.
