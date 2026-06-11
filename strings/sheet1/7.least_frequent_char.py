def least_frequent_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    min_freq = min(freq.values())
    for ch in s:
        if freq[ch] == min_freq:
            return ch

result = least_frequent_char("statistics")  # 'a'
