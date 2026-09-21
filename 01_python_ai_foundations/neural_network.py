from __future__ import annotations
from math import exp


def sigmoid(x: float) -> float:
    return 1 / (1 + exp(-x))

if __name__ == "__main__":
    for value in [-2, 0, 2]: print(value, "->", round(sigmoid(value), 3))
