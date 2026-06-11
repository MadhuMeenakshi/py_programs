def consecutive_freq(s):
    if not s:
        return {}
    result = {}
    count = 1
    prev = s[0]
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            result[prev] = result.get(prev, 0) + count
            prev = ch
            count = 1
    result[prev] = result.get(prev, 0) + count
    return result

result = consecutive_freq("aabccddd")  # {'a': 2, 'b': 1, 'c': 2, 'd': 3}
