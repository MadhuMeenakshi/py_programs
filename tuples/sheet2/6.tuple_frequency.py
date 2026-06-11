def tuple_frequency(t: tuple[int, ...]) -> dict[int, int]:
    freq = {}
    for value in t:
        freq[value] = freq.get(value, 0) + 1
    return freq

result = tuple_frequency((1, 2, 2, 3, 3, 3))
