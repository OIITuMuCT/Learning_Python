class Name:
    "name descriptor docs"

    def __get__(self, instance, owner):
        print("fetch...")
        return instance._name

    def __set__(self, instance, value):
        print("change...")
        instance._name = value

    def __delete__(self, instance):
        print("remove...")
        del instance._name


class Age:
    "age descriptor docs"

    def __get__(self, instance, owner):
        print("fetch age...")
        return instance._age

    def __set__(self, instance, value):
        print("change age...")
        instance._age = value

    def __delete__(self, instance):
        print("remove age...")
        del instance._age


class Super:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    name = Name()
    age = Age()

class Person(Super):
    pass

if __name__ == "__main__":
    bob = Person("Bob Smith", 40)
    john = Person("John Rambo", 35)
    print(bob.name)
    print(bob.age)
    bob.name = "Robert Smith"
    bob.age -= 15
    print(bob.name)
    print(bob.age)
    del bob.name
    del bob.age

    print("-" * 20)
    sue = Person("Sue Jones", 18)
    print(sue.name)
    sue.age = 25
    print(sue.age)
    print(Name.__doc__)
