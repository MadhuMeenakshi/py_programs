def contains_in_nested_tuples(t: tuple[tuple[str, ...], ...], value: str) -> bool:
    return any(value in inner for inner in t)

result = contains_in_nested_tuples((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), 'White')
