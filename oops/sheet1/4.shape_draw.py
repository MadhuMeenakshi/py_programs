class Shape:
    def draw(self) -> str:
        return "Drawing a shape"

class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a circle"

class Square(Shape):
    def draw(self) -> str:
        return "Drawing a square"

def draw_circle() -> str:
    return Circle().draw()

result = draw_circle()
