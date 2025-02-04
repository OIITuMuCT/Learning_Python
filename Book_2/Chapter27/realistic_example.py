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
        return f'[Person: {self.name}, {self.pay}]'


class Manager(Person):
    def giveRaise(self, percent, bonus=0.10):               # Плохой способ:
        self.pay = int(self.pay * (1 * percent + bonus))    # вырезание и вставка


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue.__dict__)
    print(list(name for name in Person.__dict__.keys() if not name.endswith('__')))
    print(bob)
    print(sue)
