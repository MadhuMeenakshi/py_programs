def gcd(a, b):
    x = abs(a)
    y = abs(b)
    while x != 0 and y != 0:
        if x > y:
            x -= y
        else:
            y -= x
    return x or y

result = gcd(48, 18)  # 6
