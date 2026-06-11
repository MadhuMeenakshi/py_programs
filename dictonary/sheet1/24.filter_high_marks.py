def filter_high_marks(scores: dict[str, int], threshold: int) -> list[str]:
    return [subject for subject, mark in scores.items() if mark > threshold]

result = filter_high_marks({'math': 75, 'science': 55, 'english': 82}, 60)
