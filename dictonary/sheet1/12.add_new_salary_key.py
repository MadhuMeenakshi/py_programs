def add_new_salary_key(salaries: dict[str, int]) -> dict[str, int]:
    salaries['C'] = 25000
    return salaries

result = add_new_salary_key({'A': 20000, 'B': 30000})
