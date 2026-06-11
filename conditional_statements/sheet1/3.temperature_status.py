def classify_temperature(temp):
    if temp > 75:
        return "Overheat"
    if temp >= 25:
        return "Normal"
    return "Low Temp"

result = classify_temperature(18)  # Low Temp
