def reverse_dict_keys(d: dict[str, int]) -> dict[str, int]:
    return dict(reversed(list(d.items())))

result = reverse_dict_keys({'first': 1, 'second': 2, 'third': 3})
