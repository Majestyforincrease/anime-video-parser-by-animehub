from anime_video_parser.security import classify_format, is_allowed_url


def test_animelib_url_allowlist():
    assert is_allowed_url(
        "https://video1.cdnlibs.org/uploads/converted_videos/anime/1/player/1/file_1080.mp4",
        hosts={"video1.cdnlibs.org", "cdnlibs.org"},
        path_fragment="/uploads/converted_videos/",
        require_mp4=True,
    )
    assert not is_allowed_url(
        "https://example.com/uploads/converted_videos/anime/file_1080.mp4",
        hosts={"video1.cdnlibs.org", "cdnlibs.org"},
        path_fragment="/uploads/converted_videos/",
        require_mp4=True,
    )


def test_credentials_and_plain_http_are_rejected():
    hosts = {"video1.cdnlibs.org"}
    assert not is_allowed_url("http://video1.cdnlibs.org/file.mp4", hosts=hosts)
    assert not is_allowed_url("https://user:pass@video1.cdnlibs.org/file.mp4", hosts=hosts)


def test_format_detection():
    assert classify_format("https://example.test/episode/master.m3u8") == "hls"
    assert classify_format("https://example.test/episode_1080.mp4") == "mp4"

