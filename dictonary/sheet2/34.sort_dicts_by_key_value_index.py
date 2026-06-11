def sort_dicts_by_key_value_index(dicts: list[dict[str, list[int]]], index: int) -> list[dict[str, list[int]]]:
    return sorted(dicts, key=lambda d: next(iter(d.values()))[index])

result = sort_dicts_by_key_value_index([{'a': [5, 1]}, {'a': [3, 4]}, {'a': [7, 0]}], 1)
