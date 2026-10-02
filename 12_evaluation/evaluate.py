from __future__ import annotations

import argparse

from lab.embeddings import cosine, embed


DEFAULT_CASES = [
    ("cats", "cats"),
    ("cats", "cat"),
    ("cats", "quantum physics"),
    ("ai systems", "machine learning"),
    ("agent", "tool-calling assistant"),
]


def evaluate_case(left: str, right: str, threshold: float = 0.5) -> tuple[bool, float]:
    score = cosine(embed(left), embed(right))
    return score >= threshold, score


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Tiny evaluation script for similarity-based checks.")
    parser.add_argument("--threshold", type=float, default=0.5, help="Similarity threshold for a passing case.")
    parser.add_argument("--verbose", action="store_true", help="Print each case with its score.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    passed = 0
    total = 0

    for left, right in DEFAULT_CASES:
        total += 1
        ok, score = evaluate_case(left, right, args.threshold)
        if args.verbose:
            print(f"{left!r} vs {right!r}: score={score:.3f}, pass={ok}")
        if ok:
            passed += 1

    print(f"Passed {passed}/{total} cases with threshold {args.threshold:.2f}")


if __name__ == "__main__":
    main()
