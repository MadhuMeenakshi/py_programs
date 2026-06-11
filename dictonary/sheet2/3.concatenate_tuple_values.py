def concatenate_tuple_values(t: tuple[int, ...]) -> int:
    return int(''.join(str(value) for value in t))

result = concatenate_tuple_values((1, 2, 3))
