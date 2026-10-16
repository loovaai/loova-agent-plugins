---
name: loova-mimic-motion
description: "Make a target character perform movement from a reference video with Loova, separating identity, body motion, camera, and environment. Use for reference-motion transfer or motion plans; use source-video identity editing when the original scene must remain unchanged."
metadata:
  version: "2.1.0"
  brand: "Loova"
  category: "video-creation"
---

# Mimic Motion

Extract recognizable movement for a target character without unintentionally copying the source person's identity, setting, or camera.

## Reference roles

Require a target character image and an accessible motion video. Inspect target anatomy, clothing, and usable joint range. Identify the performer in multi-person footage. Adapt stride and amplitude for different body proportions while preserving the motion's intent rather than forcing an incompatible skeleton.

The character image provides identity and specified appearance; the motion video provides action sequence, body phase, speed, and contact. Neither automatically provides the new scene or camera. If the user needs the original scene and camera unchanged, treat the task as source-video identity replacement instead.

## Extract the motion

1. Identify preparation, initiation, peak or contact, absorption, and recovery with visible time points and support feet. For dance, inspect weight and limb phase; for handling, inspect hands and objects; for jumps, inspect takeoff and landing.
2. Separate camera and body movement. A pan is not body translation, and a zoom is not forward movement by the character.
3. Identify hidden or ambiguous gestures rather than treating them as observed. A text description permits a text-based motion plan, not a claim of extracted trajectories.
4. Build a compact beat map: time range, pose, support or contact, direction, relative speed, and next state. Use meaningful phases rather than unnecessary frame-by-frame lists.

## Transfer and execute

1. Retarget for the character's proportions, prioritizing direction, timing, balance changes, and recognizable poses.
2. Frame the new scene so important limbs and contact points remain visible. Use a clear full-body view where useful; do not hide errors behind rapid camera movement.
3. Preserve specified rhythm. Loova's dedicated motion tool derives duration from the reference and model rules; do not pass an arbitrary duration override. If retiming is requested, explain any required supported source-editing step before creating the task.
4. Read [Loova execution](references/execution.md). Verify motion-reference, pose-control, or retargeting support. Text-to-video alone may approximate an action but is not proof of precise reference following.
5. Join segments at stable poses or compatible phases. Keep left/right direction and endpoint continuity; avoid arbitrary cuts halfway through landing or rotation.

## Quality and delivery

Check action order, limb direction, phase, support, contact, anatomy, and clothing stability. Two clips both containing dance do not establish motion correspondence. Inspect foot sliding, penetration, and recovery. Check that source camera, background, and identity have not leaked into the result.

Repair the specific phase, support, or amplitude issue and reduce unnecessary camera movement. Do not disguise errors through slow motion or occlusion. Deliver the requested video or beat plan, explaining approximation and inspection limits without claiming frame-level matching from sampled checks.
