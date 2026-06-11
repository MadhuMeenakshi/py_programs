def count_zero_digits(n):
    value = abs(n)
    if value == 0:
        return 1
    count = 0
    while value > 0:
        if value % 10 == 0:
            count += 1
        value //= 10
    return count

result = count_zero_digits(1002030)  # 4
