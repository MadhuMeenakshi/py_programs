import difflib

def close_matches(target, candidates):
    return difflib.get_close_matches(target, candidates, cutoff=0.7)

result = close_matches("apple", ["apply", "apples", "ape", "maple"])  # ['apply', 'apples']
