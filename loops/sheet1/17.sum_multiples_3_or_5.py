def sum_multiples_3_or_5():
    total = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

result = sum_multiples_3_or_5()  # 233168
