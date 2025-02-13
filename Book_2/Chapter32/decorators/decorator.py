def decorator(cls):
    class Proxy:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Proxy

@decorator
class C: ... 


if __name__ == '__main__':
    X = C()
    X.name = "Jason"
    X.age = 40
    X.lastname = 'Bourne'
    
    print(X.name, X.age, X.lastname)
    print(X.__dict__)
    