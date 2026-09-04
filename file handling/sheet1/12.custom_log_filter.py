import re
from datetime import datetime

input_file = "small_log.txt"

start_time = "2024-01-01 00:00:00"
end_time = "2024-12-31 23:59:59"
keyword = "ERROR"

start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"

try:
    with open(input_file, "r") as file:

        for line in file:
            match = re.search(pattern, line)

            if match:
                timestamp = datetime.strptime(
                    match.group(1),
                    "%Y-%m-%d %H:%M:%S"
                )

                if start <= timestamp <= end and keyword in line:
                    print(line.strip())

except FileNotFoundError:
    print("File not found.")