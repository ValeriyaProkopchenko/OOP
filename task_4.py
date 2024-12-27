import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 50
        self.stamina = 100

    def attack(self, opponent):
        if self.stamina > 0:
            damage = random.randint(10, 30)
            self.stamina -= 10
            opponent.defend(damage)
            print(f"{self.name} атакует {opponent.name} на {damage} урона!")
        else:
            damage = random.randint(0, 10)
            opponent.defend(damage)
            print(f"{self.name} атакует {opponent.name} на {damage} урона (с уменьшением урона из-за усталости)!")

    def defend(self, incoming_damage):
        if self.armor > 0:
            armor_loss = random.randint(0, 10)
            damage_after_armor = max(incoming_damage - armor_loss, 0)
            self.health -= damage_after_armor
            self.armor -= armor_loss
            print(f"{self.name} защищается! Потеряно здоровья: {damage_after_armor}, потеряно брони: {armor_loss}.")
        else:
            damage = random.randint(10, 30)
            self.health -= damage
            print(f"{self.name} защищается без брони! Потеряно здоровья: {damage}.")

    def is_alive(self):
        return self.health > 10

    def display_status(self):
        print(f"{self.name}: Здоровье: {self.health}, Броня: {self.armor}, Выносливость: {self.stamina}")

def main():
    warrior1 = Warrior("Воин 1")
    warrior2 = Warrior("Воин 2")

    while warrior1.is_alive() and warrior2.is_alive():
        warrior1.display_status()
        warrior2.display_status()

        action1 = random.choice(["attack", "defend"])
        action2 = random.choice(["attack", "defend"])

        if action1 == "attack":
            warrior1.attack(warrior2)
        else:
            print(f"{warrior1.name} решает защищаться.")

        if action2 == "attack":
            warrior2.attack(warrior1)
        else:
            print(f"{warrior2.name} решает защищаться.")

    winner = warrior1 if warrior1.is_alive() else warrior2
    print(f"{winner.name} одерживает победу!")

    if not winner.is_alive():
        decision = input("Убить поверженного воина? (да/нет): ")
        if decision.lower() == "да":
            print(f"{winner.name} был убит!")
        else:
            print(f"{winner.name} был пощажен!")

if __name__ == "__main__":
    main()
