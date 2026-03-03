class Hero:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    def attack(self, target):
        target.take_damage(self.atk)
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
class Warrior(Hero):
    def __init__(self, name, hp, atk, armor):
        super().__init__(name, hp, atk)
        self.armor = armor
    def take_damage(self, amount):
        damage = amount - self.armor
        if damage < 0:
            damage = 0
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
class Mage(Hero):
    def __init__(self, name, hp, atk, mana):
        super().__init__(name, hp, atk)
        self.mana = mana
    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.atk * 2)
        else:
            target.take_damage(self.atk)
w_data = input().split()
m_data = input().split()
warrior = Warrior(w_data[1], int(w_data[2]), int(w_data[3]), int(w_data[4]))
mage = Mage(m_data[1], int(m_data[2]), int(m_data[3]), int(m_data[4]))
n = int(input())
for _ in range(n):
    action = input().split()
    attacker_name = action[0]

    if attacker_name == warrior.name:
        warrior.attack(mage)
    elif attacker_name == mage.name:
        mage.attack(warrior)
print(f"{warrior.name} HP: {warrior.hp}")
print(f"{mage.name} HP: {mage.hp}")