def print_student_marks(students: dict[str, dict[str, object]]) -> list[tuple[str, dict[str, int]]]:
    return [(name, student['marks']) for name, student in students.items()]

result = print_student_marks({
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
})
