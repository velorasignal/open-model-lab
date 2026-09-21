from __future__ import annotations
import argparse, os
from lab.providers import DemoProvider, OllamaProvider

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "gemma3:1b")); parser.add_argument("--demo", action="store_true")
    args = parser.parse_args(); provider = DemoProvider() if args.demo else OllamaProvider(args.model)
    print(provider.generate(input("Prompt: ")))
