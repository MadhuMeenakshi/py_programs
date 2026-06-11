def multiply_list(items: list[int]) -> int:
    product = 1
    for num in items:
        product *= num
    return product

result = multiply_list([1, 2, 3, 4])
