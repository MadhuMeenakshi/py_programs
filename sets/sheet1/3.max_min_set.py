def max_min_set(scores: set[int]) -> tuple[int, int]:
    return max(scores), min(scores)

result = max_min_set({3, 7, 10, 2, 9})
