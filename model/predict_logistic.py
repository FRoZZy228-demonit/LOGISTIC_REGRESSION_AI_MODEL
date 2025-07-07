import numpy as np

def sigmoid(z):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-z))

def predict_logistic(X, weights, bias):
    """
    Predicts binary output (0 or 1) using logistic regression.

    Parameters:
    - X: numpy array of input features, shape (1, n_features)
    - weights: numpy array, shape (n_features, 1)
    - bias: float or array of shape (1,)

    Returns:
    - int: 0 or 1 prediction
    """
    # Ensure input is 2D
    if X.ndim == 1:
        X = X.reshape(1, -1)

    # Compute z = X·w + b
    z = np.dot(X, weights) + bias

    # Apply sigmoid
    prob = sigmoid(z)

    # Binary classification threshold
    return int(prob >= 0.5)
