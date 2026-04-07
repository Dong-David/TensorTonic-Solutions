import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x_array = np.array(x, dtype=float)
    res = 1 / (1 + np.exp(-x_array))

    return res