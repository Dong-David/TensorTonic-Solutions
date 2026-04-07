import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    rows, cols = A.shape

    res = np.zeros((cols, rows), dtype=A.dtype)
    i, j = np.indices((rows, cols))

    res[j, i] = A
    return res