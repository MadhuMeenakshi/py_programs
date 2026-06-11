def matrix_3x3(rows: int, cols: int) -> list[list[int]]:
    return [[r for _ in range(cols)] for r in range(rows)]

result = matrix_3x3(3, 3)
