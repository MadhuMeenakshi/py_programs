def classify_voltage(voltage):
    if voltage < 3.0:
        return "Under Voltage"
    if voltage <= 3.3:
        return "Nominal"
    return "Over Voltage"

result = classify_voltage(3.35)  # Over Voltage
