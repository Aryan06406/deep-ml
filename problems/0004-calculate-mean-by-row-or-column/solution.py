def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if not matrix or not matrix[0]:
        return []
    if mode == "row":
        return [sum(row) / len(row) for row in matrix]
    elif mode == "column":
        cols = len(matrix[0])
        return [
            sum(row[col] for row in matrix) / len(matrix)
            for col in range(cols)
        ]
    else:
        raise ValueError("mode must be 'row' or 'column'")