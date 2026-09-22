# 1. Python and AI Foundations

This chapter introduces the smallest useful building blocks behind machine-learning models. It starts with ordinary Python functions and gradually connects them to the ideas used in neural networks: inputs, weights, biases, activations, layers, predictions, and inference.

The examples are intentionally small enough to read line by line. You do not need a machine-learning framework to understand the core calculations shown here.

## Learning goals

By the end of this chapter, you should be able to:

- describe a model as a function that maps inputs to outputs;
- explain the difference between a feature, a weight, and a bias;
- calculate a linear prediction using `y = weight * x + bias`;
- explain why a neuron is a weighted sum followed by an activation function;
- distinguish linear behavior from non-linear behavior;
- recognize the role of sigmoid, ReLU, and softmax;
- trace data through a dense layer and a small multilayer perceptron;
- distinguish **training** from **inference**; and
- change model parameters and predict how the output will respond.

## The central idea

A model is a function with parameters:

```text
output = model(input, parameters)
```

For these examples, the parameters are mainly weights and biases. A model uses them to transform input features into a prediction.

A useful mental model is:

```text
inputs -> weighted combinations -> activation functions -> prediction
```

The examples in this directory demonstrate the forward calculation. They do not yet implement a complete training loop, automatic differentiation, or a production-ready machine-learning library.

## Files in this chapter

| File | What it demonstrates |
| --- | --- |
| [`linear_model.py`](./linear_model.py) | A one-feature linear model and the meaning of slope and intercept |
| [`neural_network.py`](./neural_network.py) | Activation functions, a neuron, a dense layer, and a tiny MLP |

## Prerequisites

You only need:

- Python 3.9 or newer;
- a terminal or command prompt; and
- a basic understanding of variables, functions, lists, and loops.

No third-party packages are required.

## Run the examples

From the repository root:

```bash
python 01_python_ai_foundations/linear_model.py
python 01_python_ai_foundations/neural_network.py
```

On systems where Python 3 is invoked as `python3`, use:

```bash
python3 01_python_ai_foundations/linear_model.py
python3 01_python_ai_foundations/neural_network.py
```

You can also import the functions from another Python file or an interactive Python session:

```python
from 01_python_ai_foundations.linear_model import predict
```

Because Python module names cannot normally begin with a number in an import statement, the direct script commands above are the simplest way to run these files. If you want to import the functions, run from inside this directory or load the file with your preferred Python tooling.

## 1. Linear models

The first example uses one input feature:

```text
y = w * x + b
```

Where:

- `x` is the input feature;
- `w` is the weight, which controls how strongly the feature affects the output;
- `b` is the bias, which shifts the output even when `x` is zero; and
- `y` is the prediction.

With `w = 2` and `b = 1`:

```text
x = 0  -> y = 1
x = 1  -> y = 3
x = 2  -> y = 5
x = 3  -> y = 7
```

The weight is the slope of the line. Increasing the weight makes the output change more for each unit increase in `x`. The bias is the y-intercept: it moves the whole line up or down without changing its slope.

A model with several features follows the same idea:

```text
y = w1*x1 + w2*x2 + ... + wn*xn + b
```

This weighted sum is the basic calculation performed inside a neuron.

## 2. Neurons and activation functions

A neuron first calculates a pre-activation value, often called `z`:

```text
z = bias + sum(input_i * weight_i)
```

It then applies an activation function:

```text
output = activation(z)
```

The weighted sum lets the model combine features. The activation function introduces non-linearity, allowing stacked layers to represent patterns that a single straight-line equation cannot.

### Sigmoid

The sigmoid function maps any real number to a value between `0` and `1`:

```text
sigmoid(z) = 1 / (1 + e^(-z))
```

It is useful for probability-like output in a binary decision, although a sigmoid value is not automatically a calibrated probability.

Important reference points:

- `sigmoid(0) = 0.5`;
- large positive values approach `1`; and
- large negative values approach `0`.

### ReLU

The Rectified Linear Unit is defined as:

```text
relu(z) = max(0, z)
```

It keeps positive values and replaces negative values with zero. ReLU is common in hidden layers because it is simple and preserves positive signal while adding non-linearity.

### Softmax

