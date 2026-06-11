def tuple_sums(lst: list[tuple[int, ...]]) -> list[int]:
    return [sum(t) for t in lst]

result = tuple_sums([(1, 2), (2, 3), (3, 4)])
