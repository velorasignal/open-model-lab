from lab.sampling import sample, softmax

if __name__ == "__main__":
    tokens = ["mat", "floor", "roof"]
    logits = [3.0, 1.0, 0.2]
    for temperature in [0.2, 1.2]:
        probabilities = softmax(logits, temperature)
        print(temperature, dict(zip(tokens, [round(x, 3) for x in probabilities])), sample(tokens, probabilities, seed=7))
