#!/usr/bin/env python3 
# 
# 
# ==========================================================
# 1. Armstrong Numbers (3-digit)
# ==========================================================

print("1. Armstrong Numbers:")
for num in range(100, 1000):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    if total == num:
        print(num)

print("\n" + "=" * 50)


# ==========================================================
# 2. Multiplication Table Without *
# ==========================================================

print("2. Multiplication Table Without *:")
n = 5

for i in range(1, 11):
    result = 0

    for _ in range(i):
        result += n

    print(f"{n} x {i} = {result}")

print("\n" + "=" * 50)


# ==========================================================
# 3. Prime Numbers Between 2 and n
# ==========================================================

print("3. Prime Numbers:")
n = 30

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print("\n" + "=" * 50)


# ==========================================================
# 4. Number Pyramid
# ==========================================================

print("4. Number Pyramid:")
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + "=" * 50)


# ==========================================================
# 5. Reverse Number
# ==========================================================

print("5. Reverse Number:")
n = 12345

while n > 0:
    print(n % 10, end="")
    n //= 10

print("\n" + "=" * 50)


# ==========================================================
# 6. Palindrome Number
# ==========================================================

print("6. Palindrome Check:")
n = 12321

temp = n
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")

print("\n" + "=" * 50)


# ==========================================================
# 7. GCD
# ==========================================================

print("7. GCD:")
a = 18
b = 12

while b != 0:
    a, b = b, a % b

print("GCD =", a)

print("\n" + "=" * 50)


# ==========================================================
# 8. Hollow Square
# ==========================================================

print("8. Hollow Square:")
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n" + "=" * 50)


# ==========================================================
# 9. Repeated Digit Sum
# ==========================================================

print("9. Repeated Digit Sum:")
n = 9875

while n >= 10:
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    n = total

print(n)

print("\n" + "=" * 50)


# ==========================================================
# 10. Count Digits
# ==========================================================

print("10. Count Digits:")
n = 54321
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)

print("\n" + "=" * 50)


# ==========================================================
# 11. Factorial
# ==========================================================

print("11. Factorial:")
n = 5

fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

print("\n" + "=" * 50)


# ==========================================================
# 12. Right Aligned Triangle
# ==========================================================

print("12. Right Aligned Triangle:")
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

print("\n" + "=" * 50)


# ==========================================================
# 13. Sum of Odd Numbers
# ==========================================================

print("13. Sum of Odd Numbers:")
n = 10
total = 0

for i in range(1, n + 1, 2):
    total += i

print(total)

print("\n" + "=" * 50)


# ==========================================================
# 14. Perfect Number
# ==========================================================

print("14. Perfect Number Check:")
n = 28
total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")

print("\n" + "=" * 50)


# ==========================================================
# 15. Print n to 1
# ==========================================================

print("15. Print n to 1:")
n = 5

while n >= 1:
    print(n)
    n -= 1

print("\n" + "=" * 50)


# ==========================================================
# 16. Count Zeros
# ==========================================================

print("16. Count Zeros:")
n = 1002000
count = 0

while n > 0:
    if n % 10 == 0:
        count += 1

    n //= 10

print(count)

print("\n" + "=" * 50)


# ==========================================================
# 17. Sum of Multiples of 3 or 5 Below 1000
# ==========================================================

print("17. Sum of Multiples of 3 or 5 Below 1000:")

total = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)

print("\n" + "=" * 50)


# ==========================================================
# 18. Smallest Divisor Greater Than 1
# ==========================================================

print("18. Smallest Divisor:")
n = 35

for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break

print("\n" + "=" * 50)


# ==========================================================
# 19. Double Triangle Pattern
# ==========================================================

print("19. Double Triangle:")
n = 4

for i in range(1, n + 1):
    print("*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i)

print("\n" + "=" * 50)


# ==========================================================
# 20. nth Fibonacci Number
# ==========================================================

print("20. Fibonacci Number:")
n = 10

a = 0
b = 1

for _ in range(n):
    a, b = b, a + b

print(a)

print("\n" + "=" * 50)