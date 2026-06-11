def substring_indices(text: str, substring: str) -> list[int]:
    indices = []
    start = 0
    while True:
        index = text.find(substring, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices

result = substring_indices("abracadabra", "abra")
