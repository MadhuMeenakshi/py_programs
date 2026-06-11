def double_triangle(n):
    lines = []
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        lines.append(line)
    star_line = "" 
    for _ in range(2 * n - 1):
        star_line += "*"
    lines.append(star_line)
    return lines

result = double_triangle(5)
