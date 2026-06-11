def remove_set_item(toys: set[str], item: str) -> set[str]:
    toys.discard(item)
    return toys

result = remove_set_item({"robot", "car", "doll"}, "doll")
