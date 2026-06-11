def sort_by_digit_count(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
    def digit_count(pair: tuple[int, int]) -> int:
        return sum(len(str(x)) for x in pair)
    return sorted(lst, key=digit_count)

result = sort_by_digit_count([(1, 2), (10, 11), (3, 44)])
