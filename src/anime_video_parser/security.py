from __future__ import annotations

from urllib.parse import urlsplit


def is_allowed_url(
    value: str,
    *,
    hosts: set[str],
    path_fragment: str = "",
    require_mp4: bool = False,
) -> bool:
    """Accept only HTTPS URLs for explicitly trusted provider hosts."""
    try:
        parts = urlsplit(str(value or "").strip())
        port = parts.port
    except ValueError:
        return False
    host = (parts.hostname or "").lower().rstrip(".")
    if parts.scheme != "https" or parts.username or parts.password or port not in (None, 443):
        return False
    if host not in hosts and not any(host.endswith(f".{item}") for item in hosts):
        return False
    if path_fragment and path_fragment not in parts.path:
        return False
    if require_mp4 and not parts.path.lower().endswith(".mp4"):
        return False
    return True


def classify_format(url: str) -> str:
    path = urlsplit(url).path.lower()
    if path.endswith(".m3u8") or ".m3u8?" in url.lower():
        return "hls"
    if path.endswith(".mp4") or ".mp4?" in url.lower():
        return "mp4"
    return "unknown"

