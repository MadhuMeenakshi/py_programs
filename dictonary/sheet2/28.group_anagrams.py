def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for word in words:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

result = group_anagrams(['listen', 'silent', 'enlist', 'hello', 'ohlle'])
