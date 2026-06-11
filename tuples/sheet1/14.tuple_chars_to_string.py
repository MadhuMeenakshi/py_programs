def tuple_chars_to_string(t: tuple[str, ...]) -> tuple[str, tuple[str, ...]]:
    s = ''.join(t)
    return s, tuple(s)

result = tuple_chars_to_string(('P', 'y', 't', 'h', 'o', 'n'))
