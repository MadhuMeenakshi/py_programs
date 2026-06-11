def vowel_count(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)

result = vowel_count("education")  # 5
