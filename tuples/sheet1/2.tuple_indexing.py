def tuple_indexing(my_tuple: tuple[int, ...]) -> tuple[int, int]:
    return my_tuple[0], my_tuple[-1]

result = tuple_indexing((10, 20, 30, 40, 50))
