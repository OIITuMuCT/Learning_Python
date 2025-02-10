"""
Объектно-ориентированное программирование и композиция: отношения "имеет" 
OOP and Composition: “Has-a” Relationships
"""
from __future__ import print_function

from employees import PizzaRobot, Server

class Customer:
    """ Покупатель """
    def __init__(self, name):
        self.name = name
    def order(self, server):
        """ Заказ"""
        print(self.name, 'orders from', server)
    def pay(self, server):
        """ Оплата """
        print(self.name, 'pays for item to', server)

class Oven:
    """ Печь """
    def bake(self):
        """ Духовой шкаф выпекает """
        print('oven bakes')
class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')


