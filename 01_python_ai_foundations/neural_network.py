from __future__ import annotations

from math import exp


# ---------------------------
# 1) Activation functions
# ---------------------------

def sigmoid(x: float) -> float:
    """Convert a real number into a value between 0 and 1.

    This is useful when we want a probability-like output.
    Example: sigmoid(0) == 0.5
    """
    return 1.0 / (1.0 + exp(-x))


def relu(x: float) -> float:
    """Rectified Linear Unit.

    If x > 0, keep it. If x <= 0, return 0.
    It is one of the most common activation functions in hidden layers.
    """
    return max(0.0, x)


# ---------------------------
# 2) Probability conversion
# ---------------------------

def softmax(values: list[float]) -> list[float]:
    """Turn raw scores into probabilities that sum to 1.

    Example:
        softmax([1.0, 2.0, 3.0])
    gives values that behave like class probabilities.
    """
    exps = [exp(v) for v in values]
    total = sum(exps)
    return [v / total for v in exps]


# ---------------------------
# 3) Single neuron
# ---------------------------

def neuron(inputs: list[float], weights: list[float], bias: float = 0.0) -> float:
    """A simple neuron.

    Formula:
        z = bias + sum(input_i * weight_i)
        output = sigmoid(z)

    This is the basic building block of a neural network.
    """
    z = bias + sum(x * w for x, w in zip(inputs, weights))
    return sigmoid(z)


# ---------------------------
# 4) A whole layer of neurons
# ---------------------------

def dense_layer(inputs: list[float], weights: list[list[float]], biases: list[float]) -> list[float]:
    """Compute one fully connected layer.

    Each output neuron does:
        output = bias + sum(input_i * weight_i)

    Here, `weights` is a matrix where each row is one neuron.
    """
    return [
        sum(x * w for x, w in zip(inputs, row)) + bias
        for row, bias in zip(weights, biases)
    ]


# ---------------------------
# 5) Tiny neural network example
# ---------------------------

def simple_mlp(inputs: list[float]) -> list[float]:
    """A tiny MLP (Multi-Layer Perceptron) example.

    Structure:
    1. Input layer: takes the raw numbers
    2. Hidden layer: apply ReLU
    3. Output layer: apply sigmoid

    This is not a trained model yet. It is just a simple demonstration
    of how layers work together.
    """
    # Hidden layer parameters
    hidden_weights = [[0.6, -0.2], [-0.4, 0.8], [0.3, 0.5]]
    hidden_biases = [0.1, -0.2, 0.0]

    # Output layer parameters
    output_weights = [[0.5], [-0.3], [0.7]]
    output_bias = 0.2

    # First, compute hidden values
    hidden = dense_layer(inputs, hidden_weights, hidden_biases)

    # Apply activation function to hidden layer
    hidden_activated = [relu(value) for value in hidden]

    # Then compute output logits and apply sigmoid
    output_logits = [
        sum(value * weight for value, weight in zip(hidden_activated, row)) + output_bias
        for row in output_weights
    ]
    return [sigmoid(value) for value in output_logits]


if __name__ == "__main__":
    # A few single function examples
    print("Example 1: sigmoid")
    print("sigmoid(-2) ->", round(sigmoid(-2), 3))
    print("sigmoid(0) ->", round(sigmoid(0), 3))
    print("sigmoid(2) ->", round(sigmoid(2), 3))

    print("\nExample 2: ReLU")
    print("relu(-1.5) ->", relu(-1.5))
    print("relu(3.0) ->", relu(3.0))

    print("\nExample 3: softmax")
    print("softmax([1, 2, 3]) ->", [round(v, 3) for v in softmax([1.0, 2.0, 3.0])])

    print("\nExample 4: one neuron")
    print(
        "neuron([0.5, 1.0], [0.7, -0.3], bias=0.2) ->",
        round(neuron([0.5, 1.0], [0.7, -0.3], bias=0.2), 3),
    )

    print("\nExample 5: tiny neural network")
    print("simple_mlp([0.8, 1.2]) ->", [round(v, 3) for v in simple_mlp([0.8, 1.2])])

    # Small learning note:
    # - weights decide how important each input is
    # - bias shifts the value before activation
    # - activation functions introduce non-linearity
    # - hidden layers help the model learn more complex patterns
