def rotationally_equivalent(a: str, b: str) -> bool:
    return len(a) == len(b) and b in (a + a)

result = rotationally_equivalent("abcde", "cdeab")
