from anime_video_parser.providers.animelib import parse_animelib_payload
from anime_video_parser.providers.anilibria import parse_anilibria_payload
from anime_video_parser.providers.kodik import parse_kodik_payload


def test_animelib_quality_map_is_normalized():
    result = parse_animelib_payload({
        "player": {
            "quality": {
                "1080": "https://video1.cdnlibs.org/uploads/converted_videos/anime/1/player/1/file_1080.mp4",
                "720": "https://video1.cdnlibs.org/uploads/converted_videos/anime/1/player/1/file_720.mp4",
            }
        }
    }, anime_id="20", episode=1)
    assert [item.quality for item in result.episodes[0].variants] == [1080, 720]


def test_untrusted_provider_urls_are_dropped():
    result = parse_kodik_payload({"url": "https://evil.example/video.m3u8"}, anime_id="20", episode=1)
    assert result.episodes[0].variants == []
    assert result.warnings


def test_anilibria_hls_is_preserved():
    result = parse_anilibria_payload({
        "release": {"player": "https://anilibria.top/episodes/20/1/master_1080.m3u8"}
    }, anime_id="20", episode=1)
    assert result.episodes[0].variants[0].format == "hls"

