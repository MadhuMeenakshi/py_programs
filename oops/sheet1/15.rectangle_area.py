class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def rectangle_values() -> tuple[float, float]:
    rect = Rectangle(5, 3)
    return rect.area(), rect.perimeter()

result = rectangle_values()
