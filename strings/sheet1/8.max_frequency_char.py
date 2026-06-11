def max_frequency_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    max_freq = max(freq.values())
    for ch in s:
        if freq[ch] == max_freq:
            return ch

result = max_frequency_char("banana")  # 'a'
