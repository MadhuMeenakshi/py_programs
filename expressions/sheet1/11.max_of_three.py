def max_of_three(a, b, c):
    return a if a >= b and a >= c else (b if b >= c else c)

result = max_of_three(14, 27, 19)  # 27
