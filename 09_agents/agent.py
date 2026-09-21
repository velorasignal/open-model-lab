from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lab.agent import Agent
from lab.memory import ConversationMemory
from lab.providers import DemoProvider, OllamaProvider
from lab.safe_tools import make_safe_tools


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "gemma3:1b"))
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    provider = DemoProvider() if args.demo else OllamaProvider(args.model)
    agent = Agent(provider, make_safe_tools(), ConversationMemory())
    print("Safe agent ready. Type 'quit' to stop.")
    while True:
        question = input("You: ")
        if question.lower() in {"quit", "exit"}: break
        print("Agent:", agent.run(question))

if __name__ == "__main__": main()
