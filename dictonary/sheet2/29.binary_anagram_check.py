def binary_anagram_check(num1: int, num2: int) -> bool:
    return sorted(bin(num1)[2:]) == sorted(bin(num2)[2:])

result = binary_anagram_check(5, 6)
