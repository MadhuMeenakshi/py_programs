def is_palindrome_number(n):
    original = abs(n)
    reversed_value = 0
    value = original
    while value > 0:
        reversed_value = reversed_value * 10 + (value % 10)
        value //= 10
    if original == reversed_value:
        return "Palindrome"
    return "Not Palindrome"

result = is_palindrome_number(12321)  # Palindrome
