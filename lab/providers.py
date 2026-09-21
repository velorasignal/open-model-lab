from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Protocol


class LLMProvider(Protocol):
    def generate(self, prompt: str, *, temperature: float = 0.7) -> str: ...


@dataclass
class OllamaProvider:
    model: str = "gemma3:1b"
    host: str = "http://localhost:11434"
    timeout: int = 120

    def generate(self, prompt: str, *, temperature: float = 0.7) -> str:
        payload = json.dumps({"model": self.model, "prompt": prompt, "stream": False,
                              "options": {"temperature": temperature}}).encode()
        request = urllib.request.Request(self.host.rstrip("/") + "/api/generate", payload,
                                         headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read())['response']
        except urllib.error.URLError as exc:
            raise RuntimeError(
                "Ollama does not appear to be running. Start Ollama, install the model "
                f"with `ollama pull {self.model}`, and try again. Details: {exc}"
            ) from exc
        except KeyError as exc:
            raise RuntimeError("Ollama returned an unexpected response.") from exc


class DemoProvider:
    """Offline provider for tests and first-run architecture experiments."""

    def generate(self, prompt: str, *, temperature: float = 0.7) -> str:
        return f"[demo response] I received: {prompt[:160]}"
