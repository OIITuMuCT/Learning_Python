from types import FunctionType
from decotools import tracer, timer

class MetaTrace(type):
    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:
                classdict[attr] = tracer(attrval)
        return type.__new__(meta, classname, supers, classdict)


class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):  # giveRaise = tracer(giverRaise)
        self.pay *= 1.0 + percent  # onCall запоминает giveRaise


    def lastName(self):  # lastName = tracer (lastName)
        return self.name.split()[-1]


if __name__ == "__main__":
    bob = Person("Bob Smith", 50000)
    sue = Person("Sue Jones", 100000)
    print(bob.name, sue.name)
    sue.giveRaise(0.10)  # Запускается onCall(sue, .10)
    print("%.2f" % sue.pay)
    print(
        bob.lastName(), sue.lastName()
    )  # Запускается onCall (bob) , # запоминается lastName
