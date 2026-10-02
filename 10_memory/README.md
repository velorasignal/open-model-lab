# 10. Memory and conversational state

A model does not remember your previous messages on its own unless the application keeps the conversation state and passes it back in. This is where memory enters the system. In a real app, memory is not just a list of messages; it is a design choice about what to preserve, what to summarize, and what to discard.

This chapter keeps the idea clean and readable. We do not build a huge memory store. We show the basic pattern behind chat history, short-term context, and stateful applications.

```text
user message
    -> add to memory
    -> prompt includes recent history
    -> model sees context
    -> answer is built with state in mind
```

The purpose of memory is not to make the model "remember" in a human-like sense. The purpose is to let your app provide the relevant context for the next turn.

## Learning goals

By the end of this chapter, you should be able to:

- explain the difference between short-term memory and long-term memory;
- describe why a conversation history is useful in chat applications;
- understand how prompt assembly depends on stored messages;
- identify the difference between model weights and application state;
- reason about why too much memory can be noisy or expensive; and
- connect memory to the larger agent loop from chapter 09.

## The central idea

There are several kinds of memory in an AI system:

- model parameters (learned weights);
- short-term conversation memory (recent messages);
- persistent storage (database or document store);
- retrieval memory (documents fetched by RAG);
- tool state (the result of a function call).

The example in this chapter focuses on the simplest and most common one: conversation memory.

```text
conversation history -> prompt assembly -> model -> response
```

A memory object stores messages such as user, assistant, and tool outputs. The app can then include that history in the next prompt. This is how a chatbot appears to remember what was just discussed.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`memory.py`](./memory.py) | A tiny in-memory conversation log and prompt builder |
| [`../lab/memory.py`](../lab/memory.py) | The reusable `ConversationMemory` class used by later lessons |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- the ideas from chapters 1–9: functions, prompts, structured output, and safe tool use.

No third-party packages are required.

## Run the examples

From the repository root:

```bash
python 10_memory/memory.py
python 10_memory/memory.py --limit 2
python 10_memory/memory.py --clear
```

If your system uses `python3`, replace `python` with `python3`.

You can also run a few manual examples in a Python shell:

```python
from lab.memory import ConversationMemory

memory = ConversationMemory()
memory.add("user", "My name is Ada.")
memory.add("assistant", "Nice to meet you, Ada.")
print(memory.prompt())
```

## What the script does

The script creates a `ConversationMemory` object and adds messages. It then prints the assembled prompt. In a real app, the prompt would be sent to the model. The usefulness is simple:

- the model sees the conversation history;
- the app can decide how much context to include;
- late messages can override earlier assumptions; and
- state flows through the conversation in a controlled way.

This is not the same as a database or a long-term memory system, but it is the same mental model used by chat interfaces.

## Why memory matters

Without memory, a model sees each message in isolation. That makes the bot forgetful and brittle. With memory, the app can carry a small slice of previous dialogue forward.

Good uses of memory:

- conversation context;
- user preferences;
- recent tasks or follow-up questions;
- tool results used in a multi-step flow.

Poor or risky uses of memory:

- storing sensitive secrets in plain text;
- keeping infinite context without trimming it;
- mixing unrelated conversations together;
- forgetting to remove stale or incorrect facts.

The memory layer sits between the model and the rest of the app. It is an application concern, not magic learning inside the model.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Add three user messages and two assistant messages. What does the final prompt look like?
2. Compare a memory with only the last turn versus a memory with the full conversation.
3. Add a tool result to memory and inspect how it would appear in a model prompt.
4. Remove older messages with a limit or summarizer. Why does this reduce cost and noise?
5. Compare this chapter with chapter 09. Which part is the agent loop, and which part is the memory?
6. Add a fake long-term memory store and decide which entries should be summarized.
7. Write a helper that shows only the last 3 messages.
8. Add a message with repeated or contradictory information. Which message should be trusted more?

## Common vocabulary

- **Conversation memory:** stored prior messages available to the model.
- **Prompt assembly:** turning stored messages into text for a model call.
- **Short-term memory:** recent interaction state kept within the current session.
- **Long-term memory:** persistent state stored outside the active chat.
- **Context window:** the max number of tokens the model can consider at once.
- **State:** information the app keeps between requests or turns.

## Scope and limitations

This chapter intentionally does not implement:

- persistent databases or retrieval indexes;
- automatic summarization of long histories;
- per-user memory in a production system;
- security controls for stored secrets; or
- a full event-sourced memory architecture.

The goal is to show the core idea clearly: a model becomes context-aware when the app gives it the right history.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- why memory is different from learned model weights;
- how conversation history is assembled into a prompt;
- why context limits matter for memory choices;
- when memory is useful and when it becomes noisy; and
- how memory supports agents and retrieval-based systems.

