def union_of_n_arrays(arrays: list[list[str]]) -> set[str]:
    result: set[str] = set()
    for array in arrays:
        result |= set(array)
    return result

result = union_of_n_arrays([['red', 'blue'], ['green', 'red'], ['yellow', 'blue']])
