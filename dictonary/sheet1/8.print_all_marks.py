def print_all_marks(student: dict[str, int]) -> list[tuple[str, int]]:
    return list(student.items())

result = print_all_marks({'math': 90, 'english': 88, 'science': 92})
