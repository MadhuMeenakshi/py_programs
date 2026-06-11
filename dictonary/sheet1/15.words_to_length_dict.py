def words_to_length_dict(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}

result = words_to_length_dict(['dog', 'cat', 'rabbit'])
