def middle_character(s):
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return s[n//2 - 1:n//2 + 1]

result = middle_character("python")  # 'th'
