from __future__ import annotations

from typing import Any

import requests


class HttpClient:
    """Small explicit HTTP helper; callers choose URLs and timeouts."""

    def __init__(self, *, timeout: float = 15, user_agent: str = "anime-video-parser-kit/0.1"):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent, "Accept": "application/json"})

    def get_json(self, url: str, *, params: dict[str, Any] | None = None) -> Any:
        response = self.session.get(url, params=params or {}, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

