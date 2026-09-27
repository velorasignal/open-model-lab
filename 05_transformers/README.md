# 5. Attention and transformers

A transformer does not read words one at a time like a dictionary lookup. Instead, each token is compared to the others in the current context through **attention**. The model asks: “Which nearby tokens are most relevant to this one?” Then it mixes their information into a richer representation.

This chapter keeps the math small but faithful to the core idea: a query is compared against keys, the results are turned into weights, and those weights are used to combine values.

## Learning goals

By the end of this chapter, you should be able to:

- explain the purpose of attention in a transformer;
- distinguish a **query**, **key**, and **value**;
- compute a dot-product similarity between a query and each key;
- explain how softmax turns similarity scores into attention weights;
- describe why attention produces a weighted sum of values;
- compare a strong match with a weak match in a tiny example; and
- explain why this script is intentionally simplified compared with a real Transformer block.

## The central idea

Attention is a weighted lookup.

```text
query -> compare to each key -> softmax -> weighted sum of values
```

A tiny example is enough to see the pattern:

```text
query = [1, 0]
keys  = [[1, 0], [0, 1], [1, 1]]
values = [[10, 0], [0, 10], [5, 5]]
```

The model scores how similar the query is to each key. For a query like `[1, 0]`, the key `[1, 0]` is a strong match. The model gives that position more weight, then combines the corresponding values.

This is the same conceptual shape used in a real Transformer layer:

```text
token embeddings
    -> linear projections to query, key, value
    -> attention scores
    -> softmax weights
    -> mixed value vectors
```

The educational script below makes the math visible without hiding it behind a large framework or a massive model.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`attention_demo.py`](./attention_demo.py) | A beginner-friendly attention example with multiple queries and a simple explanation of the output |
| [`../lab/attention.py`](../lab/attention.py) | The reusable educational attention helper used in this lesson |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- the ideas from chapters 1–4: vectors, logits, probabilities, and simple Python functions.

No third-party packages are required.

## Run the examples

From the repository root:

```bash
python 05_transformers/attention_demo.py
python 05_transformers/attention_demo.py --query 1 0
python 05_transformers/attention_demo.py --query 0 1
```

If your system uses `python3`, replace `python` with `python3`.

You can also run the same ideas from Python:

```python
from lab.attention import attention

query = [1.0, 0.0]
keys = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
values = [[10.0, 0.0], [0.0, 10.0], [5.0, 5.0]]
print(attention(query, keys, values))
```

## Reading the output

The demo prints the attention score for each key, the softmax weights, and the final weighted value vector.

A typical result looks like this:

```text
Query: [1.0, 0.0]
Scores: [1.00, 0.00, 1.00]
Weights: [0.422, 0.155, 0.423]
Output: [6.34, 3.67]
```

This means the model paid the most attention to the two keys that best matched `[1, 0]` and combined their values.

## Why the values matter

The keys tell the model where to look. The values are the information to gather. In a real model, values are vectors containing a learned representation of a token or context position.

The formula is:

```text
score_i = query · key_i
weight_i = softmax(score_i)
output = sum(weight_i * value_i)
```

This is the heart of attention. The model is not just picking the most similar item; it is blending several positions according to a distribution.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Change the query from `[1, 0]` to `[0, 1]`. Which key becomes more important?
2. Set the query to `[1, 1]`. Which key or keys receive the strongest weights?
3. Increase the magnitude of one key. Does this change the attention pattern? Why or why not?
4. Replace one value vector with a very large or very small vector. Does the output change in the expected direction?
5. Compare this lesson with `04_language_models/language_model.py`. Which part of the model produces the scores?
6. Add a new key/value pair. How does the output change?
7. Try a query that is perpendicular to a key. What happens to the dot product?

## Common vocabulary

- **Query:** the representation being matched against other tokens.
- **Key:** a representation used to compare similarity with the query.
- **Value:** the information carried by a token or position and mixed in the output.
- **Attention score:** a similarity score between query and key.
- **Softmax:** a function that converts scores into positive weights that sum to `1`.
- **Attention weights:** the normalized importance assigned to each key.
- **Weighted sum:** combining values using the attention weights.
- **Self-attention:** attention where each token compares against other tokens in the same sequence.
- **Transformer block:** a stack of attention and feed-forward computations used in modern language models.

## Scope and limitations

This chapter intentionally does not implement:

- a full Transformer model or multi-head attention;
- learned projection matrices;
- causal masking or positional encoding;
- a complete feed-forward block and layer normalization;
- a large token vocabulary or production tokenizer; or
- training or optimization.

The goal is to make the central dynamic of attention clear before later chapters introduce larger local models and agent behavior.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- why attention compares a query to keys;
- why softmax is used to turn scores into weights;
- why values are combined with those weights;
- how a strong match changes the output; and
- why this example is a simplified attention mechanism rather than a full Transformer.
