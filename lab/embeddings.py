from __future__ import annotations

import hashlib
import math
import re
from collections.abc import Iterable


def tokenize(text: str) -> list[str]:
    """A deliberately tiny tokenizer: words and punctuation become tokens."""
    return re.findall(r"[A-Za-z0-9_]+|[^\w\s]", text.lower())


def embed(text: str, dimensions: int = 32) -> list[float]:
    """Deterministic hashing vector; real embeddings are learned representations."""
    vector = [0.0] * dimensions
    for token in tokenize(text):
        digest = hashlib.sha256(token.encode()).digest()
        index = int.from_bytes(digest[:4], "big") % dimensions
        vector[index] += 1.0
    norm = math.sqrt(sum(x * x for x in vector)) or 1.0
    return [x / norm for x in vector]


def cosine(a: Iterable[float], b: Iterable[float]) -> float:
    return sum(x * y for x, y in zip(a, b))
