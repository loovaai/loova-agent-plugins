---
name: loova-product-video-maker
description: "Turn product images into showcase videos with Loova, coordinating camera motion, product motion, and shot continuity. Use for image-to-product-video work or storyboards; not for presenter ads, reference-ad recreation, or character motion transfer."
metadata:
  version: "2.1.4"
  brand: "Loova"
  category: "video-creation"
---

# Product Video Maker

Give a static product image a clear showcase purpose. Motion should reveal silhouette, material, structure, or a supported use, rather than causing arbitrary floating or deformation.

## Inputs and motion choices

Inspect product images, available angles, use, and requested duration, format, and sound. Confirm matching SKUs before assigning references to full views, details, and scenes. A front view is not evidence of a real back or internal structure.

If a generic short showcase has no duration, propose approximately ten seconds, subject to the selected tool's supported durations. Preserve explicit timing and silence requirements. Do not add a presenter or voiceover by default.

Choose a hero shot for silhouette and material, a detail shot for documented features, a context shot for plausible use, or a purposeful multi-shot sequence. Prefer gentle camera travel or limited rotation when available references cannot support revealing unknown surfaces.

## Workflow

1. Identify the main feature and locked structure. Do not invent waterproofing, disassembly, or other functional demonstrations from appearance.
2. Assign motion to the camera, product, or environment. Simple showcases usually need one main source of motion; combine them only when useful and supported.
3. Define the start and end state. Obtain more angles or choose limited movement before exposing an unknown side. Do not call a partial turn a verified 360-degree reconstruction.
4. Write shot cards with duration, reference roles, framing, main motion, amplitude, speed, endpoint, and audio. For multiple shots, establish shared product references and keyframes when supported.
5. Read [Loova execution](references/execution.md). Confirm image references, frame controls, duration, and assembly support. Prompt wording is not proof that a model locks those controls precisely.

## Quality and delivery

Inspect the opening, middle, ending, and cuts for swelling, melting, changing parts, and unstable logos. Check reflections, contact shadows, background parallax, and hand contact. Reuse verified product states. Reduce excessive motion when it causes identity drift rather than repeatedly regenerating a broken subject.

Return actual duration, aspect ratio, and audio status with the video. Distinguish independent clips from a fully assembled film. For an eight-second perfume push-in, avoid adding cap removal, spraying, or an unverified rear view.
