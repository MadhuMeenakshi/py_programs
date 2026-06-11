def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

result = min_max([8, 3, 5, 2, 10])  # (2, 10)
