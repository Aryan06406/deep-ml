def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    r1, c1 = len(a), len(a[0])
    r2, c2 = len(b), len(b[0]) 
    if c1 != r2:
        return -1
    cols = list(zip(*b))
    result = []
    for row in a:
        result_row = []
        for col in cols:
            result_row.append(sum(x*y for x, y in zip(row, col)))
        result.append(result_row)
    return result                        