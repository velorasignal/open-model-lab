from __future__ import annotations

"""Tiny structured-output demo for a beginner-friendly LLM app.

The goal is simple: ask for JSON, parse it, and validate the required keys
before using the output. We keep the model call intentionally small and use the
repository's DemoProvider so the focus remains on the application pattern.
"""

import argparse
import json

from lab.providers import DemoProvider


REQUIRED_FIELDS = {"answer", "confidence"}


def validate_response(raw: str) -> dict[str, object]:
    """Parse a JSON response and validate the required schema."""
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"The model response was not valid JSON: {raw!r}") from exc

    if not isinstance(payload, dict):
        raise ValueError("The model response must be a JSON object.")

    missing = REQUIRED_FIELDS - payload.keys()
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Missing required field(s): {missing_list}")

    answer = payload["answer"]
    confidence = payload["confidence"]

    if not isinstance(answer, str):
        raise ValueError("'answer' must be a string.")
    if not isinstance(confidence, (int, float)):
        raise ValueError("'confidence' must be a number.")
    if not 0.0 <= float(confidence) <= 1.0:
        raise ValueError("'confidence' must be between 0.0 and 1.0.")

    return payload


def parse_args() -> argparse.Namespace:
    """Create the command-line interface used by this lesson."""
    parser = argparse.ArgumentParser(
        description="Ask a demo LLM for JSON and validate the result before using it."
    )
    parser.add_argument(
        "--prompt",
        default='Return JSON with keys "answer" and "confidence".',
        help="instruction sent to the demo provider",
    )
    return parser.parse_args()


def main() -> None:
    """Ask the model for JSON, then validate and print the parsed output."""
    args = parse_args()
    provider = DemoProvider()
    raw_response = provider.generate(args.prompt)

    print("Raw model output:")
    print(raw_response)
    print()

    try:
        parsed = validate_response(raw_response)
    except ValueError as exc:
        print(f"Validation failed: {exc}")
        return

    print("Validated structured output:")
    print(json.dumps(parsed, indent=2))


if __name__ == "__main__":
    main()
