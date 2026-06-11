def sort_by_values_sum(d: dict[str, list[int]]) -> list[tuple[str, list[int]]]:
    return sorted(d.items(), key=lambda item: sum(item[1]))

result = sort_by_values_sum({'x': [5, 5], 'y': [1, 2, 3], 'z': [10]})
