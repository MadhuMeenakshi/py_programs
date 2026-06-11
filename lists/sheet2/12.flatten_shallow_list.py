def flatten_shallow_list(nested: list[list[int]]) -> list[int]:
    return [item for sublist in nested for item in sublist]

result = flatten_shallow_list([[1, 2], [3, 4], [5, 6]])
