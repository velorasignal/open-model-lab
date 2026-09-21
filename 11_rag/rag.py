from __future__ import annotations
import argparse
from lab.providers import DemoProvider
from lab.rag import Retriever

DOCS = ["Inference means running fixed weights on new input.", "RAG retrieves relevant document context before generation.", "An agent combines a model, tools, state, and a loop."]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--question", default="What does inference mean?")
    question = parser.parse_args().question; context = "\n".join(Retriever(DOCS).search(question))
    print(DemoProvider().generate(f"Context:\n{context}\nQuestion: {question}"))
