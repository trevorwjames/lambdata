"""
Attempting to create classes to do OOP
"""


class Character:
    # Create you character
    def __init__(self, name: str, weight: int, power: int):
        self.name = name
        self.weight = weight
        self.power = power

    def add_weight(self, food: int) -> str:
        # giving food to increase weight
        self.weight += food
        return f'Yummy now I am {self.weight}'

    def power_boost(self, more: int):
        # performing a power boost
        self.power += more
        return f'Power Level increase! {self.power}'


class Wizard(Character):
    def __init__(self, name, weight, power, spells: str):
        super().__init__(name, weight, power)
        self.spells = spells

    def cast_spell(self):
        return 'Abrakadabra'


if __name__ == '__main__':
    x = Character('trevor', 200, 100)
    print(x.weight)
