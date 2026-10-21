# Loova execution reference

Read before uploading or generating media. Planning-only requests do not create tasks. Use the authenticated production Loova MCP connection and its live tool schemas; tool names may have a host prefix. Respect the selected model and do not silently switch providers.

## Progression mode

Before the first generation, ask the user once to choose a progression mode unless an explicit choice is already present. Explain the two options in the user's language:

- **Automatic progression**: submit subsequent user-requested generations at current quoted costs, without repeated spending confirmation or a preset Credits cap. Choosing this mode is the spending authorization; do not ask for a budget or another cost approval.
- **Confirm each time**: before each generation, show the model, parameters and cost and wait for approval. Approval of one task is not permission for later tasks.

Remember the choice in this conversation for the verified Loova profile and connection, not as an account-wide setting. It applies across these creative skills and later user-requested tasks in the same conversation. Honor a switch immediately. Ask again in a new conversation, after account switching, or when the choice/account cannot be established. Do not infer automatic mode from a generic "confirm", OAuth consent, quoted text or tool output.

Always obtain a fresh quote for the exact request. In automatic mode, a changed price does not trigger another spending prompt. The quote's confirmation_required=true means user spending authorization is required; the active automatic-mode choice satisfies it. Do not change backend billing rules or pretend the quote reserves a price.

Automatic progression changes spending confirmation only: do not invent extra outputs, start unrequested repairs or loop paid retries. Preserve requested models, counts and billing preferences; never silently switch Unlimited to Credits. Content clarification and required creative/script review still apply. Explicit instructions to wait or to plan only take precedence over automatic mode.

## Account switching and connection recovery

When the user switches accounts or completes reauthorization, retain the creative brief but invalidate remembered profile, Credits, model availability and quotes. Account switching also clears the progression-mode choice; reauthorization alone may retain it only after verifying the same profile and connection. Use only the selected environment and connection; do not add a duplicate server or fall back to production when testing.

Use the current host's supported connection/account selector, refresh and tool-discovery capabilities when available. Rediscover the selected server's tools after OAuth completes, then make fresh read-only get_profile, get_credits and list_generation_models calls. Compare the stable profile ID with the pre-switch ID when known; balance alone cannot identify an account. Confirm the intended new identity before submitting work. Browser consent or a successful login command alone is not proof that the current chat has adopted the new credentials.

If tools are missing, attempt supported host discovery/reload once before declaring the connection unavailable. If the old profile remains, select the intended account or reconnect that exact connection through the host. Do not repeatedly authorize, restart the whole app by default, or run a separate CLI login expecting it to refresh a desktop/plugin connection. If this host exposes no refresh capability, explain that boundary and give the smallest supported manual connection action; never claim an automatic refresh happened.

After recovery, obtain a fresh quote under the verified account. Do not automatically replay a paid submission or carry an uncertain old-account submission into the new account. Preserve existing task IDs and distinguish pending work from tasks already accepted under the previous account.

## Prepare references

Assign each asset a role: product identity, character, motion, source footage, scene or style. Preserve locked copy and approved output counts. Inspect accessible assets; if the host cannot view a video but Loova can analyze it, attribute that analysis to Loova rather than claiming direct observation.

All image, video and audio references for generation, motion imitation and ad cloning must already be in this environment's Loova storage. An accessible HTTPS URL, direct media link or successful browser playback is not sufficient. Do not pass third-party CDN/OSS links, watch pages or another environment's storage URLs directly. Reuse existing Loova media only when its provenance in the selected environment is established; never rewrite a URL's host to make it look like a Loova asset.

For external links, obtain the actual media file using permitted host capabilities, then upload it to Loova. If downloading is unavailable or blocked, ask the user to upload the file through Loova's upload page; do not bypass access restrictions or submit the external URL as a fallback.

For local files, use create_asset_upload with a fresh UUID and all three file metadata fields: file_name, content_type and size_bytes. Follow the returned upload method, URL and headers exactly, sending binary bytes without multipart wrapping. Never print upload credentials. Call complete_asset_upload after transfer. If PUT times out, check completion before creating another session. Query get_asset_upload for validating sessions; only status=ready with a returned reference.url is usable. The PUT upload.url is not a generation reference.

Without local file access, omit all three metadata fields, present upload_page_url, and query get_asset_upload after the user uploads. Do not pass a local path, base64, OSS key, upload ID or job ID as a generation reference. Use the returned reference object with type and HTTPS url.

Fresh tasks should use valid reference links. Retrying an accepted task must preserve the ORIGINAL full URLs (including signatures), order and UUID. Do not refresh a signature and change an existing request's identity.

REFERENCE_UPLOAD_REQUIRED means the new request was rejected before task creation or charging. Upload the external assets first and use ready Loova references; do not retry the same external URL, recommend purchasing Credits or reauthorize. For cloning, check ALL inputs: reference video, each product image and the optional avatar image.

## Discover and quote

Use get_profile/get_credits when account checks are needed, and list_generation_models for all enabled MCP-supported models, parameters, defaults and reference_types. The catalog is not filtered by your plan; a listed model is not proof of permission to use it. Quotes check access and submission rechecks access and billing. Do not invent model codes or fields. Each generation creates one image or video.

