def joining_extending_lists() -> tuple[list[str | int], list[str | int]]:
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    concatenated = list1 + list2
    list1.extend(list2)
    return concatenated, list1

result = joining_extending_lists()
