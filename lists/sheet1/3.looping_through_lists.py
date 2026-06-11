def looping_through_lists() -> tuple[list[int], list[int], list[int]]:
    numbers = list(range(1, 6))
    for_loop_result = [n for n in numbers]
    while_loop_result = []
    i = 0
    while i < len(numbers):
        while_loop_result.append(numbers[i])
        i += 1
    squared = [n * n for n in numbers]
    return for_loop_result, while_loop_result, squared

result = looping_through_lists()
