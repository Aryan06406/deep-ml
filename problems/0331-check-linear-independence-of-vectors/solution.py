import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    if not vectors:
        return True
    n = len(vectors[0])
    if any (len(v) != n for v in vectors):
        raise ValueError("All vectorsmust be of same dimension!")
    matrix = [list(row) for row in zip(*vectors)]
    rows = len(matrix)
    cols = len(vectors)
    rank = 0
    eps = 1e-10
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if abs(matrix[row][col]) > eps:
                pivot = row
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for row in range(rank + 1, rows):
            factor = matrix[row][col] / matrix[rank][col]
            for j in range(col, cols):
                matrix[row][j] -= factor * matrix[rank][j]
        rank += 1
    return rank == cols    