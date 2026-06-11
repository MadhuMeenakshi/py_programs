def adding_removing_items() -> tuple[list[str], list[str], list[str], list[str]]:
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    after_insert = fruits.copy()
    fruits.insert(1, "mango")
    after_remove = fruits.copy()
    fruits.remove("apple")
    after_pop = fruits.copy()
    fruits.pop()
    after_clear = fruits.copy()
    fruits.clear()
    return after_insert, after_remove, after_pop, fruits

result = adding_removing_items()
