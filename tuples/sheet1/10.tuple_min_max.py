def tuple_min_max(t: tuple[int, ...]) -> tuple[int, int]:
    return max(t), min(t)

result = tuple_min_max((11, 3, 55, 21))
