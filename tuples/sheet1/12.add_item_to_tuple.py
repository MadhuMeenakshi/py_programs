def add_item_to_tuple(t: tuple[int, ...], item: int) -> tuple[int, ...]:
    return tuple(list(t) + [item])

result = add_item_to_tuple((1, 2, 3), 4)
