def find_armstrong_numbers():
    result = []
    for num in range(100, 1000):
        temp = num
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit * digit * digit
            temp //= 10
        if total == num:
            result.append(num)
    return result

result = find_armstrong_numbers()  # [153, 370, 371, 407]
