def update_age(ages: dict[str, int]) -> dict[str, int]:
    ages['Anil'] = 22
    return ages

result = update_age({'Anil': 21, 'Sunita': 20})
