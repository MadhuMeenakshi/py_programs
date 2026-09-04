import json

input_file = "config.json"
output_file = "updated_config.json"

try:
    with open(input_file, "r") as file:
        config = json.load(file)

    config["timeout"] = 60
    config["retries"] = 5

    with open(output_file, "w") as file:
        json.dump(config, file, indent=4)

    print("Configuration updated successfully.")

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")