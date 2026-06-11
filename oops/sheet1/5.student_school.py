class Student:
    school_name = "Central High School"

    def __init__(self, name: str) -> None:
        self.name = name

def get_school_names() -> tuple[str, str]:
    s1 = Student("Alice")
    s2 = Student("Bob")
    return s1.school_name, s2.school_name

result = get_school_names()
