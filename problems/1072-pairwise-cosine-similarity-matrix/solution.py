import numpy as np

def pairwise_cosine_similarity(X):
    X = np.array(X, dtype=float)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    X_normalised = X / norms
    s = X_normalised @ X_normalised.T
    return np.round(s, 4).tolist()