from __future__ import annotations

import argparse

from lab.rag import Retriever, chunk


DOCS = [
    "Inference means running fixed model weights on new input.",
    "RAG retrieves relevant document context before generation.",
    "An agent combines a model, tools, memory, and a loop.",
    "Safety checks keep model actions constrained and predictable.",
    "A local model can run on your machine through a provider such as Ollama.",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple retrieval demo for a beginner-friendly RAG pipeline.")
    parser.add_argument("--question", type=str, default="What does retrieval do?", help="The user question to search for.")
    parser.add_argument("--top-k", type=int, default=2, help="How many result chunks or documents to show.")
    parser.add_argument("--show-chunks", action="store_true", help="Print the chunks produced from a sample document.")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.show_chunks:
        sample = "RAG is useful when a model needs fresh facts or private documents. It retrieves context before generation."
        print("Chunks:")
        for index, piece in enumerate(chunk(sample, size=5), start=1):
            print(f"  {index}. {piece}")
        return

    retriever = Retriever(DOCS)
    matches = retriever.search(args.question, k=args.top_k)
    print(f"Question: {args.question}")
    print("Top matches:")
    for index, match in enumerate(matches, start=1):
        print(f"  {index}. {match}")


if __name__ == "__main__":
    main()
