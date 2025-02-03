
class Human(Character):
    def __init__(self, name, age, health, mana, vigor, ability):
        Character.__init__(self, name, age, health, mana, vigor)
        self.ability = ability
    def __str__(self):
        return f"Человек Способность: {self.ability}"

if __name__ == '__main__':
    bill = Human('Fly')
