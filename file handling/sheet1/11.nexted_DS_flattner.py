def flatten(data, parent_key="", result=None):
    if result is None:
        result = {}

    for key, value in data.items():

        new_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            flatten(value, new_key, result)
        else:
            result[new_key] = value

    return result


data = {
    "user": {
        "name": "Madhu",
        "details": {
            "age": 25,
            "city": "Bangalore"
        }
    }
}

flattened_data = flatten(data)

print(flattened_data)