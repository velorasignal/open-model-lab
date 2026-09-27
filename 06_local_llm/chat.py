from __future__ import annotations

"""Small command-line wrapper for the local-model provider boundary.

This file is intentionally easy to read: it picks a provider, sends a prompt,
and prints the response. The real logic lives in ``lab.providers`` so the lesson
can stay focused on the high-level idea.
"""

import argparse
import os

from lab.providers import DemoProvider, OllamaProvider


def parse_args() -> argparse.Namespace:
    """Create the command-line interface used by this lesson."""
    parser = argparse.ArgumentParser(
        description="Send a prompt to either the offline demo provider or a local Ollama model."
    )
    parser.add_argument(
        "--model",
        default=os.getenv("OLLAMA_MODEL", "gemma3:1b"),
        help="model name for Ollama, such as gemma3:1b",
    )
    parser.add_argument(
        "--prompt",
        default="Explain inference in one sentence.",
        help="text to send to the selected provider",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="use the offline demo provider instead of Ollama",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="temperature value passed through to the provider",
    )
    return parser.parse_args()


def main() -> None:
    """Run one prompt through the chosen provider and print the result."""
    args = parse_args()

    provider = DemoProvider() if args.demo else OllamaProvider(model=args.model)
    response = provider.generate(args.prompt, temperature=args.temperature)

    print(f"Provider: {'demo' if args.demo else args.model}")
    print(f"Prompt: {args.prompt}")
    print("Response:")
    print(response)


if __name__ == "__main__":
    main()
