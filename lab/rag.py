from __future__ import annotations

from dataclasses import dataclass
from .embeddings import cosine, embed


def chunk(text: str, size: int = 80) -> list[str]:
    words = text.split()
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]


@dataclass
class Retriever:
    documents: list[str]

    def search(self, query: str, k: int = 3) -> list[str]:
        scored = [(cosine(embed(query), embed(doc)), doc) for doc in self.documents]
        return [doc for _, doc in sorted(scored, reverse=True)[:k]]
