from __future__ import annotations
import json
from lab.providers import DemoProvider

if __name__ == "__main__":
    raw = DemoProvider().generate('Return JSON with keys "answer" and "confidence".')
    try: print(json.loads(raw))
    except json.JSONDecodeError: print("Validation failed: the response was not JSON", raw)
