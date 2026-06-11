import itertools

def string_permutations(s):
    return ["".join(p) for p in itertools.permutations(s)]

result = string_permutations("abc")  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
