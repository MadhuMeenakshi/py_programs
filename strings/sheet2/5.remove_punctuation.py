import string

def remove_punctuation(text: str) -> str:
    allowed = set(string.ascii_letters + string.digits + " ")
    return ''.join(ch for ch in text if ch in allowed)

result = remove_punctuation("Hello, world! How are you?")
