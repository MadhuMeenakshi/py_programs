def remove_ith_char(s, i):
    if i < 0 or i >= len(s):
        return s
    return s[:i] + s[i+1:]

result = remove_ith_char("Python", 2)  # "Pythn"
