#! /usr/bin/env python3


# 1. Voltage Status
voltage = 3.45
print("Under Voltage" if voltage < 3.0 else "Nominal" if 3.0 <= voltage <= 3.3 else "Over Voltage")


# 2. Check MSB of 8-bit Register
reg = 0b10100110
print("MSB set" if reg & 0b10000000 else "MSB not set")


# 3. Temperature Status
temp = 18
print("Overheat" if temp > 75 else "Normal" if 25 <= temp <= 75 else "Low Temp")


# 4. AND, OR, XOR Gate Outputs
a = 1
b = 0
print(f"AND: {a & b}, OR: {a | b}, XOR: {a ^ b}")


# 5. Sensor Range Check
sensor = 950
print("Sensor Fault" if sensor < 100 or sensor > 900 else "Sensor OK")


# 6. Error Code Category
code = 230
print("Critical" if code >= 1000 else "Warning" if 100 <= code <= 999 else "Info")


# 7. System Safety Status
power_on = True
overcurrent = True
overvoltage = False

print(
    "Critical Failure" if overcurrent and overvoltage else
    "Shut Down: Overcurrent" if overcurrent else
    "Shut Down: Overvoltage" if overvoltage else
    "System Safe" if power_on else
    "System Off"
)


# 8. Determine Quadrant
val = 145

print(
    "Quadrant 1" if 0 <= val <= 63 else
    "Quadrant 2" if 64 <= val <= 127 else
    "Quadrant 3" if 128 <= val <= 191 else
    "Quadrant 4" if 192 <= val <= 255 else
    "Invalid"
)


# 9. Frequency Band
freq = 8000

print(
    "Low Band" if freq < 1000 else
    "Mid Band" if 1000 <= freq <= 9999 else
    "High Band" if 10000 <= freq <= 99999 else
    "Out of Range"
)


# 10. Majority Sensor Check
s1 = 40
s2 = 65
s3 = 70

print("Majority High" if ((s1 > 50) + (s2 > 50) + (s3 > 50)) >= 2 else "Majority Low")


# 11. Even or Odd Parity
value = 0xAAAA
print("Parity: Even" if bin(value).count('1') % 2 == 0 else "Parity: Odd")


# 12. Voltage and Current Safety Check
voltage = 2.8
current = 600

print(
    "Power Error" if not (3.0 <= voltage <= 3.3) and not (10 <= current <= 500) else
    "Voltage Error" if not (3.0 <= voltage <= 3.3) else
    "Current Error" if not (10 <= current <= 500) else
    "Power OK"
)


# 13. LED Status
led1 = 0
led2 = 1
led3 = 0

print(
    "All LEDs off" if led1 == led2 == led3 == 0 else
    f"{'LED1 ON ' if led1 else ''}{'LED2 ON ' if led2 else ''}{'LED3 ON' if led3 else ''}"
)


# 14. Device Mode
mode = 2

print(
    "Standby" if mode == 0 else
    "Active" if mode == 1 else
    "Fault" if mode == 2 else
    "Unknown mode"
)


# 15. Analog Reading Match
a1 = 98
a2 = 101

print("Match" if abs(a1 - a2) <= 5 else "No Match")