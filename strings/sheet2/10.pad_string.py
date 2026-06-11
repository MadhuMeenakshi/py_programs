def pad_string(text: str, length: int, pad_char: str = ' ', direction: str = 'left') -> str:
    if len(pad_char) != 1:
        raise ValueError("pad_char must be a single character")
    pad_count = max(0, length - len(text))
    if direction == 'left':
        return pad_char * pad_count + text
    return text + pad_char * pad_count

result = pad_string("cat", 6, "*")
