from math import pi

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


def circle_metrics() -> tuple[float, float]:
    circle = Circle(3)
    return circle.area(), circle.perimeter()

result = circle_metrics()
