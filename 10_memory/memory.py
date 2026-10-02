from __future__ import annotations

import argparse

from lab.memory import ConversationMemory


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Demonstrate how conversation memory turns prior turns into prompt context.")
    parser.add_argument("--limit", type=int, default=None, help="Show only the most recent N messages in the memory prompt.")
    parser.add_argument("--clear", action="store_true", help="Clear the memory before adding the demo messages.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    memory = ConversationMemory()

    if args.clear:
        memory.clear()

    memory.add("user", "My name is Ada.")
    memory.add("assistant", "Nice to meet you, Ada.")
    memory.add("user", "What should I remember about AI systems?")
    memory.add("assistant", "Remember the difference between model weights and application state.")
    memory.add("tool", "Tool result: safety checks matter before execution.")

    if args.limit is not None:
        recent = memory.messages[-args.limit :]
        print("\n".join(f"{role}: {content}" for role, content in recent))
        return

    print(memory.prompt())


if __name__ == "__main__":
    main()
