import json
from pathlib import Path

import pytest

from anime_video_parser.providers.anilibria import parse_anilibria_payload
from anime_video_parser.providers.animelib import parse_animelib_payload
from anime_video_parser.providers.kodik import parse_kodik_payload


ROOT = Path(__file__).parents[1]


@pytest.mark.parametrize(
    ('provider', 'parser'),
    [
        ('kodik', parse_kodik_payload),
        ('anilibria', parse_anilibria_payload),
        ('animelib', parse_animelib_payload),
    ],
)
def test_redacted_examples_are_parseable(provider, parser):
    fixture_path = ROOT / 'examples' / '{}-episode.json'.format(provider)
    payload = json.loads(fixture_path.read_text(encoding='utf-8'))

    result = parser(payload, anime_id='fixture-anime', episode=1)

    assert result.provider == provider
    assert result.warnings == []
    assert len(result.episodes) == 1
    assert result.episodes[0].variants
    assert all(item.url.startswith('https://') for item in result.episodes[0].variants)
