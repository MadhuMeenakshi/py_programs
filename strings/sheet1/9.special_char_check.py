def special_char_check(s):
    for ch in s:
        if not ch.isalnum():
            return "Yes"
    return "No"

result = special_char_check("Hello@123")  # Yes
