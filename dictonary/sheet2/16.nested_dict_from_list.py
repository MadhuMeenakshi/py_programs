def nested_dict_from_list(lst: list[str]) -> dict[str, object]:
    nested: dict[str, object] = {}
    for item in reversed(lst):
        nested = {item: nested}
    return nested

result = nested_dict_from_list(['a', 'b', 'c', 'd'])
