import sys
class Vehicle:
    def __init__(self, plate):
        self.plate = plate
    def calculate_toll(self):
        return 40
class Truck(Vehicle):
    def __init__(self, plate, weight):
        super().__init__(plate)
        self.weight = weight
    def calculate_toll(self):
        base = super().calculate_toll()
        return base + self.weight * 10
class Bus(Vehicle):
    def __init__(self, plate, passengers):
        super().__init__(plate)
        self.passengers = passengers
    def calculate_toll(self):
        base = super().calculate_toll()
        return base + self.passengers * 5
n = int(sys.stdin.readline().strip())
for _ in range(n):
    parts = sys.stdin.readline().split()
    vehicle_type = parts[0]
    if vehicle_type == "Vehicle":
        plate = parts[1]
        vehicle = Vehicle(plate)
    elif vehicle_type == "Truck":
        plate = parts[1]
        weight = int(parts[2])
        vehicle = Truck(plate, weight)
    elif vehicle_type == "Bus":
        plate = parts[1]
        passengers = int(parts[2])
        vehicle = Bus(plate, passengers)
    print(f"{vehicle.plate}: ${vehicle.calculate_toll()}")