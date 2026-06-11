class Employee:
    def __init__(self, name: str, hourly_rate: float) -> None:
        self.name = name
        self.hourly_rate = hourly_rate

    def pay(self, hours: float) -> float:
        return self.hourly_rate * hours


def employee_pay() -> float:
    employee = Employee("Eve", 25.0)
    return employee.pay(40)

result = employee_pay()
