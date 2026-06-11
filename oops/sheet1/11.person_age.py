from datetime import date

class Person:
    def __init__(self, name: str, birth_year: int, birth_month: int, birth_day: int) -> None:
        self.name = name
        self.birth_date = date(birth_year, birth_month, birth_day)

    def age(self, today: date) -> int:
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years


def person_age() -> str:
    person = Person("Alice", 2000, 5, 25)
    return f"{person.name} is {person.age(date(2025, 5, 25))} years old."

result = person_age()
