def kth_word_char_position(words: list[str], k: int, char: str) -> int:
    if k < 1 or k > len(words):
        raise ValueError("k is out of range")
    word = words[k - 1]
    index = word.find(char)
    return index + 1 if index != -1 else -1

result = kth_word_char_position(["hello", "world"], 2, "r")
