def power_status(voltage, current):
    voltage_error = voltage < 3.0 or voltage > 3.3
    current_error = current < 10 or current > 500
    if voltage_error and current_error:
        return "Power Error"
    if voltage_error:
        return "Voltage Error"
    if current_error:
        return "Current Error"
    return "Power OK"

result = power_status(3.1, 100)  # Power OK
