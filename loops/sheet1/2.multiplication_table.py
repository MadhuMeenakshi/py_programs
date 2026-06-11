def multiplication_table(n):
    def multiply(a, b):
        total = 0
        for _ in range(b):
            total += a
        return total

    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {multiply(n, i)}")
    return table

result = multiplication_table(5)
