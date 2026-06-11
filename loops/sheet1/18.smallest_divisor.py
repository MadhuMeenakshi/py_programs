def smallest_divisor(n):
    if n <= 1:
        return None
    value = abs(n)
    divisor = 2
    while divisor <= value:
        if value % divisor == 0:
            return divisor
        divisor += 1
    return value

result = smallest_divisor(91)  # 7
