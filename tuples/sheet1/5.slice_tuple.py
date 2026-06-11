def slice_tuple(t: tuple[int, ...]) -> tuple[int, ...]:
    return t[1:4]

result = slice_tuple((0, 1, 2, 3, 4, 5))
