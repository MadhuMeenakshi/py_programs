def iterate_tuple(t: tuple[str, ...]) -> list[str]:
    return [item for item in t]

result = iterate_tuple(("apple", "banana", "cherry"))
