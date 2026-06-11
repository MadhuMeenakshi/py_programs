def dict_with_most_pairs(dicts: list[dict]) -> dict:
    return max(dicts, key=lambda d: len(d))

result = dict_with_most_pairs([{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}])
