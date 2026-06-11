def filter_tuples_by_length(lst: list[tuple], length: int) -> list[tuple]:
    return [t for t in lst if len(t) == length]

result = filter_tuples_by_length([(1, 2, 3), (4, 5), (6, 7, 8)], 3)
