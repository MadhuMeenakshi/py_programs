def sort_by_tuple_last(items: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(items, key=lambda item: item[-1])

result = sort_by_tuple_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
