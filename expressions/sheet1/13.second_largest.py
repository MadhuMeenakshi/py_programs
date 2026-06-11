def second_largest(a, b, c):
    minimum = a if a <= b and a <= c else (b if b <= c else c)
    maximum = a if a >= b and a >= c else (b if b >= c else c)
    return a + b + c - minimum - maximum

result = second_largest(20, 12, 18)  # 18
