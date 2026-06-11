def classify_frequency(freq):
    if freq < 1000:
        return "Low Band"
    if freq <= 9999:
        return "Mid Band"
    if freq <= 99999:
        return "High Band"
    return "Out of Range"

result = classify_frequency(8000)  # Mid Band
