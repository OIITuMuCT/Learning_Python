instance = {}
def singleton(aClass):                                  # При декорировании @

    def onCall(*args, **kwargs):                        # При создании экземпляров
        if aClass not in instance:                      # Один элемент словаря на класс
            instance[aClass] = aClass(*args, **kwargs)
        return instance[aClass]

    return onCall

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__(self, val):
        self.attr = val
bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())          # В действительности вызывается onCall

sue = Person("Sue", 50, 20)         # To же самое, единственный объект
print(sue.name, sue.pay())      
X = Spam(val=42)
Y = Spam(99)
print(X.attr, Y.attr)
