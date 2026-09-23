from __future__ import annotations

"""Inspect the tiny educational tokenizer used by this repository.

The tokenizer itself lives in ``lab.embeddings`` so later lessons can reuse it.
This script adds explanations around that function: token positions, character
spans, local demonstration IDs, statistics, and comparisons.

The output is intentionally educational. The toy IDs are not IDs from a real
LLM vocabulary; a production model must use its own tokenizer and vocabulary.
"""

import argparse
import json
import re
from dataclasses import asdict, dataclass

from lab.embeddings import tokenize


# Keep this pattern aligned with lab.embeddings.tokenize. ``finditer`` gives us
# character spans while the shared function remains the source of token values.
_TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_]+|[^\w\s]")


@dataclass(frozen=True)
class TokenDetail:
    """The useful observations for one token in the original input."""

    index: int
    token: str
    start: int
    end: int
    toy_id: int | None = None


def inspect_text(text: str, include_ids: bool = False) -> list[TokenDetail]:
    """Return tokens with their positions in *text*.

    ``tokenize`` is deliberately used for the token values so this explorer
    tests the same public function used by the rest of the lab. The regular
    expression supplies offsets, which the small tokenizer API does not expose.
    """
    tokens = tokenize(text)
    matches = list(_TOKEN_PATTERN.finditer(text.lower()))

    if len(tokens) != len(matches):
        raise RuntimeError("Tokenizer pattern and tokenize() returned different lengths")

    # A sorted vocabulary gives repeatable IDs within this example. Real IDs
    # come from a model-specific, trained vocabulary and are not recreated here.
    vocabulary = {token: index for index, token in enumerate(sorted(set(tokens)))}
    return [
        TokenDetail(
            index=index,
            token=token,
            start=match.start(),
            end=match.end(),
            toy_id=vocabulary[token] if include_ids else None,
        )
        for index, (token, match) in enumerate(zip(tokens, matches))
    ]


def print_table(text: str, details: list[TokenDetail], include_ids: bool) -> None:
    """Print a readable token table for one input string."""
    print(f"Input: {text!r}")
    if not details:
        print("(no tokens: the input contains only whitespace)")
        return

    id_header = " toy_id" if include_ids else ""
    print(f"{'#':>3} {'token':<20} {'characters':<12}{id_header}")
    print("-" * (42 + (8 if include_ids else 0)))
    for detail in details:
        span = f"[{detail.start}:{detail.end}]"
        token = repr(detail.token)
        toy_id = f" {detail.toy_id:>6}" if include_ids else ""
        print(f"{detail.index:>3} {token:<20} {span:<12}{toy_id}")


def print_stats(text: str, details: list[TokenDetail]) -> None:
    """Print simple counts that make tokenization measurable."""
    characters_without_spaces = len("".join(text.split()))
    average = characters_without_spaces / len(details) if details else 0.0
    print("\nStatistics")
    print(f"  characters:       {len(text)}")
    print(f"  non-whitespace:   {characters_without_spaces}")
    print(f"  tokens:           {len(details)}")
    print(f"  unique tokens:    {len({detail.token for detail in details})}")
    print(f"  characters/token:  {average:.2f}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Explore token boundaries in the lab's tiny educational tokenizer."
    )
    parser.add_argument(
        "text",
        nargs="*",
        help="text to inspect; words are joined with spaces (default: Hello AI)",
    )
    parser.add_argument(
        "--ids",
        action="store_true",
        help="show local demonstration IDs (not real model vocabulary IDs)",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="show token and character statistics",
    )
    parser.add_argument(
        "--compare",
        action="append",
        default=[],
        metavar="TEXT",
        help="inspect another complete string; repeat this option to compare inputs",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit machine-readable JSON instead of the table",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    first_text = " ".join(args.text) if args.text else "Hello AI"
    inputs = [first_text, *args.compare]
    inspected = [(text, inspect_text(text, include_ids=args.ids)) for text in inputs]

    if args.json:
        payload = [
            {"text": text, "tokens": [asdict(detail) for detail in details]}
            for text, details in inspected
        ]
        print(json.dumps(payload[0] if len(payload) == 1 else payload, indent=2))
        return

    for number, (text, details) in enumerate(inspected):
        if number:
            print("\nComparison")
        print_table(text, details, include_ids=args.ids)
        if args.stats:
            print_stats(text, details)


if __name__ == "__main__":
    main()
