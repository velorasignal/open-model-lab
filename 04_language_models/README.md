# 4. Language models

A language model assigns scores to possible next tokens. It uses the tokens that came before to estimate what should come next:

```text
prompt -> logits -> probabilities -> next-token choice
```

This chapter turns the ideas from the first three chapters into a small, runnable next-token prediction experiment. The model is intentionally hand-written: it is a **toy language model**, not a trained neural network or a replacement for an LLM.

## Learning goals

By the end of this chapter, you should be able to:

- explain why a language model predicts one token at a time;
- distinguish a **logit** from a probability;
- explain how softmax converts scores into a probability distribution;
- describe how temperature changes the sharpness of that distribution;
- compare greedy selection with seeded random sampling;
- read a small context-to-logits model; and
- explain why this example is useful for learning but is not a production LLM.

## The central idea

A language model estimates a conditional distribution:

```text
P(next token | tokens already seen)
```

For example, after the prompt `The cat sat on the`, a model might give a high score to `mat` and smaller scores to `floor` and `roof`.

The scores produced before softmax are called **logits**. They are not probabilities and can be negative, greater than `1`, or any other real number. Softmax turns them into non-negative values that add up to `1`:

```text
probability_i = exp(logit_i / temperature)
                --------------------------------
                sum of all exp(logit_j / temperature)
```

A larger logit still means a more likely token. Temperature controls how strongly the largest score dominates:

- a low temperature such as `0.2` makes the distribution sharp and predictable;
- a high temperature such as `1.2` spreads more probability across alternatives; and
- temperature must be positive.

The shared `lab.sampling.softmax` function uses a numerically safer version of this calculation: it subtracts the largest scaled logit before calling `exp`.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`language_model.py`](./language_model.py) | A readable context-to-logits toy model, probability conversion, greedy choice, and seeded sampling |
| [`next_token_demo.py`](./next_token_demo.py) | A command-line experiment that prints probability tables at one or more temperatures |
| [`../lab/sampling.py`](../lab/sampling.py) | Reusable softmax and weighted sampling helpers used by this lesson and later lessons |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- the ideas from chapters 1–3: functions, lists, tokens, and vectors.

No third-party package is required. The example uses only the Python standard library and the small shared `lab` package.

## Run the examples

Run these commands from the repository root:

```bash
python 04_language_models/language_model.py
python 04_language_models/next_token_demo.py
```

On systems where Python 3 is invoked as `python3`, replace `python` with `python3`.

### Try different prompts and temperatures

```bash
python 04_language_models/next_token_demo.py --prompt "The cat sat on the" --temperature 0.2 1.2
python 04_language_models/next_token_demo.py --prompt "The dog chased the" --temperature 0.5 1.0 2.0 --seed 7
```

The prompt selects a row in the tiny hand-written model. Unknown prompts use a neutral fallback row so the program remains useful while you experiment.

### Inspect the raw scores

```bash
python 04_language_models/next_token_demo.py --show-logits
```

The program prints the logits, their softmax probabilities, the greedy choice, and a randomly sampled choice. The random choice is reproducible when `--seed` is supplied.

## Read the code in four steps

1. `toy_next_token_logits` maps a short context to candidate tokens and logits. This is the model's pretend prediction step.
2. `probabilities_for_prompt` calls `softmax` with a temperature. This turns scores into a distribution.
3. `greedy_next_token` chooses the largest probability. It always makes the same choice for the same input.
4. `sample_next_token` uses the distribution to make a weighted choice. A seed makes the experiment repeatable.

This is the same high-level shape used by a real autoregressive language model, even though a real model obtains logits from many learned layers rather than a dictionary of hand-written values.

## Greedy decoding versus sampling

Suppose the candidate probabilities are:

```text
mat    0.70
floor  0.20
roof   0.10
```

Greedy decoding always returns `mat`. Sampling usually returns `mat`, but occasionally returns one of the alternatives. Sampling can make generated text less repetitive, while greedy decoding is easier to reproduce and inspect.

The example uses a seeded `random.Random` instance. That is important for teaching and testing: it gives us randomness without changing Python's global random state.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Compare temperatures `0.2`, `1.0`, and `2.0`. Which distribution is most concentrated?
2. Change one logit in `language_model.py`. Which token becomes more likely?
3. Set all logits to the same value. What should softmax return?
4. Use `--seed 7` twice. Why is the sampled token the same both times?
5. Remove the seed. Why can the sampled token change between runs?
6. Try an unknown prompt. Why does the fallback distribution keep the program running?
7. Change `greedy_next_token` to choose from logits instead of probabilities. Does the result change? Why not?
8. Add a new context row and a new candidate token. What other parts of the program need to change?
9. Compare this lesson with `05_transformers/attention_demo.py`. Which part of a real model would produce context-dependent logits?

## Common vocabulary

- **Language model:** a model that estimates the likelihood of token sequences, commonly by predicting the next token.
- **Context:** the tokens or text already provided to the model.
- **Candidate token:** one possible token that could be generated next.
- **Logit:** an unnormalized score produced before softmax.
- **Softmax:** a function that converts scores into values that sum to `1`.
- **Probability distribution:** non-negative values whose total is `1`.
- **Temperature:** a positive scaling value that controls how flat or sharp softmax is.
- **Greedy decoding:** selecting the highest-scoring candidate every time.
- **Sampling:** selecting a candidate according to its probability.
- **Autoregressive generation:** generating one token, adding it to the context, and predicting again.
- **Vocabulary:** the set of tokens a model can predict.

## Scope and limitations

This chapter intentionally does not implement:

- a trained neural network or Transformer;
- a production tokenizer or model vocabulary;
- a loss function, dataset, backpropagation, or optimizer;
- beam search, top-k, or nucleus (top-p) sampling;
- multiple generated tokens with a chat template; or
- a claim that the hand-written scores contain language understanding.

The goal is to make the final step of the prediction pipeline visible before the repository introduces attention and Transformer-style models.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- why logits are not probabilities;
- why softmax outputs add up to `1`;
- how temperature changes a distribution;
- when greedy decoding and sampling differ; and
- why a real language model needs learned parameters and a much larger vocabulary.
