# Concepts

A model is a parameterized function. Training adjusts parameters using data and an objective; inference runs the fixed parameters on new input. An LLM predicts a probability distribution for the next token, not a sentence from a database. A Transformer uses attention to let token representations mix information from relevant context.

A local AI application surrounds the model with ordinary software: prompts, parsers, validation, tools, state, retrieval, and evaluation. Those parts can produce useful behavior without being intelligence inside the weights. See the numbered lessons for executable versions.
