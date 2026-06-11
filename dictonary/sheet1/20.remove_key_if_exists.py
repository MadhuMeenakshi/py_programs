def remove_key_if_exists(d: dict[str, int], key: str) -> str:
    if key in d:
        del d[key]
        return 'Removed'
    return 'Key not found'

result = remove_key_if_exists({'x': 1, 'y': 2}, 'z')
