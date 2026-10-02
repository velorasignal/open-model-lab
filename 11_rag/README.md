# 11. RAG and retrieval-augmented generation

A language model has a fixed set of parameters. It does not automatically know your private files, your notes, or the latest product spec unless you provide that information. Retrieval-augmented generation (RAG) addresses this by retrieving relevant documents before generation.

The pipeline is simple but important:

```text
documents -> chunks -> embeddings -> vector search -> relevant context -> prompt -> model -> answer
```

This chapter does not build a production vector database. Instead, it shows the beginner-level pattern that many real systems follow.

## Learning goals

By the end of this chapter, you should be able to:

- explain what RAG is in plain terms;
- describe why a model's parameters are not a live document index;
- explain what a chunk is and why chunking matters;
- describe the role of embeddings in retrieval;
- contrast retrieval from instruction-following; and
- connect RAG to both memory and tool use in a larger AI app.

## The central idea

RAG is useful when the answer depends on context that is not fully inside the model. Common examples:

- internal docs;
- support knowledge bases;
- project notes;
- product manuals; or
- private company data.

The app does this:

1. split documents into smaller chunks;
2. embed the chunks;
3. compare the user question with those embeddings;
4. fetch the best matches;
5. add that text to the model prompt;
6. let the model answer using the retrieved context.

This is often more reliable than asking the model to remember everything from scratch.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`ingest.py`](./ingest.py) | Breaking text into chunks before retrieval |
| [`retrieve.py`](./retrieve.py) | Asking a simple retriever for the most similar documents |
| [`rag.py`](./rag.py) | Combining retrieval and a demo provider into a tiny RAG flow |
| [`../lab/rag.py`](../lab/rag.py) | The educational retriever and chunking helpers |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- the ideas from chapters 1–10: vectors, embeddings, prompts, memory, and the general model pipeline.

No special libraries are required for this lesson.

## Run the examples

From the repository root:

```bash
python 11_rag/ingest.py
python 11_rag/retrieve.py
python 11_rag/rag.py --question "What does retrieval do?"
python 11_rag/rag.py --question "How is memory different from RAG?" --top-k 2
```

If your system uses `python3`, replace `python` with `python3`.

You can also inspect the exact steps from Python:

```python
from lab.rag import Retriever, chunk

texts = [
    "RAG retrieves relevant documents before answering.",
    "Conversation memory keeps recent chat context.",
]
result = Retriever(texts).search("What is retrieval?", k=1)
print(result)
```

## What the scripts do

### 1. Ingest

`ingest.py` splits documents into chunks using a simple token or word chunker. In production, chunking is a big design decision because a chunk that is too long may hide the best evidence, while a chunk that is too short may lose context.

### 2. Retrieve

`retrieve.py` takes a query and a set of documents. It compares the embedding of the query with each document embedding and returns the top matches. This is a simple nearest-neighbor search.

### 3. RAG

`rag.py` combines retrieval with a demo provider. It fetches the most relevant context, adds it to a prompt, and asks the model to answer the user question using that information.

## Why this matters

A model can be very capable without being a real-time document store. RAG solves a specific problem: the answer may depend on information outside the model's parameters and outside the current conversation.

This is why many AI applications use a retrieval layer:

- external docs are often fresher than model weights;
- private knowledge can be kept away from model training data;
- retrieval provides a traceable source of context; and
- the app can combine memory, tools, and documents in one response.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Change the chunk size and compare the output. Why might smaller chunks be better for some queries?
2. Add a new document about model safety and ask a question related to it.
3. Try a query that matches only one document. How does the ranking change?
4. Compare a question about a local concept with one about a global concept. Which document should rank higher?
5. Compare this chapter with chapter 10. What is the difference between memory and RAG?
6. Change `k` from `1` to `3`. What happens to the context length and answer quality?
7. Add a duplicate and a noisy document. Which one should rank higher?
8. Write your own helper that returns the scores alongside the matched documents.

## Common vocabulary

- **RAG:** retrieval-augmented generation, or using external context in a model answer.
- **Chunking:** splitting a long document into smaller pieces.
- **Embedding:** a numeric representation of text used to compare meaning.
- **Retriever:** code that chooses relevant chunks for a query.
- **Context window:** the maximum amount of retrieved text a model can consider in one request.
- **Grounding:** basing an answer on real documents or evidence rather than only model memory.

## Scope and limitations

This chapter intentionally does not implement:

- a production vector database or hybrid search index;
- metadata filters and access control;
- chunk overlap optimization and reranking;
- large-scale document ingestion pipelines; or
- rigorous evaluation of retrieval quality.

The focus is on the core pattern: retrieve relevant evidence, include it in the prompt, and answer with that context in mind.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- why a model does not inherently know all current documents;
- how chunks and embeddings support retrieval;
- why retrieval is different from conversation memory;
- how a document context gets added to a prompt; and
- why RAG is useful when information is external to the model.

