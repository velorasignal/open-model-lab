from __future__ import annotations
from lab.embeddings import cosine, embed

if __name__ == "__main__":
    pairs = [("cats chase mice", "a cat hunts a mouse"), ("cats chase mice", "quantum physics")]
    for left, right in pairs: print(f"{left!r} vs {right!r}: {cosine(embed(left), embed(right)):.3f}")
