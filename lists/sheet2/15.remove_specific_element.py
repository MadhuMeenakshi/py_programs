def remove_specific_element(items: list[int], value: int) -> list[int]:
    return [item for item in items if item != value]

result = remove_specific_element([1, 2, 3, 2, 4, 2, 5], 2)
