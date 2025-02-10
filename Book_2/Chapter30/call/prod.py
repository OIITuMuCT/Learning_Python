class Prod:
    def __init__(self, value):
        self.value = value
    def __call__(self, other):
        return self.value * other
    def comp(self, other):
        return self.value * other
    
if __name__ == '__main__':
    x = Prod(2)
    print(x(3))
    print(x(4))
    y = Prod(3)
    print(y.comp(3))
    print(y.comp(4))