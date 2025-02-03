class Character:
    def __init__(self, endurance=10, vigor=10, dexterity=10,
                strength=10, intelligence=10, faith=10, mind=10, arcane=10):
        self.endurance = endurance
        self.vigor = vigor
        self.__dexterity = dexterity
        self.__strength = strength
        self.__intelligence = intelligence
        self.__faith = faith
        self.__mind = mind
        self.__arcane = arcane
        
    def set_endurance(self, endurance):
        self.endurance = endurance
        
    def set_vigor(self, vigor):
        self.vigor = vigor
        
    def get_endurance(self):
            return f'Базовая ловкость: {self.endurance}'
    def get_vigor(self):
        return f'Базовая энергия {self.vigor}'
    
    def __str__(self):
        return 'Базовый персонаж со всеми характеристиками равными 10 очков.'

class Human(Character):

    def __init__(
        self,
        name,
        age,
        race="Human",
        endurance=10,
        vigor=10,
        dexterity=10,
        strength=10,
        intelligence=10,
        faith=10,
        mind=10,
        arcane=10,
    ):
        Character.__init__(
            self,

        )
        self.name = name
        self.age = age
        self.race = race

    def set_endurance(self, endurance):
        self.endurance = endurance
    
    def get_endurance(self):
        return f'Ловкость {self.race}: {self.endurance}'
    
    def __str__(self):
        return f'{self.race}: name: {self.name}, age: {self.age}'

class Elf(Character):
    def __init__(self, name, age, race='Эльф'):
        self.name = name
        self.age = age
        self.race = race
        
    def set_endurance(self, endurance):
        self.endurance = endurance
        return self.endurance
    
    def get_endurance(self):
        return f'Ловкость эльфа: {self.endurance}'
    
    def get_vigor(self):
        return self.vigor

    def get_name(self):
        return f"{self.race}: name: {self.name}, age: {self.age}"
    def __str__(self):
        return f'Race: {self.race} name: {self.name}: age {self.age}:'
if __name__ == '__main__':
    john = Character()
    bill = Character()
    elis = Human('Elis', 18)
    elis.set_endurance(13)
    bill.get_endurance()
    print(john)
    print(elis)
    nemo = Elf('Nemo', 22)
    print(nemo)
    print(elis.get_endurance())
