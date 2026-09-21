from __future__ import annotations

from dataclasses import dataclass
from lab.memory import ConversationMemory
from lab.providers import LLMProvider
from lab.tools import ToolRegistry, parse_tool_request


@dataclass
class Agent:
    llm: LLMProvider
    tools: ToolRegistry
    memory: ConversationMemory
    max_steps: int = 4

    def run(self, user_text: str) -> str:
        self.memory.add("user", user_text)
        for _ in range(self.max_steps):
            prompt = ("You are a safe tool-using assistant. If a tool is needed, reply with only "
                      "JSON like {\"tool\":\"calculator\",\"arguments\":{\"expression\":\"2+2\"}}. "
                      "Otherwise answer normally.\n" + self.memory.prompt())
            response = self.llm.generate(prompt)
            request = parse_tool_request(response)
            if not request:
                self.memory.add("assistant", response)
                return response
            try:
                result = self.tools.call(request["tool"], request.get("arguments", {}))
            except (KeyError, TypeError, ValueError) as exc:
                result = f"Tool error: {exc}"
            self.memory.add("tool", result)
        return "I stopped after the safe tool-step limit."
