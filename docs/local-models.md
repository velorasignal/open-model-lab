# Local models in plain language

A local model download usually includes learned **weights**, a **tokenizer**, metadata, and an inference format/engine. A checkpoint is a saved set of weights. **Quantization** stores weights with fewer bits, reducing RAM and sometimes quality. GGUF is a common file format in the llama.cpp ecosystem. The context window is the maximum amount of tokenized input and generated context the model can use.

CPU inference works on an ordinary laptop but may be slow. A GPU can accelerate matrix operations and needs VRAM. Smaller quantized models are useful for learning because they start quickly and fit on more machines; they are not automatically as capable as larger models.

Install Ollama from [ollama.com](https://ollama.com/), start the application, then choose a current small model shown by `ollama list` or the Ollama library. This lab defaults to `gemma3:1b` as an example, but `OLLAMA_MODEL` or `--model` can change it.

The client uses Ollama's stable local `POST /api/generate` endpoint. If the server is unavailable, the error explains how to start it. No model is downloaded by this repository.
