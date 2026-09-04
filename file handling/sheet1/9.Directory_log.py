import os

directory = "logs"

info_count = 0
warning_count = 0
error_count = 0

for filename in os.listdir(directory):

    if filename.endswith(".log"):
        filepath = os.path.join(directory, filename)

        try:
            with open(filepath, "r") as file:
                for line in file:
                    if "INFO" in line:
                        info_count += 1
                    elif "WARNING" in line:
                        warning_count += 1
                    elif "ERROR" in line:
                        error_count += 1

        except FileNotFoundError:
            print("File not found:", filename)

print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)