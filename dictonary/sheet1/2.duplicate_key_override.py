def duplicate_key_override() -> dict[str, int]:
    d = {'x': 1, 'y': 2, 'x': 5}
    return d

result = duplicate_key_override()
