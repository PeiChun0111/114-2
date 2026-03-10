class Transport:
    def __init__(self, capacity):
        self.capacity = capacity
    def calculate_cost(self, distance):
        return 0
class Truck(Transport):
    def calculate_cost(self, distance):
        return distance * 20
class Drone(Transport):
    def calculate_cost(self, distance):
        return distance * 5 + 50
n = int(input())
transports = []
for _ in range(n):
    t, cap = input().split()
    cap = int(cap)
    if t == "Truck":
        transports.append(Truck(cap))
    elif t == "Drone":
        transports.append(Drone(cap))
m = int(input())
for _ in range(m):
    weight, distance = map(int, input().split())
    costs = []
    for t in transports:
        if t.capacity >= weight:
            costs.append(t.calculate_cost(distance))
    if costs:
        print(f"Lowest Cost: {min(costs)}")
    else:
        print("No transport available")