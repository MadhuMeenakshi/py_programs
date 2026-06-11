def string_stats(s):
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    for ch in s:
        if ch.isdigit():
            digit_count += 1
        elif ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count, digit_count

result = string_stats("Hello123")  # (2, 5, 3)
