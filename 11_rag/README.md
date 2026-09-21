# 11 — RAG

Retrieval augmented generation is **documents → chunks → embeddings → vector search → context → model**. It exists because a model's parameters are not a live, private document index. This lab uses a tiny hash embedding and cosine search so the mechanism is visible.

```bash
python 11_rag/rag.py --question "What does inference mean?"
```

**Experiment:** add a document, change `k`, or replace the embedder. A real system needs better embedding models, chunking, metadata, access control, and retrieval evaluation.
