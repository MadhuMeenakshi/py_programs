def is_perfect_number(n):
    if n <= 1:
        return "Not Perfect"
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return "Perfect Number" if total == n else "Not Perfect"

result = is_perfect_number(28)  # Perfect Number
