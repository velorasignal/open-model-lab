# 7. LLM applications and structured output

A model alone is not an application. A useful application adds a prompt, a clear output contract, and validation around the raw model response.

In this chapter, the focus is not on building a giant app or a new framework. The goal is to make the pattern visible: prompt the model, ask for a specific format, and validate the result before using it.

## Learning goals

By the end of this chapter, you should be able to:

- explain why prompt design matters in an LLM application;
- describe what a structured output contract is;
- explain why JSON is useful for machine-readable responses;
- validate required keys before using a model output;
- recognize the difference between raw model text and application-safe data;
- explain why this example uses a demo provider instead of a real model runtime; and
- connect this chapter to the provider pattern introduced in chapter 06.

## The central idea

A language model can generate text, but an application usually needs a reliable shape.

```text
user request -> prompt -> model response -> parse -> validate -> use data
```

Without validation, a model may return:

- missing fields;
- extra text around the JSON;
- values with the wrong type;
- malformed or partial output.

This chapter uses a tiny prompt that asks for JSON with a known schema:

```json
{
  "answer": "...",
  "confidence": 0.87
}
```

That is the basic pattern behind many LLM-powered tools: convert text into a structured object before you do anything else with it.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`structured_output.py`](./structured_output.py) | Prompting for a JSON response and validating the fields before use |
| [`../lab/providers.py`](../lab/providers.py) | The demo provider used in this lesson while the app remains model-agnostic |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- the ideas from chapters 1–6: models, softmax, attention, and providers.

No third-party packages are required. This example uses only Python's standard library.

## Run the examples

From the repository root:

```bash
python 07_llm_application/structured_output.py
```

If your system uses `python3`, replace `python` with `python3`.

To explore the idea in a small interactive way, change the prompt in the script and run it again.

```bash
python 07_llm_application/structured_output.py --prompt "Return JSON with keys 'city' and 'country'."
```

## What the script does

The app sends a prompt like this:

```text
Return JSON with keys "answer" and "confidence".
```

The demo provider responds with text. The script then:

1. parses the text as JSON;
2. checks that the result is a dictionary;
3. verifies that both required keys are present;
4. validates the types of the values; and
5. prints the final object or a human-readable validation error.

This is the same pattern you'd use in a real app before passing data to a UI, database, tool-call layer, or workflow engine.

## Why validation matters

A real model can be very creative, and that is not always desirable when your software expects a strict contract.

Examples of validation problems:

- the model returns plain text instead of JSON;
- the model forgets one required field;
- the answer is a number instead of a string;
- the confidence value is outside the expected range.

If an app receives untrusted model output, validation is the guardrail that keeps the rest of the code safe.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Change the prompt to require a different schema, such as `title`, `summary`, and `difficulty`.
2. Change the field names in the validation check. What breaks?
3. Remove one required key from the model output. Does the script fail in the expected way?
4. Change `confidence` to a string or a negative number. Why should an app reject it?
5. Compare this lesson to the provider pattern in chapter 06. Which part is prompt design, and which part is runtime infrastructure?
6. Add a new field such as `tags` with a list of strings.
7. Write a second helper that checks `confidence` is between `0.0` and `1.0`.

## Common vocabulary

- **Prompt:** the instruction or request sent to the model.
- **Structured output:** a response in a defined format like JSON.
- **Schema:** the required shape of the output data.
- **Validation:** checking that the output matches the expected shape and types.
- **JSON:** a common text format for machine-readable data.
- **Application boundary:** the layer where raw model text becomes safe business data.
- **Parsing:** converting raw text into a Python object.

## Scope and limitations

This chapter intentionally does not implement:

- a complete web app or API layer;
- database storage or user authentication;
- complex prompt chaining;
- streaming chat history;
- model evaluation or quality scoring; or
- a full tool-calling runtime.

The goal is to show the basic application boundary clearly before later chapters add tools, memory, retrieval, and agents.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- why prompt design matters for LLM applications;
- why a schema is useful even for a tiny response;
- why JSON is a common output format;
- why validation is necessary before using model output; and
- how this chapter fits into the larger app pattern of provider + prompt + validation.
