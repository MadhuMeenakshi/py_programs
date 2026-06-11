def flip_nested_dict(d: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    return {inner_key: {outer_key: inner_val} for outer_key, inner in d.items() for inner_key, inner_val in inner.items()}

result = flip_nested_dict({'x': {'p': 1}, 'y': {'q': 2}})
