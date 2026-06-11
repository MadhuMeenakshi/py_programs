def filter_strings_by_substrings(words: list[str], substrings: list[str]) -> list[str]:
    return [word for word in words if all(sub in word for sub in substrings)]

result = filter_strings_by_substrings(
    ["applebanana", "apple", "banana", "applebananacherry"],
    ["apple", "banana"]
)
