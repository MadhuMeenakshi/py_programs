def intersection_of_two_lists(list1: list[str], list2: list[str]) -> set[str]:
    return set(list1) & set(list2)

result = intersection_of_two_lists(['dino', 'star', 'moon'], ['star', 'rocket', 'moon'])
