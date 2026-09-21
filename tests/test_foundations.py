from lab.embeddings import cosine, embed, tokenize
from lab.rag import Retriever


def test_tokenizer_and_embedding_are_deterministic():
    assert tokenize("Hello!") == ["hello", "!"]
    assert embed("same") == embed("same")
    assert cosine(embed("same"), embed("same")) == 1.0


def test_retriever_returns_a_document():
    result = Retriever(["cats", "physics"]).search("cats", k=1)
    assert result == ["cats"]
