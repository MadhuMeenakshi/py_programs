from math import sqrt

class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side * self.side

    def perimeter(self) -> float:
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, base: float, height: float, side1: float, side2: float) -> None:
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def perimeter(self) -> float:
        return self.base + self.side1 + self.side2


def triangle_area() -> float:
    triangle = Triangle(6, 4, 5, 5)
    return triangle.area()

result = triangle_area()
