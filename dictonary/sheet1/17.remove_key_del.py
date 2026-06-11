def remove_key_del(marks: dict[str, int]) -> dict[str, int]:
    del marks['math']
    return marks

result = remove_key_del({'math': 80, 'science': 85})
