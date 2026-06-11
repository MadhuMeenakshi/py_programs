def toggle_bit(n, bit_position):
    return n ^ (1 << bit_position)

result = toggle_bit(12, 2)  # 8
