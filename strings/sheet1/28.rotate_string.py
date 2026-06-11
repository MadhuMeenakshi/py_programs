def rotate_string(s, k):
    k %= len(s) if s else 1
    return s[-k:] + s[:-k]

result = rotate_string("hello", 2)  # "lohel"
