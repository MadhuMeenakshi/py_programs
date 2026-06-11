def majority_high(reading1, reading2, reading3, threshold=50):
    above_threshold = sum(1 for reading in (reading1, reading2, reading3) if reading > threshold)
    return "Majority High" if above_threshold >= 2 else "Majority Low"

result = majority_high(40, 65, 70)  # Majority High
