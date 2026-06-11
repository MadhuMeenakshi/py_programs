def convert_string_numbers_tuple(t: tuple[tuple[str, str], ...]) -> tuple[tuple[int, int], ...]:
    return tuple(tuple(int(x) for x in pair) for pair in t)

result = convert_string_numbers_tuple((("11", "22"), ("33", "44")))
