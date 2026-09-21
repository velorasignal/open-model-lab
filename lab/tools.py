from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Callable

Tool = Callable[..., str]


@dataclass
class ToolRegistry:
    tools: dict[str, Tool] = field(default_factory=dict)

    def add(self, name: str, function: Tool) -> None:
        self.tools[name] = function

    def call(self, name: str, arguments: dict[str, Any]) -> str:
        if name not in self.tools:
            raise ValueError(f"Tool {name!r} is not allowed")
        return str(self.tools[name](**arguments))


def parse_tool_request(text: str) -> dict[str, Any] | None:
    """Parse the deliberately explicit JSON protocol used by the toy agent."""
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) and "tool" in value else None
