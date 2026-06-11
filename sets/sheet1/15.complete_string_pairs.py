import string

def complete_string_pairs(A: set[str], B: set[str]) -> list[tuple[str, str]]:
    alphabet = set(string.ascii_lowercase)
    pairs = []
    for a in A:
        for b in B:
            if alphabet.issubset(set(a.lower()) | set(b.lower())):
                pairs.append((a, b))
    return pairs

result = complete_string_pairs({'abc', 'defg', 'xyz'}, {'mnopq', 'rstuv', 'wxyz'})
