def device_mode(mode):
    if mode == 0:
        return "Standby"
    if mode == 1:
        return "Active"
    if mode == 2:
        return "Fault"
    return "Unknown mode"

result = device_mode(1)  # Active
