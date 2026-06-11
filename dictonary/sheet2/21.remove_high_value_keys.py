def remove_high_value_keys(d: dict[str, object], limit: int) -> dict[str, object]:
    return {k: v for k, v in d.items() if not isinstance(v, (int, float)) or v <= limit}

result = remove_high_value_keys({'a': 5, 'b': 10, 'c': 15, 'd': 'big'}, 10)
