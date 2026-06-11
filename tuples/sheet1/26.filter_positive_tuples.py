def filter_positive_tuples(lst: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    return [t for t in lst if all(x > 0 for x in t)]

result = filter_positive_tuples([(1, 2), (-3, 4), (5, 6)])
