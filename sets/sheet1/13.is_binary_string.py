def is_binary_string(note: str) -> bool:
    return set(note).issubset({'0', '1'})

result = is_binary_string('101010')
