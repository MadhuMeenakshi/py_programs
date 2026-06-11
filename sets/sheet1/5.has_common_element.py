def has_common_element(list1: list[str], list2: list[str]) -> bool:
    return bool(set(list1) & set(list2))

result = has_common_element(["Tom", "Jerry", "Ben 10"], ["Powerpuff", "Jerry", "Scooby"])
