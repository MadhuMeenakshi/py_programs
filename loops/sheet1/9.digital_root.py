def digital_root(n):
    value = abs(n)
    while value >= 10:
        total = 0
        while value > 0:
            total += value % 10
            value //= 10
        value = total
    return value

result = digital_root(9875)  # 2
