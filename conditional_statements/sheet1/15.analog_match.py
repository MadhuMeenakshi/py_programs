def analog_match(reading1, reading2):
    return "Match" if abs(reading1 - reading2) <= 5 else "No Match"

result = analog_match(98, 101)  # Match
