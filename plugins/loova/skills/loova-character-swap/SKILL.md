---
name: loova-character-swap
description: "Replace a specified person or character in source footage using Loova video editing, retaining the agreed scene, motion, camera, timing, and audio. Use for identity replacement in an existing video; not for performing reference motion in a new scene."
metadata:
  version: "2.1.0"
  brand: "Loova"
  category: "video-creation"
---

# Character Swap

Replace a defined character in existing footage. The source supplies timing, movement, camera, and scene; the target image supplies identity.

## Required sources and scope

Require accessible source video and a target identity reference. Identify the target when several people are present. Clarify face-only, whole-person, clothing, or fictional-character scope when material to the result. Do not interpret a character change as permission to change voice or all styling.

Keep source audio unless the user requests otherwise. Retain clothing and prop relationships unless a full-character replacement requires a different silhouette or the user specifies another outfit. The target reference's pose and background are not automatically part of the edit.

## Workflow

1. Inspect cuts, turns, exits, rapid movement, occlusions, held objects, and interactions. Do not judge feasibility only from the opening frame.
2. Define the target and protected areas. Preserve contact points, foot placement, occlusion order, other people, background, and relevant shadows. Do not draw a replacement in front of objects that should cover it.
3. Separate source-preservation constraints from identity changes. Face-only replacement protects hair, clothing, and body. Whole-person replacement may change the silhouette without changing the original action's rhythm.
4. Read [Loova execution](references/execution.md). Require actual source-video editing or identity-replacement support. If only similar-action generation is available, offer a regeneration alternative without calling it a source-video swap.
5. For longer footage, use existing cuts or suitable segment boundaries with a consistent time map and identity reference. Check segment joins for duplicates and audio drift.
6. Reattach original audio only if the time map remains aligned; otherwise correct timing first. Treat an audio change as a separate requested edit.

## Quality and delivery

Check identity through front, side, back, and occlusion recovery. Inspect protected scenery and bystanders, held objects, crossing limbs, feet, edge blending, and shadows. Compare actual duration, cuts, frame rate, action beats, and sound sync.

Repair the affected segment or narrow the edit scope when necessary; do not change the source action to conceal a failure. Promise pixel-level preservation only when supported by the real masking or compositing path. Deliver the video with a concise scope summary and any unmet shot or synchronization requirement.
