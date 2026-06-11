def assignment_alias_effect() -> tuple[dict[str, list[int]], dict[str, list[int]]]:
    a = {'x': [1, 2]}
    b = a
    b['x'].append(3)
    return a, b

result = assignment_alias_effect()
