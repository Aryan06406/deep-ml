import numpy as np

def to_categorical(x, n_col: int = None):
    if n_col is None:
        n_col = np.max(x) + 1

    encoded = np.zeros((len(x), n_col), dtype=float)
    encoded[np.arange(len(x)), x] = 1

    return encoded