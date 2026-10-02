# 12. Evaluation and measuring system quality

A demo that works once is not enough. In real AI systems, we want to know whether a result is correct, grounded, useful, safe, fast, or cheap. This is the job of evaluation.

Evaluation is the discipline of turning vague ideas like "good" or "useful" into checkable tests. For beginners, the pattern is simple:

```text
example cases -> expected behavior -> scoring -> improvement loop
```

This chapter keeps the tests small and readable. We are not trying to build a full benchmark suite. We are showing the same idea used in research and production: measure a behavior, compare it against expectations, and iterate.

## Learning goals

By the end of this chapter, you should be able to:

- explain why evaluation matters in AI systems;
- distinguish a one-off demo from a measured system;
- describe the role of expected outputs and test cases;
- identify different kinds of evaluation such as correctness, grounding, and safety;
- understand why even a small benchmark is useful for iteration; and
- connect evaluation to earlier chapters on RAG, memory, and agent behavior.

## The central idea

A system can look impressive in a single run and still be unreliable. Evaluation introduces repeatable checks.

Examples of evaluation questions:

- Does the model answer the question correctly?
- Does it use the retrieved documents instead of guessing?
- Does the tool call obey the valid schema?
- Does the agent respond safely on a malicious prompt?
- Is the output fast enough and cheap enough?

The educational example in this folder uses a small set of sentence pairs and checks whether the model output matches the expected result in a simple way.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`evaluate.py`](./evaluate.py) | A tiny benchmark runner with a few cases and a simple success metric |
| [`../lab/embeddings.py`](../lab/embeddings.py) | The embedding helper reused for similarity-based checks |

## Prerequisites

You only need:

- Python 3.10 or newer;
- a terminal or command prompt; and
- the ideas from chapters 1–11: vectors, prompts, retrieval, tools, and agents.

No extra packages are required.

## Run the examples

From the repository root:

```bash
python 12_evaluation/evaluate.py
python 12_evaluation/evaluate.py --verbose
python 12_evaluation/evaluate.py --threshold 0.5
```

If your system uses `python3`, replace `python` with `python3`.

You can also test a single case in Python:

```python
from lab.embeddings import embed, cosine

score = cosine(embed("cats"), embed("cats"))
print(round(score, 3))
```

## What the script does

The simple demo defines a few test cases such as:

- `("cats", "cats")` -> should be very similar;
- `("cats", "quantum physics")` -> should be less similar;
- maybe a few more examples with the same concept and a distractor.

The program computes the similarity and reports whether the result is above a threshold. This is not a full benchmark, but it demonstrates the way evaluation turns judgments into numbers.

## Why this matters

A system's quality depends on more than whether a single response looks okay. Good evaluation helps answer questions like:

- Are we improving the model output over time?
- Are the retrieved documents actually relevant?
- Does the prompt produce valid JSON reliably?
- Are safety checks catching bad tool calls?
- Is a bigger context window helping or just costing more?

Without evaluation, it is hard to tell whether the system is getting better or just getting louder.

## Suggested experiments

Run each experiment before inspecting the result and write down your prediction:

1. Add a new case like `("dog", "cat")` and compare the result with `("dog", "dog")`.
2. Change the similarity threshold. Which cases pass or fail?
3. Add a manual case for a weird phrase such as `("AI", "banana")`.
4. Compare a good case, a weak case, and a clearly unrelated case.
5. Use a different metric such as exact string matching, token overlap, or retrieval hit rate.
6. Compare evaluation against a single demo run. Which is more informative?
7. Write a tiny function that counts how many cases pass.
8. Add a case for a prompt injection or tool-call failure and decide what "good" means.

## Common vocabulary

- **Evaluation:** measuring whether a system behaves as expected.
- **Benchmark:** a set of tests used to compare systems or versions.
- **Threshold:** a cutoff score used to decide pass or fail.
- **Metric:** a numerical measure of quality or behavior.
- **Grounded answer:** an answer supported by retrieved or trusted evidence.
- **Safety check:** a policy or programmatic check for unwanted behavior.

## Scope and limitations

This chapter intentionally does not implement:

- a large benchmark suite;
- human ratings or preference data;
- statistical significance tests;
- leaderboards and production metrics dashboards; or
- advanced evaluation frameworks.

The idea here is to make evaluation concrete and beginner-friendly before a learner moves on to more advanced benchmark design.

## Completion checklist

You are ready to finish the lab when you can explain, without copying the code:

- why a one-off demo is not enough;
- what a test case and a success threshold are;
- how evaluation helps compare system versions;
- why many metrics are needed in real AI systems; and
- how evaluation ties together the earlier lessons on model output, retrieval, tools, and memory.

