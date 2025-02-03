import example2


class ThirdClass(example2.SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, ohter):
        return ThirdClass(self.data + ohter)
    
    def plus(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return f"[ThirdClass: {self.data}]"

    def mul(self, other):
        self.data *= other


if __name__ == "__main__":
    a = ThirdClass("abc")
    a.display()
    print(a + 'zya')
    print(a.data)
    b = a + "xyz"
    print(b.data)
    b.display()
    c = a.plus('PYTHON')
    print(isinstance(c, ThirdClass))
    print(isinstance(c, str))
    print(b)
    a.mul(3)
    a.display()
    print(a)
    print(isinstance(b, ThirdClass))
    print(ThirdClass.__bases__)

