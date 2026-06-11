def factorial(n):
    if n < 0:
        return None
    result_value = 1
    for i in range(1, n + 1):
        result_value *= i
    return result_value

result = factorial(5)  # 120
