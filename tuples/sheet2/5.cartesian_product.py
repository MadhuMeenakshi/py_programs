def cartesian_product(t1: tuple[int, ...], t2: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(a, b) for a in t1 for b in t2]

result = cartesian_product((1, 2), (3, 4))
