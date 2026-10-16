# Loova execution reference

Read before uploading or generating media. Planning-only requests do not create tasks. Use the authenticated production Loova MCP connection and its live tool schemas; tool names may have a host prefix. Respect the selected model and do not silently switch providers.

## Prepare references

Assign each asset a role: product identity, character, motion, source footage, scene or style. Preserve locked copy and approved output counts. Inspect accessible assets; if the host cannot view a video but Loova can analyze it, attribute that analysis to Loova rather than claiming direct observation.

For local files, use create_asset_upload with a fresh UUID and all three file metadata fields: file_name, content_type and size_bytes. Follow the returned upload method, URL and headers exactly, sending binary bytes without multipart wrapping. Never print upload credentials. Call complete_asset_upload after transfer. If PUT times out, check completion before creating another session. Query get_asset_upload for validating sessions; only ready results provide usable references.

Without local file access, omit all three metadata fields, present upload_page_url, and query get_asset_upload after the user uploads. Do not pass a local path, base64, OSS key, upload ID or job ID as a generation reference. Use the returned reference object with type and HTTPS url.

Fresh tasks should use valid reference links. Retrying an accepted task must preserve the ORIGINAL full URLs (including signatures), order and UUID. Do not refresh a signature and change an existing request's identity.

## Discover and quote

Use get_profile/get_credits when account checks are needed, and list_generation_models for the user's available models, parameters, defaults and reference_types. Do not invent model codes or fields. Each generation creates one image or video.

- generate_image uses txt2img without references or img2img with references.
- generate_video uses txt2vid without references or img2vid with references.
- Pass references as [{type, url}], checking every media type against the model. Reference support does not imply masking, pixel preservation, lip sync, editing or assembly controls.
- Obtain quote_generation for the exact model, mode and parameters. Present the estimate and obtain explicit approval before generation; sufficient prior approval for that exact scope need not be repeated. A quote is not saved or price-locked and provides no quote ID to generation.
- For ordinary image/video Unlimited requests, use billing_preference=unlimited in BOTH quote and generation, and show eligibility and expected queue wait. Never silently fall back to paid default. Default follows the backend's normal billing and benefits. Do not pass billing_preference to specialized tools unless their current schema supports it.
- reference_video_duration and has_reference_video are quote-only inputs when required by the live schema. Measure or obtain reliable duration; do not guess it or forward quote-only fields to generation.
- Do not submit provider, pay_type, user_id or task_type. Account authorization and asset upload alone are not spending approval.

## Motion imitation

Discover mode=motion_imitation. Prepare one character image and one motion video. Quote using reference_video_duration and the model's supported parameters. After approval call generate_motion_imitation with model_code, image_url, motion_video_url, parameters, optional prompt and idempotency_key. Execution measures duration under the backend's model rules; do not add an arbitrary output-duration override.

## Ad video clone

Use create_video_clone_project → get_video_clone_project → quote_video_clone → confirm_video_clone_script. Select a permitted img2vid model and provide the reference video, 1–3 product images and optional avatar image. Model and duration are set during project creation. Analysis has no separate Credits charge and does not start video generation.

When ready, show the analysis summary, COMPLETE editable script and estimate. Submit the user's approved script and current script_version only after explicit confirmation. Confirmation can adjust only declared options such as resolution and aspect ratio. On SCRIPT_VERSION_CONFLICT retrieve the current script and obtain renewed approval. The backend handles orchestration: do not also submit duplicate per-shot tasks.

Character swaps and outfit changes use supported general generation/editing capabilities and prompts, not invented dedicated tools. Motion imitation is not proof of pixel-preserving footage editing. Explain unsupported requirements before proposing an alternative.

## Retry and retrieve

Use a new UUID per intentionally new task. For retries keep tool, model, parameters, prompt, billing preference, full references and UUID unchanged. REQUEST_IN_PROGRESS permits a later identical retry. UPSTREAM_SUBMISSION_UNCERTAIN requires stopping and reporting the uncertainty; never change UUID to force another submission.

Retain returned project/job IDs. Query get_generation_job for generation results and follow poll_after_seconds with bounded polling. If still running, report status and resume later. credits_cost=null means unknown, not zero. Additional variants or repairs need remaining approval and budget; do not loop paid attempts.

## Inspect and deliver

Compare actual output with the skill's quality checks. A completed task is not proof of visual quality. Check video beginning, middle, end, cuts, contact/occlusion and audio where possible; sampled frames do not prove frame-level consistency. Say which checks could not be performed.

Deliver actual media through the host preview or result links, state actual dimensions/duration/audio and unfinished work, and preserve source assets. Do not claim exact text, logos, background pixels or source audio were preserved without checking. Never log tokens, upload credentials or signed URLs; result links may be shared with the user for delivery.
