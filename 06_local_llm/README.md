# 06 — Local LLMs

Ollama provides a local inference server; Python sends a prompt over HTTP. It is not the model itself. See `docs/local-models.md`.

```bash
ollama pull gemma3:1b
python 06_local_llm/chat.py --model gemma3:1b
```

The provider interface also has an offline demo, so you can inspect the application boundary without a model.
