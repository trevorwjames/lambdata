"""
Creating a character class in OOP to demonstrate
understanding and build on knowledge
"""


class Character:
    # Create your character
    def __init__(self, name: str, weight: int, power: int):
        self.name = name
        self.weight = weight
        self.power = power

    def add_weight(self, amount: int) -> str:
        # giving food to increase weight
        self.weight += amount
        return f'Yummy now I am {self.weight}'

    def power_boost(self, more: int):
        # performing a power boost
        self.power += more
        return f'Power Level increase! {self.power}'


class Wizard(Character):
    # Wizard class with field spells and function cast_spell
    def __init__(self, name, weight, power, spells: str):
        super().__init__(name, weight, power)
        self.spells = spells

    def cast_spell(self) -> str:
        # method specific to wizards
        return 'Abrakadabra'


if __name__ == '__main__':
    x = Wizard('trevor', 200, 100, 'fun')
    print(x.cast_spell())

