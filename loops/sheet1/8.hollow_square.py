def hollow_square(n):
    if n < 3:
        return []
    lines = []
    for row in range(1, n + 1):
        if row == 1 or row == n:
            lines.append("*" * n)
        else:
            lines.append("*" + " " * (n - 2) + "*")
    return lines

result = hollow_square(5)
