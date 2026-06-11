def access_value(marks: dict[str, int], subject: str) -> int:
    return marks[subject]

result = access_value({'math': 75, 'science': 80}, 'science')
