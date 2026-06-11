def set_to_tuple_and_back(toys_set: set[str]) -> tuple[tuple[str, ...], set[str]]:
    t = tuple(toys_set)
    return t, set(t)

result = set_to_tuple_and_back({'teddy', 'robot', 'ball'})
