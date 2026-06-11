def convert_list_tuple(lst: list[int], tup: tuple[int, ...]) -> tuple[tuple[int, ...], list[int]]:
    return tuple(lst), list(tup)

result = convert_list_tuple([1, 2, 3], (4, 5, 6))
