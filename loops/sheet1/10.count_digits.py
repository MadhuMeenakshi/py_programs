def count_digits(n):
    value = abs(n)
    if value == 0:
        return 1
    count = 0
    while value > 0:
        count += 1
        value //= 10
    return count

result = count_digits(12345)  # 5
