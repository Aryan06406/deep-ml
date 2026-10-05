import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    A = np.array(A, dtype=float, copy=True)
    m, n = A.shape
    rank, row = 0, 0
    for col in range(n):
        pivot_row = row + np.argmax(np.abs(A[row:, col]))
        if row >= m or abs(A[pivot_row, col]) <= tol:
            continue
        if pivot_row != row:
            A[[row, pivot_row]] = A[[pivot_row, row]]
        for r in range(row + 1, m):
            if abs(A[r, col]) > tol:
                factor = A[r, col] / A[row, col]
                A[r, col:] -= factor * A[row, col:]
        rank += 1
        row += 1
        if row == m:
            break        
    return rank        