def add_science_mark(students: dict[str, dict[str, object]]) -> dict[str, dict[str, object]]:
    students['Simran']['marks']['science'] = 93
    return students

result = add_science_mark({
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
})
