def sort_dict_by_key(d: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(d.items())

result = sort_dict_by_key({'b': 2, 'a': 1, 'c': 3})
