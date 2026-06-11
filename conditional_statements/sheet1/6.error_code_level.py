def classify_error_code(code):
    if code >= 1000:
        return "Critical"
    if code >= 100:
        return "Warning"
    return "Info"

result = classify_error_code(230)  # Warning
