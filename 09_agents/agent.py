from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lab.agent import Agent
from lab.memory import ConversationMemory
from lab.providers import DemoProvider, OllamaProvider
from lab.safe_tools import make_safe_tools


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a tiny safe agent.")
    parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "gemma3:1b"), help="Ollama model name when not in demo mode.")
    parser.add_argument("--demo", action="store_true", help="Use the demo provider instead of a live Ollama server.")
    parser.add_argument("--prompt", type=str, default=None, help="Run one prompt once and exit. Useful for shell examples and tests.")
    parser.add_argument("--max-steps", type=int, default=4, help="Maximum number of tool steps before stopping.")
    return parser


def run_single_question(agent: Agent, question: str) -> str:
    print(f"You: {question}")
    answer = agent.run(question)
    print(f"Agent: {answer}")
    return answer


def main() -> None:
    args = build_parser().parse_args()
    provider = DemoProvider() if args.demo else OllamaProvider(args.model)
    agent = Agent(provider, make_safe_tools(), ConversationMemory(), max_steps=args.max_steps)

    if args.prompt:
        run_single_question(agent, args.prompt)
        return

    print("Safe agent ready. Type 'quit' to stop.")
    while True:
        question = input("You: ")
        if question.strip().lower() in {"quit", "exit", "q"}:
            print("Goodbye.")
            break
        run_single_question(agent, question)


if __name__ == "__main__":
    main()
