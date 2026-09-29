from __future__ import annotations

"""
8. Tools: beginner-friendly tool-calling demo.

This lesson teaches the pattern behind function calling:
    model proposes a call
    app validates the call
    app runs a safe tool
    app returns a clean result

The repository already defines a small tool registry and safe tools in:
    - lab.tools
    - lab.safe_tools

This file is intentionally simple and readable so new learners can follow
every step without needing a large framework.
"""

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser used by this script.

    Returns:
        An ArgumentParser with options for expression and demo mode.
    """
    parser = argparse.ArgumentParser(
        description="Demonstrate safe tool calling in the Open AI Systems Lab."
    )
    parser.add_argument(
        "--expression",
        type=str,
        default="(2 + 3) * 4",
        help="expression to pass to the calculator tool (default: (2 + 3) * 4)",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="run the demo sequence that shows both valid and blocked calls",
    )
    return parser.parse_args()


def print_header() -> None:
    """Print a friendly introduction to the tool-calling lesson.

    This helps readers understand the context before seeing code output.
    """
    print("8. Tools and safe tool calling")
    print("A model calls a tool through a registry. The app decides whether to allow it.")
    print("")


def safe_tool_demo() -> None:
    """Run a sequence of tool calls demonstrating success and blocked access.

    This demo shows:
    1. A valid calculator tool call
    2. A valid current_time tool call
    3. A blocked attempt to call a disallowed tool

    The intent is to make the safety boundary visible in action.
    """
    from lab.safe_tools import make_safe_tools

    # Create the registry of allowed tools.
    tools = make_safe_tools()

    # Example 1: successful calculator call
    print("Example 1: valid calculator call")
    print("User input: Calculate (2 + 3) * 4")
    result = tools.call("calculator", {"expression": "(2 + 3) * 4"})
    print(f"Tool result: {result}")
    print(f"Expected: 20\n")

    # Example 2: successful current_time call
    print("Example 2: current time tool")
    print("User input: What time is it?")
    time_value = tools.call("current_time", {})
    print(f"Tool result: {time_value}")
    print(f"This is the current time in ISO format.\n")

    # Example 3: blocked tool call (security boundary in action)
    print("Example 3: blocked tool call")
    print("User input: Run a shell command")
    print("Model proposes: tools.call('shell', {})")
    try:
        # The app tries to call a disallowed tool.
        # The registry should reject this before execution.
        tools.call("shell", {})
    except ValueError as exc:
        # This is the intended behavior: clear error message, no execution.
        print(f"Blocked: {exc}")
        print(f"Result: The model's tool call was rejected. No shell access granted.\n")
    else:
        print("Unexpected: 'shell' was not blocked. This should not happen.")


def run_custom_expression(expression: str) -> None:
    """Run a calculator tool with a user-supplied expression.

    Parameters:
        expression: A mathematical expression like "(12 + 8) / 2"

    The calculator validates the expression before evaluation to prevent
    arbitrary code execution.
    """
    from lab.safe_tools import make_safe_tools

    tools = make_safe_tools()
    result = tools.call("calculator", {"expression": expression})
    print(f"Expression: {expression}")
    print(f"Result: {result}")


def main() -> None:
    """Run the example in a friendly, beginner-focused way.

    This function coordinates the entire script flow:
    1. Show a header
    2. Check if demo mode is requested
    3. Either run the full demo or a single custom expression
    """
    print_header()

    # Parse command-line arguments
    args = build_parser()

    # If --demo is set, run the full sequence
    if args.demo:
        safe_tool_demo()
        return

    # Otherwise, run a single calculator call with the provided expression
    run_custom_expression(args.expression)


if __name__ == "__main__":
    # This block runs only when the file is executed directly.
    main()
