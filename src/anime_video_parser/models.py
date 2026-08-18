from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal


VideoFormat = Literal["hls", "mp4", "unknown"]


@dataclass(frozen=True)
class QualityVariant:
    url: str
    quality: int | None = None
    format: VideoFormat = "unknown"
    label: str = ""
    source: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class EpisodeLinks:
    provider: str
    anime_id: str
    episode: int
    translation_id: str = ""
    translation_name: str = ""
    variants: list[QualityVariant] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def add(self, variant: QualityVariant) -> None:
        if any(item.url == variant.url for item in self.variants):
            return
        self.variants.append(variant)
        self.variants.sort(key=lambda item: item.quality or 0, reverse=True)

    def to_dict(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "anime_id": self.anime_id,
            "episode": self.episode,
            "translation_id": self.translation_id,
            "translation_name": self.translation_name,
            "variants": [item.to_dict() for item in self.variants],
            "metadata": self.metadata,
        }


@dataclass
class ParseResult:
    provider: str
    episodes: list[EpisodeLinks] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "episodes": [item.to_dict() for item in self.episodes],
            "warnings": self.warnings,
        }

