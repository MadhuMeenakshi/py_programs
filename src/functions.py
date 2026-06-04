#!/usr/bin/env python3

# 1. print_details(name, age)

def print_details(name, age):
    print(f"Name: {name}, Age: {age}")

print_details("Alice", 25)


# 2. multiply(x, y)

def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)


# 3. greet_person(name, greeting)

def greet_person(name, greeting):
    print(f"{greeting}, {name}!")

greet_person("John", "Hi")


# 4. area_of_circle(radius)

import math

def area_of_circle(radius):
    return math.pi * radius ** 2

print(area_of_circle(3))


# 5. is_negative(number)

def is_negative(number):
    return number < 0

print(is_negative(-7))
print(is_negative(0))


# 6. grade(score)

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print(grade(85))
print(grade(72))
print(grade(50))


# 7. sign(num)

def sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(sign(10))
print(sign(-4))
print(sign(0))


# 8. power(base, exponent=2)

def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 5))


# 9. introduction(name, country='India')

def introduction(name, country='India'):
    print(f"My name is {name} and I am from {country}.")

introduction("Sara")
introduction("Alex", "USA")


# 10. calculate(a, b)

def calculate(a, b):
    return a + b, a - b

s, d = calculate(10, 3)

print("Sum:", s)
print("Difference:", d)


# 11. string_stats(s)

def string_stats(s):
    vowels = 0
    consonants = 0
    digits = 0

    for ch in s:
        if ch.lower() in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1

    return vowels, consonants, digits

print(string_stats("Hello123"))


# 12. factorial(n) using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))


# 13. sum_list(lst) using recursion

def sum_list(lst):
    if len(lst) == 0:
        return 0

    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))


# 14. reverse_string(s) using recursion

def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))


# 15. fibonacci(n) using recursion

def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


# 16. min_max(numbers)

def min_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)

    return smallest, largest

small, large = min_max([8, 3, 5, 2, 10])

print("Smallest:", small)
print("Largest:", large)
