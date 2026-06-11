def print_items(d: dict[str, int]) -> list[tuple[str, int]]:
    return list(d.items())

result = print_items({'a': 10, 'b': 20, 'c': 30})
