
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.

    Args:
        matrix: A square matrix (n x n) represented as a list of lists.

    Returns:
        Tuple of (determinant, trace).
    """
    n = len(matrix)
    if n == 0:
        raise ValueError("Matrix must not be empty")
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square")
    trace = sum(matrix[i][i] for i in range(n))
    if n == 1:
        return (matrix[0][0], trace)
    if n == 2:
        det = (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )
        return (det, trace)
    det = 0
    for col in range(n):
        minor = [
            [matrix[row][j] for j in range(n) if j != col]
            for row in range(1, n)
        ]

        sign = (-1) ** col
        minor_det = matrix_determinant_and_trace(minor)[0]
        det += sign * matrix[0][col] * minor_det

    return (det, trace)
