def number_pyramid(n):
    lines = []
    for row in range(n, 0, -1):
        line = ""
        for num in range(1, row + 1):
            line += str(num)
        lines.append(line)
    return lines

result = number_pyramid(5)  # ['12345', '1234', '123', '12', '1']
