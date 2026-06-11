def set_to_string(letters: set[str]) -> str:
    return ''.join(sorted(letters))

result = set_to_string({'A', 'B', 'C'})
