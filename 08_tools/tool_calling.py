from lab.safe_tools import make_safe_tools

if __name__ == "__main__":
    tools = make_safe_tools()
    print(tools.call("calculator", {"expression": "(2 + 3) * 4"}))
    try: print(tools.call("shell", {}))
    except ValueError as exc: print("Blocked:", exc)
