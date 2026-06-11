def elementwise_tuple_sum(t1: tuple[int, ...], t2: tuple[int, ...], t3: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b + c for a, b, c in zip(t1, t2, t3))

result = elementwise_tuple_sum((1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1))
