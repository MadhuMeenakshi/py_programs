class Vehicle:
    pass

class Bus(Vehicle):
    pass

def check_bus_subclass() -> bool:
    return issubclass(Bus, Vehicle)

result = check_bus_subclass()
