from __future__ import annotations

"""Tiny helper for the local Ollama pattern used in this repository.

This file is intentionally small. It shows the interface clearly without hiding
important details: a model name, a server URL, and a prompt are all part of the
setup.
"""

from lab.providers import OllamaProvider


def make_client(model: str = "gemma3:1b", host: str = "http://localhost:11434") -> OllamaProvider:
    """Create a local client configured for a specific model and host."""
    return OllamaProvider(model=model, host=host)


def main() -> None:
    """Send a simple prompt to a local model and print the answer."""
    client = make_client()
    prompt = "Explain inference in one sentence."
    print(client.generate(prompt))


if __name__ == "__main__":
    main()
