# Декоратор отслеживания вызовов для функций и методов
def tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

if __name__ == '__main__':
    # Применяется к простым функциям
    @tracer
    def spam(a, b, c):                      # spam = tracer (spam)
        print(a + b + c)                    # onCall запоминает spam
    @tracer
    def eggs(N):
        return 2 ** N
    spam(1, 2, 3)                           # Запускается onCall (1, 2, 3)
    spam(a=5, b=6, c=7)
    print(eggs(32))
    # Применяется также к функциям методов уровня класса!
    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay
        @tracer
        def giveRaise(self, percent):           # giveRaise = tracer(giveRaise)
            self.pay *= (1.0 + percent)         # onCall запоминает giveRaise

        @tracer
        def lastName(self):
            return self.name.split()[-1]
    print("methods....")                        # методы...
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())       # Запускается onCall (bob),
    # lastName в области видимости
