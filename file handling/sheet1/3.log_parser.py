input_file = "small_log.txt"

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split(" ", 3)

        timestamp = parts[0] + " " + parts[1]
        severity = parts[2]
        message = parts[3]

        print("Timestamp:", timestamp)
        print("Severity:", severity)
        print("Message:", message)
        print()

except FileNotFoundError:
    print("File not found.")