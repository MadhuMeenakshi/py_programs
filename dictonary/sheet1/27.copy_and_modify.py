def copy_and_modify(original: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    copied = original.copy()
    copied['car'] = 'green'
    return original, copied

result = copy_and_modify({'car': 'red', 'bike': 'blue'})