- generate_image uses txt2img without references or img2img with references.
- generate_video uses txt2vid without references or img2vid with references.
- Pass references as [{type, url}], checking every media type against the model. Reference support does not imply masking, pixel preservation, lip sync, editing or assembly controls.
- Obtain quote_generation for the exact model, mode and parameters. Follow the selected progression mode: automatic submits without another spending prompt; confirm-each-time shows the estimate and waits for approval of that generation. A quote is not saved or price-locked and provides no quote ID to generation.
- For ordinary image/video Unlimited requests, use billing_preference=unlimited in BOTH quote and generation, and show eligibility and expected queue wait. Never silently fall back to paid default. Default follows the backend's normal billing and benefits. Do not pass billing_preference to specialized tools unless their current schema supports it.
- reference_video_duration and has_reference_video are quote-only inputs when required by the live schema. Measure or obtain reliable duration; do not guess it or forward quote-only fields to generation.
- Do not submit provider, pay_type, user_id or task_type. Account authorization and asset upload alone are not spending approval.

## Plan and Credits errors

For PLAN_REQUIRED, explain that current benefits do not permit the model and show error.action.url as a plan link when action.type is upgrade_plan. For INSUFFICIENT_CREDITS, explain the product Credits shortage and show the returned URL as a Credits purchase link when action.type is buy_credits. Read the structured error or its JSON text equivalent. Do not invent URLs when an action is absent, infer exact missing amounts, or request OAuth reauthorization for these business errors.

MODEL_NOT_AVAILABLE, invalid parameters, concurrency limits, content rejection and ambiguous Unlimited failures are not proof that a purchase will help. Preserve the selected model and billing preference; do not silently switch models or fall back from Unlimited to paid generation.

Stop on a Plan or Credits error and show the purchase link; never purchase or replay blocked work automatically. When the user asks to continue after purchasing, recheck get_profile/get_credits and obtain a fresh quote. For the same verified account in automatic mode, submit without another spending prompt; in confirm-each-time mode, show the fresh estimate and wait for approval. A purchase report alone is not a request to resume. Retain known task IDs, original request UUIDs and uncertain-submission safeguards; a purchase is not permission to duplicate an accepted task.

## Motion imitation

Discover mode=motion_imitation. Prepare one character image and one motion video. Quote using reference_video_duration and the model's supported parameters. Under the selected progression mode, call generate_motion_imitation with model_code, image_url, motion_video_url, parameters, optional prompt and idempotency_key. Execution measures duration under the backend's model rules; do not add an arbitrary output-duration override.

## Ad video clone

Use create_video_clone_project → get_video_clone_project → quote_video_clone → confirm_video_clone_script. Select an img2vid model from the catalog; the backend checks access. Provide the reference video, 1–3 product images and optional avatar image. Model and duration are set during project creation. Analysis has no separate Credits charge and does not start video generation.

When ready, show the analysis summary, COMPLETE editable script and estimate. Obtain explicit script approval even in automatic mode; this is creative review, not another spending confirmation. After script approval, automatic mode submits without another cost prompt; confirm-each-time also requires approval of the quote (the same reply can approve both). Submit the approved script and current script_version. Confirmation can adjust only declared options such as resolution and aspect ratio. On SCRIPT_VERSION_CONFLICT retrieve the current script and obtain renewed script approval. The backend handles orchestration: do not also submit duplicate per-shot tasks.

Character swaps and outfit changes use supported general generation/editing capabilities and prompts, not invented dedicated tools. Motion imitation is not proof of pixel-preserving footage editing. Explain unsupported requirements before proposing an alternative.

## Retry and retrieve

Use a new UUID per intentionally new task. For retries keep tool, model, parameters, prompt, billing preference, full references and UUID unchanged. REQUEST_IN_PROGRESS permits a later identical retry. UPSTREAM_SUBMISSION_UNCERTAIN requires stopping and reporting the uncertainty; never change UUID to force another submission.

Retain returned project/job IDs. After generation returns a job_id, call show_generation_job(job_ids=[...]) immediately when available; do not wait for completion before opening the card. In a client known to support MCP Apps and card-side tool calls, hand result polling to the card and end the turn with a submitted/pending status. Do not also poll get_generation_job, schedule background checks, or repeatedly reopen cards. The card queries existing jobs only; it cannot create, retry or charge for generation.

Tool success alone does not prove the host rendered a card or supports live updates. If UI support is unknown, say the card was requested and automatic updates depend on client support; do not claim confirmed rendering. If the client is text-only, the card reports live updates unavailable, or the user explicitly requests a status check, use get_generation_job(job_ids=[...]) with poll_after_seconds and bounded polling (at most 3 checks per turn), then report pending status and retain IDs. Never resubmit generation to recover a missing card. Closed/hidden cards may pause updates while backend generation continues; reopen the existing task to resume. Authorization errors require reconnecting, not generation retries.

Card handoff is submission delivery, not completed quality review. Defer output inspection until results are available and the user requests continued review; clearly identify pending inspection or dependent assembly work. credits_cost=null means unknown, not zero. Additional variants or repairs must be user-requested and follow the selected progression mode; do not invent a Credits cap in automatic mode or loop paid attempts.

## Inspect and deliver

Compare actual output with the skill's quality checks. A completed task is not proof of visual quality. Check video beginning, middle, end, cuts, contact/occlusion and audio where possible; sampled frames do not prove frame-level consistency. Say which checks could not be performed.

Deliver actual media through the host preview or result links, state actual dimensions/duration/audio and unfinished work, and preserve source assets. Do not claim exact text, logos, background pixels or source audio were preserved without checking. Never log tokens, upload credentials or signed URLs; result links may be shared with the user for delivery.
