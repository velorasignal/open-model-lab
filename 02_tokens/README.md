# 2.Tokens

Models do not receive raw strings; tokenizers turn text into token units and IDs. This tiny tokenizer is for intuition, not a production tokenizer.

```bash
python 02_tokens/token_explorer.py "The cat sat on the mat."
```

**Experiment:** punctuation, spelling, and long words can change token boundaries.
