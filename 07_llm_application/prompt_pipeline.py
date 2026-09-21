from lab.providers import DemoProvider

if __name__ == "__main__":
    question = "What is inference?"
    prompt = f"Answer this beginner question in two sentences: {question}"
    print(DemoProvider().generate(prompt))
