def sort_dict_items_and_values(d: dict[str, list[int]]) -> list[tuple[str, list[int]]]:
    return [(key, sorted(value)) for key, value in sorted(d.items())]

result = sort_dict_items_and_values({'c': [3, 1], 'a': [2, 4], 'b': [5, 1]})
