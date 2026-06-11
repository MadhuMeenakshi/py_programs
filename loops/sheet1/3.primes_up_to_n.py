def primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

result = primes_up_to(30)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
