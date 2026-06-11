def reverse_digits(n):
    reversed_value = 0
    value = abs(n)
    while value > 0:
        reversed_value = reversed_value * 10 + (value % 10)
        value //= 10
    return -reversed_value if n < 0 else reversed_value

result = reverse_digits(12345)  # 54321
