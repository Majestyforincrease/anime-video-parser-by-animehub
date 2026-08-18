# Provider Notes

These notes capture the integration boundaries used by the AnimeHub project
without copying its Flask application or credentials.

## Kodik

AnimeHub resolves a title and episode to a translation catalog first, then
resolves the selected translation to an HLS plan and optional quality URLs.
Keep the translation id and the expected episode range together. A translation
can cover only part of a long-running series.

The standalone adapter therefore accepts a decoded payload and retains
translation metadata. Token acquisition and upstream API policy belong in the
calling application.

## AniLibria

AnimeHub searches releases by title, verifies the release against the expected
episode count, and extracts HLS/quality URLs from the release player data.
Provider responses vary between title, release and episode endpoints, so the
adapter walks nested payloads and leaves provider-specific selection to the
caller.

## AniLib / Animelib

AnimeHub uses AniLib for direct player and quality fallbacks. Direct media URLs
are accepted only from the known CDN path under `video1.cdnlibs.org` or a
trusted `cdnlibs.org` subdomain and must end in `.mp4`. Redirects must be
validated again after every hop.

## What is intentionally out of scope

- scraping browser cookies or private sessions;
- embedding provider secrets in the repository;
- downloading or redistributing media;
- treating an arbitrary URL as a video proxy target;
- assuming one provider's response shape is stable forever.

