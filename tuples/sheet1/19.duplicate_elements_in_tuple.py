def duplicate_elements_in_tuple(t: tuple[int, ...]) -> list[int]:
    seen = set()
    duplicates = []
    for item in t:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates

result = duplicate_elements_in_tuple((2, 4, 6, 2, 8, 4, 6, 2))
