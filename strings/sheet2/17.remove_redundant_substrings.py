def remove_redundant_substrings(words: list[str]) -> list[str]:
    result = []
    for w in words:
        for size in range(1, len(w)//2 + 1):
            if len(w) % size == 0 and w == w[:size] * (len(w) // size):
                result.append(w[:size])
                break
        else:
            result.append(w)
    return result

result = remove_redundant_substrings(["hellohello", "world", "testtesttest"])
