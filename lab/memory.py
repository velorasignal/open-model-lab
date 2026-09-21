from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ConversationMemory:
    messages: list[tuple[str, str]] = field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        self.messages.append((role, content))

    def prompt(self) -> str:
        return "\n".join(f"{role}: {content}" for role, content in self.messages)

    def clear(self) -> None:
        self.messages.clear()
