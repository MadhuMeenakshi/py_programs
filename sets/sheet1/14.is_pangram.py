import string

def is_pangram(sentence: str) -> bool:
    letters = {ch.lower() for ch in sentence if ch.isalpha()}
    return set(string.ascii_lowercase).issubset(letters)

result = is_pangram('The quick brown fox jumps over a lazy dog')
