def distinct_substring_count_rabin_karp(s: str) -> int:
    base = 257
    mod = 2**61 - 1
    n = len(s)
    substrings: dict[int, None] = {}
    for length in range(1, n + 1):
        hash_val = 0
        power = 1
        for i in range(length):
            hash_val = (hash_val * base + ord(s[i])) % mod
            if i < length - 1:
                power = (power * base) % mod
        substrings[hash_val] = None
        for i in range(length, n):
            hash_val = (hash_val - ord(s[i-length]) * power) % mod
            hash_val = (hash_val * base + ord(s[i])) % mod
            substrings[hash_val] = None
    return len(substrings)

result = distinct_substring_count_rabin_karp('abc')
