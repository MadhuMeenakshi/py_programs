def count_matching_strings(strings: list[str]) -> int:
    return sum(1 for s in strings if len(s) >= 2 and s[0] == s[-1])

result = count_matching_strings(['abc', 'xyz', 'aba', '1221'])
