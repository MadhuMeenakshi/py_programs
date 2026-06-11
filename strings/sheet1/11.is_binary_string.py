def is_binary_string(s):
    return all(ch in "01" for ch in s)

result = is_binary_string("101101")  # True
