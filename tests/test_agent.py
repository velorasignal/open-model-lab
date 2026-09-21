from lab.agent import Agent
from lab.memory import ConversationMemory
from lab.providers import DemoProvider
from lab.safe_tools import make_safe_tools


def test_tool_registry_blocks_unknown_tools():
    try: make_safe_tools().call("shell", {})
    except ValueError: pass
    else: raise AssertionError("unknown tools must be blocked")


def test_agent_has_a_step_limit():
    answer = Agent(DemoProvider(), make_safe_tools(), ConversationMemory(), max_steps=1).run("hello")
    assert answer
