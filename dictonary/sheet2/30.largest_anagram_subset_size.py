def largest_anagram_subset_size(words: list[str]) -> int:
    groups: dict[str, int] = {}
    for word in words:
        key = ''.join(sorted(word))
        groups[key] = groups.get(key, 0) + 1
    return max(groups.values())

result = largest_anagram_subset_size(['bat', 'tab', 'eat', 'tea', 'tan', 'nat'])
