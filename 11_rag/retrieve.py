from lab.rag import Retriever

if __name__ == "__main__":
    print(Retriever(["Inference runs fixed model weights.", "RAG retrieves external context."]).search("How does retrieval work?"))
