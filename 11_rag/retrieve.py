from __future__ import annotations

import argparse

from lab.rag import Retriever


DOCS = [
    "Inference runs a model on new input using fixed weights.",
    "RAG adds relevant external context before the model answers.",
    "Conversation memory keeps the recent chat state in the app.",
    "Tools allow a model to request safe functions under application control.",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Demonstrate retrieval ranking with a few example documents.")
    parser.add_argument("--query", type=str, default="How does retrieval help a model?", help="The query to rank against the documents.")
    parser.add_argument("--top-k", type=int, default=2, help="How many matches to print.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    retriever = Retriever(DOCS)
    matches = retriever.search(args.query, k=args.top_k)
    print(f"Query: {args.query}")
    print("Best matches:")
    for index, match in enumerate(matches, start=1):
        print(f"  {index}. {match}")


if __name__ == "__main__":
    main()
