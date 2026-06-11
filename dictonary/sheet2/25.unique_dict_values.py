def unique_dict_values(d: dict[str, int]) -> list[int]:
    return list(dict.fromkeys(d.values()))

result = unique_dict_values({'a': 1, 'b': 2, 'c': 2, 'd': 3})
