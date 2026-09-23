# 3. Embeddings

An embedding maps a piece of text, a token, or another object to a vector of numbers. Once the text is represented as numbers, a model can compare items by similarity, combine them with weights, and use them inside larger neural-network computations.

This chapter keeps the example intentionally small and deterministic. Instead of training a real embedding table, it uses a hash-based vector so you can inspect the mechanics without downloading a model or setting up a deep-learning stack.

## Learning goals

By the end of this chapter, you should be able to:

- explain what an embedding is in plain terms;
- describe how a token string becomes a numeric vector;
- explain why similarity is often measured with cosine similarity;
- compare related and unrelated phrases using the same embedding function;
- describe the difference between a toy educational embedding and a learned model embedding; and
- reason about why vector dimension and token overlap influence similarity.

## The central idea

A model needs numeric values, not raw text. A simple pipeline is:

```text
text -> tokenizer -> tokens -> embedding lookup -> vector
```

In this repository, the tiny tokenizer in `lab.embeddings` breaks text into pieces such as:

```text
"cats chase mice" -> ["cats", "chase", "mice"]
```

Then each token contributes to a vector. A basic educational version is:

```text
for each token:
    hash token -> index in vector
    add 1.0 to that slot
normalize the vector
```

The result is a vector with fixed length, for example 32 floats. This does not mean it is a learned semantic embedding, but it does show the same high-level idea: a token or phrase becomes a compact numeric representation.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`embedding_demo.py`](./embedding_demo.py) | A tiny similarity demo showing how phrase vectors compare |
| [`../lab/embeddings.py`](../lab/embeddings.py) | The tokenization and embedding functions reused by the lesson |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- a basic understanding of strings, lists, and loops.

No third-party packages are required.

## Run the demo

From the repository root:

```bash
python 03_embeddings/embedding_demo.py
```

If your system uses `python3`, replace `python` with `python3`.

You can also inspect a single comparison by editing the sample pairs in the script or by invoking the functions from another Python session:

```python
from lab.embeddings import embed, cosine

left = embed("cats chase mice")
right = embed("a cat hunts a mouse")
print(cosine(left, right))
```

## What the demo is measuring

The `embed` function produces a normalized vector based on the tokens in the input:

```python
vector = [0.0] * dimensions
for token in tokenize(text):
    digest = sha256(token)
    index = digest % dimensions
    vector[index] += 1.0
vector = vector / norm(vector)
```

This means:

- each token contributes to a few positions in the vector;
- repeated tokens increase the same entries;
- the final vector is normalized so length is stable; and
- different phrases may end up closer or farther apart depending on the overlap in hashed positions.

This is a clean teaching mechanism, not a trained semantic model. A real embedding table is learned from data and usually has dimensions such as 768, 1024, or larger.

## Why vector similarity matters

Similarity is computed by comparing the direction of two vectors. A common measure is cosine similarity:

```text
cosine(a, b) = a · b / (|a| * |b|)
```

This produces a value between `-1` and `1` for vectors in a common space. A cosine value near `1.0` means the vectors point in the same direction, and a value near `0.0` means they are less aligned.

In LLM systems, embeddings are used for:

- retrieval and search;
- semantic matching;
- nearest-neighbor lookup;
- model inputs after tokenization; and
- downstream training of language models.

## How this script works

The demo compares phrase pairs such as:

```python
pairs = [
    ("cats chase mice", "a cat hunts a mouse"),
    ("cats chase mice", "quantum physics"),
]
```

The script prints the cosine similarity for each pair. You can add your own comparison with a different phrase and observe how the score changes.

The educational hash-based embedding is deterministic. The same input always produces the same vector, which makes the examples easy to reason about and test.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Compare `"cats chase mice"` with `"a cat hunts a mouse"`. Why does it score higher?
2. Compare it with `"quantum physics"`. Why is the similarity lower?
3. Change the dimension from `32` to `8` or `128` in `embed()`. How does the collision risk change?
4. Compare very similar phrases like `"cat"` vs `"cats"` and `"cat"` vs `"dog"`.
5. Try a phrase with repeated words, such as `"cat cat cat"`. What happens to the vector?
6. Add a pair containing punctuation or capital letters. Does the tokenizer normalize them in a way that affects similarity?
7. Inspect the tokenization in `lab/embeddings.py` and trace where the hashing happens.

## Common vocabulary

- **Embedding:** a vector representation of data such as a word, sentence, or token.
- **Vector:** a list of numbers, often with a fixed length called the dimension.
- **Dimension:** the size of the vector; it is the number of numeric slots.
- **Cosine similarity:** a measure of how aligned two vectors are.
- **Normalization:** scaling a vector so its length is 1.0 or otherwise standardized.
- **Hashing:** converting input data into a pseudo-random index using a deterministic function.
- **Learned embedding:** a vector table trained from data in a real model.
- **Toy embedding:** a simple educational representation for demonstration and understanding.

## Scope and limitations

This lesson intentionally does not implement:

- a trained embedding table;
- gradient-based learning;
- large-scale retrieval indexes;
- a production semantic-search stack; or
- exact model-specific embeddings.

The goal is to show the core idea: semantic text can be represented numerically, and similarity can be measured in vector space. Once that is clear, the next step is to study learned embeddings in larger transformer models.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- what an embedding is;
- how a string becomes a vector in this educational example;
- why cosine similarity is useful;
- how token overlap changes similarity; and
- why a toy hashing embedding is different from a learned embedding in a real model.
