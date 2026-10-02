from __future__ import annotations

import argparse

from lab.providers import DemoProvider
from lab.rag import Retriever


DOCS = [
    "Inference means running fixed weights on new input.",
    "RAG retrieves relevant document context before generation.",
    "An agent combines a model, tools, memory, and a loop.",
    "Evaluation measures whether a system behaves as expected.",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Tiny RAG pipeline that retrieves context and passes it to a demo model.")
    parser.add_argument("--question", type=str, default="What does inference mean?", help="Question to answer using retrieved context.")
    parser.add_argument("--top-k", type=int, default=2, help="Number of retrieved documents to include in the prompt.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    context = "\n".join(Retriever(DOCS).search(args.question, k=args.top_k))
    prompt = f"Context:\n{context}\n\nQuestion: {args.question}\nAnswer using the context and be concise."
    print(prompt)
    print("\n--- demo model response ---")
    print(DemoProvider().generate(prompt))


if __name__ == "__main__":
    main()
