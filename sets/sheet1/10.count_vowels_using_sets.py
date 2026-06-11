def count_vowels_using_sets(msg: str) -> int:
    vowels = set('aeiou')
    return sum(1 for ch in msg.lower() if ch in vowels)

result = count_vowels_using_sets('hello world')
