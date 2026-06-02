
#!/usr/bin/env python3

n = 2
num = 15
a = 5
b = 10
c = 3
x = 7
y = 14
z = 21
divisor = 4
k = 3

print("1. Square of n:", n * n)

print("2. Quadratic (a*x^2 + b*x + c):", a * x**2 + b * x + c)

print("3. Remainder (num % divisor):", num % divisor)

print("4. Sign of num:", "Positive" if num > 0 else ("Negative" if num < 0 else "Zero"))

print("5. Absolute of n:", abs(n))

# 6. Swap example without mutating originals
swapped_a, swapped_b = b, a
print("6. Swap a,b ->", swapped_a, swapped_b)

print("7. Average of x,y,z:", (x + y + z) / 3)

print("8. Minimum of a and b:", a if a < b else b)

print("9. Bitwise OR (x|y):", x | y)
print("9b. Bitwise XOR (x^y):", x ^ y)

print("10. Divisible by 2 and 3:", num % 2 == 0 and num % 3 == 0)

largest = (a if a > b else b) if (a if a > b else b) > c else c
print("11. Largest of a,b,c:", largest)

print("12. Is n power of two:", n > 0 and (n & (n - 1)) == 0)

second_largest = a + b + c - largest - (a if a < b else b if (a if a < b else b) < c else c)
print("13. Second largest (approx):", second_largest)

print("14. Toggle 3rd bit of n:", n ^ (1 << 3))

print("15. Count of 1 bits in n:", bin(n).count('1'))

print("16. Sign of n (-1,0,1):", (n > 0) - (n < 0))

print("17. Multiple of 4 but not 8:", n % 4 == 0 and n % 8 != 0)

print("18. Rotate left 8-bit by k:", ((n << k) & 0xFF) | (n >> (8 - k)))

min_val = (a if a < b else b) if (a if a < b else b) < c else c
print("19. Difference between largest and smallest:", largest - min_val)

print("20. Set nth bit of n:", n | (1 << n))