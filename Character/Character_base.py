class Character:
    """Персонаж"""

    def __init__(self, name="Noname", age="Noage", health=100, mana=80, vigor=70):
        self.__name = name
        self.__age = age
        self.__health = health
        self.__mana = mana
        self.__vigor = vigor

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_health(self, health):
        self.__health = health

    def set_mana(self, mana):
        self.__mana = mana

    def set_vigor(self, vigor):
        self.__vigor = vigor

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def get_vigor(self):
        return self.__vigor

    def __str__(self):
        return f"Базовый класс персонаж {self.__name} , health = {self.__health}"



if __name__ == "__main__":
    nick = Character()
    print(nick)
    print(nick.get_health())
    nick.set_name('John')
    print(nick.get_name())
    print(nick)
    noname = Character()
    print(noname)