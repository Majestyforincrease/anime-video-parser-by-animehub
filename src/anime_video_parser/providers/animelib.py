from __future__ import annotations

from typing import Any

from ..models import EpisodeLinks, ParseResult, QualityVariant
from ..security import is_allowed_url
from .base import looks_like_url, quality_from_text, walk_strings


ANIMELIB_VIDEO_HOSTS = {"video1.cdnlibs.org", "cdnlibs.org"}


def parse_animelib_payload(
    payload: Any,
    *,
    anime_id: str,
    episode: int,
    translation_id: str = "",
    translation_name: str = "",
) -> ParseResult:
    """Extract direct Animelib MP4 quality variants from a decoded response."""
    result = ParseResult(provider="animelib")
    links = EpisodeLinks(
        provider="animelib",
        anime_id=str(anime_id),
        episode=max(1, int(episode)),
        translation_id=str(translation_id or ""),
        translation_name=str(translation_name or ""),
    )
    for path, value in walk_strings(payload):
        if not looks_like_url(value):
            continue
        if not is_allowed_url(
            value,
            hosts=ANIMELIB_VIDEO_HOSTS,
            path_fragment="/uploads/converted_videos/",
            require_mp4=True,
        ):
            continue
        links.add(QualityVariant(
            url=value,
            quality=quality_from_text(path, value),
            format="mp4",
            label=path.rsplit(".", 1)[-1] if path else "mp4",
            source="animelib",
        ))
    if not links.variants:
        result.warnings.append("No trusted Animelib MP4 URLs were found in the payload.")
    result.episodes.append(links)
    return result

