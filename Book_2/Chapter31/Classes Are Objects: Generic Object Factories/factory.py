def factory(aClass, *args, **kwargs):   # Кортеж или словарь с переменным количеством аргументов
    return aClass(*args, **kwargs)      # Вызывает aClass (или apply в Pyhton 2.X)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

if __name__ == '__main__':
    object1 = factory(Spam)
    object2 = factory(Person, "Arthur", "King")
    object3 = factory(Person, name='Brian')
    object1.doit(99)
    print((object2.name, object3.job))

