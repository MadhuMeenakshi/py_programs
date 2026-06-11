def unzip_pairs(lst: list[tuple[int, str]]) -> tuple[list[int], list[str]]:
    first, second = zip(*lst)
    return list(first), list(second)

result = unzip_pairs([(1, 'a'), (2, 'b'), (3, 'c')])
