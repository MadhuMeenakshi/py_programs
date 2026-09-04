import csv
import json

input_file = "input.csv"
output_file = "output.json"

try:
    data = []

    with open(input_file, "r") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            data.append(row)

    with open(output_file, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("CSV converted to JSON successfully.")

except FileNotFoundError:
    print("File not found.")