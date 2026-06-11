def rotate_left(n, k):
    return ((n << k) & 0xFF) | ((n & 0xFF) >> (8 - k))

result = rotate_left(150, 2)  # 90
