def tuple_index(t: tuple[str, ...], value: str) -> int:
    return t.index(value)

result = tuple_index(("cat", "dog", "rabbit"), "dog")
