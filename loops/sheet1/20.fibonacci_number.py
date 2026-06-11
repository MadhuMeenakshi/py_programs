def fibonacci_number(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

result = fibonacci_number(10)  # 34
