class Character:
    def __init__(self, endurance=10, vigor=10, dexterity=10, 
                strength=10, intelligence=10, faith=10, mind=10, arcane=10):
        self.__endurance = endurance
        self.__vigor = vigor
        self.__dexterity = dexterity
        self.__strength = strength
        self.__intelligence = intelligence
        self.__faith = faith
        self.__mind = mind
        self.__arcane = arcane
    
    def __str__(self):
        return 'Базовый персонаж со всеми характеристиками равными 10 очков.'

class Human(Character):
    def __init__(self, name, age, race='Human'):
        self.name = name
        self.age = age
        self.race = race
    
    def __str__(self):
        return f'{self.race}: name: {self.name}, age: {self.age}'

if __name__ == '__main__':
    john = Character()
    bill = Character()
    elis = Human('Elis', 18)
    print(john)
    print(elis)
    