import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.zeros((0, 0), dtype=int)

    if max_len is None:
            max_len = max(len(seq) for seq in seqs)

    N = len(seqs)

    padded_array = np.full((N, max_len), pad_value, dtype=int)
    for i, seq in enumerate(seqs):
        valid_length = min(len(seq), max_len)
        padded_array[i, :valid_length] = seq[:valid_length]
    
    return padded_array