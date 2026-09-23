from __future__ import annotations

"""Tiny embedding demo for understanding vector similarity.

This script demonstrates the core idea behind embeddings using the repository's
small educational tokenizer and hash-based vector generator. It is not a trained
model, and the values are intentionally simple enough to inspect by hand.
"""

import argparse

from lab.embeddings import cosine, embed


DEFAULT_PAIRS = [
    ("cats chase mice", "a cat hunts a mouse"),
    ("cats chase mice", "quantum physics"),
    ("the cat sat on the mat", "the cat sat on the rug"),
]


def print_pair_summary(left: str, right: str, dimensions: int = 32) -> None:
    """Show a single phrase comparison and a compact vector summary."""
    left_vector = embed(left, dimensions=dimensions)
    right_vector = embed(right, dimensions=dimensions)
    score = cosine(left_vector, right_vector)

    non_zero = sum(1 for value in left_vector if value != 0.0)
    print(f"Left:  {left!r}")
    print(f"Right: {right!r}")
    print(f"Cosine similarity: {score:.4f}")
    print(f"Dimensions: {dimensions}, non-zero entries in left vector: {non_zero}")
    print(f"Left vector sample:  {left_vector[:8]}")
    print(f"Right vector sample: {right_vector[:8]}")
    print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare toy embeddings for related and unrelated phrases."
    )
    parser.add_argument(
        "--dimensions",
        type=int,
        default=32,
        help="embedding size to use for the toy vectors",
    )
    parser.add_argument(
        "--pair",
        action="append",
        default=[],
        metavar="LEFT|RIGHT",
        help="add a custom comparison pair in the format 'left|right'; repeat for more pairs",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    pairs = []
    for raw_pair in args.pair:
        try:
            left, right = raw_pair.split("|", 1)
        except ValueError as exc:
            raise SystemExit(
                "Each --pair must be in the format 'left|right'."
            ) from exc
        pairs.append((left.strip(), right.strip()))

    if not pairs:
        pairs = DEFAULT_PAIRS

    print("Toy embedding similarity demo")
    print("These vectors are deterministic and educational, not learned model embeddings.\n")

    for left, right in pairs:
        print_pair_summary(left, right, dimensions=args.dimensions)


if __name__ == "__main__":
    main()
