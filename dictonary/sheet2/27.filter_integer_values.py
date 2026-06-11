def filter_integer_values(d: dict[str, object]) -> dict[str, int]:
    return {k: v for k, v in d.items() if isinstance(v, int)}

result = filter_integer_values({'x': 100, 'y': 'hello', 'z': 200})
