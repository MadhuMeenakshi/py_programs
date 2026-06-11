def check_msb(value):
    return "MSB set" if (value & 0x80) != 0 else "MSB not set"

result = check_msb(0b10010010)  # MSB set
