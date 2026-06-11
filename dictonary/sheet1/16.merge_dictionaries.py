def merge_dictionaries(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    merged = d1.copy()
    merged.update(d2)
    return merged

result = merge_dictionaries({'x': 1}, {'y': 2})
