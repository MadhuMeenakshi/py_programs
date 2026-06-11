def check_types() -> tuple[str, str]:
    integer_type = str(type(5))
    string_type = str(type("hello"))
    return integer_type, string_type

result = check_types()
