# 8. Tools and the tool-calling boundary

Tools are ordinary Python functions that an application exposes to a model in a controlled way. The model does not get unrestricted access to the machine. Instead, it proposes a structured request, the app validates the request, and the app decides whether to run the tool.

This chapter keeps the idea simple and safe. The goal is not to build a full tool runtime. The goal is to make the security pattern visible:

```text
model says: "I want to call this tool with these arguments"
    -> app checks whether the tool is allowed
    -> app validates the arguments
    -> app runs the tool
    -> app returns a safe result to the model
```

This is the same basic pattern used in agent systems, workflow tools, and function-calling APIs.

## Learning goals

By the end of this chapter, you should be able to:

- explain why tools are a security boundary;
- describe the difference between a raw model response and an allowed tool call;
- explain what makes a tool "safe";
- understand why validation matters before running tool functions;
- recognize the shape of a simple tool-calling interface;
- compare the tool-calling pattern to the prompting pattern from chapter 07; and
- see how a tiny app can expose a limited set of functions without giving the model arbitrary control.

## The central idea

A large model is statistically good at producing text, but it is not automatically trusted to execute code. In a real app, the model should propose an action, not directly run it.

```text
user request
    -> model decides a tool might help
    -> app parses the tool call
    -> app checks the allow-list
    -> app runs a safe function
    -> app returns the result
```

The repository uses a deliberately tiny tool registry. It keeps the pattern readable so beginners can inspect every step.

The important lesson is that tools are not magic. They are just functions with a narrow contract.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`tool_calling.py`](./tool_calling.py) | A beginner-friendly tool call demo with validation and a blocked-tool example |
| [`../lab/tools.py`](../lab/tools.py) | The small registry used to register available functions |
| [`../lab/safe_tools.py`](../lab/safe_tools.py) | A safe, allow-listed set of example tools |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- the ideas from chapters 1–7: models, logits, prompting, and structured output.

No third-party packages are required. This is intentionally a standard-library-only lesson.

## Run the examples

From the repository root:

```bash
python 08_tools/tool_calling.py
python 08_tools/tool_calling.py --expression "(12 + 8) / 2"
python 08_tools/tool_calling.py --demo
```

If your system uses `python3`, replace `python` with `python3`.

The file demonstrates three things:

1. a safe calculator tool;
2. the current time tool;
3. a blocked call that should fail in a controlled way.

## What the script does

The script creates a tool registry and registers a few functions. It then calls them through the same interface an app would use:

```python
tools = make_safe_tools()
tools.call("calculator", {"expression": "(2 + 3) * 4"})
```

The logic is intentionally simple:

1. the tool name is looked up in a registry;
2. arguments are checked by the called function;
3. the function runs only if that function is allowed;
4. disallowed or invalid calls raise a clear error instead of silently executing arbitrary code.

This model is safe because the application sits between the model and the real system.

## Why this matters

A model is very good at generating text, but that does not mean it should run shell commands or access arbitrary local data.

Examples of risky behavior:

- running unrestricted shell commands;
- executing arbitrary Python code with `eval`;
- calling functions with unexpected arguments;
- allowing any tool name without validation;
- exposing secrets or internal files to an untrusted model.

The allow-list is the boundary. It says: these are the functions we trust, and nothing else.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Change the calculator expression to use division by zero. What should the function return?
2. Add a new safe tool like `square` or `average`.
3. Try calling a blocked tool such as `shell` or `eval`. What happens?
4. Attempt to call a tool with a missing argument. Why does the app reject it?
5. Compare this chapter to chapter 07. Which part is prompt validation, and which part is tool execution?
6. Add a new tool that reads a public text file but never accepts user-supplied paths.
7. Write a tiny helper that prints the name of the tool being called before execution.

## Common vocabulary

- **Tool:** a small function exposed to an application or model.
- **Registry:** a lookup structure mapping tool names to actual functions.
- **Allow-list:** a trusted set of functions that the app permits.
- **Validation:** checking that arguments and inputs are acceptable.
- **Execution boundary:** the point where the application decides whether to run code.
- **Function calling:** the model requesting a tool with structured arguments.
- **Safety check:** a guardrail that prevents destructive or untrusted behavior.

## Scope and limitations

This chapter intentionally does not implement:

- a complete agent runtime;
- chat memory or multi-step planning;
- real browser or OS automation;
- a true security sandbox;
- a production tool protocol; or
- a full model-to-tool loop with retries and error handling.

The purpose is clarity, not production scale. The examples stay intentionally small so the basic safety pattern is easy to understand.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- why tools need a safety boundary;
- how a registry maps tool names to functions;
- why validation is important before execution;
- how a blocked call differs from a valid tool call; and
- how this chapter connects to the larger pattern of model + app + tool boundary.
