class Super:
    def __init__(self, x):
        self.square = x ** 2

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)
        self.y = y * x

I = Sub(1, 2)
print(I.square)