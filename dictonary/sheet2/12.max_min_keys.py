def max_min_keys(valuables: dict[str, int]) -> tuple[str, str]:
    max_key = max(valuables, key=valuables.get)
    min_key = min(valuables, key=valuables.get)
    return max_key, min_key

result = max_min_keys({'ring': 5, 'necklace': 9, 'watch': 2})
