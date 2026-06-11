def remove_duplicates(items: list[int]) -> list[int]:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

result = remove_duplicates([1, 2, 3, 2, 4, 3, 5])
