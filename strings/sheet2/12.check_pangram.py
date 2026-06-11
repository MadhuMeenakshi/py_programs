import string

def check_pangram(text: str) -> bool:
    letters = set(ch.lower() for ch in text if ch.isalpha())
    return set(string.ascii_lowercase).issubset(letters)

result = check_pangram("The quick brown fox jumps over the lazy dog")
