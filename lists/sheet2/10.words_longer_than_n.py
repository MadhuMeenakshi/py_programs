def words_longer_than_n(words: list[str], n: int) -> list[str]:
    return [word for word in words if len(word) > n]

result = words_longer_than_n(['hello', 'world', 'python', 'is', 'great'], 4)
