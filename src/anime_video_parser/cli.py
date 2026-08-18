from __future__ import annotations

import argparse
import json
from pathlib import Path

from .resolver import parse_provider_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Normalize anime video links from a provider payload.")
    parser.add_argument("--provider", required=True, choices=("kodik", "anilibria", "animelib"))
    parser.add_argument("--payload", required=True, type=Path, help="JSON file returned by the provider")
    parser.add_argument("--anime-id", required=True)
    parser.add_argument("--episode", required=True, type=int)
    parser.add_argument("--translation-id", default="")
    parser.add_argument("--translation-name", default="")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    payload = json.loads(args.payload.read_text(encoding="utf-8"))
    result = parse_provider_payload(
        args.provider,
        payload,
        anime_id=args.anime_id,
        episode=args.episode,
        translation_id=args.translation_id,
        translation_name=args.translation_name,
    )
    print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    return 0

