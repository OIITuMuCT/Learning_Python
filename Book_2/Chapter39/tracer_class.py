class Tracer:
    def __init__(self, aClass):
        self.aClass = aClass
    def __call__(self, *args):
        self.wrapped = self.aClass(*args)
        return self
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)
@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)
    
food = Spam()
food.display()
    
@Tracer
class Person:
    def __init__(self, name):
        self.name = name
bob = Person('Bob')
sue = Person('Sue')
print(sue.name)
print(bob.name)
