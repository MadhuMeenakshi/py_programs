def system_status(power_on, overcurrent, overvoltage):
    if overcurrent and overvoltage:
        return "Critical Failure"
    if overcurrent:
        return "Shut Down: Overcurrent"
    if overvoltage:
        return "Shut Down: Overvoltage"
    if power_on:
        return "System Safe"
    return "System Off"

result = system_status(True, True, False)  # Shut Down: Overcurrent
