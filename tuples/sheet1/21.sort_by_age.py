def sort_by_age(lst: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(lst, key=lambda pair: pair[1])

result = sort_by_age([("Alice", 25), ("Bob", 20), ("Eve", 22)])
