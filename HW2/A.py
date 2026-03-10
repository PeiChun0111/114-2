class Effect:
    def __init__(self, duration):
        self.duration = duration
    def apply(self, character):
        self.duration -= 1
class Poison(Effect):
    def apply(self, character):
        character.hp -= 10
        self.duration -= 1
class Regen(Effect):
    def apply(self, character):
        character.hp += 15
        self.duration -= 1
class Character:
    def __init__(self, hp):
        self.hp = hp
        self.effects = []
    def add_effect(self, effect):
        self.effects.append(effect)
    def next_turn(self):
        new_effects = []
        for effect in self.effects:
            effect.apply(self)
            if effect.duration > 0:
                new_effects.append(effect)
        self.effects = new_effects
hp = int(input())
n = int(input())
character = Character(hp)
for _ in range(n):
    command = input().split()
    if command[0] == "add":
        effect_type = command[1]
        duration = int(command[2])
        if effect_type == "Poison":
            character.add_effect(Poison(duration))
        elif effect_type == "Regen":
            character.add_effect(Regen(duration))
    elif command[0] == "turn":
        character.next_turn()
        print(f"Current HP: {character.hp}")