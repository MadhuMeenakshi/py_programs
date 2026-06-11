def insert_element(items: list[int], element: int, position: int) -> list[int]:
    result = items.copy()
    result.insert(position, element)
    return result

result = insert_element([1, 2, 3, 4], 5, 2)
