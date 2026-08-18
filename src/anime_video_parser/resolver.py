from __future__ import annotations

from typing import Any

from .errors import UnsupportedProvider
from .models import ParseResult
from .providers import parse_anilibria_payload, parse_animelib_payload, parse_kodik_payload


def parse_provider_payload(
    provider: str,
    payload: Any,
    *,
    anime_id: str,
    episode: int,
    translation_id: str = "",
    translation_name: str = "",
) -> ParseResult:
    key = provider.strip().lower().replace("/", "")
    parser = {
        "kodik": parse_kodik_payload,
        "anilibria": parse_anilibria_payload,
        "animelib": parse_animelib_payload,
        "anilib": parse_animelib_payload,
    }.get(key)
    if parser is None:
        raise UnsupportedProvider(f"Unsupported provider: {provider}")
    return parser(
        payload,
        anime_id=anime_id,
        episode=episode,
        translation_id=translation_id,
        translation_name=translation_name,
    )

