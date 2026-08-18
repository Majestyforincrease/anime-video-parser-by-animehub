from __future__ import annotations

from collections.abc import Iterator
from typing import Any
from urllib.parse import urlsplit


def walk_strings(value: Any) -> Iterator[tuple[str, str]]:
    """Yield string leaves with their dotted payload path."""
    def visit(item: Any, path: str) -> Iterator[tuple[str, str]]:
        if isinstance(item, dict):
            for key, nested in item.items():
                next_path = f"{path}.{key}" if path else str(key)
                yield from visit(nested, next_path)
        elif isinstance(item, list):
            for index, nested in enumerate(item):
                yield from visit(nested, f"{path}.{index}" if path else str(index))
        elif isinstance(item, str):
            yield path, item.strip()

    yield from visit(value, "")


def quality_from_text(*values: str) -> int | None:
    import re

    text = " ".join(str(value or "") for value in values)
    matches = re.findall(r"(?<!\d)(\d{3,4})(?:p|k)?(?!\d)", text.lower())
    candidates = [int(item) for item in matches if int(item) in {240, 360, 480, 489, 576, 720, 1080, 1440, 2160, 2160}]
    return max(candidates) if candidates else None


def looks_like_url(value: str) -> bool:
    parts = urlsplit(value)
    return parts.scheme in {"http", "https"} and bool(parts.netloc)

