def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper

if __name__ == '__main__':
    @Tracer
    class Spam:
        def display(self):
            print('Spam!' * 8)
    
    @Tracer
    class Person:
        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate
        def pay(self):
            return self.hours * self.rate
    
    food = Spam()
    food.display()
    print([food.fetches])
    
    bob = Person('Bob', 180, 40)
    print(bob.name)
    print(bob.pay())
    
    sue = Person('Sue', rate=100, hours=60)
    print(sue.name)
    print(sue.pay())
    print(sue.name)
    
    print(bob.name)
    print(bob.pay())
    print([bob.fetches, sue.fetches])