class Shape:
    def draw(self) -> str:
        raise NotImplementedError

    def fill(self, color: str) -> str:
        raise NotImplementedError

class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a circle"

    def fill(self, color: str) -> str:
        return f"Filling the circle with {color}"

class Square(Shape):
    def draw(self) -> str:
        return "Drawing a square"

    def fill(self, color: str) -> str:
        return f"Filling the square with {color}"


def shape_fill() -> tuple[str, str]:
    circle = Circle()
    return circle.draw(), circle.fill("blue")

result = shape_fill()
