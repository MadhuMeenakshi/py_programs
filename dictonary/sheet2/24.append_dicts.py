def append_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    merged = d1.copy()
    merged.update(d2)
    return merged

result = append_dicts({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
