def words_with_all_vowels(words: list[str]) -> list[str]:
    vowels = set('aeiou')
    return [word for word in words if vowels.issubset(set(word.lower()))]

result = words_with_all_vowels(['education', 'python', 'sequoia'])
