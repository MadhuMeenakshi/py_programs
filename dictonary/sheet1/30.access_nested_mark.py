def access_nested_mark(students: dict[str, dict[str, object]]) -> int:
    return students['Rahul']['marks']['english']

result = access_nested_mark({
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
})
