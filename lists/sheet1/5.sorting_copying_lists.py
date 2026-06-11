def sorting_copying_lists() -> tuple[list[int], list[int], list[int]]:
    numbers = [3, 1, 4, 2, 5]
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    copy_of_ascending = ascending.copy()
    return ascending, descending, copy_of_ascending

result = sorting_copying_lists()
