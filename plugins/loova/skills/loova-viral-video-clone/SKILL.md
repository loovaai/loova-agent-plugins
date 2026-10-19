---
name: loova-viral-video-clone
description: "Adapt a reference video into a new product video with Loova, preserving the requested pacing and shot structure while using the user's product. Use for reference-led ad recreation; not for replacing only a person in the original footage."
metadata:
  version: "2.1.1"
  brand: "Loova"
  category: "video-creation"
---

# Viral Video Clone

Translate a reference video's creative structure into a video for the user's product. "Clone" describes reference-led recreation, not a guarantee of identical frames or commercial performance.

## Inputs and reference roles

Use an accessible reference video and target product information. The product image supplies identity; the video supplies the requested pacing, shot functions, camera, or editing reference. If the host cannot inspect it but Loova can, use the project's server-side analysis and attribute its source. If neither can inspect it, request an accessible copy or provide a labeled description-based plan without invented timecodes.

Establish which elements the user wants to follow. Do not import the original brand, person, distinctive copy, or soundtrack by default. Respect explicitly requested elements within the actual assets and tool capabilities.

## Workflow

1. Record observable events with time ranges: opening, product entry, action changes, demonstrations, and ending. Separate observation from inferred marketing purpose.
2. Give key shots a function, such as revealing scale, showing operation, or illustrating a supported benefit. Map that function to something the new product can actually do; rewrite incompatible actions.
3. Build a compact adaptation map: reference segment, shot function, new product action, new scene, retained rhythm, and excluded elements. Do not infer sales or conversion performance from the reference's appearance.
4. Lock the requested duration and aspect ratio. If duration changes, retain meaningful beat order and allow each action to complete instead of compressing all shots mechanically.
5. Define continuity between shots: orientation, position, hand contact, action endpoint, and transition. Write each shot as a start state, main change, end state, and reason for the cut.
6. Read [Loova execution](references/execution.md). Prefer Loova's clone project workflow: create, query analysis/script, quote, show the complete script and estimate, then confirm only after user approval. The backend orchestrates generation; do not also generate each shot separately. Use shot-by-shot regeneration only as an agreed alternative with suitable tools, not as a claim of source-footage editing.

## Quality and delivery

For multi-shot work, reuse product references and accepted shots, then assemble only with supported tools. A request for one clip must not become an unrequested campaign package.

Check that actions belong to the new product, product state remains coherent across cuts, approved claims have factual support, and the original identity or branding has not leaked through. Inspect actual timing and audio endings. Repair the specific identity, action, or cut problem within the approved budget.

Deliver the requested adaptation plan, prompts, or finished video and briefly identify the main adaptations. For example, coffee-pouring beats can become a lamp's switch-on and illumination sequence; do not make a lamp perform the reference product's physical actions.
