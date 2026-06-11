def nested_student_records() -> dict[str, dict[str, object]]:
    return {
        'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
        'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
    }

result = nested_student_records()
