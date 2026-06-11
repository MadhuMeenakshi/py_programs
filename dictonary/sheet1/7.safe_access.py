def safe_access(scores: dict[str, int], key: str) -> str:
    return str(scores.get(key, 'Not found'))

result = safe_access({'math': 80, 'science': 90}, 'history')
