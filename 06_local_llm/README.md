# 6. Local LLMs and model providers

A local LLM is not a special kind of program. It is usually a standard model file served by a local runtime such as Ollama, and your Python code talks to it over a small HTTP interface.

This chapter shows the boundary clearly: the code does not need to know every detail of the model file or the server. It only needs a provider that can accept a prompt and return a response.

## Learning goals

By the end of this chapter, you should be able to:

- explain why a provider boundary separates application code from model runtime details;
- describe what Ollama does in a local LLM setup;
- distinguish an offline demo provider from a real local model provider;
- explain why a model name and a host URL matter when connecting to local inference;
- read the provider pattern used by the repository; and
- understand how a small local model still follows the same prompt-to-response idea as bigger models.

## The central idea

A language model is only one part of an application. The application also needs:

- a way to send text to the model;
- a way to receive text back;
- a model identifier or URL;
- a place to handle errors if the model is not running.

In this repository, that boundary is represented by the `LLMProvider` protocol and the `OllamaProvider` implementation in `lab/providers.py`.

```text
Python app -> provider interface -> local model server -> response text
```

The important idea is that the app talks to a consistent interface, not to Ollama-specific details everywhere in the code base.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`chat.py`](./chat.py) | A small CLI that asks for a prompt and then calls the chosen provider |
| [`ollama_client.py`](./ollama_client.py) | A tiny helper that makes the local Ollama pattern explicit |
| [`../lab/providers.py`](../lab/providers.py) | The provider interface, the actual Ollama client, and the offline demo provider |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- a local installation of Ollama if you want to use a real model.

Optional but recommended:

- `ollama pull gemma3:1b`
- a running Ollama server on `http://localhost:11434`

No third-party packages beyond the standard library are required for this lesson.

## Run the examples

From the repository root:

```bash
python 06_local_llm/chat.py --demo --prompt "Explain inference in one sentence."
python 06_local_llm/chat.py --model gemma3:1b --prompt "What is a local LLM?"
```

If your system uses `python3`, replace `python` with `python3`.

If you want to test the real Ollama path, install and start Ollama first:

```bash
ollama pull gemma3:1b
ollama serve
python 06_local_llm/chat.py --model gemma3:1b
```

The demo mode is useful when you want to verify the application flow without needing a running model.

## What the provider does

The provider interface is intentionally small:

```python
class LLMProvider(Protocol):
    def generate(self, prompt: str, *, temperature: float = 0.7) -> str: ...
```

The actual implementation for Ollama sends a JSON request to the local server:

```text
POST /api/generate
{
  "model": "gemma3:1b",
  "prompt": "Explain inference in one sentence.",
  "stream": false,
  "options": { "temperature": 0.7 }
}
```

The response is then returned as a string. The application code does not need to know all the internals of that HTTP call.

## Demo versus local model

The repository includes two provider styles:

- `DemoProvider`: returns a predictable placeholder response and is useful for tests and architecture checks.
- `OllamaProvider`: sends the prompt to a real local model over HTTP.

This is a very common pattern in real applications: one code path for local/offline testing and another code path for actual model serving.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Try the demo provider with several prompts. What changes in the output?
2. Switch the model name to a different Ollama model you have installed. Does the program still work?
3. Change the temperature in the provider call. Does the response become more or less creative?
4. Try a prompt that is too long or too short. What kind of errors might show up?
5. Compare this chapter with `04_language_models/README.md`. Which part is the model, and which part is the runtime boundary?
6. Add a second CLI option for a custom temperature.
7. Use the demo provider in tests to avoid requiring Ollama during CI.

## Common vocabulary

- **Provider:** an abstraction that hides the implementation details of how a model is accessed.
- **Ollama:** a local model runtime that serves models over HTTP.
- **Model name:** the identifier used by Ollama to select a downloaded model.
- **Prompt:** the user input sent to the model.
- **Temperature:** a value controlling how creative or conservative the model output is.
- **Demo provider:** a fake provider used to test app behavior without a real model.
- **Local inference:** running a model on your own machine instead of a remote API service.

## Scope and limitations

This chapter intentionally does not implement:

- a full chat loop with message history;
- model streaming or token-by-token generation;
- error retries for transient network failures;
- a production mapping layer for multiple providers; or
- a custom local server setup beyond the Ollama wrapper.

The goal is to make the runtime boundary visible and easy to understand before later chapters add prompting, tools, memory, and retrieval.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- what a provider is doing in a local LLM app;
- why the app does not need to know Ollama internals everywhere;
- why a demo provider is useful for tests and examples;
- how a prompt is sent to a local model server; and
- why this is a model-access layer rather than the model itself.
