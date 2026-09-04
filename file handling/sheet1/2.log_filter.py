input_file = "small_log.txt"
output_file = "error_logs.txt"

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    with open(output_file, "w") as file:
        for line in lines:
            if "ERROR" in line:
                file.write(line)

    print("ERROR logs written successfully.")

except FileNotFoundError:
    print("File not found.")