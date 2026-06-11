def max_minus_min(a, b, c):
    minimum = a if a <= b and a <= c else (b if b <= c else c)
    maximum = a if a >= b and a >= c else (b if b >= c else c)
    return maximum - minimum

result = max_minus_min(8, 27, 14)  # 19
