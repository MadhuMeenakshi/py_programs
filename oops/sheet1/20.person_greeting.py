class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return f"Hello, my name is {self.name}."


def person_greeting() -> str:
    person = Person("Liam")
    return person.greet()

result = person_greeting()
