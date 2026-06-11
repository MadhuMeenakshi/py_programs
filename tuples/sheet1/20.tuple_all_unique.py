def tuple_all_unique(t: tuple[int, ...]) -> bool:
    return len(t) == len(set(t))

result = tuple_all_unique((1, 2, 3, 4, 5))