Softmax converts a list of scores, often called logits, into values that sum to `1`:

```text
softmax(zi) = exp(zi) / sum(exp(zj))
```

The resulting values can be interpreted as a distribution across classes. The class with the largest score receives the largest softmax value. In real systems, numerically stable implementations usually subtract the largest logit before exponentiating.

## 3. Layers and the tiny MLP

A dense, or fully connected, layer applies a weighted sum for every output neuron. Each neuron has its own row of weights and its own bias:

```text
output_j = sum(input_i * weight_j_i) + bias_j
```

`neural_network.py` uses this sequence:

```text
input values
    -> dense layer
    -> ReLU activation
    -> output weighted sum
    -> sigmoid activation
    -> final output
```

This is a tiny **multilayer perceptron (MLP)**. It demonstrates the shape of a neural network without hiding the arithmetic behind a framework.

The parameters in the example are hand-written demonstration values. They have not been learned from a dataset, so the output should be read as a result of the chosen parameters rather than as a meaningful prediction about the real world.

## Training versus inference

These two ideas are related but different:

- **Inference** means using fixed weights and biases to calculate an output.
- **Training** means changing the weights and biases so the model's predictions become better according to a loss function.

A typical training process is:

```text
1. make a prediction (forward pass)
2. compare it with the target using a loss function
3. calculate how each parameter contributed to the error
4. update the parameters
5. repeat over many examples
```

The current scripts show step 1. They intentionally leave out the dataset, loss, gradients, optimizer, and parameter-update loop so the forward computation is easy to inspect.

## Suggested experiments

Run each experiment before looking at the result. Write down your prediction, then compare it with the program output.

### Linear model experiments

1. Change `weight` from `2.0` to `0.5`. How does the slope change?
2. Change `bias` from `1.0` to `-3.0`. Which outputs change, and by how much?
3. Add negative inputs such as `-1` and `-2`. What does a positive weight do to them?
4. Try a negative weight. What happens to the direction of the line?
5. Rewrite the example with two features and two weights.

### Neural-network experiments

1. Evaluate `sigmoid(-2)`, `sigmoid(0)`, and `sigmoid(2)`. Why do the results stay between `0` and `1`?
2. Try negative and positive values with `relu`. Where does its behavior change?
3. Change one hidden-layer weight in `simple_mlp`. Which part of the output changes?
4. Set one hidden-layer pre-activation to a negative value and observe how ReLU removes it.
5. Change the output bias. Does the final sigmoid output increase or decrease?
6. Verify that the values returned by `softmax` add up to approximately `1.0`.
7. Add assertions for input and weight lengths so shape mistakes are easier to find.

## Common vocabulary

- **Feature:** an input value used by a model.
- **Parameter:** a value learned or selected by the model, such as a weight or bias.
- **Weight:** a parameter controlling the influence of an input.
- **Bias:** an additive parameter that shifts a weighted sum.
- **Logit:** a raw model score before a probability-producing activation.
- **Activation function:** a function applied to a neuron or layer output.
- **Layer:** a group of computations performed together.
- **Forward pass:** calculating a prediction from inputs and current parameters.
- **Loss:** a numerical measure of how far a prediction is from its target.
- **Gradient:** a measure of how changing a parameter would change the loss.
- **Inference:** producing outputs with fixed parameters.
- **Training:** adjusting parameters using examples and a learning procedure.

## Scope and limitations

These examples are deliberately educational. They do not provide:

- data loading or preprocessing;
- parameter validation for every possible input shape;
- a loss function or optimizer;
- backpropagation or gradient descent;
- numerical-stability protections for every input range;
- batching, evaluation metrics, or model persistence; or
- guarantees that outputs represent accurate real-world probabilities.

Those are natural next steps after understanding the arithmetic here. Keeping this chapter dependency-free makes the foundations visible before introducing libraries such as NumPy, PyTorch, or other machine-learning tools.

## Completion checklist

You are ready for the next chapter when you can explain, without copying the code:

- why `weight * input + bias` is a model;
- why a neuron applies an activation after its weighted sum;
- why ReLU enables a network to model more than one straight line;
- how a dense layer differs from a single neuron; and
- why the scripts demonstrate inference but not training.
