import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x, dtype=float)
    p = np.array(p, dtype=float)

    if np.sum(p) != 1.0:
        raise ValueError("Xác suất chưa bằng 1")
        return
    
    E = 0.0
    for i in range(len(x)):
        E = E + x[i] * p[i]

    return E;