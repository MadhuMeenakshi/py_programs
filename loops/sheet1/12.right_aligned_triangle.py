def right_aligned_triangle(n):
    lines = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * i
        lines.append(spaces + stars)
    return lines

result = right_aligned_triangle(5)
