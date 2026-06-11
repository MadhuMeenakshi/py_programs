def find_keys_by_substring(d: dict[str, int], substring: str) -> list[str]:
    return [key for key in d if substring in key]

result = find_keys_by_substring({'hello': 1, 'world': 2, 'hell': 3}, 'hell')
