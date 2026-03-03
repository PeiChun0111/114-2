import sys
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "..."
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
def create_animal(kind, name):
    if kind == "Dog":
        return Dog(name)
    elif kind == "Cat":
        return Cat(name)
    else:
        return Animal(name)
n = int(sys.stdin.readline().strip())
for _ in range(n):
    kind, name = sys.stdin.readline().split()
    animal = create_animal(kind, name)
    print(f"{animal.name} says {animal.make_sound()}")