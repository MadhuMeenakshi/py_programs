def parse_log(line):
    parts = line.strip().split(" ", 3)

    timestamp = parts[0] + " " + parts[1]
    severity = parts[2]
    message = parts[3]

    return timestamp, severity, message


def group_by_severity(logs):
    grouped = {}

    for timestamp, severity, message in logs:
        if severity not in grouped:
            grouped[severity] = []

        grouped[severity].append({
            "timestamp": timestamp,
            "message": message
        })

    return grouped


def read_logs(filename):
    logs = []

    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    logs.append(parse_log(line))

    except FileNotFoundError:
        print("File not found.")

    return logs


filename = "small_log.txt"

logs = read_logs(filename)
grouped_logs = group_by_severity(logs)

for severity, entries in grouped_logs.items():
    print(f"\n{severity}:")
    for entry in entries:
        print(entry)