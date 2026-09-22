from __future__ import annotations

from math import exp


def sigmoid(x: float) -> float:
    """Standard activation function used in binary classification."""
    return 1.0 / (1.0 + exp(-x))


def relu(x: float) -> float:
    """Rectified Linear Unit used in hidden layers of neural networks."""
    return max(0.0, x)


def softmax(values: list[float]) -> list[float]:
    """Convert logits into probabilities that sum to 1."""
    exps = [exp(v) for v in values]
    total = sum(exps)
    return [v / total for v in exps]


def neuron(inputs: list[float], weights: list[float], bias: float = 0.0) -> float:
    """A single artificial neuron with weighted sum followed by sigmoid."""
    z = bias + sum(x * w for x, w in zip(inputs, weights))
    return sigmoid(z)


def dense_layer(inputs: list[float], weights: list[list[float]], biases: list[float]) -> list[float]:
    """Compute a fully connected layer output."""
    return [
        sum(x * w for x, w in zip(inputs, row)) + bias
        for row, bias in zip(weights, biases)
    ]


def simple_mlp(inputs: list[float]) -> list[float]:
    """Simple two-layer foundation neural network example.

    - Hidden layer: ReLU activation
    - Output layer: Sigmoid activation for binary output
    """
    hidden_weights = [[0.6, -0.2], [-0.4, 0.8], [0.3, 0.5]]
    hidden_biases = [0.1, -0.2, 0.0]
    output_weights = [[0.5], [-0.3], [0.7]]
    output_bias = 0.2

    hidden = dense_layer(inputs, hidden_weights, hidden_biases)
    hidden_activated = [relu(value) for value in hidden]

    output_logits = [
        sum(value * weight for value, weight in zip(hidden_activated, row)) + output_bias
        for row in output_weights
    ]
    return [sigmoid(value) for value in output_logits]


if __name__ == "__main__":
    print("sigmoid(-2) ->", round(sigmoid(-2), 3))
    print("sigmoid(0) ->", round(sigmoid(0), 3))
    print("sigmoid(2) ->", round(sigmoid(2), 3))
    print("relu(-1.5) ->", relu(-1.5))
    print("softmax([1, 2, 3]) ->", [round(v, 3) for v in softmax([1.0, 2.0, 3.0])])
    print("neuron([0.5, 1.0], [0.7, -0.3], bias=0.2) ->", round(neuron([0.5, 1.0], [0.7, -0.3], bias=0.2), 3))
    print("simple_mlp([0.8, 1.2]) ->", [round(v, 3) for v in simple_mlp([0.8, 1.2])])
