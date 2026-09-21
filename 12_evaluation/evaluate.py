from lab.embeddings import cosine, embed

CASES = [("cats", "cats"), ("cats", "quantum physics")]
if __name__ == "__main__":
    for left, right in CASES: print(left, right, round(cosine(embed(left), embed(right)), 3))
