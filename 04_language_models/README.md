# 04 — Language models

A language model estimates the next-token distribution. Logits are raw scores; softmax makes probabilities. Temperature changes how sharply the distribution is sampled. This tiny example is not trained.

**Experiment:** use temperatures `0.2` and `1.2`, then change the logits.
