from __future__ import annotations

"""Command-line microscope for the chapter 4 language-model example."""

import argparse

from language_model import predict, greedy_next_token, sample_next_token


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line interface used by this lesson."""
    parser = argparse.ArgumentParser(
        description="Inspect toy next-token probabilities at different temperatures."
    )
    parser.add_argument(
        "--prompt",
        default="The cat sat on the",
        help="prompt used to select a row in the toy model",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        nargs="+",
        default=[0.2, 1.2],
        metavar="T",
        help="one or more positive temperatures (default: 0.2 1.2)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=7,
        help="seed for reproducible sampling; omit with --random for variation",
    )
    parser.add_argument(
        "--random",
        action="store_true",
        help="sample without a fixed seed",
    )
    parser.add_argument(
        "--show-logits",
        action="store_true",
        help="print raw logits before the probability table",
    )
    return parser


def main() -> None:
    """Parse arguments and print one prediction report per temperature."""
    args = build_parser().parse_args()

    # Calling predict here also validates temperature through the shared
    # softmax helper, which gives a clear error for zero or negative values.
    for temperature in args.temperature:
        prediction = predict(args.prompt, temperature=temperature)
        seed = None if args.random else args.seed

        print(f"Prompt: {args.prompt!r}")
        print(f"Temperature: {temperature}")
        if args.show_logits:
            print("Raw logits:", dict(zip(prediction.tokens, prediction.logits)))
        print("Probabilities:")
        for token, probability in zip(prediction.tokens, prediction.probabilities):
            print(f"  {token:<10} {probability:.3f}")
        print(f"Greedy choice:  {greedy_next_token(prediction)!r}")
        print(f"Sampled choice: {sample_next_token(prediction, seed=seed)!r}")
        print()


if __name__ == "__main__":
    main()
