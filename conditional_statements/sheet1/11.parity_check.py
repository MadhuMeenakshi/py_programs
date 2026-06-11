def parity_check(value):
    return "Parity: Even" if bin(value).count("1") % 2 == 0 else "Parity: Odd"

result = parity_check(0xAAAA)  # Parity: Even
