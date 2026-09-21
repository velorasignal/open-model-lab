from __future__ import annotations
import argparse, os
from lab.providers import DemoProvider, OllamaProvider

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--demo", action="store_true"); parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "gemma3:1b")); args = parser.parse_args()
    provider = DemoProvider() if args.demo else OllamaProvider(args.model)
    print("Type quit to stop.")
    while True:
        text = input("You: ")
        if text.lower() in {"quit", "exit"}: break
        print("Local model:", provider.generate(text))
