def access_missing_key(marks: dict[str, int]) -> str:
    try:
        return str(marks['english'])
    except KeyError:
        raise

result = None
