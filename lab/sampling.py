from __future__ import annotations

import math
import random


def softmax(logits: list[float], temperature: float = 1.0) -> list[float]:
    if temperature <= 0:
        raise ValueError("temperature must be positive")
    scaled = [x / temperature for x in logits]
    peak = max(scaled)
    values = [math.exp(x - peak) for x in scaled]
    total = sum(values)
    return [x / total for x in values]


def sample(items: list[str], probabilities: list[float], seed: int | None = None) -> str:
    return random.Random(seed).choices(items, weights=probabilities, k=1)[0]
