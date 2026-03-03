import sys
class Appliance:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def use(self, hours):
        return self.power * hours
class SmartAC(Appliance):
    def __init__(self, name, power, temperature):
        super().__init__(name, power)
        self.temperature = temperature
    def use(self, hours):
        total = super().use(hours)
        if self.temperature < 25:
            total = total * 1.2
        return int(total)
class SmartTV(Appliance):
    def use(self, hours):
        total = super().use(hours)
        return int(total * 0.9)
n = int(sys.stdin.readline().strip())
for _ in range(n):
    parts = sys.stdin.readline().split()
    kind = parts[0]
    if kind == "AC":
        name = parts[1]
        power = int(parts[2])
        temperature = int(parts[3])
        hours = int(parts[4])
        appliance = SmartAC(name, power, temperature)
    elif kind == "TV":
        name = parts[1]
        power = int(parts[2])
        hours = int(parts[3])
        appliance = SmartTV(name, power)
    else:  # Normal
        name = parts[1]
        power = int(parts[2])
        hours = int(parts[3])
        appliance = Appliance(name, power)
    print(f"{name} used {appliance.use(hours)} Wh")