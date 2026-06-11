def increase_salaries(salaries: dict[str, float]) -> dict[str, float]:
    return {k: v * 1.1 for k, v in salaries.items()}

result = increase_salaries({'A': 20000, 'B': 30000})
