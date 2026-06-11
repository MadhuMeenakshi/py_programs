def is_heterogram(word: str) -> bool:
    return len(set(word.lower())) == len(word)

result = is_heterogram('lamp')
