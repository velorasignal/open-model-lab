from __future__ import annotations
import argparse
from lab.embeddings import tokenize

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("text", nargs="*", default=["Hello", "AI"])
    text = " ".join(parser.parse_args().text)
    for index, token in enumerate(tokenize(text)): print(f"{index:>3}: {token!r}")
