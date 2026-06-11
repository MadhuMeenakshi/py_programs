def reverse_sort_string(s: str) -> str:
    return ''.join(sorted(s, reverse=True))

result = reverse_sort_string("python")
