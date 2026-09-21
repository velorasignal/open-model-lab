from lab.providers import OllamaProvider

# Reusable provider boundary: later modules depend on this interface, not Ollama details.
LocalLLM = OllamaProvider

if __name__ == "__main__": print(LocalLLM().generate("Explain inference in one sentence."))
