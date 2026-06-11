def remove_empty_tuples(lst: list[tuple]) -> list[tuple]:
    return [t for t in lst if t]

result = remove_empty_tuples([(), (), ('a', 'b'), ('c',)])
