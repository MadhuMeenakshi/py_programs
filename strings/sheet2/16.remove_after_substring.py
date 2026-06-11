def remove_after_substring(text: str, substring: str) -> str:
    index = text.find(substring)
    return text if index == -1 else text[:index + len(substring)]

result = remove_after_substring("abcdeFGhiJK", "FG")
