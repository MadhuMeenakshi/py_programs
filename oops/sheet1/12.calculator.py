class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        return a / b


def calculate() -> tuple[float, float]:
    calc = Calculator()
    return calc.add(4, 5), calc.divide(10, 2)

result = calculate()
