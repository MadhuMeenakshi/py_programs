def pop_name(info: dict[str, str]) -> tuple[str, dict[str, str]]:
    removed = info.pop('name')
    return removed, info

result = pop_name({'name': 'Amit', 'city': 'Pune'})
