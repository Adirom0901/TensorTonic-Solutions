import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """

    

    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)

    result = []

    for seq in seqs:
        seq = list(seq[:max_len])

        while len(seq) < max_len:
            seq.append(pad_value)

        result.append(seq)

    return np.asarray(result, dtype=int).reshape(len(seqs), max_len)
        
    # Your code here
    pass