class Character:
    """Персонаж"""

    def __init__(self, name="Noname", age="Noage", health=100, mana=80, vigor=70):
        self.__name = name
        self.__age = age
        self.__hit_point = health
        self.__mana = mana
        self.__vigor = vigor

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_health(self, health):
        self.__hit_point = health

    def set_mana(self, mana):
        self.__mana = mana

    def set_vigor(self, vigor):
        self.__vigor = vigor

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_health(self):
        return self.__hit_point

    def get_mana(self):
        return self.__mana

    def get_vigor(self):
        return self.__vigor

    def __str__(self):
        return f"Базовый класс персонаж {self.__name} , health = {self.__hit_point}"


class Human(Character):
    def __init__(self, ability, name='No_name', age=22, health=120, mana=100, vigor=100, ):
        Character.__init__(self, name, age, health, mana, vigor)
        self.ability = ability
        self.name = name
    def set_name(self, name):
        self.name = name
    
    # def get_name(self):
    #     return f'Имя человека {self.name}'
    def get_age(self):
        return f'Возраст человека: {self.get_age}'

    def __str__(self):
        return f"Человек {self.name} Способность: {self.ability}"


if __name__ == "__main__":
    nick = Character()
    print(type(nick))
    # print(nick.get_health())
    # nick.set_name('John')
    # print(nick.get_name())
    # print(nick)
    # noname = Character()
    # print(noname)
    human = Human('Fly')
    # human.set_name('Bill')
    print(human.get_health())
    human.set_health(150)
    print(human.get_health())
    human.set_name("Имя через метод get_name() Bill")
    print('human.get_name() = ', human.get_name())
    # human.name = 'Billy J'
    print(human.name)

    print(human.ability)
