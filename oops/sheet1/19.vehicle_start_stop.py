class Vehicle:
    def __init__(self, model: str) -> None:
        self.model = model
        self.running = False

    def start(self) -> str:
        self.running = True
        return f"{self.model} started"

    def stop(self) -> str:
        self.running = False
        return f"{self.model} stopped"


def vehicle_control() -> tuple[str, str]:
    car = Vehicle("Sedan")
    return car.start(), car.stop()

result = vehicle_control()
