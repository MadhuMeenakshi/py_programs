def remove_from_tuple(t: tuple[int, ...], value: int) -> tuple[int, ...]:
    return tuple(x for x in t if x != value)

result = remove_from_tuple((1, 2, 3, 4), 2)
