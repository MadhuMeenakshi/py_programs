class Vehicle:
    pass

class Bus(Vehicle):
    pass

def check_bus_instance() -> bool:
    return isinstance(Bus(), Vehicle)

result = check_bus_instance()
