def tuple_product(t: tuple[int, ...]) -> int:
    product = 1
    for value in t:
        product *= value
    return product

result = tuple_product((4, 3, 2, 2, -1, 18))
