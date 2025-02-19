class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, "mgr", pay)              # Внедрение объекта Person

    def giveRaise(self, percent, bonus=0.10):
        self.person.giveRaise(percent + bonus)              # Перехват и делегирование

    def __getattr__(self, attr):
        return getattr(self.person, attr)                   # Делегирование всех
        # остальных атрибутов
    # def __repr__(self):
    #     return str(self.person)             # Снова требуется перегрузка (в Python З.Х)


if __name__ == '__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager("Tom Jones", 50000)       # Manager.__ init__
    print(tom.lastName())                   # Manager.__ getattr__ -> Person.lastName
    tom.giveRaise(0.10)                     # Manager.giveRaise -> Person.giveRaise
    print(tom)                              # Manager.__ repr__ -> Person.__ repr__
