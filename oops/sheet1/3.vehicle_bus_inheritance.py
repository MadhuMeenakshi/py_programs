class Vehicle:
    def move(self) -> str:
        return "Vehicle is moving"

class Bus(Vehicle):
    pass

def bus_moves() -> str:
    bus = Bus()
    return bus.move()

result = bus_moves()
