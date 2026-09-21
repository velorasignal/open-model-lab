from __future__ import annotations


def predict(x: float, weight: float = 2.0, bias: float = 1.0) -> float:
    return weight * x + bias

if __name__ == "__main__":
    for x in [0, 1, 2, 3]: print(f"x={x} -> y={predict(x):.1f}")
