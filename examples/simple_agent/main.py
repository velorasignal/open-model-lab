#!/usr/bin/env python3
"""Small capstone: local provider + tools + memory + optional RAG context."""
from __future__ import annotations
import argparse, os
from lab.agent import Agent
from lab.memory import ConversationMemory
from lab.providers import DemoProvider, OllamaProvider
from lab.safe_tools import make_safe_tools
from lab.rag import Retriever

DOCS = ["This lab teaches tokens, embeddings, inference, tools, agents, memory, and RAG.", "The calculator is allow-listed and does not execute arbitrary shell commands."]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--demo", action="store_true"); parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "gemma3:1b"))
    args = parser.parse_args(); provider = DemoProvider() if args.demo else OllamaProvider(args.model)
    retrieved = Retriever(DOCS).search("AI systems lab")
    memory = ConversationMemory(); memory.add("system", "Relevant local notes: " + " ".join(retrieved))
    agent = Agent(provider, make_safe_tools(), memory)
    print("Mini local agent. Ask a question or type quit.")
    while True:
        question = input("You: ")
        if question.lower() in {"quit", "exit"}: break
        print("Agent:", agent.run(question))
