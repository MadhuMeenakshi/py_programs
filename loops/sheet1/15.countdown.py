def countdown(n):
    result = []
    for i in range(n, 0, -1):
        result.append(i)
    return result

result = countdown(5)  # [5, 4, 3, 2, 1]
