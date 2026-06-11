def word_frequency(s):
    freq = {}
    for word in s.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

result = word_frequency("apple apple orange")  # {'apple': 2, 'orange': 1}
