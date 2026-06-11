def missing_additional_values(old_hw: list[str], new_hw: list[str]) -> tuple[list[str], list[str]]:
    old_set = set(old_hw)
    new_set = set(new_hw)
    return list(old_set - new_set), list(new_set - old_set)

result = missing_additional_values(["math", "science", "art"], ["math", "history", "science"])
