def invert_nested_dict(d: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    inverted: dict[str, dict[str, int]] = {}
    for outer_key, inner in d.items():
        for inner_key, value in inner.items():
            inverted.setdefault(inner_key, {})[outer_key] = value
    return inverted

result = invert_nested_dict({'math': {'john': 90, 'jane': 80}, 'science': {'john': 85, 'jane': 95}})
