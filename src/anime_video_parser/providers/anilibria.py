from __future__ import annotations

from typing import Any

from ..models import EpisodeLinks, ParseResult, QualityVariant
from ..security import classify_format, is_allowed_url
from .base import looks_like_url, quality_from_text, walk_strings


ANILIBRIA_HOSTS = {"anilibria.tv", "anilibria.top", "aniliberty.top", "aniliberty.pro"}


def parse_anilibria_payload(
    payload: Any,
    *,
    anime_id: str,
    episode: int,
    translation_id: str = "",
    translation_name: str = "",
) -> ParseResult:
    """Extract HLS or MP4 variants from common AniLibria release shapes."""
    result = ParseResult(provider="anilibria")
    links = EpisodeLinks(
        provider="anilibria",
        anime_id=str(anime_id),
        episode=max(1, int(episode)),
        translation_id=str(translation_id or ""),
        translation_name=str(translation_name or ""),
    )
    for path, value in walk_strings(payload):
        if not looks_like_url(value):
            continue
        if not is_allowed_url(value, hosts=ANILIBRIA_HOSTS):
            continue
        links.add(QualityVariant(
            url=value,
            quality=quality_from_text(path, value),
            format=classify_format(value),
            label=path.rsplit(".", 1)[-1] if path else "stream",
            source="anilibria",
        ))
    if not links.variants:
        result.warnings.append("No trusted AniLibria video URLs were found in the payload.")
    result.episodes.append(links)
    return result

