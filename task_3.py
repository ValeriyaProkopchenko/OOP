import random

class Unit:
  def __init__(self, name):
    self.name = name
    self.health = 100

  def attack(self, opponent):
    damage = 20
    opponent.health -= damage
    print(f"{self.name} атакует {opponent.name}. У {opponent.name} осталось {opponent.health} здоровья.")

def main():
  Unit1 = Unit("Воин 1")
  Unit2 = Unit("Воин 2")

  while Unit1.health > 0 and Unit2.health > 0:
    attacker = random.choice([Unit1, Unit2])
    defender = Unit1 if attacker == Unit2 else Unit2

    attacker.attack(defender)

    if defender.health <= 0:
      print(f"{defender.name} повержен. {attacker.name} одерживает победу!")
      break

if __name__ == "__main__":
    main()