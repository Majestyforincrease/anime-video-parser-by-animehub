# Anime Video Link Parser Kit

Anime Video Link Parser Kit is an open-source Python library and CLI for
normalizing anime episode video links from Kodik, AniLibria and
AniLib/Animelib responses.

The project provides a common model for episodes, translations, HLS playlists
and direct MP4 quality variants. It keeps provider-specific parsing behind a
stable API so anime catalogs, media indexers, research tools and personal
viewing applications can integrate multiple providers without duplicating
parsing logic.

The library validates schemes, hosts, paths and redirects before returning
video URLs. It does not bypass authentication or access controls, scrape
private browser sessions, or redistribute media. It parses provider responses
that the calling application is authorized to use.

The project is being developed as a genuine public open-source utility with
tests, redacted fixtures, documentation, CI and a contributor-friendly
workflow. Contributions and corrections are welcome through Pull Requests.
Please open an issue first for substantial changes, include tests for parser
behavior, and never submit private tokens, cookies or unreleased media links.

The project is deliberately split into two concerns:

- provider adapters turn upstream JSON or HTML-derived data into a common model;
- the resolver validates redirects and keeps unsafe or unrelated URLs out of
  the result.

This repository does not bypass authentication, defeat access controls, or
redistribute copyrighted media. It parses links returned by an account or API
that the caller is authorized to use. Check each provider's terms and the
rights for the content you handle.

## Quick start

```bash
python -m venv .venv
python -m pip install -e .
python -m anime_video_parser --help
```

Parse a saved provider payload:

```bash
python -m anime_video_parser \
  --provider animelib \
  --payload examples/animelib-episode.json \
  --anime-id 20 \
  --episode 1
```

The output is JSON with normalized `hls` and `mp4` variants, quality labels,
provider metadata and validation warnings.

## Supported providers

### Kodik

The adapter accepts a decoded provider response and extracts translation
entries, HLS links and quality variants. It does not contain a hard-coded
token or scrape a browser session. This keeps credentials and upstream policy
outside the parser package.

### AniLibria

The adapter handles the common release/player shapes used by AniLibria APIs:
HLS playlists, episode maps and quality dictionaries. It preserves the
release title and translation/team metadata so callers can select a dub.

### AniLib / Animelib

The adapter recognizes direct MP4 quality URLs from the CDN path used by
Animelib and rejects non-video hosts, credentials in URLs and untrusted
redirects.

## Design notes

The normalized model is intentionally independent from Flask, a database or a
particular anime catalog. A web application can persist the result, while a
CLI or worker can consume it directly. Provider HTTP calls are not performed
implicitly by parsing functions; callers pass already-fetched payloads or use
the small HTTP helper explicitly.

## Tests

```bash
python -m pytest
```

The tests focus on URL validation, quality normalization and provider payload
shapes. Add recorded, redacted fixtures for any upstream response that is
stable enough to test.

## Contributing

Bug reports, provider fixtures, documentation fixes and implementation
improvements are welcome. All changes must be proposed through a fork and a
Pull Request; direct pushes to the default branch are not part of the project
workflow. See [CONTRIBUTING.md](CONTRIBUTING.md) for the review checklist and
the rules for safe, reproducible fixtures.

## Project status

This is an early, actively maintained toolkit. Provider response formats can
change without notice, so integrations should pin versions, handle validation
warnings and keep their own fallback behavior.

## License

Released under the MIT License. See [LICENSE](LICENSE).
