def lost_element_from_duplicate_array(yesterday: list[int], today: list[int]) -> int:
    missing = set(yesterday) - set(today)
    return missing.pop() if missing else None

result = lost_element_from_duplicate_array([1, 2, 3, 4], [1, 4, 2])
