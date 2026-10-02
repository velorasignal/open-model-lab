# Open AI Systems Lab

A small, local-first laboratory for learning how modern AI systems work by building them from understandable Python programs.

> **Understand → Implement → Run → Experiment → Connect**

This is not a framework and it does not promise AGI. It is a guided path from a weighted function and next-token prediction to a small local agent with tools, memory, retrieval, and evaluation.

## Five-minute first success

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
python examples/local_chatbot/chat.py --demo
```

The demo works without Ollama and makes the provider boundary visible. For a real local answer, install [Ollama](https://ollama.com/), start it, and pull a small model:

```bash
ollama pull gemma3:1b
python examples/local_chatbot/chat.py --model gemma3:1b
```

The model name is configurable; use any model installed on your machine.

## What you will learn

| Level | Focus | Start here |
|---|---|---|
| 0 | Python for AI systems | `01_python_ai_foundations/` |
| 1 | weights, neurons, inference | `01_python_ai_foundations/` |
| 2 | tokens, embeddings, attention, sampling | `02_tokens/`–`05_transformers/` |
| 3 | local models, Ollama, model files | `06_local_llm/` and `docs/local-models.md` |
| 4 | prompting and structured output | `07_llm_application/` |
| 5 | tools and the agent loop | `08_tools/`, `09_agents/` |
| 6 | memory and RAG | `10_memory/`, `11_rag/` |
| 7 | evaluation and capstone | `12_evaluation/`, `examples/simple_agent/` |

Recommended order: **01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12**.

## Install

Python 3.10+ is recommended. The core lessons use only the standard library. Optional development dependencies are installed with:

```bash
python -m pip install -e '.[dev]'       # macOS/Linux
python -m pip install -e ".[dev]"       # PowerShell
```

No cloud API key is required. Copy `.env.example` only if you later add provider configuration.

## Architecture

```mermaid
flowchart TD
    User --> App[Python application]
    App --> Provider[LLMProvider interface]
    Provider --> Ollama[Ollama / local model]
    App --> Tools[Safe tools]
    App --> Memory[Conversation memory]
    App --> RAG[Chunk → embed → retrieve]
    App --> Eval[Evaluation checks]
    Tools --> App
    Memory --> App
    RAG --> App
    Eval --> App
```

The numbered lessons reuse the small `lab` package. Toy code is deliberately transparent; it is not a replacement for optimized Transformer runtimes.

## Run experiments

```bash
python 01_python_ai_foundations/linear_model.py
python 02_tokens/token_explorer.py "The cat sat on the mat"
python 03_embeddings/embedding_demo.py
python 04_language_models/next_token_demo.py --prompt "The cat sat on the" --temperature 0.2 1.2
python 05_transformers/attention_demo.py
python 06_local_llm/chat.py --demo --prompt "Explain inference in one sentence."
python 07_llm_application/structured_output.py
python 08_tools/tool_calling.py
python 09_agents/agent.py --demo
python 09_agents/agent.py --demo --prompt "Use the calculator to add 7 and 8"
python 10_memory/memory.py
python 11_rag/ingest.py
python 11_rag/retrieve.py
python 11_rag/rag.py --question "What does retrieval do?"
python 12_evaluation/evaluate.py --verbose
python -m pytest
```

Each lesson README answers what, why, how, what to run, and what to change. Try temperature `0.2` versus `1.2`, alter the attention query, add a document, create a tool, inspect memory, or compare retrieval results.

## What not to miss

**Tokens** are the model's units; **embeddings** are numeric vector representations; **logits** are unnormalized scores; **softmax** turns scores into probabilities; **attention** mixes information from context; **providers** hide local runtime details; **tools** create a controlled execution boundary; **memory** keeps relevant conversation state; **RAG** adds external documents before generation; and **evaluation** measures whether the system is working.

## Safety

The examples never expose unrestricted shell execution. Treat model output and documents as untrusted. Keep secrets out of prompts, validate structured output, use an allow-list of tools, restrict file access, and keep evaluation checks honest.

## Research direction

Once attention is clear, read [Attention Is All You Need](https://arxiv.org/abs/1706.03762). Then explore representation learning, retrieval evaluation, inference optimization, tool use, alignment, and scalable memory design.

## Capstone

`examples/simple_agent/` combines a local provider, safe calculator/time tools, conversation memory, and optional document retrieval. Extend it with a new read-only tool and write an evaluation checklist for a few realistic user tasks.

## Contributing

See `CONTRIBUTING.md`. Small, runnable, explanatory changes are preferred over new framework dependencies. Licensed under MIT.
