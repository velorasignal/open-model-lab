from __future__ import annotations

"""
Foundation-style example of a linear model.

A linear model is the simplest form of machine learning model.
It assumes the output can be described by a straight line:

    y = weight * x + bias

where:
- x is the input feature
- weight controls the slope (how steep the line is)
- bias shifts the line up or down

This script shows how to define the model and test it with a few values.
"""


def predict(x: float, weight: float = 2.0, bias: float = 1.0) -> float:
    """
    Return the model prediction for one input value.

    The function follows the formula:
        y = weight * x + bias

    Parameters:
        x: Input feature value.
        weight: Slope of the line; how much x influences the output.
        bias: Intercept; the value added even when x is zero.

    Returns:
        The predicted output value for the given input.
    """
    # A linear model is a straight line.
    # The variable 'weight' acts like the slope (m),
    # and 'bias' acts like the y-intercept (b).
    return weight * x + bias


if __name__ == "__main__":
    # This block runs only when the file is executed directly.
    # It helps us visually inspect the model's behavior.
    sample_inputs = [0, 1, 2, 3]

    print("Simple Linear Model Demo")
    print("Model equation: y = weight * x + bias")
    print(f"Current settings: weight={2.0}, bias={1.0}")

    for x in sample_inputs:
        y = predict(x)
        print(f"x={x} -> y={y:.1f}")
