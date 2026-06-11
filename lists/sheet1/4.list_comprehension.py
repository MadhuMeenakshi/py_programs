def list_comprehension() -> tuple[list[str], list[str], list[str]]:
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    contains_a = [fruit for fruit in fruits if "a" in fruit]
    uppercased = [fruit.upper() for fruit in fruits]
    replaced = ["orange" if fruit == "banana" else fruit for fruit in fruits]
    return contains_a, uppercased, replaced

result = list_comprehension()
