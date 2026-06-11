def unzip_tuples(items: list[tuple[int, str]]) -> tuple[list[int], list[str]]:
    first, second = zip(*items)
    return list(first), list(second)

result = unzip_tuples([(1, 'a'), (2, 'b'), (3, 'c')])
