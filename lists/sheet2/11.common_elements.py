def common_elements(list1: list[int], list2: list[int]) -> list[int]:
    return [item for item in list1 if item in list2]

result = common_elements([1, 2, 3, 4], [3, 4, 5, 6])
