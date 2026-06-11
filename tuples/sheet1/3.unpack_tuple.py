def unpack_tuple(t: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c = t
    return a, b, c

result = unpack_tuple((1, 2, 3))
