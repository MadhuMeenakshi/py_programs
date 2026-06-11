def extract_common_keys(d: dict[str, int], keys: list[str]) -> dict[str, int]:
    return {key: d[key] for key in keys if key in d}

result = extract_common_keys({'a': 100, 'b': 200, 'c': 300}, ['b', 'c', 'd'])
