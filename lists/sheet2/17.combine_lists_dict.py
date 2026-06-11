def combine_lists_dict(keys: list[str], values: list[int]) -> dict[str, int]:
    return dict(zip(keys, values))

result = combine_lists_dict(['a', 'b', 'c'], [1, 2, 3])
