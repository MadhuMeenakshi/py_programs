def letter_frequency(text: str) -> dict[str, int]:
    freq: dict[str, int] = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

result = letter_frequency('apple')
