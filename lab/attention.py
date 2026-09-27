from __future__ import annotations

import math


def attention(query: list[float], keys: list[list[float]], values: list[list[float]]) -> list[float]:
    """Compute a single-head attention output for one query.

    The function follows the common attention pattern:

        score_i = query · key_i
        weight_i = softmax(score_i)
        output = sum(weight_i * value_i)

    Parameters:
        query: The vector being compared against the keys.
        keys: One vector per key position.
        values: One vector per key position. The number of values must match the
            number of keys, and each value vector must have the same length.

    Returns:
        A new vector created by taking a weighted sum of the value vectors.
    """
    if not query:
        raise ValueError("query must not be empty")
    if not keys or not values:
        raise ValueError("keys and values must not be empty")
    if len(keys) != len(values):
        raise ValueError("keys and values must have the same length")
    if any(len(key) != len(query) for key in keys):
        raise ValueError("every key must have the same length as the query")
    if any(len(value) != len(values[0]) for value in values):
        raise ValueError("every value vector must have the same length")

    scores = [sum(q * k for q, k in zip(query, key)) for key in keys]
    if not scores:
        raise ValueError("attention requires at least one key")

    peak = max(scores)
    weights = [math.exp(score - peak) for score in scores]
    total = sum(weights)
    if total == 0:
        raise ValueError("softmax failed because all scores were zero")

    weights = [weight / total for weight in weights]
    return [
        sum(weight * value[index] for weight, value in zip(weights, values))
        for index in range(len(values[0]))
    ]
