def snake_to_pascal(s: str) -> str:
    return ''.join(word.capitalize() for word in s.split('_'))

result = snake_to_pascal("my_variable_name")
