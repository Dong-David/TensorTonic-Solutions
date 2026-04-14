import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    if rng is not None:
        rands = rng.random(x.shape)
    else:
        rands = np.random.random(x.shape)

    keep_mask = rands >= p

    scale_factor = 1.0 / (1.0 - p)

    dropout_pattern = keep_mask.astype(float) * scale_factor

    output = x * dropout_pattern

    return output, dropout_pattern