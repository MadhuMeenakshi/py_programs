def unique_elements_in_nested_tuples(t: tuple[tuple[int, ...], ...]) -> set[int]:
    return {item for sub in t for item in sub}

result = unique_elements_in_nested_tuples(((1, 2), (2, 3), (4, 5)))
