def find_key_by_value(d: dict[str, int], value: int) -> str:
    for key, val in d.items():
        if val == value:
            return key
    raise ValueError('Value not found')

result = find_key_by_value({'x': 100, 'y': 200}, 200)
