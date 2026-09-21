# 10 — Memory

Conversation history is short-term application state. Persistent memory is stored state. RAG knowledge is retrieved document context. Model parameters are learned weights. These are different things: adding a message does not retrain a model.

Run `python 10_memory/memory.py` and inspect the prompt assembled from messages.
