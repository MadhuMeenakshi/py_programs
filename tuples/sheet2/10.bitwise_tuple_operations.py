def bitwise_tuple_operations(t1: tuple[int, ...], t2: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    and_result = tuple(a & b for a, b in zip(t1, t2))
    xor_result = tuple(a ^ b for a, b in zip(t1, t2))
    return and_result, xor_result

result = bitwise_tuple_operations((1, 2, 3), (2, 2, 2))
