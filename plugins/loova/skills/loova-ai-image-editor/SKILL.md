---
name: loova-ai-image-editor
description: "Edit a supplied image with Loova, changing specified objects, backgrounds, details, or visual style while preserving the agreed subject and composition. Use for image edits; not for creating an unrelated image or only resizing a layout."
metadata:
  version: "2.1.3"
  brand: "Loova"
  category: "image-creation"
---

# AI Image Editor

Make a bounded change to an existing image. Identify the edit area and protected content before choosing a method.

## Define the edit

Require the actual source image. Identify the target object or region, desired change, and protected subject, text, and layout. If a phrase such as "make this red" has several plausible targets, clarify the target rather than redesigning the image.

Use local editing for object removal, recoloring, and small defects; foreground protection and compositing for background changes; or a global style transformation with identity and composition constraints for restyling.

## Workflow

1. Inspect boundaries, occlusion, shadows, and reflections. Removing an object may require filling hidden background; a plausible reconstruction is not proof of the original scene.
2. Record what may change and what must remain. A watercolor restyle may change brushwork and material rendering without changing identity, product structure, or object count.
3. Use the smallest effective editing region. Update affected shadows and reflections together with the object. For a background replacement, distinguish surface color from environmental color spill.
4. Read [Loova execution](references/execution.md). Use a tool that accepts the required source image and edit controls. Protect exact pixels through masking or compositing when available; do not claim pixel preservation for a full-image regeneration.
5. Compare source and output. Inspect the intended region and protected areas, including text, logos, transparent edges, hair, fine openings, perspective, and contact shadows.

## Repair and delivery

Repair seams at the seam, lighting at the affected light boundary, and identity drift from the original source. Do not keep repainting a drifted result. If the available tools cannot meet a preservation requirement, explain the specific limitation and offer a suitable alternative.

Return the edited image and one sentence describing the change. Keep the source and identify meaningful differences between requested variants. If execution is unavailable, label the output as an edit plan, not a completed edit.
