def check_key_exists(d: dict[str, str], key: str) -> bool:
    return key in d

result = check_key_exists({'fruit': 'apple', 'veg': 'carrot'}, 'fruit')
