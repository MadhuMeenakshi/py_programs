def list_methods_practice() -> tuple[int, int, list[str], list[str]]:
    colors = ["red", "green", "blue", "green"]
    green_count = colors.count("green")
    blue_index = colors.index("blue")
    colors.reverse()
    reversed_colors = colors.copy()
    colors.clear()
    return green_count, blue_index, reversed_colors, colors

result = list_methods_practice()
