def uncommon_words(s1, s2):
    set1 = set(s1.split())
    set2 = set(s2.split())
    return sorted(list((set1 | set2) - (set1 & set2)))

result = uncommon_words("red blue green", "blue yellow red")  # ['green', 'yellow']
