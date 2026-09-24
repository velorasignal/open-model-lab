from __future__ import annotations

"""A tiny, readable language model for learning next-token prediction.

This module deliberately uses hand-written logits instead of a trained neural
network. That keeps the important ideas visible:

    context -> logits -> probabilities -> next-token choice

A real autoregressive model performs the same kind of final conversion, but it
learns its logits from data using many neural-network layers.
"""

from dataclasses import dataclass

from lab.sampling import sample, softmax


@dataclass(frozen=True)
class Prediction:
    """The complete prediction information for one context and temperature."""

    tokens: list[str]
    logits: list[float]
    probabilities: list[float]


# Each row is an intentionally small stand-in for a trained model's output.
# The keys are normalized prompts, and each value contains candidate tokens and
# their raw scores. Higher scores should become higher probabilities.
TOY_MODEL: dict[str, tuple[list[str], list[float]]] = {
    "the cat sat on the": (["mat", "floor", "roof"], [3.0, 1.0, 0.2]),
    "the dog chased the": (["ball", "cat", "car"], [2.6, 1.2, 0.4]),
    "once upon a": (["time", "day", "place"], [2.8, 1.0, 0.5]),
}

# Unknown contexts use this row rather than failing. It lets beginners change
# the prompt first and explore the rest of the pipeline immediately.
FALLBACK_ROW = (["mat", "floor", "roof"], [1.0, 1.0, 1.0])


def normalize_prompt(prompt: str) -> str:
    """Return the simple form used as a key in ``TOY_MODEL``."""
    return " ".join(prompt.lower().split())


def toy_next_token_logits(prompt: str) -> tuple[list[str], list[float]]:
    """Return candidate tokens and hand-written logits for ``prompt``.

    This function represents the part that a real language model would learn.
    Returning copies prevents a caller from accidentally changing the shared
    model table while experimenting.
    """
    tokens, logits = TOY_MODEL.get(normalize_prompt(prompt), FALLBACK_ROW)
    return list(tokens), list(logits)


def predict(prompt: str, temperature: float = 1.0) -> Prediction:
    """Convert the toy model's logits into a probability distribution."""
    tokens, logits = toy_next_token_logits(prompt)
    probabilities = softmax(logits, temperature=temperature)
    return Prediction(tokens, logits, probabilities)


def greedy_next_token(prediction: Prediction) -> str:
    """Return the candidate with the highest probability."""
    # max(..., key=...) keeps the token attached to its probability. In a tie,
    # Python returns the first candidate, making this choice deterministic.
    return max(zip(prediction.tokens, prediction.probabilities), key=lambda pair: pair[1])[0]


def sample_next_token(prediction: Prediction, seed: int | None = None) -> str:
    """Choose one token using its probability, optionally reproducibly."""
    return sample(prediction.tokens, prediction.probabilities, seed=seed)


def print_prediction(prompt: str, temperature: float, seed: int | None = 7) -> None:
    """Print one beginner-friendly prediction table."""
    prediction = predict(prompt, temperature=temperature)
    print(f"Prompt: {prompt!r}")
    print(f"Temperature: {temperature}")
    print("Candidate       Logit       Probability")
    print("-" * 42)
    for token, logit, probability in zip(
        prediction.tokens, prediction.logits, prediction.probabilities
    ):
        print(f"{token:<15} {logit:>6.2f}       {probability:>8.3f}")
    print(f"Greedy choice:   {greedy_next_token(prediction)!r}")
    print(f"Sampled choice:  {sample_next_token(prediction, seed=seed)!r}")
    print()


if __name__ == "__main__":
    # A direct run gives a useful first success without requiring arguments.
    print("Toy next-token language model")
    print("The scores are hand-written for education, not learned from data.\n")
    for temperature in (0.2, 1.2):
        print_prediction("The cat sat on the", temperature)
