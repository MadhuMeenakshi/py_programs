def symmetric_difference_string(word1: str, word2: str) -> str:
    return ''.join(sorted(set(word1) ^ set(word2)))

result = symmetric_difference_string('apple', 'orange')
