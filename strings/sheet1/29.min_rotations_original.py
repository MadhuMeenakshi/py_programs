def min_rotations_original(s):
    if not s:
        return 0
    original = s
    count = 1
    rotated = s[1:] + s[0]
    while rotated != original:
        rotated = rotated[1:] + rotated[0]
        count += 1
    return count

result = min_rotations_original("abcde")  # 5
