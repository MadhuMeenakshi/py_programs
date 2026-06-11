def tuple_pairs_to_dict(t: tuple[tuple[str, int], ...]) -> dict[str, int]:
    return dict(t)

result = tuple_pairs_to_dict((('a', 1), ('b', 2), ('c', 3)))
