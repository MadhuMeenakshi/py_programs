def list_creation_indexing() -> tuple[str, list[str], int]:
    fruits = ["apple", "banana", "cherry"]
    second_item = fruits[1]
    fruits[1] = "kiwi"
    length = len(fruits)
    return second_item, fruits, length

result = list_creation_indexing()
