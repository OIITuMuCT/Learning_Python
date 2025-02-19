class Person:
    def __init__(self, name):
        self._name = name

    def __getattribute__(self, attr):               # При [obj .любой_атрибут]
        print("get: " + attr)
        if attr == "name":                          # Перехват всех имен
            attr = "_name"                          # Отображение на внутреннее имя
        return object.__getattribute__(self, attr)  # Избегание зацикливания

    def __setattr__(self, attr, value):
        print("set: " + attr)
        if attr == "name":
            attr = "_name"
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print("def: " + attr)
        if attr == "name":
            attr = "_name"
        del self.__dict__[attr]


if __name__ == "__main__":
    bob = Person("Bob Smith")
    print(bob.name)
    bob.name = "Robert Smith"
    print(bob.name)
    del bob.name
    print("-" * 20)
    sue = Person("Sue Jones")
    print(sue.name)
    # print(Person.name.__doc__)
