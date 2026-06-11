def count_tuples_divisible_by_k(lst: list[tuple[int, ...]], k: int) -> int:
    return sum(1 for t in lst if all(x % k == 0 for x in t))

result = count_tuples_divisible_by_k([(3, 6), (9, 12, 15), (4, 8)], 3)
