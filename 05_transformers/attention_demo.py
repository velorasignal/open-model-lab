from __future__ import annotations

"""A tiny attention demo for learning the core idea behind transformers.

The script keeps the math fully visible:

    score_i = query · key_i
    weight_i = softmax(score_i)
    output = sum(weight_i * value_i)

This is not a full Transformer layer. It is a single, easy-to-read example of
how a model decides which context positions deserve attention.
"""

import argparse
import math

from lab.attention import attention


DEFAULT_KEYS = [
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0],
]

DEFAULT_VALUES = [
    [10.0, 0.0],
    [0.0, 10.0],
    [5.0, 5.0],
]


def softmax(scores: list[float]) -> list[float]:
    """Convert raw similarity scores into a probability-like distribution."""
    if not scores:
        raise ValueError("scores must not be empty")

    peak = max(scores)
    weights = [math.exp(score - peak) for score in scores]
    total = sum(weights)
    if total == 0:
        raise ValueError("softmax failed: all scores were extremely small")
    return [weight / total for weight in weights]


def print_attention_case(label: str, query: list[float]) -> None:
    """Show the scores, weights, and output for one query."""
    scores = [sum(q * k for q, k in zip(query, key)) for key in DEFAULT_KEYS]
    weights = softmax(scores)
    output = [
        sum(weight * value[i] for weight, value in zip(weights, DEFAULT_VALUES))
        for i in range(len(DEFAULT_VALUES[0]))
    ]

    print(f"{label}")
    print(f"Query: {query}")
    print(f"Scores: {[round(score, 3) for score in scores]}")
    print(f"Weights: {[round(weight, 3) for weight in weights]}")
    print(f"Output: {[round(value, 3) for value in output]}")
    print(f"Library result: {[round(value, 3) for value in attention(query, DEFAULT_KEYS, DEFAULT_VALUES)]}")
    print()


def parse_args() -> argparse.Namespace:
    """Create the command-line interface for this lesson."""
    parser = argparse.ArgumentParser(
        description="Explore the core idea of attention in a tiny toy model."
    )
    parser.add_argument(
        "--query",
        nargs="+",
        type=float,
        default=[1.0, 0.0],
        help="query vector to compare against the default keys",
    )
    return parser.parse_args()


def main() -> None:
    """Print a readable attention report for a few educational examples."""
    args = parse_args()

    if len(args.query) != 2:
        raise SystemExit("The demo query must contain exactly two numbers.")

    print("Toy attention demo")
    print("This is a single-head attention example designed for teaching, not for production use.\n")

    print_attention_case("Example 1: query matches the first key", [1.0, 0.0])
    print_attention_case("Example 2: query matches the second key", [0.0, 1.0])
    print_attention_case("Example 3: mixed query", [1.0, 1.0])
    print_attention_case("Custom query", list(args.query))


if __name__ == "__main__":
    main()
