""" Объектно-ориентированное программирование и наследование: отношения "является" 
OOP and Inheritance: “Is-a” Relationships"""

from __future__ import print_function


class Employee:
    """Сотрудник"""

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        """Увеличивает salary на заданный процент от 0 до 1"""
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        """Печатает имя и действие объекта"""
        print(self.name, "does stuff")

    def __repr__(self):
        return f"<Employee: name={self.name}, salary=${self.salary:,.2f}>"


class Chef(Employee):
    """Шеф-повар"""

    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "makes food")


class Server:
    """Официант"""

    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        """Принимает заказ у клиента"""
        print(self.name, "interfaces with customer")

    def __repr__(self):
        return f"<Employee: name={self.name}, salary=${self.salary:,.2f}>"

    # def __str__(self):
    #     return f'Server: {self.name}'


class PizzaRobot(Chef):
    """В терминах ООП мф называем такие отношения связями
    "является": робот является шеф-поваром, который является сотрудником.
    """

    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, "makes pizza")


class Customer:
    """Покупатель"""

    def __init__(self, name):
        self.name = name

    def order(self, server):
        """Заказ"""
        print(self.name, "orders from", server)

    def pay(self, server):
        """Оплата"""
        print(self.name, "pays for item to", server)


class Oven:
    """Печь"""

    def bake(self):
        """Духовой шкаф выпекает"""
        print("oven bakes")


class PizzaShop:
    def __init__(self):
        self.server = Server("Pat")
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    bob = PizzaRobot("bob")
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob)
    print()
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
    print()
    scene = PizzaShop()
    scene.order("Homer")
    print("...")
    scene.order("Shaggy")
    # print(PizzaRobot(PizzaRobot.__name__))
