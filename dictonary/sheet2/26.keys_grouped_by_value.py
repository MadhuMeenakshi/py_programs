def keys_grouped_by_value(d: dict[str, int]) -> dict[int, list[str]]:
    grouped: dict[int, list[str]] = {}
    for key, value in d.items():
        grouped.setdefault(value, []).append(key)
    return grouped

result = keys_grouped_by_value({'m': 1, 'n': 2, 'o': 1})
