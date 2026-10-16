# Website distribution

Build from the repository with `python3 scripts/build_release.py`. The source of all creative instructions is `plugins/loova/skills`; both plugin clients and downloadable ZIPs use those files.

Upload the CONTENTS of the generated versioned directory to an HTTPS release directory. Keep relative paths intact. Serve JSON as `application/json`, Markdown as UTF-8 text, and ZIPs as `application/zip` with an appropriate download filename. Do not rewrite file paths to the website HTML shell. Configure cross-origin reads only where the hosting page or loader requires them.

The directory contains ten complete skill folders, ten individual ZIPs in `downloads/`, a full bundle, `catalog.json`, `manifest.json` and `SHA256SUMS`. The separate deployment ZIP contains this entire directory. The full user bundle contains the skills, catalog and reading/deployment instructions, not nested download ZIPs or plugin installation scripts.

Use immutable caching for versioned URLs; revalidate any stable latest-release pointer. Do not overwrite published releases. The build refuses existing output paths; use a temporary output directory for repeat validation, and increment the release version for changed public content.

`manifest.json` records content sizes and SHA-256 values, excluding itself and `SHA256SUMS`. `SHA256SUMS` includes the manifest and all other release files except itself. These detect corruption but do not constitute a signed release.

Before publishing, verify downloadable hashes, MIME types, relative links and extraction layout. Test skill loading in every advertised client, production OAuth and read-only tools. Paid image/video workflow acceptance requires separate user approval. Offline package checks do not establish model quality or guarantee support for masking, identity editing, audio, lip sync or assembly.
