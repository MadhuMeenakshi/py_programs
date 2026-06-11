def split_groups(s: str, n: int) -> list[str]:
    return [s[i:i+n] for i in range(0, len(s), n)]

result = split_groups("abcdefgh", 3)
