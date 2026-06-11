def remove_keys_with_substring(d: dict[str, int], substring: str) -> dict[str, int]:
    return {k: v for k, v in d.items() if substring not in k}

result = remove_keys_with_substring({'sun': 1, 'sunny': 2, 'rain': 3}, 'sun')
