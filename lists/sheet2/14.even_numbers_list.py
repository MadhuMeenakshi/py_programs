def even_numbers_list(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]

result = even_numbers_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
