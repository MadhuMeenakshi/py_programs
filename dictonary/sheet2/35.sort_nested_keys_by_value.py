def sort_nested_keys_by_value(d: dict[str, dict[str, int]]) -> dict[str, list[tuple[str, int]]]:
    return {outer: sorted(inner.items(), key=lambda item: item[1]) for outer, inner in d.items()}

result = sort_nested_keys_by_value({'group1': {'b': 2, 'a': 1}, 'group2': {'c': 3, 'd': 0}})
