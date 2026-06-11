def check_sensor_value(value):
    if value < 100 or value > 900:
        return "Sensor Fault"
    return "Sensor OK"

result = check_sensor_value(950)  # Sensor Fault
