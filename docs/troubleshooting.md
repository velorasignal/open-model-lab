# Troubleshooting

- **Ollama does not appear to be running:** start Ollama, confirm `ollama list`, pull a model, and retry.
- **Model not found:** pass the exact installed tag, for example `--model gemma3:1b`.
- **Slow response:** use a smaller quantized model, reduce the prompt, or accept that CPU inference is slower than a cloud GPU.
- **PowerShell activation blocked:** use `Set-ExecutionPolicy -Scope Process Bypass`, or invoke `.venv\\Scripts\\python.exe` directly.
- **Import errors:** run commands from the repository root and install with `python -m pip install -e .`.

Never “fix” a setup problem by putting an API key into source code.
