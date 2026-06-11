def conditional_sign(num):
    return "Positive" if num > 0 else ("Zero" if num == 0 else "Negative")

result = conditional_sign(-8)  # "Negative"
