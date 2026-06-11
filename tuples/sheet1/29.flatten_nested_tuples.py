def flatten_nested_tuples(t: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(item for sub in t for item in sub)

result = flatten_nested_tuples(((1, 2), (3, 4), (5, 6)))
