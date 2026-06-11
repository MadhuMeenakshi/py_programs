def filter_tuples_by_length(lst: list[tuple], length: int) -> list[tuple]:
    return [item for item in lst if len(item) == length]

result = filter_tuples_by_length([(1, 2, 3), (4, 5), (6, 7, 8)], 3)
