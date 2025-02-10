class adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class addrepr(adder):
    def __repr__(self):
        return 'addrepr (%s)' % self.data

x = addrepr(2)
x.__add__(1)
x.__init__(5)
x.__add__(1)
print(x)
print(type(x))
print(x.__class__)
