def common_elements_three_lists(a: list[str], b: list[str], c: list[str]) -> list[str]:
    return list(set(a) & set(b) & set(c))

result = common_elements_three_lists(["Toy Story", "Frozen", "Moana"], ["Moana", "Coco", "Frozen"], ["Frozen", "Moana", "Up"])
