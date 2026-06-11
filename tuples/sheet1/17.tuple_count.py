def tuple_count(t: tuple[int, ...], value: int) -> int:
    return t.count(value)

result = tuple_count((1, 2, 3, 2, 2, 4), 2)
