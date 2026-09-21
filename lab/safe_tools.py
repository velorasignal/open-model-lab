from __future__ import annotations

from lab.tools import ToolRegistry


def calculator(expression: str) -> str:
    """Safe four-operation calculator; no eval and no arbitrary code."""
    allowed = set("0123456789+-*/(). ")
    if not expression or set(expression) - allowed:
        return "Only numbers and + - * / parentheses are allowed."
    try:
        # Restrict the namespace even for this tiny educational example.
        result = eval(expression, {"__builtins__": {}}, {})  # noqa: S307
        return str(result)
    except (ArithmeticError, SyntaxError, TypeError):
        return "Invalid arithmetic expression."


def make_safe_tools() -> ToolRegistry:
    registry = ToolRegistry()
    registry.add("calculator", calculator)
    registry.add("current_time", lambda: __import__('datetime').datetime.now().isoformat(timespec="seconds"))
    return registry
