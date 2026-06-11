def detect_quadrant(value):
    if 0 <= value <= 63:
        return "Quadrant 1"
    if 64 <= value <= 127:
        return "Quadrant 2"
    if 128 <= value <= 191:
        return "Quadrant 3"
    if 192 <= value <= 255:
        return "Quadrant 4"
    return "Out of Range"

result = detect_quadrant(150)  # Quadrant 3
