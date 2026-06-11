def change_last_value(lst: list[tuple[int, int, int]], new_value: int) -> list[tuple[int, int, int]]:
    return [(a, b, new_value) for a, b, _ in lst]

result = change_last_value([(10, 20, 40), (40, 50, 60), (70, 80, 90)], 100)
