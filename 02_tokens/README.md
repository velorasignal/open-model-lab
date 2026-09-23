# 2. Tokens

A language model does not read a raw string as a human does. Before a prompt reaches the model, a **tokenizer** turns the string into a sequence of tokens, and a vocabulary maps each token to an integer ID:

```text
"Cats sleep." -> ["cats", "sleep", "."] -> [42, 817, 13]
```

Those IDs are then used to look up vectors called embeddings. The model processes the vectors, not the original characters directly.

This chapter uses a deliberately small, readable tokenizer. It is designed to make the ideas visible, not to reproduce the subword tokenizer used by a production LLM.

## Learning goals

By the end of this chapter, you should be able to:

- explain why text must be tokenized before a model can process it;
- distinguish characters, words, tokens, and token IDs;
- describe why whitespace is usually not preserved as a separate token here;
- predict how punctuation, capitalization, numbers, and symbols affect boundaries;
- explain why one word is not necessarily one token in a real language model;
- inspect token positions and compare two pieces of text; and
- explain how token count contributes to a model's context-window limit and cost.

## The central idea

A tokenizer is a deterministic function:

```text
text -> token pieces -> integer IDs
```

For the tiny tokenizer in `lab.embeddings`, the first step is approximately:

```text
"Hello, AI!" -> ["hello", ",", "ai", "!"]
```

It lowercases text, keeps runs of letters/numbers/underscores together, and makes each non-whitespace symbol its own token. The explorer can also assign **toy IDs** to the tokens in the current example. These IDs are useful for learning the pipeline, but they are not IDs from a real model vocabulary.

A simplified real-model pipeline is:

```text
characters
    -> tokenizer
    -> token IDs
    -> embedding vectors
    -> neural network
    -> logits for the next token
```

Tokenization happens before embeddings, attention, and next-token prediction. That is why understanding token boundaries is an important foundation for understanding LLMs.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`token_explorer.py`](./token_explorer.py) | A command-line microscope for token boundaries, spans, toy IDs, statistics, and comparisons |
| [`../lab/embeddings.py`](../lab/embeddings.py) | The tiny `tokenize` function reused by later lessons and the deterministic educational embedding |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- a basic understanding of strings, lists, loops, and regular expressions.

No third-party packages are required.

## Run the explorer

Run these commands from the repository root:

```bash
python 02_tokens/token_explorer.py "The cat sat on the mat."
python 02_tokens/token_explorer.py "Hello, AI! 42"
```

If your system uses `python3`, replace `python` with `python3`.

With no text argument, the script uses a small default example:

```bash
python 02_tokens/token_explorer.py
```

### Show toy IDs and statistics

```bash
python 02_tokens/token_explorer.py --ids --stats "Hello, AI! Hello"
```

The IDs are assigned only for the displayed text. They illustrate the shape of the data passed to an embedding lookup; they are not stable IDs from an LLM vocabulary.

### Compare several inputs

```bash
python 02_tokens/token_explorer.py \
  --compare "I like cats." \
  --compare "I like cat's!"
```

Repeat `--compare` for each additional text. The positional text, when supplied, is shown first.

### Machine-readable output

```bash
python 02_tokens/token_explorer.py --json --ids "Token counts are useful."
```

The JSON form is convenient when experimenting from another script. It includes the original text, tokens, character spans, and toy IDs.

## Reading the output

For an input such as `Hello, AI!`, the explorer shows a table similar to:

```text
  # token             characters  toy_id
  0 hello             [0:5]       1
  1 ,                 [5:6]       0
  2 ai                [7:9]       2
  3 !                 [9:10]      3
```

- **index** is the token's position in this sequence;
- **token** is the text piece after the tiny tokenizer lowercases it;
- **characters** is the half-open span in the original input, useful for seeing what happened to spaces; and
- **toy_id** is a local integer assigned by the explorer when `--ids` is requested.

The comma and exclamation mark are tokens. The space between the comma and `AI` is not a token in this implementation. Real tokenizers make different choices: some encode whitespace together with a following word, and many split words into subword pieces.

## What counts as a token here?

The educational rule is:

```text
[A-Za-z0-9_]+     one token for a run of ASCII letters, digits, or `_`
[^\\w\\s]         one token for each non-word, non-whitespace character
```

Examples:

| Input | Tiny-tokenizer intuition |
| --- | --- |
| `Hello` | `hello` |
| `hello-world` | `hello`, `-`, `world` |
| `42.5` | `42`, `.`, `5` |
| `can't` | `can`, `'`, `t` |
| `:)` | `:`, `)` |
| `New\nYork` | `new`, `york` |

Capitalization is normalized because this tokenizer calls `.lower()`. Punctuation is retained because it can change meaning and sentence structure. Whitespace separates pieces but is discarded.

## Tiny tokenizer versus production tokenizer

This example is intentionally simpler than the tokenizers used by GPT-style or other modern models. Production tokenizers commonly use a learned or carefully designed **subword** vocabulary, such as byte-pair encoding (BPE), WordPiece, or an equivalent scheme. A long or uncommon word may therefore become several pieces:

```text
unfamiliarword -> ["un", "familiar", "word"]  # illustrative only
```

There is no universal token boundary or universal token ID. The result depends on the model and its tokenizer vocabulary. Never use this tiny tokenizer to estimate the exact token count for a particular API or downloaded model; use that model's own tokenizer.

Token count still matters because a model's context window is measured in tokens. More tokens can mean less room for an answer, more memory use, and sometimes higher usage cost.

## Suggested experiments

Run each experiment before inspecting the output and write down your prediction:

1. Compare `"The cat sat."` with `"The cat sat!"`. Which token changes?
2. Compare `"AI"` with `"ai"`. Why do they produce the same tiny tokens?
3. Compare `"long-word"` with `"long word"`. What happens to the hyphen and space?
4. Try `"42"`, `"42.0"`, and `"42%"`. How many tokens does each produce?
5. Try an emoji, accented text, or non-Latin text. What does this ASCII-focused tokenizer miss?
6. Use `--stats` on a sentence and calculate the average characters per token.
7. Use `--compare` to find a change that adds one token without adding many characters.
8. Open `lab/embeddings.py` and trace how the token list is turned into a deterministic vector.

## Common vocabulary

- **Character:** one symbol in the original string.
- **Whitespace:** spaces, tabs, and line breaks used to separate text.
- **Token:** a text unit selected by a tokenizer; it may be a character, word, punctuation mark, or subword.
- **Tokenization:** converting text into a sequence of tokens.
- **Vocabulary:** the collection of token pieces known to a tokenizer.
- **Token ID:** the integer index assigned to a vocabulary entry.
- **Subword:** a token representing part of a word.
- **Context window:** the maximum number of tokens a model can consider in one request and generation context.
- **Embedding:** a learned or generated vector representation looked up from token IDs.
- **Tokenizer vocabulary:** a model-specific mapping; IDs from one model cannot be assumed to work for another.

## Scope and limitations

This lesson intentionally does not implement:

- a production BPE, WordPiece, or byte-level tokenizer;
- a trained vocabulary or model-specific token IDs;
- Unicode-aware linguistic segmentation;
- tokenization of chat templates and special control tokens; or
- an exact context-window or API billing calculator.

The goal is transparency. Once these boundaries are clear, inspect a real model's tokenizer to see how production systems extend the same basic pipeline.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- why a model receives token IDs rather than a raw Python string;
- why punctuation and whitespace affect token sequences;
- why token IDs belong to a particular vocabulary;
- why a real word can become multiple subword tokens; and
- why token count matters for context windows and inference.
