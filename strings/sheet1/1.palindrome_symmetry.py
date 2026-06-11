def check_palindrome_symmetry(s):
    is_palindrome = s == s[::-1]
    half = len(s) // 2
    left = s[:half]
    right = s[-half:]
    is_symmetrical = left == right[::-1]
    return "Yes" if is_palindrome else "No", "Yes" if is_symmetrical else "No"

result = check_palindrome_symmetry("madam")  # ("Yes", "Yes")
