def tuple_contains(my_tuple: tuple[str, ...], value: str) -> bool:
    return value in my_tuple

result = tuple_contains(('a', 'b', 'c'), 'b')
