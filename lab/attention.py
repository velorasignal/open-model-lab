from __future__ import annotations


def attention(query: list[float], keys: list[list[float]], values: list[list[float]]) -> list[float]:
    """Educational scaled dot-product attention for one query."""
    if not keys or len(keys) != len(values):
        raise ValueError("keys and values must be non-empty and aligned")
    scores = [sum(q * k for q, k in zip(query, key)) for key in keys]
    peak = max(scores)
    weights = [__import__('math').exp(score - peak) for score in scores]
    total = sum(weights)
    weights = [weight / total for weight in weights]
    return [sum(weight * value[i] for weight, value in zip(weights, values))
            for i in range(len(values[0]))]
